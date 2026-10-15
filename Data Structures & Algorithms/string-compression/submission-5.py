class Solution:
    def compress(self, chars: List[str]) -> int:
        first_char = chars[0]
        out = ""
        num = 1
        out += (first_char)
        for i in range(1, len(chars)) : 
            if chars[i] == first_char: 
                num += 1
                if i == len(chars) - 1 and num > 1: 
                    for c in str(num) : 
                        out += (c)
            else : 
                if num > 1 : 
                    for c in str(num) : 
                        print(c)
                        out += (c)
                first_char = chars[i]
                num = 1 
                out += (first_char)
        for i in range(len(out)) :
            chars[i] = out[i]
        return len(out)

