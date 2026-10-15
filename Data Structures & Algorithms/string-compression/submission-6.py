class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        groupLen = 1
        currChar = chars[0]
        for i in range(1, len(chars)):
            if chars[i] == currChar:
                groupLen += 1
            else:
                s += currChar + (str(groupLen) if groupLen > 1 else "")
                groupLen = 1
                currChar = chars[i]

        s += currChar + (str(groupLen) if groupLen > 1 else "")   # add last group

        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)