class NumList:
    def __init__(self):
        self.Coders = []

    def add_Coders(self, list):
        self.Coders.extend(list)

    def find_indices(self, target):
        return [(i, j) 
                for i, x in enumerate(self.Coders) 
                for j, y in enumerate(self.Coders[i+1:], start=i+1) 
                if x + y == target] or -1

list = NumList()
list.add_Coders([1, 2, 3, 4, 5])
target = 7
result = list.find_indices(target)
print("indexlər:", result)
