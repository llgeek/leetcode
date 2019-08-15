from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        acc = 1
        curchar = chars[0]
        for idx, c in enumerate(chars[:]):
            if not curchar:
        