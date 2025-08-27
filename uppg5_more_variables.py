"""  
Skapa en variabel för ditt namn.
Skapa en variabel för din ålder.
Skriv ut ditt namn med hjälp av variabeln.

Skapa en variabel och låt användaren skriva in sitt namn med hjälp av input.
Skapa en variabel och låt användaren skriva in sin ålder med hjälp av input.

Skriv ut en mening som använder sig av alla 4 variabler. Åldern ska adderas ihop.

Exempel på utskrift, det inom () ska ändras om variablerna ändras:
Välkommen till mitt program (Oskar). Du och (Hampus) är (53) år tillsammans.

"""

his_name =input("What is his name?: ")
his_age =input("How old is he?: ")
your_name = input("What is your name?: ")
your_age = input("How old are you?: ")
total_age = int(his_age) + int(your_age)
print(f"Welcome to my program {your_name} and {his_name}. You guys is {total_age} years old together.")
