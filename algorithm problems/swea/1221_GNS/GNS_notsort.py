import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())

for _ in range(T):
    tc, N = input().split()
    N = int(N)
    arr = list(input().split())

    num_dict = {'ZRO':0, 'ONE':0, 'TWO':0, 'THR':0, 'FOR':0, 'FIV':0, 'SIX':0, 'SVN':0, 'EGT':0, 'NIN':0}
    for word in arr:
        num_dict[word] += 1

    print(tc)
    for k, v in num_dict.items():
        for _ in range(v):
            print(k, end=' ')
    print()