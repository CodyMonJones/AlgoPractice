# Time: O(nLog(n)) | Space: O(1)
# def two_number_sum(array, target_sum):
#     array.sort()
#     right_index = len(array) - 1
#     left_index = 0

#     while left_index < right_index:
#         val_check = array[right_index] + array[left_index]
#         if val_check > target_sum:
#             right_index -= 1
#         elif val_check < target_sum:
#             left_index += 1
#         elif val_check == target_sum:
#             return[array[left_index], array[right_index]]
#     return []

#Time: O(n) | Space: O(n)
def two_number_sum(array, target_sum):
    seen = {}

    for num in array:
        target_val = target_sum - num
        if target_val in seen:
            return num, target_val
        else:
            seen[num] = target_val
    return []


print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))
