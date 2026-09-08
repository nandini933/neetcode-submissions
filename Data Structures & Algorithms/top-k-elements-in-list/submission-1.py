class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Count frequency
        dic = {}

        for num in nums:
            dic[num] = dic.get(num, 0) + 1

        # Step 2: Create buckets
        bucket = [[] for _ in range(len(nums) + 1)]

        # Step 3: Put each number into its frequency bucket
        for num in dic:
            frequency = dic[num]
            bucket[frequency].append(num)

        # Step 4: Take elements from highest frequency
        result = []

        for frequency in range(len(nums), 0, -1):
            for num in bucket[frequency]:
                result.append(num)

                if len(result) == k:
                    return result
            
        