def sum_nums(nums):
    """Given list of numbers, return sum of those numbers.

    For example:
      sum_nums([1, 2, 3, 4])

    Should return (not print):
      10
    """  

    # Python has a built-in function `sum()` for this, but we don't
    # want you to use it. Please write this by hand.

    # YOUR CODE HERE
    results = 0
    for i in range(0, len(nums)):
        results = results + nums[i]
    return results

print("sum_nums returned", sum_nums([1, 2, 3, 4]))
