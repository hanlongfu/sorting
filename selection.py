
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


print(selection_sort([4, 2, 6, 5, 1, 3]))
