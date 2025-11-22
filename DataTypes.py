"""
Python Data Types
This file is used to show the data types in Python.
@author: Yaohui Zhang @tomie
"""
# String type data
Name = "John Doe"

#Integer type data, can only be integer
Age = 28

#List type data, can be a list of any data 
Skills = ["Python", "SQL", "Power BI"]

#Tuple type data , can be a list of any data but cannot be changed
Education = ("BSc Computer Science", 2020)

#Dictionary type data, can be a dictionary of any data
Contact_details = {
    "email": "tomieweb@gmail.com",
    "phone": "+1234567890",
}

#Set type data, can be a set of any data but should be unique
#This is a set of certifications, which are unique and cannot be duplicated
# it is will be removed repeated items automatically
Certifications = {"Azure", "AWS", "Azure"}

#print
print(Name)
print(Age)
print(Skills)
print(Education)
print(Contact_details)
print(Certifications)