import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon = {}
for i in range(1, N+1):
    pp = input().rstrip()
    pokemon[pp] = i
    pokemon[str(i)] = pp

for _ in range(M):
    w = input().rstrip()
    print(pokemon[w])