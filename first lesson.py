

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





