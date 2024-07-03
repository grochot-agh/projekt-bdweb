[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/jsTzsySB)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=15151784)

Proposal:

Projekt: Gra hasłowa
Grupa: BDWeb (Jakub Bukowski, Irmina Drabas)

Temat: Gra hasłowa
Cel projektu:
Celem gry jest sprawdzenie i rozwinięcie kreatywności oraz koncentracji gracza. Gra zachęca do twórczego myślenia i skupienia poprzez tworzenie haseł, które muszą spełniać określone warunki.
Opis projektu:
Gra hasłowa to interaktywna aplikacja internetowa, w której zadaniem gracza jest stworzenie hasła spełniającego określone kryteria. Przykładowe wymagania dla hasła mogą obejmować:
Zawieranie konkretnego słowa.
Suma cyfr w haśle musi równać się określonej liczbie.
Hasło musi zawierać symbol pierwiastka chemicznego.
Gracz wprowadza swoje hasło do pola tekstowego, a aplikacja sprawdza, czy hasło spełnia podane warunki. Jeśli hasło jest poprawne, gracz przechodzi do następnego poziomu z nowym zestawem wymagań. Gra kończy się po osiągnięciu określonej liczby poziomów lub po przekroczeniu limitu czasu.

Wykorzystywane technologie:
HTML: Struktura strony internetowej, frontend.
Bootstrap: Ostylowanie aplikacji.
JavaScript: Renderowanie frontendu, interaktywność.
jQuery: Ułatwienie manipulacji DOM i obsługi zdarzeń.
Flask: Obsługa backendu

Możliwe kierunki rozwoju (do zrealizowania jeśli zostanie czas):
Aplikacje można rozwinąć w kierunku scrabble online z utrudnieniami, co może uatrakcyjnić rozgrywkę i pobudzić kreatywność graczy

Dokumenatcja:

Nazwa projektu: Gra hasłowa (Password Game)

Nazwa grupy: BDWeb (Jakub Bukowski, Irmina Drabas)

Opis projektu:
Gra polega na wymyśleniu hasła, dokładniej słowa z języka angielskiego, które spełnia trzy określone wymagania. W aktualnej wersji gry, do wymagań należą określona ilość znaków w haśle oraz uwzględnienie w haśle określonej litery.
Aby zagrać w grę, użytkownicy muszą stworzyć własne konta, a następnie się zalogować. Potem mogą stworzyć pokój lub dołączyć do już istniejącego. W oby dwóch przypadkach, potrzebne są nazwa pokoju oraz hasło. 
Gra nie rozpocznie się dopóki właściciel pokoju (osoba która go stworzyła) nie wciśnie przycisku start. Maksymalna liczba osób jakie mogą być w pokoju to 10.
Na odpowiedź gracze mają 30 sekund. Po każdej rundzie zostanie wyświetlona tabela wyników (nazwa użytkownika oraz liczba punktów). Punkty są doliczane do aktualnej ilości punktów gracza na podstawie poprawności odpowiedzi oraz czasu w jakim została podana. Następną rundę rozpoczyna właściciel pokoju.
Gra trwa aż gracz nie wyjdzie z pokoju lub jeżeli właściciel pokoju z niego wyjdzie (pokój jest wtedy usuwany).

Najważniejsze wykorzystywane technologie:
•	HTML – do struktury strony internetowej;
•	CSS – do stylu strony;
•	Bootstrap v.5.3.3 – do układu i stylu stron;
•	JavaScript z frameworkiem jQuery – do obsługi gry, eventów oraz animacji;
•	Flask – do backendu;
•	Flask-WTF – do walidacji danych z formularza;
•	Flask-Login – do logowania i rejestracji;
•	Flask-SocketIO – do obsługi gry, komunikacja klient-serwer, moduł multiplayer.

