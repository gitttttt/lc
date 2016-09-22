class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        tmp = preorder.split(",")
        res = []
        for i in tmp:
            res.append(i)
            while len(res) > 2:
                if res[-1] == "#" and res[-2] == "#" and res[-3] != "#":
                    res.pop()
                    res.pop()
                    res[-1] = "#"
                else:
                    break
            print res
        return len(res) == 1 and res[0] == "#"

print Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")