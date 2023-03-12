x, y, w, h = map(int, input().split())

l = [w-x, x, y, h-y]
print(min(l))