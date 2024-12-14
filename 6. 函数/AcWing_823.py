n = int(input())

path = [0 for _ in range(n)]
used = [False for _ in range(n)]

def dfs(u):
    if u == n:
        for i in range(n):
            print(path[i] + 1, end=' ')
        print()

    for i in range(n):
        if not used[i]:
            used[i] = True
            path[u] = i
            dfs(u + 1)
            used[i] = False
            path[u] = 0

if __name__ == "__main__":
    dfs(0)
