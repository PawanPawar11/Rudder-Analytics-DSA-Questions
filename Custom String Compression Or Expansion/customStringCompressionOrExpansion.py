class Solution:
    def decodeString(self, s: str) -> str:
        str_stack = []
        num_stack = []

        curr = ""
        num = 0
        i = 0

        while i < len(s):
            ch = s[i]

            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == "[":
                str_stack.append(curr)
                num_stack.append(num)
                curr = ""
                num = 0

            elif ch == "]":
                repeat = num_stack.pop()
                prev = str_stack.pop()
                curr = prev + curr * repeat

            else:  # letter
                curr += ch

                # handle a10 style
                j = i + 1
                if j < len(s) and s[j].isdigit():
                    count = 0
                    while j < len(s) and s[j].isdigit():
                        count = count * 10 + int(s[j])
                        j += 1
                    curr += ch * (count - 1)
                    i = j - 1

            i += 1

        return curr
