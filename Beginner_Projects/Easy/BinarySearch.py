number_list = list(range(0, 60000000))
num_list = list(range(0, 10))

# Binary Search using a recursive method
def Recursive_BinarySearch(target, number_list, high, low):
    mid = (high + low) // 2
    if target < number_list[mid]:
        return Recursive_BinarySearch(target, number_list, mid - 1, 0)
    elif target > number_list[mid]:
        return Recursive_BinarySearch(target, number_list, high, mid + 1)
    else:
        if target == number_list[mid]:
            return number_list[mid]
        else:
            return -1

# Binary Search using a iterative method
def Iterative_BinarySearch(target, list):
    max_index = len(list) - 1
    min_index = 0

    while max_index >= min_index:
        half = (max_index + min_index) // 2
        if target < list[half]:
            max_index = half + 1
        elif target > list[half]:
            min_index = half + 1
        else:
            return list[half]

    return -1

if __name__ == "__main__":
    print(Recursive_BinarySearch(5000, number_list, len(number_list), 0))
