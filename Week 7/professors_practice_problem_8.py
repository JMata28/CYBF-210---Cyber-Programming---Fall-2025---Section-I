#This practice problem is LeetCode's classic "Valid Parentheses" problem found here: https://leetcode.com/problems/valid-parentheses/description/ 

#I included a link in our slides to one way of writing a solution. But my preferred solution is the one found in this link instead: https://www.youtube.com/watch?v=WTzjTskDFMg 
#This is the solution shown below

def isValid(s: str) -> bool:
    pairs = {")" : "(", 
             "}" : "{", 
             "]" : "["}
    stack = []
    for character in s:
        if character in pairs:  #closing bracket
            if stack and stack[-1] == pairs[character]:
                stack.pop()
            else:
                return False
        else: #it's an open bracket
            stack.append(character)
    if stack:
        return False
    else:        
        return True
    

test_string_1 = "()"
test_string_2 = "()[]\{\}"
test_string_3 = "(]"
test_string_4 = "([])"
test_string_5 = "([])"

print(isValid(test_string_1))