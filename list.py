
#listy
bicycles = ['trekingowy', 'górski', 'miejski', 'szosowy']
print(bicycles[-2].title())

print(f"Moim zdaniem najlepszym rowerem jest rower typu {bicycles[-1].title()}")

bicycles[-2] = 'hybrydowy' # zmiana 
print(bicycles[-2])


#dodawanie elementów do listy: 
bicycles.append('elektryczny') #method to add another element
print(bicycles)

cars = [] #create a list 
cars.insert(0, 'ducati') #pozwala na stworzenie elementu w każdym możliwym miejscu listy, poprzez przesuwanie elementów
print(cars)




#usuwanie elementów z listy:
del bicycles[0] #można usunąć każdy element o ile znamy jego indeks, niema powrotu do tego elementu / używane jeżeli nie masz zamiaru już z niego korzystać.
print(bicycles)

cars = ['BMW','AUDI','Tesla'] 
popped_cars = cars.pop(1) #usuwa element, ale dalej można z niego korzystać. Zostaje on przeniesiony do popped_cars. / masz zamiar z niego jeszcze korzystać.
print(popped_cars)

print(cars)
nowe_auta = 'Tesla'
cars.remove(nowe_auta) #usuwa element, którego nie znam indeks ani pozycję, tylko wartość / usuwa tylko jeden raz, jeżeli znajduję się więcej podobnych elementów należy użyć pętli
print(cars)

#sortowanie listy 

#trwałe metody sortowania 
bicycles.sort() #alfabetycznie
print(bicycles)
bicycles.sort(reverse=True) #odwortna kolejność alfabetyczna
print(bicycles)

#tymczasowe metody sortowania // nie wpływają na rzeczywistę umiejscowienie listy
print(sorted(bicycles, reverse=True))

#odwrócenie pierwotnej kolejności listy można za pomocą: // po następnym użyciu wraca do normy
cars.reverse()
print(cars)
cars.reverse()

#określanie wielkości listy można za pomocą: //
print(len(bicycles))




#petla for 
for bicycle in bicycles:
    print(f"Modele rowerów dostępny na rynku {bicycle.title()}")
    print(f"Z niecierpliwością czekam na twój kolejny występ, {bicycle.title()}.\n")

for value in range(1,6):
    print(value)

numbers = list(range(2,11,2))
print(numbers)

#obliczanie drugiej potęgi dla liczb całkowitych z zakresu od 1 do 10
liczby = []
for squares in range(1,11):
    wynik = squares**2
    liczby.append(wynik)
    #liczby.append(squares**2) // skrócona wersja 
print(liczby)

wniosek = [cyfry**2 for cyfry in range(1,11)] # lista składane-> list comprehension
print(wniosek)


print(min(liczby)) #wyciąga najmniejszą liczbę
print(max(liczby)) #wycigą największą liczbę
print(sum(liczby)) #sumuje wszystkie liczby z listy


for wycinek in bicycles[:3]:#wycinek listy // praca na określonych indeksach do 3 ale zawsze jeden mniejszy
    print(wycinek)

skopiowana_lista = cars[:]#kopiowanie listy za pomocą wycinka
print(skopiowana_lista)

wartosci = (250, 500)#krotka(ang.tuples)   czyli lista ale ze stałymi wartościami, zawsze  w okrągłym nawiasie  i nawet przy jednej wartości musi być ,
print(wartosci[0]) 
print(wartosci[1])

#nie mozna modyfikować krotki, ale istnieje możliwość przypisania zupełnie nowej wartości zmiennej przechowującej tę krotkę
wartosci = (200,400)
print(wartosci[0]) 
print(wartosci[1])


age = 18
if age <= 12: #używa się  w przypadku jednego bloku , jezeli więcej not worth
    #do sprawdzania warunków używamy and,or lub not in / in do sprawdzania elementów w listach
    price = '12zl'
    print(price)
elif age <= 18: #mozna uzywac ile się chce 
    price = '20zl'
    print(price)
else: # można nie trzeba używać 
    price = '40zl'
    print(price)

    #znak = to przypisanie
    #znak == to porównanie jeżeli są równe to true , znak != jeżeli nie są równe to true 



requested_toppings = ['ananas', 'double cheese']
if requested_toppings: #sprawdzanie czy lista nie jest pusta
    for requested_topping in requested_toppings:
        print(f"Dodaje {requested_topping}")
else:
     print("Czy na pewno ma być pizza bez dodatków?")


#użycie wielu list
dostepne_produkty = ['ananas', 'podwójny ser', 'papryka', 'szynka']
zamowione_produkty = ['ananas', 'ogorki']

for zamowiony_produkt in zamowione_produkty:  
    if zamowiony_produkt in dostepne_produkty: #sprawdzanie czy element jest w liście 
        print(f"\nDodaje {zamowiony_produkt}")
    else:
        print(f"zamowiony produkt {zamowiony_produkt} nie jest dostepny ") 

