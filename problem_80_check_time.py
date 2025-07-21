def count_positive_sum_negative(arr):
    count_pos = 0
    sum_neg = 0
    for num in arr:
        if str(num).startswith('-'):
            sum_neg += num
        else:
            count_pos += 1
    return count_pos, sum_neg
# 16 minutes