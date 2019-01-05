"""
version in CLRS textbook, page 1006
"""


def compute_prefix(pattern):
    k = 0
    pi = [0] * len(pattern)
    for m in range(1, len(pattern)):
        while k > 0 and pattern[k] != pattern[m]:
            k = pi[k-1]
        if pattern[k] == pattern[m]:
            k += 1
        pi[m] = k
    return pi

def kmp_match(text, pattern):
    pi = compute_prefix(pattern)
    k = 0
    matched_idx = []
    for n in range(0, len(text)):
        while k > 0 and pattern[k] != text[n]:
            k = pi[k-1]
        if pattern[k] == text[n]:
            k += 1

        if k == len(pattern):
            matched_idx.append(n - k + 1)
            k = pi[k-1]
    return matched_idx


if __name__ == '__main__':
    # p = 'ababca'
    # text = 'bacbababcabacbead'
    # p = 'issipi'
    p = 'sis'
    text = 'mississisppi'

    print(kmp_match(text, p))
            

