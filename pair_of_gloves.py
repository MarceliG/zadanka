def number_of_pairs(gloves):
    if len(gloves) == 0:
       return 0
    else:
        result = 0
        for element in gloves:
            if gloves.count(element) >2:
                result += int(gloves.cout(element)%2)
        return result

gloves = ["gray","black","purple","purple","gray","black"]
# gloves = []
print(gloves.count('gray')%2)
# print(number_of_pairs(gloves))

# test.describe("Basic tests")
# test.assert_equals(number_of_pairs(["red","red"]),1)
# test.assert_equals(number_of_pairs(["red","green","blue"]),0)
# test.assert_equals(number_of_pairs(["gray","black","purple","purple","gray","black"]),3)
# test.assert_equals(number_of_pairs([]),0)
# test.assert_equals(number_of_pairs(["red","green","blue","blue","red","green","red","red","red"]),4)