import pygame
import config
from game_manager import GameManager
from utils.draw_text import draw_text

pygame.init()
pygame.mixer.init()  # 初始化声音
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
clock = pygame.time.Clock()

ico = pygame.image.load("static/images/maze.png").convert()
pygame.display.set_icon(ico)
pygame.display.set_caption("汽车迷宫")

pygame.mixer.music.load("static/sounds/bgm.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)  # 参数-1表示循环播放

game_manager = GameManager(screen, 1)

running = True
success_time = -1  # -1表示当前没有获胜，否则表示获胜的时刻
success_finished = False  # 是否已通关
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif success_finished and event.type == pygame.KEYDOWN:  # 如果已通关，则按任意键结束
            running = False

    if success_finished:
        screen.fill("black")
        draw_text(screen, "Win!", 200, config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT / 2)
    else:
        if success_time >= 0:
            if pygame.time.get_ticks() - success_time > 2000:  # 如果获胜后已经等待了2秒，则加载下一关
                has_next = game_manager.next_level()
                if not has_next:  # 如果没有下一关，则游戏结束
                    success_finished = True
                    continue
                success_time = -1   # 将获胜时间清空
        screen.fill("black")
        if game_manager.update():
            success_time = pygame.time.get_ticks()  # 更新获胜时刻

    pygame.display.flip()
    clock.tick(config.FPS)

pygame.quit()
