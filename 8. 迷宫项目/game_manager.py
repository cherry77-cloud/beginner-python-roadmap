import pygame
from player import Player
from wall import Wall
from star import Star
from target import Target
from utils.collided import collided_rect, collided_circle
import os


class GameManager:
    def __init__(self, screen, level=1):
        self.screen = screen
        self.level = level
        self.player = None
        self.walls = pygame.sprite.Group()
        self.stars_cnt = 0
        self.stars = pygame.sprite.Group()
        self.targets = pygame.sprite.Group()
        self.eat_stars_sound = pygame.mixer.Sound("static/sounds/eat_stars.wav")
        self.eat_stars_sound.set_volume(0.3)
        self.success_sound = pygame.mixer.Sound("static/sounds/success.wav")
        self.success_sound.set_volume(0.3)
        self.load()

    def load_walls(self, walls):
        self.walls.empty()  # 清空
        for x, y, width, height in walls:
            wall = Wall(x, y, width, height)
            wall.add(self.walls)

    def load_stars(self, stars):
        self.stars.empty()
        for x, y in stars:
            star = Star(x, y)
            star.add(self.stars)

    def load_targets(self, targets):
        self.targets.empty()
        for x, y in targets:
            target = Target(x, y)
            target.add(self.targets)

    def load_player(self, center_x, center_y, forward_angle):
        if self.player:
            self.player.kill()
        self.player = Player(center_x, center_y, forward_angle)

    def load(self):  # 加载当前这一关的地图信息
        with open("static/maps/level%d.txt" % self.level, 'r') as fin:
            walls_cnt = int(fin.readline())
            walls = []
            for i in range(walls_cnt):
                x, y, width, height = map(int, fin.readline().split())
                walls.append((x, y, width, height))
            self.load_walls(walls)
            self.stars_cnt = int(fin.readline())
            stars = []
            for i in range(self.stars_cnt):
                x, y = map(int, fin.readline().split())
                stars.append((x, y))
            self.load_stars(stars)
            targets_cnt = int(fin.readline())
            targets = []
            for i in range(targets_cnt):
                x, y = map(int, fin.readline().split())
                targets.append((x, y))
            self.load_targets(targets)
            center_x, center_y, forward_angle = map(int, fin.readline().split())
            self.load_player(center_x, center_y, forward_angle)

    def next_level(self):
        self.level += 1
        if not os.path.isfile("static/maps/level%d.txt" % self.level):
            return False  # 表示没有下一关
        self.load()
        return True  # 表示已经加载了下一关

    def check_collide(self):  # 检测碰撞
        if pygame.sprite.spritecollide(self.player, self.walls, False, collided_rect):
            self.player.crash()
        if pygame.sprite.spritecollide(self.player, self.stars, True, collided_circle):
            self.eat_stars_sound.play()
            self.stars_cnt -= 1
        if self.stars_cnt == 0:
            if pygame.sprite.spritecollide(self.player, self.targets, True, collided_circle):
                self.success_sound.play()
                return True  # 获胜
        return False

    def update(self):
        self.stars.update()
        self.stars.draw(self.screen)
        self.targets.update()
        self.targets.draw(self.screen)

        self.player.update()
        success = self.check_collide()
        self.screen.blit(self.player.image, self.player.rect)

        self.walls.update()
        self.walls.draw(self.screen)
        return success  # 返回是否获胜
