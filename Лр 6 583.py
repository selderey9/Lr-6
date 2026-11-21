list1 = list(map(int, input("Input your numbers(list1):").split()))
list2 = list(map(int, input("Input your numbers(list2):").split()))
nums = set()
for i in list1:
    for n in list2:
        if i == n:
            nums.add(i)
numbers = list(nums)
print(*numbers[::-1])
