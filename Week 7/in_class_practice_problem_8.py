def isValid(s):
    pairs ={")":"(", 
            "}":"{", 
            "]":"[" }
    stack=[] #this is where we keep track of the opening brackeets that we need to close
    for character in s:
        if character in pairs: #if the character is a closing bracket
            if stack and stack[-1]== pairs[character]:
                stack.pop()
            else:
                return False
        else: #if the character is an open bracket
            stack.append(character)
    if stack:
        return False
    else:
        return True 
    
test_string_1 = "()"
test_string_2 = "()[]\{\}"
test_string_3 = "(]"
test_string_4 = "([])"


print(isValid(test_string_1)) #True
print(isValid(test_string_2)) #False
print(isValid(test_string_3)) #False
print(isValid(test_string_4)) #True

