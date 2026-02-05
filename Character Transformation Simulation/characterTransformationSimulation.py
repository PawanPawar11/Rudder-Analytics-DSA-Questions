class Solution:
    def transformString(self, s: str, k: int) -> str:
        k %= 26
        vowels = {'a','e','i','o','u'}
        result = []

        for ch in s:
            pos = ord(ch) - ord('a')

            if ch in vowels:
                pos = (pos - k) % 26
            else:
                pos = (pos + k) % 26

            result.append(chr(ord('a') + pos))

        return "".join(result)
