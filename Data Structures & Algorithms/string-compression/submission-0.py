class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        first_char = chars[0]
        num = 1
        write = 0
        chars[write] = first_char
        write += 1

        for i in range(1, len(chars)):
            if chars[i] == first_char:
                num += 1
                if i == len(chars) - 1 and num > 1:
                    for c in str(num):
                        chars[write] = c
                        write += 1
            else:
                if num > 1:
                    for c in str(num):
                        chars[write] = c
                        write += 1
                first_char = chars[i]
                num = 1
                chars[write] = first_char
                write += 1

        return write