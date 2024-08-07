from Leaderboard_with_sorted_list import Entry, Leaderboard
import random 

class Tests:
    def __init__(self):
        self.array = [Entry(i, random.randint(0, 250)) for i in range(100)]
        self.leaderboard = Leaderboard(20)

    def test_insertion_and_retrieval(self):
        for entry in self.array:
            self.leaderboard.insert(entry)

        # gets the sorted array based on values
        sorted_array = sorted(self.array, key = lambda x: x.value, reverse = True)[:10]
        actual = self.leaderboard.head(10)
        if sorted_array == actual:
            print('No Errors with insertion and retrieval')
        else:
            print('Errors with insertion and retrival')
            print("Expected: ")
            print([(i.id, i.value) for i in sorted_array])
            print('Actual: ')
            print([(i.id, i.value) for i in actual])

            


    def test_search(self):
        true_element = self.leaderboard.head(random.randint(0, self.leaderboard.length))[0]
        false_element = Entry(270, 134)

        if self.leaderboard.search(true_element) == True and self.leaderboard.search(false_element) == False:
            print('No errors with searching')
        else:
            print('Errors with searching')


if __name__ == '__main__':
    test = Tests()
    test.test_insertion_and_retrieval()
    test.test_search()