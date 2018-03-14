class Solution:
    def encode(self, strs):
        """ 
        type strs: a list of strings
        rtype: an encoded string
        """
        en_str = ''
        for s in strs:
            en_str += str(len(s)) + '#' + s
        return en_str        

    def decode(self, en_str):
        """ 
        type en_str: an encoded string
        rtype: a list of decoded strings
        """
        strs = []
        i = 0
        seqidx = en_str.find('#', i, len(en_str))
        while seqidx != -1:
            num = int(en_str[i: seqidx])
            strs.append(en_str[seqidx + 1: seqidx + 1 + num])
            i = seqidx + num + 1
            seqidx = en_str.find('#', i, len(en_str))
        return strs


strs = ['ab#', '#', '#q@#', 'å', '', '###']
s = Solution()
en_str = s.encode(strs)
print(en_str)
print(s.decode(en_str))


