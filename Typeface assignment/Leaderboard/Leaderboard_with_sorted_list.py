# Implements a LeaderBoard with the use of a Sorted Array

# Implements the following functionalities
# insert(entry): inserts a key into the list
# head(k): returns the max k elements from the list
# search(entry): return True if a particular entry in within the leaderboard
# update(entry, new_value): updates the entry and the Leaderboard

class Entry:
    def __init__(self, id, value):
        self.id = id 
        self.value = value 

class Leaderboard:
    def __init__(self, size):
        self.size = size 
        self.list = []
        self.length = 0

    def search(self, entry):
        low = 0
        high = self.length - 1

        while low <= high:
            mid = (low + high)//2 
            if entry.id == self.list[mid].id:
                return True 
            
            if entry.value >= self.list[mid].value:
                high = mid - 1
            
            else:
                low = mid + 1
        return False 
    

    def insert(self, entry):
        if self.length == self.size:
            self.list.pop()
            self.length -= 1 

        index = 0
        while index < self.length:
            if entry.value > self.list[index].value:
                break 
            index += 1
        
        self.list.insert(index, entry)
        self.length += 1

    def head(self, k):
        return [self.list[index] for index in range(k)]
    
    def update(self, entry, new_value):
        if new_value == entry.value: return 

        if self.search(entry) == False: 
            entry.value = new_value
            return 
        
        index = 0
        while index < self.length:
            if self.list[index].id == entry.id:
                break 
        
        if new_value > entry.value:
            entry.value = new_value
            
            while self.list[index].value > self.list[index - 1].value and index > 0:
                self.list[index], self.list[index - 1] = self.list[index - 1], self.list[index]
                index -= 1

        else:
            entry.value = new_value
            
            while self.list[index].value < self.list[index + 1].value and index < self.length - 1:
                self.list[index], self.list[index - 1] = self.list[index - 1], self.list[index]
                index += 1
        return 







    
    
