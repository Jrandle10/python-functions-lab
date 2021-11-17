# Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

# For example:
            # largest([1, 2, 3, 4, 0])  # returns 4
# largest([10, 4, 2, 231, 91, 54])  # returns 231

def largest(nums):
  largest = 0
  for num in nums:
    if num > largest:
      largest = num
  return largest

print(largest([1, 2, 3, 4 ,5 ,6]))

print(largest([10, 8, 552, 37, 87, 99]))