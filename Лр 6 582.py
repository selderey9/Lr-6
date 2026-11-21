list1 = list(map(int, input("Input your numbers(list1):").split()))
list2 = list(map(int, input("Input your numbers(list2):").split()))
count = 0
for i in list1:
    for n in list2:
        if i == n:
            count += 1
print(count)
