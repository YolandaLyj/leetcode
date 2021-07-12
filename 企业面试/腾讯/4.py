import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    d = {}
    result = 0

    def patition(nums):
        global result
        resmax,resmin = max(nums),min(nums)
        aq = (resmax + resmin) / 2
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[r] <= aq:
                while l < r and nums[l] <= aq:
                    l += 1
                if l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    flag = 1
                else:
                    break
            else:
                r -= 1
        mid = len(nums)
        for k in range(r, len(nums)):
            if nums[k] > aq:
                mid = k
                break
        left = tuple(nums[0:mid])
        if len(left)==len(nums):
            if left not in d:
                d[left] = 1
                result += sum(left)
        else:
            right = tuple(nums[mid:len(nums)])
            if left not in d:
                d[left] = 1
                result += sum(left)
            if right not in d:
                d[right] = 1
                result += sum(right)
            if len(left) > 1:
                patition(nums[0:mid])
            if len(right) > 1:
                patition(nums[mid:len(nums)])

    patition(a)
    print(result)