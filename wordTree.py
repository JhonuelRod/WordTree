import os
import graphviz

class Node: 
    def __init__(self, letter):
        self.letter = letter
        self.children = {}

    def add_node(self, letter):
        if letter not in self.children:
            self.children[letter] = Node(letter)
        return self.children[letter]

class TheTree:
    def __init__(self, root):
        self.root = root
        self.current = root
        self.word = []

    def find_all_words(self, filename):
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)

        with open(file_path, "r") as file:
            wordsList = [line.strip() for line in file]

        for word in wordsList:
            if (word.startswith(self.root.letter)):
                self.word.append(word)
        x = 100
        if(len(self.word) > x):
            self.word = self.word[:x]

    def make_tree(self):
        for word in self.word:
            current = self.root
            for letter in word[1:]:
                current = current.add_node(letter)
                
    def visualize(self):
        
        dot = graphviz.Digraph(format='png')

        self.find_all_words("words_alpha.txt")#If you want to use change the txt file make sure you refresh and to make it work 
        self.make_tree()

        def make_edges(node, node_id):
            for letter, child in node.children.items():
                child_id = node_id + letter
                dot.node(child_id, label = letter)
                dot.edge(node_id, child_id)
                make_edges(child, child_id)
        
        root_id = self.root.letter
        dot.node(root_id, label = self.root.letter)
        make_edges(self.root, root_id)

        dot.render(filename = "test", cleanup=True)

#Testing
tree = TheTree(Node("x"))
tree.visualize()
