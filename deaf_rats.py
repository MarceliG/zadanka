
def count_deaf_rats(town):
    town_list = [element for element in list(town) if element != ' ']

    piper = False
    tw = ''
    deaf_rat = 0
    for element in town_list:
        tw += element
        if element == 'P':
            piper = True
            tw = ''
        elif tw == "O~" and piper == False: # piper is on the right
            tw = ''
            deaf_rat += 1
        elif tw == "~O" and piper == True: # piper is on the left
            tw = ''
            deaf_rat +=1
        elif tw == "O~" or tw == "~O":
            tw = ''
        
       
    return deaf_rat


    # return town

def how_should_do(town):
    return town.replace(" ","")[0::2].count("O")


rats0 = "~O~O~O~O P" # 0
rats1 = "P O~ O~ ~O O~" # 1
rats2 = "~O~O~O~OP~O~OO~" # 2


print(count_deaf_rats(rats2))
print(how_should_do(rats2))




# test.assert_equals(count_deaf_rats("~O~O~O~O P"), 0)  
# test.assert_equals(count_deaf_rats("P O~ O~ ~O O~"), 1)  
# test.assert_equals(count_deaf_rats("~O~O~O~OP~O~OO~"), 2)