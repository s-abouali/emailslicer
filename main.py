# Splits email into username & domain using index() + slicing
email= input("Enter your email: ")
index= email.index("@")

username= email[: index]
domain= email[index + 1 : ]

print(f"Your Username is {username}")
print(f"Your Domain is {domain}")

