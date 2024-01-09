def calculate_average(nums1):
    total = sum(nums1)
    count = len(nums1)
    average = total / count
    return average


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
