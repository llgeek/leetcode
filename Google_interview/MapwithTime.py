"""
带时间戳的map: put(k, v, timestamp) get(k , timestamp)EX:
put(1, haha , 3) put(1, ha, 5) get(1, 0) -> null get(1, 4) -> haha get(1, 6) -> ha
Follow Up: ArrayList, LinkedList, BST, balancedBST 分别get & put 时间复杂度

Page 1
"""
from collections import defaultdict

class Solution:
    def __init__(self):
        self.TimeMap = defaultdict{lambda : defaultdict{lambda : None})
    def put(self, key, value, timestamp):



    def get(self, key, timestamp):
