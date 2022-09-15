import sys
sys.stdin = open('sample_input.txt')


def find_cnt(x, y, h):
    di = [1, 1, -1, -1]         # 우하, 좌하, 좌상, 우상
    dj = [1, -1, -1, 1]




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * 101

