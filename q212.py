class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        board = map(lambda x: list(x), board)
        trie = Trie()
        res = []
        for i in words:
            trie.insert(i)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, trie.root, res)
        return res

    def dfs(self, board, x, y, trie, res):
        if board[x][y] == '#' or not trie.arr[ord(board[x][y]) - ord('a')]:
            return
        c = board[x][y]
        board[x][y] = '#'
        trie = trie.arr[ord(c) - ord('a')]
        if trie.word != '' and trie.word not in res:
            res.append(trie.word)
        if x > 0:
            self.dfs(board, x-1, y, trie, res)
        if x < len(board)-1:
            self.dfs(board, x+1, y, trie, res)
        if y > 0:
            self.dfs(board, x, y-1, trie, res)
        if y < len(board[0])-1:
            self.dfs(board, x, y+1, trie, res)
        board[x][y] = c


class TrieNode:
    def __init__(self, s):
        self.val = s
        self.arr = [None for _ in range(26)]
        self.word = ''

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
        node.word = s


b = ["seenew","tmriva","obsibd","wmysen","ltsnsa","iezlgn"]
w = ["pluma","holm","lippen","trag","milla","bietle","upbind","waxy","knead","nickle","reem","skice","unde","hain","savant","tryt","ribose","niton","lysis","bedad"]

print Solution().findWords(b,w)
