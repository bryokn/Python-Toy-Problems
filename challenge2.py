def digit_sum(n):
    """Calculate the sum of the digits of a number."""
    sum_of_digits = 0
    for digit in str(n):
        sum_of_digits += int(digit)
    return sum_of_digits

def solution(A):
    digit_sums = {}
    
    for num in A:
        sum_of_digits = digit_sum(num)
        if sum_of_digits in digit_sums:
            digit_sums[sum_of_digits].append(num)
        else:
            digit_sums[sum_of_digits] = [num]
    
    max_pair_sum = -1
    for sum_of_digits, numbers in digit_sums.items():
        if len(numbers) >= 2:
            numbers.sort(reverse=True)
            pair_sum = sum(numbers[:2])
            max_pair_sum = max(max_pair_sum, pair_sum)
    
    return max_pair_sum