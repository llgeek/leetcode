class Solution:
    def validIPAddress(self, IP: 'str') -> 'str':
        def validDecNumber(numstr):
            if not numstr:
                return False
            if len(numstr) > 1 and numstr[0] == '0':
                return False
            if not numstr.isdigit():
                return False
            if int(numstr) > 255 or int(numstr) < 0:
                return False
            return True
        def isIPv4(IP):
            if '.' not in IP:
                return False
            IPs = IP.split('.')
            if len(IPs) != 4:
                return False
            for numstr in IPs:
                if not validDecNumber(numstr):
                    return False
            return True

        def validHexNumber(numstr):
            if not numstr:
                return False
            if len(numstr) > 4:
                return False
            for c in numstr:
                if c not in '0123456789abcdefABCDEF':
                    return False
            return True
                
        def isIPv6(IP):
            if ':' not in IP:
                return False
            IPs = IP.split(':')
            if len(IPs) != 8:
                return False
            for numstr in IPs:
                if not validHexNumber(numstr):
                    return False
            return True

        if isIPv4(IP):
            return 'IPv4'
        if isIPv6(IP):
            return 'IPv6'
        return 'Neither'


"20EE:Fb8:85a3:0:0:8A2E:0370:7334"
