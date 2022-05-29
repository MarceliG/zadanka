def number_of_pairs(gloves):
    if len(gloves) == 0:
       return 0
    else:
        result = 0
        set_gloves = set(gloves)
        for element in set_gloves:
            result += int(gloves.count(element)/2)
        return result

# gloves = ["gray","black","purple","purple","gray","black", "gray"]
gloves = ["red","green","blue","blue","red","green","red","red","red"]

# test.describe("Basic tests")
# test.assert_equals(number_of_pairs(["red","red"]),1)
# test.assert_equals(number_of_pairs(["red","green","blue"]),0)
# test.assert_equals(number_of_pairs(["gray","black","purple","purple","gray","black"]),3)
# test.assert_equals(number_of_pairs([]),0)
# test.assert_equals(number_of_pairs(["red","green","blue","blue","red","green","red","red","red"]),4)



def num_gloves(gloves):
    return sum(gloves.count(c)//2 for c in set(gloves))


print(number_of_pairs(gloves))
print(num_gloves(gloves))