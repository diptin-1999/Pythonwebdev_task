import re

def check_password_strength(password):
  
    uppercase =(["A-Z"])
    lowercase =("[a-z]")
    digit = bool(re.search(r'\d', password))
    special_char = bool(re.search(r'[!@#$%^&*()-_=+]', password))
    long_enough = len(password) >= 8

    
    score = 0
    if uppercase:
        score += 1
    if lowercase:
        score += 1
    if digit:
        score += 1
    if special_char:
        score += 1
    if long_enough:
        score += 1

  
    if score == 5:
        return "Very Strong"
    elif score >= 3:
        return "Strong"
    elif score == 2:
        return "Moderate"
    elif score == 1:
        return "Weak"
    else:
        return "Very Weak"


password = input("Enter your password: ")
strength = check_password_strength(password)
print("Password strength:", strength)
