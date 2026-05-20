namn = input("Vad ska ditt husdjur heta? ")
health = 100
happiness = 30
hunger = 50
mess = 0
age = 1

actions = ["discipline", "feed", "play", "pet", "clean"]

print(f"\nVälkommen! Ta hand om {namn} väl.")

while health > 0:

    # 1. STATUS
    print("\n" + "-"*30)
    print(f"STATUS FÖR {namn.upper()}:")
    print(f"Hälsa:  {health}/100")
    print(f"Glädje: {happiness}/100")
    # ... + alla andra stats
    print("-" * 30)

    # 2. TIDEN GÅR
    # Varje runda blir djuret lite hungrigare och tråkigare (surare, ledsnare, deppigare)?
    hunger += 10
    happiness -= 5
    
    # 3. KONSEKVENSER 
    # UPPDRAG 1: Skriv if-satser som straffar djuret om värdena är för dåliga!
    # Till exempel: Om hunger är över 80, sänk health med 10.
    # Om smuts (mess) är över 3, sänk health med 5, och / eller gör djuret sjukt (kan inte äta).

    # Kolla om djuret dog av konsekvenserna innan vi går vidare (alltså, hur vågar du)
    if health <= 0:
        break # Avbryter loopen direkt!

    # 4. SPELARENS VAL
    print("\nVad vill du göra?")
    
    # UPPDRAG 2: Använd en for-loop för att skriva ut listan 'actions' snyggt
    print(f"Alternativ: {actions}") # Fixa

    val = input("Skriv vad du vill göra: ").lower()

    # 5. UTFÖR 
    # UPPDRAG 3: Ändra variablerna beroende på spelarens val!
    
    if val == "feed":
        print(f"Du matar {namn}.")
        hunger -= 30
        mess += 1
        # OBS: Se till att hunger inte går under 0! (Använd if-sats)
        
    elif val == "play":
        print(f"Du leker med {namn}!")
        # Vad ska hända med glädje och hunger här?
        
    # Här skriver du resten av logiken för djurets beteende
        
    else:
        print("Ogiltigt val! Djuret tittar förvirrat på dig och tiden går...")

# --- GAME OVER ---
print("\n" + "="*30)
print(f"GAME OVER. {namn} blev {age} år, men har nu dött eller rymt.")
print("="*30)