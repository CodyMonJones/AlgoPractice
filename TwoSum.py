# Time: O(nLog(n)) | Space: O(1)
def two_number_sum(array, target_sum):
    array.sort()
    right_index = len(array) - 1
    left_index = 0

    while left_index < right_index:
        val_check = array[right_index] + array[left_index]
        if val_check > target_sum:
            right_index -= 1
        elif val_check < target_sum:
            left_index += 1
        elif val_check == target_sum:
            return[array[left_index], array[right_index]]
    return []


