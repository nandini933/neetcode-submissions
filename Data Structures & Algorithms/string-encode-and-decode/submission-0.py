class Solution:

    def encode(self, strs):
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find '#'
            while s[j] != '#':
                j += 1

            # Length of the original string
            length = int(s[i:j])

            # Extract the string
            start = j + 1
            end = start + length

            result.append(s[start:end])

            # Move to next string
            i = end

        return result
