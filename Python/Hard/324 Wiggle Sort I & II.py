"""
why randomized improve the quick select performance?
The worst case of quick select sort is the original array is already sort
in this case we need O(n^2) time to sort, if we choose first or last element
[1,2,3,4,5]
will choose 1,2,3..5 to each time, worst case is O(n^2)

Randomized select pivot index will make the sort run time not depend on whether
the original arr is sort or not, and close to O(nlogn)

# Quick select to find median in O(n) time on average, 
    O(n^2) in worst case. Taking O(1) memory.
# quick sort time & space
T(n) = 2T(n / 2) + n
n = n/(2^(m-1))
T(n) = n*T[1] + nlogn  =  n + nlogn
when n -> infi nlogn much larger than n so nlogn
"""


class Solution:
    def wiggleSort1(nums) -> None:

        #         O(nlogn) sort and arrange
        #         [1, 5, 1, 1, 6, 4]
        #          0  1  2  3  4  5

        #         [1, 1, 1, 4, 5, 6]
        #             6     5     4

        """
        # s = sorted(nums)
        # for i in range(1, len(nums), 2):
        #     nums[i] = s.pop()
        # for i in range(0, len(nums), 2):
        #     nums[i] = s.pop()



#         O(n) + O(n)
#         the key for this question is to find the median of this array -> quick select
#         and rearrange the arr to three part
#         """
        import random

        n = len(nums)
        if n < 2:
            return

        def quick_select_median(nums, m):
            s, e = 0, len(nums) - 1
            while True:
                pivot = nums[random.randint(s, e)]
                i, j, k = s, s, e
                while j <= k:
                    if nums[j] < pivot:  # belong to smaller part
                        nums[i], nums[j] = nums[j], nums[i]
                        j += 1
                        i += 1
                    elif nums[j] > pivot:  # larger part
                        nums[j], nums[k] = nums[k], nums[j]
                        k -= 1
                    else:
                        j += 1
                # ?
                if i <= m - 1 <= k:
                    return pivot
                elif m - 1 < i:
                    e = i - 1
                else:
                    s = i + 1

        mid_idx = (n + 1) // 2
        md = quick_select_median(nums, mid_idx)
        print(nums)
        # 1 1 1 3 4 6
        # 0 1 2 3 4 5
        # arr = [0 for _ in range(n)]
        # # !!! we want to start from the end of smaller part not median
        # i = n // 2 - 1 if n % 2 == 0 else n // 2
        # j = n - 1
        #
        # for idx in range(len(arr)):
        #     if idx % 2 != 0:
        #         arr[idx] = nums[i]
        #         i -= 1
        #     else:
        #         arr[idx] = nums[j]
        #         j -= 1
        #
        # # even return arr
        # for i in range(len(nums)):
        #     nums[i] = arr[i]
        #
        # return nums
        """
        O(n) + O(1)
        the purpose is to find the index
        we could somehow find the mapping relation from origin index to final answer
        """

        def map_idx(i):
            # n | 1 make n become the first larger or equal number even number
            # example for even length arr with index [0,1,2,3,4,5]
            # we already divide into three parts
            # left part follow the k = 2 * i + 1 is ok
            # but right part should mod some number
            k = 2 * i + 1
            if k < n:
                return k
            else:
                return k % (n | 1)

        i, j, cur = 0, n - 1, 0
        while cur <= j:
            if nums[map_idx(cur)] < md:
                nums[map_idx(i)], nums[map_idx(cur)] = nums[map_idx(cur)], nums[map_idx(i)]
                i += 1
                cur += 1
            elif nums[map_idx(cur)] > md:
                nums[map_idx(j)], nums[map_idx(cur)] = nums[map_idx(cur)], nums[map_idx(j)]
                j -= 1
            else:
                cur += 1

        return nums
print(Solution.wiggleSort1([1,5,1,1,6,4]))
