przyklad = [-3,-5,-1,3,4,5,6]

def najblize_0(input):
    input = list(map(abs,input))
    input.sort()
    print(input[0])

najblize_0(przyklad)

 