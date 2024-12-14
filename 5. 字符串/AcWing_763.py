def game_result(action1, action2):
    # Winning combinations
    winning_combinations = {
        ("Hunter", "Gun"): "Player1",
        ("Gun", "Bear"): "Player1",
        ("Bear", "Hunter"): "Player1",
        ("Gun", "Hunter"): "Player2",
        ("Bear", "Gun"): "Player2",
        ("Hunter", "Bear"): "Player2",
    }

    if action1 == action2:
        return "Tie"
    else:
        return winning_combinations.get((action1, action2), "Tie")


T = int(input())
for _ in range(T):
    act1, act2 = input().split()
    print(game_result(act1, act2))
