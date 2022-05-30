
def count_deaf_rats(town):
    town_list = list(town)
    piper = False
    tw = ''
    deaf_rat = 0
    for element in town_list:
        tw += element
        if tw == "~O" and piper == False:
            tw = ''
            print(True)
        elif tw == "O~" and piper == False:
            tw = ''
            deaf_rat +=1
            
        # if element == "~" and element.index()+1 ==  
        # if element == 'P':
        #     piper = True
    print(deaf_rat)
    return tw


    # return town




rats0 = "~O~O~O~O P" # 0
rats1 = "P O~ O~ ~O O~" # 1
rats2 = "~O~O~O~OP~O~OO~" # 2
# print(name)

print(count_deaf_rats(rats0))





# test.assert_equals(count_deaf_rats("~O~O~O~O P"), 0)  
# test.assert_equals(count_deaf_rats("P O~ O~ ~O O~"), 1)  
# test.assert_equals(count_deaf_rats("~O~O~O~OP~O~OO~"), 2)