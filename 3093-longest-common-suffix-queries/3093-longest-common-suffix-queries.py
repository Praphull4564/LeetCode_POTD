class TrieNode:
    __slots__ = ("children", "idx")

    def __init__(self):
        self.children = {}
        self.idx = -1


class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):
        root = TrieNode()

        # index of shortest word overall
        best = min(range(len(wordsContainer)),
                   key=lambda i: len(wordsContainer[i]))

        root.idx = best

        # Build reversed trie
        for i, word in enumerate(wordsContainer):
            node = root

            # update shortest index
            if len(word) < len(wordsContainer[node.idx]):
                node.idx = i

            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                if (node.idx == -1 or
                    len(word) < len(wordsContainer[node.idx])):
                    node.idx = i

        # Answer queries
        ans = []

        for word in wordsQuery:
            node = root

            for ch in reversed(word):
                if ch not in node.children:
                    break
                node = node.children[ch]

            ans.append(node.idx)

        return ans