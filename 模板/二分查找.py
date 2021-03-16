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

print(solve([1,4,4,6,6,7,7,8,8], 8))