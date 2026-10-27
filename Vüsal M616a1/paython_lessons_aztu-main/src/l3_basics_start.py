# Dərs 3 · Blok 1 — Python-un 10 kərpici
# İşə salma (de-praktikum qovluğundan): python src/l3_basics_start.py
# Dərsdə hər kərpicin kodunu slayddan öz bölməsinə yazırıq.
# Hər bölmə əvvəlcə öz başlığını çap edir — terminalda həmişə
# ən aşağıdakı bölməyə baxın. Tam kod dərsdən sonra Teams-də olacaq.

print("=== Kərpic 1 ===")   # Proqram — əmrlər ardıcıllığı
# TODO: print(...) ilə 4 sətir (slayd «Kərpic 1»)
print("Salam, radiotexnika!")
print("Baza stansiyasi:", "BAK-0207")
print(2 + 3)
print("2 + 3")
print("=== Kərpic 2 ===")   # Dəyişən — adı olan qutu   
cell = "BAK-0207"
rsrp = -95.5
print(cell, rsrp)

rsrp = -108.1
print(cell, rsrp)

drops = 2
drops = drops + 1
print("drops =", drops)
# TODO: cell, rsrp, drops

print("=== Kərpic 3 ===")   # Tiplər: int, float, str, bool, None
print(type(3))
print(type(-95.5))
print(type("BAK-0207"))
print(type(True))
print(type(None))
# TODO: type(...) və «mətn ≠ ədəd»
a = "-95.5"
b = -95.5
print(b + 10)
print(a + "10")
print(float(a) + 10)
#print(float("N/A"))
print("=== Kərpic 4 ===")   # Müqayisə → True / False
rsrp = -108.1
print(rsrp < -105)
print(rsrp > -105)
print(rsrp == -108.1)
region = "Yasamal"
print(region == "Yasamal")
print(region == "YASAMAL")
# TODO: rsrp < -105, ==

print("=== Kərpic 5 ===")   # Siyahı (list)
rsrp_list = [-91.5, -108.1, -86.2, -103.3, -97.4]
print(rsrp_list[0])
print(rsrp_list[1])
print(rsrp_list[-1])
print(len(rsrp_list))
avg = sum(rsrp_list) / len(rsrp_list)
print(round(avg, 1))
# TODO: rsrp_list, indeks, len, orta

print("=== Kərpic 6 ===")   # Lüğət (dict)
row = {"cell_id": "BAK-0207", "region": "Yasamal", "rsrp_dbm": -108.1}
print(row["region"])
print(row["rsrp_dbm"])
row["band"] = "LTE800"
print(row)
# TODO: row = {...}, row["region"]

print("=== Kərpic 7 ===")   # Dövr (for) və şərt (if / else)
rsrp_list = [-91.5, -108.1, -86.2, -103.3, -110.4]
weak = 0
for v in rsrp_list:
    if v < -105:
        print(v, "– zeif")
        weak = weak + 1
    else:
        print(v,"- normal")
print("Zeif olcme sayi:", weak)
# TODO: zəif ölçmələri saymaq

print("=== Kərpic 8 ===")   # Funksiya: çağırmaq və yaratmaq
print(round(-97.36, 1))
print(len("BAK-0207"))
print(max([-91.5, -108.1, -86.2]))
print(round(-97.36, ndigits=1))
def is_weak(rsrp):
    return rsrp < -105
print(is_weak(-108.1))
print(is_weak(-91.5))
# TODO: round, len, max; def is_weak(rsrp)

print("=== Kərpic 9 ===")   # Nöqtə: metod
name = " YASAMAL "
print("[" + name + "]")
clean = name.strip ()
print("[" + clean + "]")
print(clean.capitalize())
print(name.strip().capitalize())
# TODO: name.strip().capitalize()

print("=== Kərpic 10 ===")  # import — hazır alət qutusu
import math

p_mw = 0.001
dbm = 10 * math.log10 (p_mw)
print(dbm)

import pandas as pd 

print(pd.__version__)
# TODO: import math; import pandas as pd
print("Vusal Mardiyev 21 yas ")
ad = input("Ad daxil edin: ")
soyad = input("Soyad: ")
yas = input("Yasinizi daxil edin: ")
print(soyad, ad, yas)
print("Novbeti yas", int(yas)+1)


