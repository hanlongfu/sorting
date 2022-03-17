# 1. create max heap
#   - by representing array as binary tree
#   - build max heap function will build the max heap (parent larger than its children)
# 2. remove largest item
#    - remove the root (largest item) and replace it with the smallest node
# 3. call heapify to ensure it is a max heap

# use minimum heap
def heapify(my_list, n, i):
    smallest = i
    # left and right child node
    l = 2*i + 1
    r = 2*i + 2
    if l < n and my_list[l] < my_list[smallest]:
        smallest = l

    if r < n and my_list[r] < my_list[smallest]:
        smallest = l

    if smallest != i:
        my_list[i], my_list[smallest] = my_list[smallest], my_list[i]
        heapify(my_list, n, smallest)


def heap_sort(my_list):
    n = len(my_list)

    # build the heap tree
    for i in range(int(n/2)-1, -1, -1):
        heapify(my_list, n, i)

    for i in range(n-1, 0, -1):
        my_list[i], my_list[0] = my_list[0], my_list[i]
        heapify(my_list, i, 0)
    my_list.reverse()
    return my_list


my_list = [2, 1, 5, 7, 9, 10, 3, 11, 8]
print(heap_sort(my_list))
