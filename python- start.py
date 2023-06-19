from pickle import TRUE


print('Witaj, Świecie') 

message = "Witaj, Świecie" 
#nazwy mogą mieć jedynie litery, cyfry i podkreślenia, nie mogą zaczynać się od cyfry
#zakaz spacji oraz lepiej używać małych liter 
print(message) 
wynik = input(str("Jak się nazywasz ")) 
print(wynik.title()) # metody formatowania ciągu tekstowego
print(wynik.upper()) 
print(wynik.lower()) 

first_name = "filip"
surname = "xxxx"
full_name = f" Imie i nazwisko to: {first_name} {surname}" # first method
#full_name = "{} {}".format(first_name, surname) #second method
print(full_name.title())

#\t - tab 
#\n similar to break line 




#białe znaki to spacje,tabulatory  etp

favourite_language = 'python '
print(favourite_language.rstrip()) #Jest to zabieg tymczasowy, jest jeszcze lstrip
favourite_language = favourite_language.strip() # Za to ten zabieg stały


#int / int  = float
#int / float = float nevetheless
universe_age = 14_000_000_000
print(universe_age)

x, y, z = 1, 2, 3
print(x, y, z)

MAX_CONNECTIONS = 5000 # nazwy zapisane wielkimi literami są traktowane jako stałe! 












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