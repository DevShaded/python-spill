import random
import time

# Innledende tilstander
våken = 50
energi = 0
timer = 0
spill_over = False


# Funksjon for å vise status på en fin måte
def status():
    print("\n" + "=" * 40)
    print(f"Timer: {timer}/8".center(40))
    print(f"Våkenhet: {våken}% | Energinivå: {energi}%".center(40))
    print("=" * 40 + "\n")


# Funksjoner for ulike handlinger
def drikk_energidrikk(sterk):
    global våken, energi
    if sterk:
        print("\nDu drikker en **STERK** energidrikk.")
        dose = random.randint(25, 40)
    else:
        print("\nDu drikker en vanlig energidrikk.")
        dose = random.randint(10, 20)

    energi += dose
    våken += dose // 2
    print(f"Energidrikken økte energinivået ditt med {dose}%.")
    time.sleep(1)
    if energi > 100:
        print("Advarsel: Du har drukket for mye energi! Du begynner å føle hjertebank.")


def sov():
    global våken, energi
    print("\nDu velger å hvile litt.")
    hvile = random.randint(10, 25)
    våken -= hvile
    energi -= hvile // 2
    print(f"Du hvilte og mistet {hvile}% våkenhet.")
    time.sleep(1)


def tren():
    global våken, energi
    print("\nDu bestemmer deg for å trene litt.")
    tren_effekt = random.randint(5, 15)
    våken += tren_effekt
    energi -= tren_effekt // 2
    print(f"Treningen økte våkenheten din med {tren_effekt}%, men du mistet energi.")
    time.sleep(1)


def spis_snack():
    global våken, energi
    print("\nDu spiser en snack.")
    snack_effekt = random.randint(5, 20)
    energi += snack_effekt // 2
    våken += snack_effekt // 3
    print(f"Snacken ga deg {snack_effekt // 2}% energi og økte våkenheten med {snack_effekt // 3}%.")
    time.sleep(1)


# Funksjon for å sjekke om spillet er over
def sjekk_tilstand():
    global spill_over, timer
    if våken >= 100:
        print("\nGratulerer! Du klarte å holde deg våken og fullføre dagen.")
        spill_over = True
    elif våken <= 0:
        print("\nDu sovnet! Spillet er over.")
        spill_over = True
    elif energi > 100:
        print("\nDu har for mye energi i kroppen, og du får hjertebank. Spillet er over.")
        spill_over = True
    elif timer >= 8:
        print("\nDu har klart å holde deg våken i 8 timer. Dagen er over, og du vinner!")
        spill_over = True


# Funksjon for å vise valg på en fin måte
def vis_valg():
    print("Hva vil du gjøre?")
    print("┌" + "─" * 38 + "┐")
    print(f"│ {'1 = Drikk vanlig energidrikk': <36} │")
    print(f"│ {'2 = Drikk sterk energidrikk': <36} │")
    print(f"│ {'3 = Sov litt': <36} │")
    print(f"│ {'4 = Tren litt': <36} │")
    print(f"│ {'5 = Spis en snack': <36} │")
    print("└" + "─" * 38 + "┘")


# Hovedspill loop
print("\n" + "=" * 40)
print("Velkommen til det utvidede energidrikk-spillet!".center(40))
print("=" * 40)
print("Målet ditt er å holde deg våken i 8 timer".center(40))
print("ved å balansere våkenhet og energi.".center(40))
print("=" * 40)

while not spill_over:
    status()

    vis_valg()

    valg = input("Velg handling (1-5): ")

    if valg == "1":
        drikk_energidrikk(sterk=False)
    elif valg == "2":
        drikk_energidrikk(sterk=True)
    elif valg == "3":
        sov()
    elif valg == "4":
        tren()
    elif valg == "5":
        spis_snack()
    else:
        print("Ugyldig valg! Prøv igjen.")
        continue

    # Øker tiden med 1 time etter hver handling
    timer += 1
    sjekk_tilstand()

print("\nTakk for at du spilte!")
