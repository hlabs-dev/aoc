import aocd
from functools import cache

patterns, designs = aocd.get_data(day=19, year=2024).split("\n\n")
designs = designs.splitlines()

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        self.maxlen = 0
        for word in words:
            self.insert(word)

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def find_prefixes(self, target):
        node = self.root
        prefixes = []
        prefix = ""
        for i,char in enumerate(target):
            if char not in node.children: break
            node = node.children[char]
            prefix += char
            if node.is_end_of_word:
                prefixes.append(prefix)
        return prefixes

trie = Trie(patterns.split(", "))

@cache
def cnt(design):
    if design == "": return 1
    return sum(cnt(design[len(pa):]) for pa in trie.find_prefixes(design))

cntlist = [cnt(de) for de in designs]

print("part1:",sum(cnt>0 for cnt in cntlist),"part2:",sum(cntlist))
