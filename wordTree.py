import os
import graphviz
import random

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
        wrdCount = 0

        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)

        with open(file_path, "r") as file:
            wordsList = [line.strip() for line in file]

        for word in wordsList:
            if (word.startswith(self.root.letter)):
                self.word.append(word)
                wrdCount += 1
        print("Total words found = " + str(wrdCount))

        x = 100
        print("Total words printed = " + str(x))
        if(len(self.word) > x):
            while(len(self.word) > x):
                current = random.randint(0, len(self.word) - 1)
                del self.word[current]
    def make_tree(self):
        for word in self.word:
            current = self.root
            for letter in word[1:]:
                current = current.add_node(letter)
                
    def visualize(self):
        
        dot = graphviz.Digraph(format='png')

        self.find_all_words("words_alpha.txt")#If you want to use change the txt file make sure you refresh and save to make it work 
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

    def find_longest_word(self):
        max = 0
        maxid = 0
        for i in range(len(self.word)) :
            if (len(self.word[i]) > max):
                max = len(self.word[i])
                maxid = self.word[i]
        print("Longest word = " + str(maxid))
        print("Length = " + str(max))

    def find_smallest_word(self):
        min = 100
        minid = 0
        for i in range(len(self.word)) :
            if (len(self.word[i]) < min):
                min = len(self.word[i])
                minid = self.word[i]
        print("Smallest word = " + str(minid))
        print("Length = " + str(min))

#Testing
tree = TheTree(Node("x"))
tree.visualize()
tree.find_longest_word()
tree.find_smallest_word()
