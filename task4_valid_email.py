import re

def valid_email(email):
    email_Pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    match=re.match(email_Pattern, email)
    return match is not None

check_emails = [
    'user@example.com',
    'user234@domain.co.us',
    'user@123.496',
    'user@invalid_domain',
    'invalid.email',
]

for email in check_emails:
    if valid_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not valid email address.")