class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.child_nodes = [None] * 26
        self.is_end_char = False


# 一组字符串集合中快速查找每个字符串
class Trie(object):

    def __init__(self):
        self.root = TrieNode('/')

    def insert_string(self, string):
        p = self.root
        for s in string:
            index = ord(s) - ord("a")
            if not p.child_nodes[index]:
                new_node = TrieNode(s)
                p.child_nodes[index] = new_node
            p = p.child_nodes[index]
        p.is_end_char = True

    def find_string(self, pattern):
        p = self.root
        for s in pattern:
            index = ord(s) - ord("a")
            if not p.child_nodes[index]:
                return False
            p = p.child_nodes[index]

        if p.is_end_char:
            return True
        else:
            return False


if __name__ == "__main__":

    trie = Trie()
    string_list = ["hello", "her", "hi", "how"]
    for s in string_list:
        trie.insert_string(s)

    for s in string_list:
        print(trie.find_string(s))





