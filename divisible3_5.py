def fizz_buzz(input):
    for i in range(input):
        print("Fizz"*(i%3<1)+(i%5<1)*"Buzz" or i)
fizz_buzz(20)