class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pointerS, pointerT = 0, 0

        while pointerS < len(s) and pointerT < len(t):
            if s[pointerS] == t[pointerT]:
                pointerT += 1
            pointerS += 1

        return len(t) - pointerT