import random

class Tamagotchi:
    def __init__(self, namn):
        self.namn = namn
        
        self.health = 100
        self.happiness = 50
        self.hunger = 30
        self.mess = 0
        self.age = 1
        self.weight = 5
    
        self.sick = False
        self.fat = False
    
        self.actions = [
            "eat", "play", "pet", "clean", "discipline", "medicine"
        ]
    def show_status(self):
        print("=" * 35)
        print(f"Status för {self.namn}")
        print("=" * 35)

        print(f"hälsa:   {self.health}/100")
        print(f"glädje:  {self.happiness}/100")
        print(f"hunger:  {self.hunger}/100")
        print(f"smuts:   {self.mess}/5")
        print(f"ålder:   {self.age} år")
        print(f"vikt:    {self.weight} kg")
        if self.age < 10:
            print("Stadie: Unge")

        elif self.age < 20:
            print("Stadie: Tonåring")


    def nästa_del(self):
    
        self.age += 1
        self.hunger += 10
        self.happiness -= 5

        if self.hunger > 80:
            self.health -= 10
            print(f"{self.namn} svälter!")
    
        if self.mess > 3:
            self.sick = True
            print(f"{self.namn} blev sjuk av all skit!")

        if self.weight > 20:
            self.sick = True
            print(f"{self.namn} har blivit för tjock!")
    
        if self.sick:
            self.health -= 15
        else:
            self.health -= 5

    def eat(self):
        if self.sick:
            print(f"{self.namn} är sjuk och kan inte äta!")
            return
        
        print(f"Du matar {self.namn}.")
        self.hunger -= 30
        self.mess += 1
        self.weight += 2

    def play(self):
        print(f"Du leker med {self.namn}!")
        self.happiness += 20
        self.hunger += 15
        self.weight -= 1

    def pet(self):
        print(f"Du klappar {self.namn}.")
        self.happiness += 10

    def clean(self):
        print(f"Du städar efter {self.namn}.")
        self.mess = 0
        if self.sick:
            self.sick = False
            print(f"{self.namn} blev frisk av att bli ren!")

    def discipline(self):
        print(f"Du disciplinerar {self.namn}.")
        self.happiness -= 15
        self.health -= 5

    def medicine(self):
        if self.sick:
            print(f"Du ger medicin till {self.namn}.")
            self.sick = False
            self.health += 20
        else:
            print(f"{self.namn} är inte sjuk och vägrar ta medicin!")

    def do_action(self, action):
        if action == "eat":
            self.eat()
        elif action == "play":
            self.play()
        elif action == "pet":
            self.pet()
        elif action == "clean":
            self.clean()
        elif action == "discipline":
            self.discipline()
        elif action == "medicine":
            self.medicine()
        else:
            print("Ogiltigt val!")



namn = input("Vad vill du döpa ditt husdjur till? ")
husdjur = Tamagotchi(namn)
print(f"Du har skapat {namn}!")

while husdjur.health > 0:
    husdjur.show_status()
    husdjur.nästa_del()

    if husdjur.health <= 0:
        print(f"{namn} har dött av dålig hälsa...")


    print("\nVad vill du göra?")
    for action in husdjur.actions:
        print(f"- {action}")
    
    val = input("Skriv vad du vill göra: ").lower()
    husdjur.do_action(val)

print("\n" + "="*30)
print("GAME OVER")
print(f"{husdjur.namn} blev {husdjur.age} år, men har nu dött.")