"""  
Låt användaren skriva in ett valfritt tal. Skriv sedan ut vad det talet blir i kvadrat:

Exempel på utskrift, det inom () ska ändras om variablerna ändras:
(3) i kvadrat är (9). 

"""
import random

a= random.randint(1,10)
b= random.randint(1,10)
c= a * b
print(f"{a} * {b} är {c}")