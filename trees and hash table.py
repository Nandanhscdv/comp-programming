class FileSystem:
    def __init__(self):
        self.tree = {}  # hash table

    def add(self, parent, child):
        if parent not in self.tree:
            self.tree[parent] = []
        self.tree[parent].append(child)

    def find(self, target):
        # check in parents and children
        for parent in self.tree:
            if parent == target:
                print("File Found")
                return
            if target in self.tree[parent]:
                print("File Found")
                return
        print("File Not Found")


# -------- Input from User --------
fs = FileSystem()

n = int(input("Enter number of relations: "))

for _ in range(n):
    parent, child = input().split()
    fs.add(parent, child)

target = input("Enter file to search: ")

fs.find(target)