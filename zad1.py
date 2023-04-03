import math

dPodloga = int(input("Dlugosc podlogi:"))
szPodloga = int(input("Szerokosc podlogi:"))
dPaneli = int(input("Dlugosc panela:"))
szPaneli = int(input("Szerokosc panela:"))
ileWOpakowaniu = int(input("Ile jest paneli w paczce:"))

def funkcja(dPodloga, szPodloga, dPaneli, szPaneli, ileWOpakowaniu):
    powierzchnia = dPodloga * szPodloga * 1.1
    panel = dPaneli * szPaneli
    ilepotrzeba = powierzchnia/panel
    opakowania = math.ceil(ilepotrzeba/ileWOpakowaniu)
    return opakowania
print(funkcja(dPodloga, szPodloga, dPaneli, szPaneli, ileWOpakowaniu))