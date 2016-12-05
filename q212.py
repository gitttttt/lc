class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        s = []
        visit = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        trie = Trie()
        res = set()
        for i in words:
            trie.insert(i)
        for i in range(len(board)):
            for j in range(len(board[0])):
                s.append(board[i][j])
                visit[i][j] = True
                if trie.isWord(s):
                    res.add(''.join(s))
                if trie.isPredix(s):
                    self.dfs(board, visit, i, j, s, trie, res)
                s.pop()
                visit[i][j] = False
        return list(map(lambda x: ''.join(x), res))

    def dfs(self, board, visit, x, y, s, trie, res):
        a = [-1, 0, 1, 0]
        b = [0, -1, 0, 1]

        for i in range(4):
                if self.isValid(board, visit, x+a[i], y+b[i]):
                    s.append(board[x+a[i]][y+b[i]])
                    visit[x+a[i]][y+b[i]] = True
                    if trie.isWord(s):
                        res.add(''.join(s))
                    if trie.isPredix(s):
                        self.dfs(board, visit, x+a[i], y+b[i], s, trie, res)
                    s.pop()
                    visit[x+a[i]][y+b[i]] = False


    def isValid(self, board, visit, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0]) and not visit[x][y]

class TrieNode:
    def __init__(self, s):
        self.val = s
        self.arr = [None for _ in range(26)]
        self.stop = False

class Trie:
    def __init__(self):
        self.root = TrieNode('')

    def insert(self, s):
        node = self.root
        for i in s:
            index = ord(i) - ord('a')
            if not node.arr[index]:
                node.arr[index] = TrieNode(i)
            node = node.arr[index]
        node.stop = True

    def isPredix(self, s):
        node = self.root
        for i in s:
            index = ord(i) - ord('a')
            if not node.arr[index]:
                return False
            node = node.arr[index]
        return True

    def isWord(self, s):
        node = self.root
        for i in s:
            index = ord(i) - ord('a')
            if not node.arr[index]:
                return False
            node = node.arr[index]
        return node.stop

b= ["baabab","abaaaa","abaaab","ababba","aabbab","aabbba","aabaab"]
w = ["aab"
 "bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]
print Solution().findWords(b, w)

print len(b), len(w)

print ['aabbbbabbaababaaaabababbaaba', 'abaabbbaaaaababbbaaaaabbbaab', 'ababaababaaabbabbaabbaabbaba']