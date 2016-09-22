class Node(object):
    def __init__(self, val):
        self.val = val
        self.child = []
        self.yes = False

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = Node(0)


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        root = self.root
        for i in range(len(word)):
            if word[i] not in map(lambda x: x.val, root.child):
                root.child.append(Node(word[i]))
            root = root.child[map(lambda x: x.val, root.child).index(word[i])]
        root.yes = True

    def search(self, word):
        return self.query(word, self.root)

    def query(self, word, root):
        for i in range(len(word)):
            if word[i] != '.':
                if word[i] in map(lambda x: x.val, root.child):
                    root = root.child[map(lambda x: x.val, root.child).index(word[i])]
                else:
                    return False
            else:
                if not root.child:
                    return False
                else:
                    return reduce(lambda x, y: x or y, map(lambda x: self.query(word[i+1:], x), root.child))
        return root.yes

a = WordDictionary()
a.addWord('a')
print a.search('.')
