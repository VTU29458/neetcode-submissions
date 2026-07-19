from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Build frequency map
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Step 2: Create buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        # Step 3: Traverse buckets from highest frequency
        ans = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans