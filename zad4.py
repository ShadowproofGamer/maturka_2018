plik = open("sygnaly.txt")
dane = plik.read().split()
slowo = ""
for i in dane[39::40]:
    slowo += i[9]
print("zad1: ", slowo)
liczba = 0
slowo_2 = ""
for i in dane:
    temp_tab = []
    for j in i:
        if temp_tab.count(j)==0:
            temp_tab.append(j)
    if len(temp_tab)>liczba:
        liczba=len(temp_tab)
        slowo_2 = i
print("zad2: ", slowo_2, liczba)
alfabet = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}
slowa_rozne_10 = []
for i in dane:
    max_difference = 0
    for j in i:
        for k in i:
            temp_dif = abs(alfabet[j]-alfabet[k])
            if temp_dif>max_difference:
                max_difference=temp_dif
    if max_difference<=10:
        slowa_rozne_10.append(i)
print("zad3: ")
for i in slowa_rozne_10:
    print(i)