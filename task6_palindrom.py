#palindrome_checker

def Palindrome_chker(str): 
    if (str== str[::-1]): 
        return "The string is a palindrome." 
    else: 
        return "The string is not a palindrome." 

string = input("Enter string: ") 
 
print(Palindrome_chker(string))    

    
    
    
    
