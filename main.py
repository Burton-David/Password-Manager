import random
import string
import openpyxl

# Function to generate a strong password


def generate_password():
    password_length = 16
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for i in range(password_length))


# Ask the user how many passwords they want to generate
num_passwords = int(input("How many passwords do you want to generate? "))

# Create a new Excel workbook
workbook = openpyxl.Workbook()

# Create a new sheet
sheet = workbook.active

# Add the headers to the sheet
sheet.append(["Username", "Website", "Password"])

# Add the passwords to the sheet, one per row
for i in range(num_passwords):
    username = input("Enter the username for password #{}: ".format(i+1))
    website = input("Enter the website for password #{}: ".format(i+1))
    password = generate_password()
    sheet.append([username, website, password])

# Save the workbook to a file
workbook.save("passwords.xlsx")
