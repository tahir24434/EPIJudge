from test_framework import generic_test
from heapq import heapify, heappop, heapreplace


def sort_k_increasing_decreasing_array(A):
    increasing = 1
    sorted_sub_arrays = []

    start_idx = 0
    for i in range(1, len(A)+1):
        if i == len(A) \
                or (A[i] < A[i-1] and increasing) \
                or (A[i] >= A[i-1] and not increasing):
            sorted_sub_arrays.append(A[start_idx:i] if increasing else A[i-1:start_idx-1:-1])
            increasing ^= 1
            start_idx = i

    # merge all sorted arrays
    return merge_sorted_arrays(sorted_sub_arrays)


def merge_sorted_arrays(ssa):
    res = []
    h = [(lst[0], 0, lst_num) for lst_num, lst in enumerate(ssa) if lst]
    heapify(h)

    while len(h):
        elem, elem_idx, lst_num = h[0]
        # If this list has some more elements
        if elem_idx+1 < len(ssa[lst_num]):
            # Pop and replace the smallest item. Also push the new one. heap size does not change
            heapreplace(h, (ssa[lst_num][elem_idx+1], elem_idx+1, lst_num))
        else:
            heappop(h)
        res.append(elem)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sort_increasing_decreasing_array.py",
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
