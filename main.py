# get user email address
email = input("Email address is : ").strip()

# slice out user name
name = email[:email.index("@")]

# slice domain name
domain = email[email.index('@')+1:]

# format message
output = "Your username is {} and your domain name is {}".format(name, domain)

# display output message
print(output)
