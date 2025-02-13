import pygame

# pygame.image.load("Bom.png")

screen = pygame.display.set_mode((500, 500),pygame.RESIZABLE)
running = True
pygame.init()
Aanvallen = ["Slaan", "Genezen"]

Speler = [10, Aanvallen, [0, 0]]
#Speler = [Levens, Aanvallen, positie]

Vijand1 = ["Matroos.png", 10, ["Zwaardslag, Blokkeren"]]
#Vijand = [Afbeelding, Levens, [Aanvallen]]

AlleVijanden = [Vijand1]

A_Bom = ["Bom.png", "Bom", "Valt elke vijand aan voor 5 schade"]
#A_Aanval = [Afbeelding, Aanval naam, Bescrijving aanval]

# Hieronder staan de hoofd functies

# Menu scherm
def menu():
    return "Begin"
# Return "Begin", of "Quit" (of "Tutorial")

# Parkour deel
def parkour():
    return "Vijand1"
# returns de tegengekomen vijand

# Gevecht deel
def gevecht(Speler, Vijand):
    return True
# returns uitslag gevecht: (Gewonnen = True)

# Game Over scherm
def game_over():
   return None

# Nieuwe aanval kiezen
def keuze(TeKiezenAanvallen):
    return "Bom"
# Returns gekozen aanval

# Het eindscherm
def eind():
    return None

# Hieronder staan de extra functies:

# functie om makkelijk nieuwe knoppen aan te maken
def knop(Positie, Grootte, Tekst):
    return False

# Displayt de hele omgeving in een gevecht
def display_gevecht(Aanvallen, Vijanden):
    return None

# Displayt de hele omgeving van het parkour
def display_parkour(SpelerPositie, Colliders, CameraPositie):
    return None

# Functie om makkelijk nieuwe colliders aan te maken
def collision(Positie, Grootte, Encounter_of_niet):
    return None

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Hoofd code:
    Encounter = parkour()
    gewonnen = gevecht(Speler, Encounter)

    if gewonnen:
        Aanvallen.append(keuze([]))
    else:
        game_over()

    screen.fill((100, 100, 100))
    pygame.display.update()


quit()