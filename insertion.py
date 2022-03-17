
# start with the second item in the list
# compare it with the item before it
# if it is less than the item before, switch
# keep doing this until there's no item before that's larger


def insertion_sort(my_list):
    # start with the second item
    for i in range(1, len(my_list)):
        # hold the value at index i
        temp = my_list[i]
        j = i - 1   # item before i
        # i < j, but j can't be out of bounds
        while temp < my_list[j] and j > -1:
            # swap items
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            # decrement j so i can be compared against more items to the left
            j -= 1
    return my_list


my_list = [4, 2, 6, 5, 1, 3]

print(insertion_sort(my_list))
