from typing import List


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        g: List[str] = ["a", "b"] if x > y else ["b", "a"]
        p: List[int] = sorted([x, y])
        res: int = 0
        for _ in range(2):
            t: List[str] = []
            for c in s:
                t.append(c)
                if t[-2:] == g:
                    del t[-2:]
                    res += p[1]
            s = t
            g = g[::-1]
            p = p[::-1]
        return res
