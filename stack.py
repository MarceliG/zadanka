from posixpath import split


class Game:
    """Start stack."""
    def __init__(self):
        self.stack = [] 


    """Return all element from stack."""
    def end(self):
        print(self.stack)


    """Pushes the integer x into the stack."""
    def push(self, number:int):
        self.stack.append(number)

    """Adds together the top two elements on the stack."""
    def add(self):
        if len(self.stack) >= 2:
            result = self.stack.pop(-1)+self.stack.pop(-1)
        pass
    
    """Subtracts the top-most element by the second top-most element on the stack."""
    def sub(self):
        pass
    
    """Multiplies the top two elements on the stack."""
    def mul(self):
        pass
    
    """Divides (integer division) the top-most element by the second top-most element on the stack."""
    def div(self):
        pass


start = Game()
push = start.push(5)
add = start.add()
sub = start.sub()
mul = start.mul()
div = start.div()
end = start.end()


#remove '(' and  ')' and return list
play_game = '(start)(push)(5)(sub)(5)'
play_game = play_game.replace('(', "")
play_game = list(filter(None, play_game.split(")")))
print(play_game)

liczby = [1,2,3,4]


print(liczby)
print(result)