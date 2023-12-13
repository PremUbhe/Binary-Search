def binary_search(input_array, value):
    L = 0
    U = len(input_array)-1

    while L <= U:
        mid = (L+U) // 2

        if input_array[mid] == value:
            return mid
        else:
            if input_array[mid] > value:
                U = mid - 1
            else:
                L = mid + 1

    return -1



test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15

print(binary_search(test_list, test_val2))
print(binary_search(test_list, test_val1))
