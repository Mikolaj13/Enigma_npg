Instrukcja obsługi:
Do otwarcia aplikacji służy plik Enigma.pyw.
1) Plugboard - kliknięcie dwuch przycisków z literami, zamienia je miejscami. Przycisk reset wraca 
wszystkie przyciski na ich miejsca. Przycisk continue przenosi do następnego okna.
2) Settings - przyciski add i subrtract a rotor zmieniają ilość rotorów w przedziale od 2 do 5. Przyciski + i - 
zmieniają startowe ustawienie rotorów na przedziale od 0 do 25. Przycisk reset zmienia wszystkie ustawienia na 0.
Przycisk continue przenosi do następnego okna.
3) Encoding/Decoding - przycisk encoding wybiera szyfrowanie, a decoding odszyfrowywanie.
4) Enigma - pisanie na klawiaturze powoduje szyfrowanie (tylko alfabet łaciński, cyfry i znaki interpunkcyjne), można
cofać tekst klawiszem BackSpace. Przycisk Load otwiera okno wyboru pliku tekstowego. Przycisk Save and close otwiera 
okno zapisu pliku tekstowego, a po wyborze zamyka okno. Przycisk Close zamyka okno

Cel projektu:
Tworzymy nowoczesną aplikację szyfrującą, inspirowaną zasadą działania historycznej maszyny
Enigma, dostosowaną do współczesnych potrzeb edukacyjnych, hobbystycznych i demonstracyjnych.
Aplikacja ma na celu zapewnienie użytkownikom prostego w
obsłudze, ale skutecznego narzędzia do szyfrowania i deszyfrowania wiadomości
tekstowych, z możliwością konfiguracji i rozszerzeń.

Główne funkcje aplikacji
Dwustopniowy mechanizm szyfrowania:

Początkowa translacja znaków: Pierwszy poziom szyfrowania oparty jest na ręcznie definiowanej translacji liter
    (np. A → B, B → Z, C → F), która stanowi bazową formę maskowania wiadomości.

Mechanizm rotorów: Drugi poziom oparty jest na zestawie rotorów, które
    przekształcają sygnały literowe na zasadzie zmieniających się mapowań.
    Rotory obracają się cyklicznie — każdy co trzeci znak, niezależnie i w swojej
    kolejności, co zapewnia dodatkową zmienność i bezpieczeństwo szyfru.

Konfigurowalność:

Użytkownik może wybrać liczbę rotorów w zakresie od dwóch do pięciu.

Istnieje możliwość ustawienia pozycji startowej każdego
rotora, co zwiększa liczbę możliwych kombinacji szyfru.

Translacja oraz ustawienia rotorów mogą być zapisywane i wczytywane, co pozwala na
zachowanie kluczy szyfrujących.

Obsługa wiadomości:

Możliwość wgrywania oraz zapisywania zaszyfrowanych i odszyfrowanych wiadomości w
formacie tekstowym.

Intuicyjny interfejs do zarządzania wiadomościami i konfiguracją szyfrowania.

Interfejs użytkownika:

Graficzna oprawa przygotowana w środowisku Python + Tkinter, pozwalająca
na łatwą obsługę przez użytkownika końcowego.

Planowane są wizualizacje pozycji rotorów, translacji oraz przebiegu szyfrowania w czasie
rzeczywistym, co zwiększy zrozumiałość działania algorytmu.

Technologie
Język programowania: Python

Biblioteki: Tkinter (GUI), opcjonalnie inne moduły Python standard library

Formaty plików: .txt (wiadomości)

Potencjał i zastosowania
Aplikacja może pełnić funkcję edukacyjną, tłumacząc zasady kryptografii na przykładzie Enigmy.

Może być wykorzystywana w celach hobbystycznych przez entuzjastów szyfrowania i historii
II wojny światowej.


