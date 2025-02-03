nums = list(map(int, input("Masukan Array: ").split()))
x = list(map(int, input("Masukan Array: ").split()))
T = True
for i in range(len(nums)):
    if x[i] != nums[i]:
        T = False
        break
print(T)