class Board():
    def __init__(self, rows):
        self.rows = rows
        self.unmarked = []
        for item in self.rows:
            for item2 in item.split():
                self.unmarked.append(item2)
        self.marked = []
        
    def mark(self, number):
        if str(number) in self.unmarked:
            self.unmarked.remove(str(number))
            self.marked.append(str(number))
            
    def check_if_won(self):
        # horizontal
        for row in self.rows:
            is_row_full = True
            for item in row.split():
                if item not in self.marked:
                    is_row_full = False
                    break
            if is_row_full:
                return True
                
        table_height = 5
        for i in range(len(self.rows)):
            is_row_full = True
            for row in self.rows:
                if row.split()[i] not in self.marked:
                    is_row_full = False
                    break
            if is_row_full:
                return True
            

def solve1(data):
    numbers = data[0]
    boards = []
    for item in data:
        if item == numbers: continue
        rows = item.splitlines()
        boards.append(Board(rows))
        
    for number in numbers.split(","):
        for b in boards:
            b.mark(number)
            if b.check_if_won():
                return int(number) * sum([int(x) for x in b.unmarked])
    return None

def solve2(data):
    numbers = data[0]
    boards = []
    for item in data:
        if item == numbers: continue
        rows = item.splitlines()
        boards.append(Board(rows))
        
    for number in numbers.split(","):
        for b in boards.copy():
            b.mark(number)
            if b.check_if_won():
                if len(boards) > 1:
                    boards.remove(b)
                else:
                    return int(number) * sum([int(x) for x in b.unmarked])
    return None
print(solve1(open("04/input.txt").read().split("\n\n")))
print(solve2(open("04/input.txt").read().split("\n\n")))