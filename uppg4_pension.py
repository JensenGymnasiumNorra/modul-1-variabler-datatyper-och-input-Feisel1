"""  
Gör ett program som frågar användaren efter namn och ålder.
Programmet ska sedan skriva ut enligt nedan.
Räkna med att man går i pension vid 67 års ålder.

Exempel på utskrift, det inom () ska ändras om variablerna ändras:
Hej och välkommen till mitt program (Hampus). Du har (39) år kvar till pension.
"""
name =input("what is yoour name?:")
age =input("how old are you?:")

retirement_age = 67

age_left = retirement_age - int(age)
print(f"hi {name} you have {age_left} years left to retirement")