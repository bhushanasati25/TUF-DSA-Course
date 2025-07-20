from collections import defaultdict

class TrieNode(object):
    def __init__(self):
        self.children = dict()
        self.name = ""
        self.deleted = False

class Solution(object):
    def deleteDuplicateFolder(self, paths):
        root = TrieNode()
        for path in paths:
            node = root
            for name in path:
                if name not in node.children:
                    node.children[name] = TrieNode()
                    node.children[name].name = name
                node = node.children[name]

        serial_map = defaultdict(list)

        def serialize(node):
            if not node.children:
                return ""
            items = []
            for name in sorted(node.children):
                child_serial = serialize(node.children[name])
                items.append("({}{})".format(name, child_serial))
            serial = "".join(items)
            serial_map[serial].append(node)
            return serial

        serialize(root)

        for nodes in serial_map.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True
        result = []

        def dfs(node, path):
            for name in node.children:
                child = node.children[name]
                if not child.deleted:
                    new_path = path + [name]
                    result.append(new_path)
                    dfs(child, new_path)

        dfs(root, [])
        return result
