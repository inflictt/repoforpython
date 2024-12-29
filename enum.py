from enum import Enum
class Name(Enum):
    User:7=input("Enter Your Name : ")
    Computer:8="Draw"
    Draw:9="Computer"
print(Name.7.value)
print(Name.7.name)
print(Name.8.value)
print(Name.8.name)