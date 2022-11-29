a, b = map(int, input().split())

cnt = 0
tmp = a/(cnt+1)**0.5+cnt

while True:
    cnt += 1
    if tmp > a/(cnt+1)**0.5+cnt:
        tmp = a/(cnt+1)**0.5+cnt
    else:
        break
    
print(tmp)