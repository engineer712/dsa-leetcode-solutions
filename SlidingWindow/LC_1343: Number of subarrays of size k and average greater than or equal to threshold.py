class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        ans = 0
        sm = 0
        i = 0

        for j in range(len(arr)):
            sm += arr[j]

            if j - i + 1 == k:
                if sm >= k * threshold:
                    ans += 1
                sm -= arr[i]
                i += 1

        return ans
