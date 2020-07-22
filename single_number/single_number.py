'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    duplicates = []
    map = {}
    size = len(arr)
    index = 1
    for i in arr:
        if i == index:
            duplicates.append(i)
            index += 1
    return duplicates


    # for i in arr:
    #     j = i + 1
    #     if i == size:
    #         duplicates.append(i)
    #     else:
    #         return duplicates


# def new_func(arr):
#     duplicates = []
#     size = len(arr)
#
#     index = 0
#     # for i in arr:
#     #     if i == arr[index]:
#     # #         index += 1
#     # #         return arr
#     for i in arr:
#         if i not in duplicates:
#             duplicates.append(i)
#
#
#     print(duplicates)

    # for i in range(len(arr)):
    #     for j in range(i + 1, len(arr)):
    #         if j == i:
    #             duplicates.append(j)
    #         return arr




# if __name__ == '__main__':
#     # Use the main function to test your implementation
#     arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
#
#     print(f"The odd-number-out is {single_number(arr)}")


arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]


print(single_number(arr))
