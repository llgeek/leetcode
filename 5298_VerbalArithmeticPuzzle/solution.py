from typing import List
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        maxwordlen = max(len(word) for word in words)
        if maxwordlen > len(result) or maxwordlen < len(result) - 1:
            return False
        allchr = set()
        for word in words:
            allchr.update(set(word))
        allchr.update(set(result))
        allchrsort = sorted(allchr)

        def backtracker(nums, begin):
            if begin >= len(nums):
                yield nums[:len(allchrsort)]
            for i in range(begin, len(nums)):
                nums[i], nums[begin] = nums[begin], nums[i]
                for res in backtracker(nums, begin+1):
                    yield res
                nums[i], nums[begin] = nums[begin], nums[i]

        def check_valid(chr2val):
            for word in words:
                if word and chr2val[word[0]] == 0:
                    return False
            if chr2val[result[0]] == 0:
                return False
            carry = 0
            for idx in range(maxwordlen):
                val = [0] * len(words)
                for i in range(len(words)):
                    word = words[i][::-1]
                    if idx >= len(word):
                        continue
                    val[i] = chr2val[word[idx]]
                if idx >= len(result):
                    return False
                levelsum = sum(val)
                carry, levelsum = divmod(levelsum + carry, 10)
                if levelsum != chr2val[result[::-1][idx]]:
                    return False
            if len(result) == maxwordlen + 1:
                return carry == chr2val[result[0]]
            else:
                return carry == 0

        for assignedvals in backtracker(list(range(10)), 0):
            # print(assignedvals)
            chr2val = dict(zip(allchrsort, assignedvals))
            if check_valid(chr2val):
                return True
        return False



if __name__ == "__main__":
    sol = Solution()
    words = ["SEND","MORE"]
    result = "MONEY"
    print(sol.isSolvable(words, result))







        # def helper(chr2num, num2chr, idx, carry):
        #     if idx > maxwordlen or idx > len(result):
        #         return False
        #     val = [0] * len(words)
        #     notassign = set()
        #     for i, word in enumerate(words):
        #         word = word[::-1]
        #         if idx >= len(word):
        #             continue
        #         if word[idx] in chr2num:
        #             val[i] = chr2num[word[idx]]
        #         else:
        #             val[i] = word[idx]
        #             notassign.add(word[idx])
            
        # def generateposs(chrs, num2chr):
        #     assign = {}
        #     usednum = set(num2chr.keys())
        #     for c in chrs:
        #         for num in range(10):
        #             if num in usednum:
        #                 continue
                    






        # words = [word[::-1] for word in words]
        # result = result[::-1]
        # def helper(chr2num, num2chr, idx, carry):
        #     val = [0] * len(words)
        #     for i, word in enumerate(words):
        #         if idx >= len(word):
        #             continue
        #         if word[idx] in chr2num:
        #             val[i] = chr2num[word[idx]]
        #         else:
        #             val[i] = word[idx]
            



        # def helper(allchr, chr2num, wordsidxs, carry, num2chr):
        #     for wordid, idx in enumerate(wordsidxs):
        #         if idx >= len(words[wordid]):
        #             continue
        #         if words[wordid][idx] in 
