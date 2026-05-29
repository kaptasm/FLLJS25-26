from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# Ha a js_base.py-ban már létrehoztad a hub-ot, 
# akkor ezt a sort ne írd be újra:
hub = PrimeHub()

# 1. Megoldás: A pontos feszültség (millivoltban, pl. 8000 mV = 8V)
# Egy teljesen feltöltött SPIKE akku kb. 8200-8400 mV körül van.
feszultseg = hub.battery.voltage()
print("Akkumulátor feszültség:", feszultseg, "mV")

# 2. Megoldás: Körülbelüli százalék (%) kiszámítása
# (A SPIKE akku 6000 mV-nál merül le teljesen, és ~8300 mV a maximum)
szazalek = int((feszultseg - 6000) / (8300 - 6000) * 100)

# Biztosítjuk, hogy a százalék 0 és 100 között maradjon
szazalek = max(0, min(100, szazalek))

print("Akkumulátor töltöttség:", szazalek, "%")

# Meg is jelenítheted a hub kijelzőjén a százalékot:
hub.display.number(szazalek)
wait(3000) # 3 másodpercig mutatja a kijelzőn