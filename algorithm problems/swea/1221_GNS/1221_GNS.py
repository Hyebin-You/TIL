import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())

for _ in range(T):
    tc, N = input().split()
    N = int(N)
    arr = list(input().split())
    num_arr = [0] * N

    num_dict = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
    num_dict_reverse = {v:k for k,v in num_dict.items()}

    for i in range(N):
        num_arr[i] = num_dict[arr[i]]

    # num_arr.sort()
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if num_arr[min_idx] > num_arr[j]:
                min_idx = j
        num_arr[i], num_arr[min_idx] = num_arr[min_idx], num_arr[i]


    print(tc)
    for i in range(N):
        print(num_dict_reverse[num_arr[i]], end=' ')
    print()