# email slicer

email = input("Enter your e-mail address : ").strip()
 
user_name = email[ : email.index('@')]

domain = email[email.index('@') + 1 : ]

print(f"Your username is {user_name} and domain is {domain}")
 
#virat.koli05@gmail.com
