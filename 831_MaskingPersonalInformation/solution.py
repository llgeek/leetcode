class Solution:
    def maskPII(self, S: str) -> str:
        if '@' in S:
            names = S.split('@')
            return '{}*****{}@{}'.format(names[0][0], names[0][-1], names[1]).lower()
        else:
            digits = list(filter(str.isdigit, S))
            return ['', '+*-', '+**-', '+***-'][len(digits)-10] + '***-***-' + ''.join((digits[-4:]))
