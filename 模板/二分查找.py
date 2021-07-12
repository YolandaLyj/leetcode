# int solve(vector<int> &T, int K) {
#     int l = 0, r = 20000000;
#     while (l + 1 < r) {
#         int mid = (l + r) / 2;
#         if (check(T, K, mid)) {
#             r = mid;
#         } else {
#             l = mid;
#         }
#     }
#     return check(T, K, l) ? l : r;
# }

# https://blog.csdn.net/Li______/article/details/104194669
# https://cloud.tencent.com/developer/article/1434845

def solve(T, K):
    l,r = 0,len(T)-1
    while l+1<r:
        m = int((l+r)/2)
        if T[m]>K:
            r=m
        else:
            l=m
    return l if K==T[l] else r



# 查找恰好等于target的（如果要查找第一个恰好等于的或者最后一个恰好等于的，根据后面的>=和<=修改即可）
# 二分查找，返回下标，不存在返回-1

def binary_search_1(nums, target, begin, end):
    if begin == end:
        return -1
    mid = begin + (end - begin - 1) // 2
    if target < nums[mid]:
        return binary_search_1(nums, target, begin, mid)
    elif target > nums[mid]:
        return binary_search_1(nums, target, mid + 1, end)
    else:
        return mid
        
# 查找第一个>=target的（若相等则返回最左边的）
def binary_search_2(nums, target, begin, end):
    if begin + 1 == end:
        return begin
    mid = begin + (end - begin - 1) // 2
    if target <= nums[mid]:
        return binary_search_2(nums, target, begin, mid + 1)
    else:
        return binary_search_2(nums, target, mid + 1, end)
# 查找最后一个<=target的（若相等则返回最右边的）
def binary_search_3(nums, target, begin, end):
    if begin + 1 == end:
        return begin
    mid = begin + (end - begin) // 2
    if target < nums[mid]:
        return binary_search_3(nums, target, begin, mid)
    else:
        return binary_search_3(nums, target, mid, end)
# 查找第一个>target的
def binary_search_4(nums, target, begin, end):
    if begin + 1 == end:
        return begin
    mid = begin + (end - begin - 1) // 2
    if target < nums[mid]:
        return binary_search_4(nums, target, begin, mid + 1)
    else:
        return binary_search_4(nums, target, mid + 1, end)
# 查找最后一个<target的
def binary_search_5(nums, target, begin, end):
    if begin + 1 == end:
        return begin
    mid = begin + (end - begin) // 2
    if target <= nums[mid]:
        return binary_search_5(nums, target, begin, mid)
    else:
        return binary_search_5(nums, target, mid, end)


# print(solve([1,4,4,6,6,7,7,8,8], 8))




# 在 a 中找到 x 合适的插入点以维持有序。参数 lo 和 hi 可以被用于确定需要考虑的子集；默认情况下整个列表都会被使用。如果 x 已经在 a 里存在，那么插入点会在已存在元素之前（也就是左边）。如果 a 是列表（list）的话，返回值是可以被放在 list.insert() 的第一个参数的。
# 返回的插入点 i 可以将数组 a 分成两部分。左侧是 all(val < x for val in a[lo:i]) ，右侧是 all(val >= x for val in a[i:hi]) 。
print(bisect.bisect_left(a, x, lo=0, hi=len(a)))
print(bisect.bisect_right(a, x, lo=0, hi=len(a)))

# 类似于 bisect_left()，但是返回的插入点是 a 中已存在元素 x 的右侧。
# 返回的插入点 i 可以将数组 a 分成两部分。左侧是 all(val <= x for val in a[lo:i])，右侧是 all(val > x for val in a[i:hi]) for the right side。
print(bisect.bisect(a, x, lo=0, hi=len(a)))

# 将 x 插入到一个有序序列 a 里，并维持其有序。如果 a 有序的话，这相当于 a.insert(bisect.bisect_left(a, x, lo, hi), x)。要注意搜索是 O(log n) 的，插入却是 O(n) 的。
bisect.insort_left(a, x, lo=0, hi=len(a))
print(a)
bisect.insort_right(a, x, lo=0, hi=len(a))
print(a)
# 类似于 insort_left()，但是把 x 插入到 a 中已存在元素 x 的右侧。
bisect.insort(a, x, lo=0, hi=len(a))
print(a)