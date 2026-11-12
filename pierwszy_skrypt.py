import random

zloto = 50
max_waga = 30.0
ekwipunek = {
    "miecz": {"ilosc": 1, "waga": 5.0, "wartosc": 20},
    "mikstura": {"ilosc": 3, "waga": 0.5, "wartosc": 5}
}

def oblicz_wage():
    return sum(item["ilosc"] * item["waga"] for item in ekwipunek.values())

def pokaz_przedmioty():
    print(f"\n EQ  Złoto: {zloto}  Waga: {oblicz_wage()}/{max_waga} kg")
    if not ekwipunek:
        print("Ekwipunek jest pusty.")
    for nazwa, item in ekwipunek.items():
        print(f" {nazwa}: {item['ilosc']} szt., waga: {item['waga']}kg, cena: {item['wartosc']} gold")

def dodaj_lub_kup_przedmiot():
    global zloto
    nazwa = input("\nPodaj nazwę przedmiotu: ").lower().strip()
    waga = round(random.uniform(1.0, 5.0), 1)
    wartosc = random.randint(5, 25)
    print(f"Parametry: waga = {waga} kg, cena = {wartosc} złota.")
    
    if zloto < wartosc:
        print("Za mało złota!")
        return
    if oblicz_wage() + waga > max_waga:
        print("Przedmiot jest za ciężki!")
        return

    zloto -= wartosc
    if nazwa in ekwipunek:
        ekwipunek[nazwa]["ilosc"] += 1
    else:
        ekwipunek[nazwa] = {"ilosc": 1, "waga": waga, "wartosc": wartosc}
    print(f"Kupiono: {nazwa}!")

def uzyj_lub_sprzedaj_przedmiot():
    global zloto
    nazwa = input("\nPodaj nazwę przedmiotu: ").lower().strip()
    if nazwa not in ekwipunek:
        print("Brak takiego przedmiotu!")
        return
    
    wybor = input("Chcesz 1 Użyć czy 2 Sprzedać?: ")
    if wybor == "1":
        ekwipunek[nazwa]["ilosc"] -= 1
        print(f"Użyto: {nazwa}.")
    elif wybor == "2":
        zloto += ekwipunek[nazwa]["wartosc"]
        ekwipunek[nazwa]["ilosc"] -= 1
        print(f"Sprzedano {nazwa} za {ekwipunek[nazwa]['wartosc']} złota.")
    else:
        print("Niepoprawny wybór.")
        return

    if ekwipunek[nazwa]["ilosc"] <= 0:
        del ekwipunek[nazwa]

def sprawdz_przedmiot():
    nazwa = input("\nSzukany przedmiot: ")
    if nazwa in ekwipunek:
        item = ekwipunek[nazwa]
        print(f"Znaleziono {nazwa}: {item['ilosc']} szt, waga: {item['waga']}kg, cena: {item['wartosc']}")
    else:
        print("Brak przedmiotu w ekwipunku.")

while True:
    print("\n MENU ")
    print("1. Pokaż  2. Kup/Dodaj  3. Użyj/Sprzedaj  4. Sprawdź  5. Wyjdź")
    wybor = input("Wybierz opcję: ")
    
    if wybor == "1": pokaz_przedmioty()
    elif wybor == "2": dodaj_lub_kup_przedmiot()
    elif wybor == "3": uzyj_lub_sprzedaj_przedmiot()
    elif wybor == "4": sprawdz_przedmiot()
    elif wybor == "5":
        print("Koniec gry!")
        break
