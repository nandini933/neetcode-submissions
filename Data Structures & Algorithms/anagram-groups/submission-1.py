class Solution:
    def groupAnagrams(self, strs):
        dic = {}

        for s in strs:
            count = [0] * 26

            for char in s:
                index = ord(char) - ord('a')
                count[index] += 1

            key = tuple(count)

            if key not in dic:
                dic[key] = []

            dic[key].append(s)

        return list(dic.values())