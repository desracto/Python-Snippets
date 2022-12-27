# Binary Search using a recursive method

number_list = list(range(0, 10000))
def BinarySearch(number, number_list):
    if len(number_list) == 1:
        if number_list[0] == number:
            print("Found")
            return number_list[0]
        else:
            return -1
    else:
        half = len(number_list) // 2
        if number < number_list[half]:
            print(number_list[:half])
            return BinarySearch(number, number_list[:half])
        else:
            print(number_list[half:])
            return BinarySearch(number, number_list[half:])

if __name__ == "__main__":
    print(BinarySearch(2, number_list))
