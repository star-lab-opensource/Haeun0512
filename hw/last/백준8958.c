t = int(input())
for _ in range(t):
    line = input()
    score = 0
    streak = 0
    for ch in line:
        if ch == 'O':
            streak += 1
            score += streak
        else:
            streak = 0
    print(score)
