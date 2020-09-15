 
def merge(left_list, right_list):

    result_list = []

    # while left and right list has elements
    while left_list and right_list:
        if left_list[0] < right_list[0]:
            result_list.append(left_list[0])
            left_list.pop(0)
        else:
            result_list.append(right_list[0])
            right_list.pop(0)

    #left list still contain elements. Append its contents to end of the result list
    if left_list:
        result_list.extend(left_list)
    else:
    #right list still contain elements. Append its contents to end of the result list
        result_list.extend(right_list)
    
    return result_list


def mergesort(list_of_items):
    list_len = len(list_of_items)

    # base case
    if list_len < 2:
        return list_of_items
    left_list = list_of_items[:list_len // 2]   # //
    right_list = list_of_items[list_len // 2:]  # "//" to force division

    # merge sort left and right list recursively
    left_list = mergesort(left_list)
    right_list = mergesort(right_list)
    return merge(left_list, right_list)

list_test = [21, 1, 26, 45, 3, 3, 4, 27, 43, 34, 46, 40]
new_list = mergesort(list_test)
for item in new_list:
    print(item, end = ', ')
