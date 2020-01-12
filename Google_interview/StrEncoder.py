"""
Given a string : aabbcb, it's encoded as 2xa2xbcb. Write the enocoder
"""
def encoder(s):
    res = []
    pre, cnt = '', 0
    for c in s:
        if pre != c:
            if cnt > 1:
                res.append('{}x{}'.format(cnt, pre))
            elif cnt == 1:
                res.append(pre)
            pre = c
            cnt = 1
        else:
            cnt += 1
    if cnt:
        res.append("{}x{}".format(cnt, pre) if cnt > 1 else pre)
    return "".join(res)


s = "aabbcb"
print(encoder(s))

