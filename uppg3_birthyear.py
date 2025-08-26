"""  
Skapa en variabel för ditt födelseår
Programmet ska sedan skriva ut din ålder

Exempel på utskrift, det inom () ska ändras om variablerna ändras:
Du är (16) år gammal.

"""
birth_year =2008
current_year=2025

age =input("what is your birth year?:")
age = current_year - int(age)
print(f"you are {age} years old")