

# merge helper method
def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    # move the remaining items
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


# merge
# 1) breaks lists in half
# 2) base case: when len(the_list) is 1
# 3) use merge() to put lists together

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    # takes care when it is decimal
    mid = int(len(my_list)/2)
    # 0 up to but not including mid
    left = my_list[:mid]
    right = my_list[mid:]
    return merge(merge_sort(left), merge_sort(right))


print(merge_sort([3, 1, 4, 2]))


