
# keep track of the index of the minimum value
# compare the next value with the value at the minimum index
# if the new value is smaller, update the minimum index with the new value
# after the first iteration, swap the value at the minium index with the first value
# each additional iteration will identify the next smallest element and move it to the immediate right of the previous minium value

# best scenario: O(n) - when a list is already listed
# worst scenario: O(n^2)

def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        # up to but not including len(my_list)
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            # swap my_list[i] with my_list[index]
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list


my_list = [4, 2, 6, 5, 1, 3]

print(selection_sort(my_list))
