n = int(input())
lst = list(map(int, input().split()))
flag = True
res = 0
while flag:
    count = 0
    for i in range(n-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            count += 1
    if count > 0:
        n -= 1
        res += count
    else:
        flag = False

print(*lst)
print(res)