def taxirechner(strecke_km, grundpreis, preis_pro_km, mindestpreis):
    preis = grundpreis + (strecke_km * preis_pro_km)
    preis = max(preis, mindestpreis)

    return round(preis, 2)


strecke = float(input("Bitte geben Sie die Strecke in Kilometern an: "))
grundpreis = float(input("Bitte geben Sie den Grundpreis an: "))
preis_pro_km = float(input("Bitte geben Sie den Preis pro Kilometer an: "))
mindestpreis = float(input("Bitte geben Sie den Mindestpreis an: "))

preis = taxirechner(strecke, grundpreis, preis_pro_km, mindestpreis)
print(f"Die Fahrt kostet {preis}€.")
