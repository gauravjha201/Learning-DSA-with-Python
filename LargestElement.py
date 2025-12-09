nums=[55,97,-89,98,-99]
largest=float("-inf")
for i in range(0,len(nums)):
    largest=max(largest,nums[i])

print(largest)
