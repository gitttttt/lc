class TrieNode(object):
    def __init__(self, val):
        """
        Initialize your data structure here.
        """
        self.val = val
        self.child = [None for _ in range(26)]
        self.stop = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in word:
            if not node.child[ord(i)-97]:
                node.child[ord(i)-97] = TrieNode(i)
            node = node.child[ord(i)-97]
        node.stop = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for i in word:
            if not node.child[ord(i)-97]:
                print 'h', i
                return False
            node = node.child[ord(i)-97]
        return node.stop


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for i in prefix:
            if not node.child[ord(i)-97]:
                print 'h', i
                return False
            node = node.child[ord(i)-97]
        return True


trie = Trie()
trie.insert("somestring")
trie.insert('sone')
print trie.startsWith("soa")
