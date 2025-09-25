# https://codeforces.com/problemset/problem/339/A

nums = list(map(int, input().split("+")))

nums.sort()

for i in range(len(nums) - 1):
    print(f"{nums[i]}+", end="")

print(f"{nums[-1]}")