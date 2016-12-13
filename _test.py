class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if '.' in IP:
            a1 = IP.split('.')
            try:
                if len(a1) == 4 and all(map(lambda x: self.part1(x), a1)):
                    return 'IPv4'
                else:
                    return "Neither"
            except:
                return "Neither"
        elif ':' in IP:
            a2 = IP.split(':')
            if len(a2) == 8 and all(map(lambda x: self.part2(x), a2)):
                return 'IPv6'
            else:
                return "Neither"
        else:
            return "Neither"

    def part1(self, s):
        if not all(map(lambda x: x.isdigit(), s)):
            return False
        if len(s) > 1 and s[0] == '0':
            return False
        return 0 <= int(s) <= 255

    def part2(self, s):
        alf = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F']
        return 1 <= len(s) <= 4 and all(map(lambda x: x.isdigit() or x in alf , s))

print Solution().validIPAddress("172.16.254.-1")