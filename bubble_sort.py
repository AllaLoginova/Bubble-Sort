n = int(input())   # длина списка
lst = list(map(int, input().split()))

flag = True
res = 0   # общее количество перестановок

while flag:
    count = 0  # количество перестановок за 1 проход по списку
    for i in range(n-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            count += 1
    if count > 0:   # если была хотя бы 1 перестановка
        n -= 1
        res += count
    else:
        flag = False # выходим из цикла

print(*lst) # отсортированный список
print(res) # общее количество перестановок
