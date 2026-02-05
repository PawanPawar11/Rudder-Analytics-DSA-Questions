class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        for _ in range(n - 1):
            next_str = ""
            count = 1

            for i in range(1, len(result)):
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    next_str += str(count) + result[i - 1]
                    count = 1

            # last group
            next_str += str(count) + result[-1]
            result = next_str

        return result
