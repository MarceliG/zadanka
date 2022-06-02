from math import gamma
import pytest

class Game:
    """Start stack."""
    def __init__(self):
        self.stack = []


    """Return all element from stack."""
    def end(self):
        print(self.stack)


    """Pushes the integer x into the stack."""
    def push(self, number:int):
        self.stack.append(int(number))

    """Adds together the top two elements on the stack."""
    def add(self):
        if len(self.stack) >= 2:
            result = self.stack.pop(-1)+self.stack.pop(-1)
            self.stack.append(result)
    
    """Subtracts the top-most element by the second top-most element on the stack."""
    def sub(self):
        if len(self.stack) >= 2:
            result = self.stack.pop(-1)-self.stack.pop(-1)
            self.stack.append(result)
    
    """Multiplies the top two elements on the stack."""
    def mul(self):
        if len(self.stack) >= 2:
            result = self.stack.pop(-1)*self.stack.pop(-1)
            self.stack.append(result)
    
    """Divides (integer division) the top-most element by the second top-most element on the stack."""
    def div(self):
        if len(self.stack) >= 2:
            result = self.stack.pop(-1)//self.stack.pop(-1)
            self.stack.append(result)


#remove '(' and  ')' and return list
play_game = '(start)(push)(5)(push)(5)(div)(end)'
play_game = play_game.replace('(', "")
play_game = list(filter(None, play_game.split(")")))
print(play_game)
index = 0
for state in play_game:
    print(state)
    if state == 'start':
        game = Game()
    elif state == 'push':
        game.push(play_game[index+1])
    elif state == 'add':
        game.add()
    elif state == 'sub':
        game.sub()
    elif state == 'mul':
        game.mul()
    elif state == 'div':
        game.div()
    elif state == 'end':
        game.end()
    index +=1
    

class TestGrame:

    def test_start(self):
        #given
        #when
        game=Game()
        #then
        assert isinstance(game, Game)
        
    def test_push(self):
        #given
        game=Game()
        number = 5
        number2 = 10
        #when
        game.push(number)
        game.push(number2)
        #then
        assert game.stack[-1] == number2
        assert game.stack[-2] == number
        
    def test_add(self):
        #given
        game=Game()
        number = 5
        number2 = 10
        game.push(number)
        game.push(number2)
        #when
        game.add()
        #then
        assert game.stack[-1] == number+number2
        
    def test_sub(self):
        #given
        game=Game()
        number = 5
        number2 = 10
        game.push(number)
        game.push(number2)
        #when
        game.sub()
        #then
        assert game.stack[-1] == number2-number
        
    def test_mul(self):
        #given
        game=Game()
        number = 5
        number2 = 10
        game.push(number)
        game.push(number2)
        #when
        game.mul()
        #then
        assert game.stack[-1] == number2*number
        
    def test_div(self):
        #given
        game=Game()
        number = 5
        number2 = 10
        game.push(number)
        game.push(number2)
        #when
        game.div()
        #then
        assert game.stack[-1] == number2//number
        
    def test_end(self, capsys):
        #given
        game=Game()
        number = 5
        number2 = 10
        game.push(number)
        game.push(number2)
        #when
        game.end()
        out, err = capsys.readouterr()
        
        #then
        assert out == '[5, 10]\n'