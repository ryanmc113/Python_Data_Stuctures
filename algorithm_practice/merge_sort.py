def mergeSort(arr):
    if len(arr) < 1:
        return arr

    middle_index = arr // 2
    left_list = arr[:middle_index]
    right_list = arr[middle_index:]
    return merge()


def merge(left_list, right_list):
    return False
