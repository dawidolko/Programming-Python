# Język skryptowy lab6

### Wyrażenia regularne
Wyrażenia regularne są potężnym narzędziem do różnego rodzaju manipulacji ciągami znaków.
Są obecne jako biblioteki w większości nowoczesnych języków programowania, a nie tylko w Pythonie.
Są przydatne do dwóch głównych zadań:
- sprawdzenie, czy ciągi są zgodne z wzorcem (na przykład, że ciąg ma format adresu e-mail),
- wykonywanie podstawień w ciągu znaków (np. zmiana wszystkich pisowni amerykańskich na angielskie).

Do wyrażeń regularnych w Pythonie można uzyskać dostęp za pomocą modułu `re`, który jest częścią standardowej biblioteki.
Po zdefiniowaniu wyrażenia regularnego można użyć funkcji `re.match` w celu ustalenia, czy pasuje ono do początku ciągu znaków.
Jeśli tak, dopasowanie zwraca obiekt reprezentujący dopasowanie, jeśli nie, zwraca `None`.
Inne funkcje do dopasowania wzorców to `re.search` i `re.findall`.
Funkcja `re.search` odnajduje dopasowanie wzorca w dowolnym miejscu ciągu.
Funkcja `re.findall` zwraca listę wszystkich podciągów pasujących do wzorca.
```Python
import re

pattern = r"spam"

if re.search(pattern, "ssspamspamspamsp"):
    print(re.search(pattern, "ssspamspamspamsp").span().__getitem__(1))
else:
    print("No mach")
```

Funkcja `search` zwraca obiekt za pomocą kilku metod, które podają szczegóły na jego temat.
Te metody obejmują grupę, która zwraca dopasowany ciąg, początek i koniec, które zwracają pozycje początkową i końcową pierwszego dopasowania, i zakres, który zwraca pozycje początkową i końcową pierwszego dopasowania jako krotkę.
```Python
import re

pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
   print(match.group())
   print(match.start())
   print(match.end())
   print(match.span())
```
### Wyszukaj i zamień

Jedną z najważniejszych metod, które używają wyrażeń regularnych jest `sub`.
```Python
re.sub(pattern, repl, string, max=0)
```
Ta metoda zastępuje wszystkie wystąpienia `pattern` w łańcuchu za pomocą `repl`, zastępując wszystkie wystąpienia, chyba że podana jest wartość `max`. Ta metoda zwraca zmodyfikowany ciąg.
```Python
import re

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)
```
### Metaznaki
Pierwszym metaznakiem, jest symbol `.` (kropka).
Dopasowuje dowolny znak, z wyjątkiem znaku nowej linii.
```Python
import re

pattern = r"gr.y"

if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "blue"):
   print("Match 3")
```
Następne dwa metaznaki to `^` i `$`.
Dopasowują odpowiednio początek i koniec ciągu znaków.
```Python
import re

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "stingray"):
   print("Match 3")
```
### Klasy znaków
Umożliwiają dopasowanie tylko jednego określonego zestawu znaków.
Klasa znaków jest tworzona przez umieszczenie znaków, które pasują w nawiasach kwadratowych.
```Python
import re

pattern = r"[aeiou]"

if re.search(pattern, "grey"):
   print("Match 1")

if re.search(pattern, "qwertyuiop"):
   print("Match 2")

if re.search(pattern, "rhythm myths"):
   print("Match 3")
```
>Wzorzec [aeiou] w funkcji wyszukiwania pasuje do wszystkich ciągów, które zawierają dowolny zdefiniowany znak.

Klasy postaci mogą również dopasowywać zakresy znaków.
Kilka przykładów:
Klasa [a-z] dopasowuje każdą literę alfabetu pisaną małymi literami.
Klasa [G-P] dopasowuje dowolną wielką literę od G do P.
Klasa [0-9] pasuje do dowolnej cyfry.
W jednej klasie można uwzględnić wiele zakresów. Na przykład [A-Za-z] pasuje do litery dowolnego rozmiaru.
```Python
import re

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"):
   print("Match 1")

if re.search(pattern, "E3"):
   print("Match 2")

if re.search(pattern, "1ab"):
   print("Match 3")
```
Umieść `^` na początku klasy postaci, aby ją odwrócić.
Powoduje to, że pasuje on do dowolnego znaku innego niż te uwzględnione.
Inne metaznaki, takie jak `$` i`.`, Nie mają znaczenia w obrębie klas znaków.
Metaznak `^` nie ma znaczenia, chyba że jest pierwszym znakiem w klasie.
```Python
import re

pattern = r"[^A-Z]"

if re.search(pattern, "this is all quiet"):
   print("Match 1")

if re.search(pattern, "AbCdEfG123"):
   print("Match 2")

if re.search(pattern, "THISISALLSHOUTING"):
   print("Match 3")
```
Inne metaznaki to `*`,`+`,`?`,`{` i `}`.
Określają one liczby powtórzeń.
Metaznak `*` oznacza zero lub więcej powtórzeń poprzedniego wzorca. Próbuje dopasować tyle powtórzeń, ile to możliwe. Poprzedni wzorzec może być pojedynczym znakiem, klasą lub grupą znaków w nawiasie.
```Python
import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
   print("Match 1")

if re.match(pattern, "eggspamspamegg"):
   print("Match 2")

if re.match(pattern, "spam"):
   print("Match 3")
```
Metaznak `+` jest bardzo podobny do `*`, z wyjątkiem tego, że oznacza jedno lub więcej powtórzeń.
```Python
import re

pattern = r"g+"

if re.match(pattern, "g"):
   print("Match 1")

if re.match(pattern, "gggggggggggggg"):
   print("Match 2")

if re.match(pattern, "abc"):
   print("Match 3")
```
Metaznak `?` oznacza zero lub jedno powtórzenie.
```Python
import re

pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
   print("Match 1")

if re.match(pattern, "icecream"):
   print("Match 2")

if re.match(pattern, "sausages"):
   print("Match 3")

if re.match(pattern, "ice--ice"):
   print("Match 4")
```
### Nawiasy klamrowe
Za pomocą nawiasów klamrowych można reprezentować liczbę powtórzeń między dwiema liczbami.
Wyrażenia regularne {x, y} oznaczają między x i y powtórzeń czegoś.
Stąd {0,1} to to samo co `?`.
Jeśli brakuje pierwszej liczby, przyjmuje się, że wynosi zero. Jeśli brakuje drugiej liczby, przyjmuje się, że jest nieskończoność.
```Python
import re

pattern = r"9{1,3}$"

if re.match(pattern, "9"):
   print("Match 1")

if re.match(pattern, "999"):
   print("Match 2")

if re.match(pattern, "9999"):
   print("Match 3")
```

## Django

### Zanim zaczniesz
Upewnij się, że zostały spełnione następujące wymagania wstępne:
* Pracujesz z PyCharm w wersji 2016.1 lub nowszej. 
* Masz co najmniej jednego interpretera języka Python poprawnie zainstalowanego na komputerze (Python 3.4.1. lub nowszy).
* Masz zainstalowany pakiet Django (Django 1.10.0 lub nowszy). Aby dowiedzieć się, jak instalować pakiety za pomocą interfejsu użytkownika PyCharm, przeczytaj sekcję https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html

### Tworzenie nowego projektu
Właściwie wszystkie nowe projekty są tworzone w ten sam sposób: klikając przycisk _Create new project_ w obszarze Szybki start ekranu powitalnego:
![image](https://user-images.githubusercontent.com/12736759/40280567-c6764e4c-5c55-11e8-8de9-976e1f7ce3cb.png)

Następnie wybierz żądany typ projektu (tutaj jest Django). Określ nazwę i lokalizację projektu.

Najlepszą praktyką Pythona jest utworzenie __virtualenv__ dla każdego projektu. Aby to zrobić, rozwiń węzeł _Project Interpreter: New Virtualenv Environment_ i wybierz narzędzie używane do tworzenia nowego środowiska wirtualnego. Wybierzmy narzędzie __Virtualenv__ i określ lokalizację oraz podstawowy interpreter używany w nowym środowisku wirtualnym.

Następnie rozwiń węzeł _More Settings_ i określ ustawienia związane z Django. W polu _Application name_ podaj nazwę aplikacji
![image](https://user-images.githubusercontent.com/12736759/40280677-48f21260-5c57-11e8-9658-c7930222d744.png)

Kliknij __Create__ - projekt Django jest gotowy.

### Eksplorowanie struktury projektu
Gotowy projekt zawiera pliki i katalogi specyficzne dla frameworku. To samo dzieje się, gdy tworzony jest projekt dowolnego obsługiwanego typu, np. Pyramid lub Google App Engine.

Zobaczmy, jak struktura nowego projektu jest widoczna w oknie narzędzia projektu.
### Widok plików projektu
Ten widok jest domyślnie wyświetlany. Pokazuje strukturę projektu Django: ankiety i katalogi mysite; zobacz także pliki _manage.py_ i _settings.py_.

![image](https://user-images.githubusercontent.com/12736759/40280690-87bec3a8-5c57-11e8-8a65-9696ad78e265.png)

### Struktura projektu
Co widzimy w widoku projektu?

* Katalog __DjangoApp__ jest kontenerem dla twojego projektu. W widoku projektu oznaczono go pogrubioną czcionką.
* __manage.py__: To narzędzie wiersza polecenia, które pozwala na interakcję z projektem Django. Szczegółowe informacje w dokumentacji Django.
* Zagnieżdżony katalog __DjangoApp__ jest aktualnym pakietem Pythona dla twojego projektu.
* __DjangoApp/\_\_init\_\_.py__: Ten pusty plik mówi Pythonowi, że ten katalog powinien być uznany za pakiet Pythona.
* __DjangoApp/settings.py__: Ten plik zawiera konfigurację twojego projektu Django.
* __DjangoApp/urls.py__: Ten plik zawiera deklaracje adresów URL dla twojego projektu Django.
* __DjangoApp/wsgi.py__: Ten plik definiuje punkt wejścia dla serwerów _WWW_, które obsługują twój projekt. 
* Zagnieżdżony katalog __MyApp__ zawiera wszystkie pliki wymagane do utworzenia aplikacji Django (w tej chwili te pliki są puste):
    * __MyApp/\_\_init\_\_.py__ mówi Pythonowi, że ten katalog powinien być traktowany jako pakiet Pythona.
    * __MyApp/models.py__: W tym pliku utworzymy modele dla naszej aplikacji.
    * __MyApp/views.py__: W tym pliku utworzymy widoki.
* Katalog szablonów (templates) jest narazie pusty. Powinien zawierać pliki szablonów.
* Zagnieżdżony katalog _migrations_ zawiera już tylko plik pakietu _init_.py, ale będzie używany w przyszłości w celu propagowania zmian wprowadzonych w modelach (dodawanie pola, usuwanie modelu itp.) do schematu bazy danych.

W razie potrzeby można utworzyć dowolną liczbę aplikacji Django. Aby dodać aplikację do projektu, uruchom zadanie `startapp` narzędzia `manage.py` (Tools | Run manage.py, a następnie wpisz polecenie startapp w konsoli).

### Konfigurowanie bazy danych
W pliku _settings.py_ określ bazę danych, której chcesz użyć w swojej aplikacji. W tym celu znajdź zmienną `DATABASES`. Następnie w linii `ENGINE` dodaj nazwę systemu zarządzania bazą danych po kropce.

W wierszu `NAME` wprowadź nazwę żądanej bazy danych, nawet jeśli jeszcze nie istnieje.
![image](https://user-images.githubusercontent.com/12736759/40280914-75081978-5c5a-11e8-918b-c172899c91db.png)

### Uruchamianie serwera Django
Ponieważ wybieramy _sqlite3_, nie musimy definiować innych wartości (poświadczenia użytkownika, port i host). Sprawdźmy teraz, czy nasze ustawienia są poprawne. Można to zrobić najłatwiej: wystarczy uruchomić zadanie `runserver` w narzędziu manage.py: naciśnij `Ctrl + Alt + R` i wpisz nazwę zadania w konsoli _manage.py_ po spacji można dopisać port na jakim chcemy aby urochomił się serwer aplikacji.
![image](https://user-images.githubusercontent.com/12736759/40280966-4ada07aa-5c5b-11e8-9103-6825ae734b0d.png)

Wybierz sugerowany link i zobacz następującą stronę:
![image](https://user-images.githubusercontent.com/12736759/40280958-25a2df52-5c5b-11e8-8212-847cc3c47a70.png)

### Tworzenie modeli
Następnie otwórz plik _models.py_ i zauważ, że instrukcja importu już istnieje. Następnie wpisz następujący kod:
```Python
from django.db import models

# the following lines added:
import datetime
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, )
    choice_test = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):

        return self.choice_test
```
### Tworzenie bazy danych
Musimy stworzyć tabele dla nowego modelu. W tym celu użyjemy magicznego skrótu `Ctrl + Alt + R` do wywołania konsoli _manage.py_. Pierwsze polecenie do wykonania to `makemigrations MyApp`:
![image](https://user-images.githubusercontent.com/12736759/40281028-333f2638-5c5c-11e8-9b57-0cdbad2eb543.png)

W ten sposób powiedziałeś Django, że zostały utworzone dwa nowe modele, mianowicie `Choise` i `Question`, i utworzyłeś migrację widoczną w strukturze projektu w katalogu _migrations_.

Następnie po znaku zachęty wpisz następujące polecenie:
`sqlmigrate MyApp 0001`
W konsoli widoczne będą wykonane zapytania do bazy danych.

Na koniec uruchom komendę `migrate`, aby faktycznie utworzyć te tabele w bazie danych. W przypadku gdy w danym projekcie posiadasz więcej aplikacji po spacji dopisz nazwię aplikacji aby migracja odnosiła sie tylko do niej.

### Wykonywanie funkcji administracyjnych
Najpierw utwórz superużytkownika. Aby to zrobić, wpisz polecenie `createsuperuser` w konsoli _manage.py_, podaj nazwę użytkownika, swój adres e-mail i hasło:

![image](https://user-images.githubusercontent.com/12736759/40281194-6e90e6a2-5c5e-11e8-8b46-12b5c87f6da2.png)

Ponieważ zdecydowaliśmy się włączyć administrację witryną, PyCharm odkomentował już odpowiednie wiersze w pliku _urls.py_.

### Przygotowywanie konfiguracji uruchamiania/debugowania
Jesteśmy teraz gotowi, aby przejść do strony administratora. Oczywiście, możliwe jest uruchomienie serwera Django, następnie przejście do przeglądarki i wpisanie całego adresu URL na pasku adresu.

### Uruchomienie strony administratora
Teraz, aby uruchomić aplikację, naciśnij Shift + F10 lub kliknij uruchom na głównym pasku narzędzi, aby otworzyć standardową stronę logowania do witryny Django:
![image](https://user-images.githubusercontent.com/12736759/40281283-0eec548c-5c60-11e8-9f5a-5998dd0396f7.png)

Po zalogowaniu się wyświetlana jest strona administracyjna. Ma sekcję __Authentication and Authorization (Groups and Users)__, ale ankiety nie są dostępne. Dlaczego tak?

Musimy powiedzieć administratorowi, że obiekty `Question` mają interfejs administratora; aby to zrobić, otwórzmy plik _MyApp/admin.py_ i wpisz następujący kod:
```Python
from django.contrib import admin
from .models import Question #this line added
admin.site.register(Question)#this line added
```

Odśwież stronę i zobacz sekcję MyApp z pytaniami.

![image](https://user-images.githubusercontent.com/12736759/40282731-e2aafdd8-5c73-11e8-9d9d-a6c1dd984a32.png)

Kliknij Dodaj, aby utworzyć kilka pytań.

### Edytowanie pliku admin.py
Jednak każde pytanie ma wiele opcji, ale wybory wciąż nie są dostępne. Ponownie otwórz edycję pliku i zmień ją w następujący sposób:
```Python
from django.contrib import admin
from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
```
Teraz spójrz na stronę zmiany pytania.
![image](https://user-images.githubusercontent.com/12736759/40281427-c678a384-5c61-11e8-8768-20d21a555bed.png)
### Pisanie widoków
Otwórz plik _MyApp/views.py_ i wpisz następujący kod Pythona:
```Python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```    
Następnie dodaj nowy plik do katalogu _MyApp_ z nazwą ___urls.py___ i wpisz w nim następujący kod:
```Python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```
Następnie otwórz plik _DjangoApp/urls.py (który PyCharm już utworzył dla ciebie) i dodaj adres URL strony indeksu. Powinieneś otrzymać następujący kod:
```Python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('polls/', include('MyApp.urls')),
    path('admin/', admin.site.urls),
]
```
Teraz otwórz stronę 127.0.0.1:8000/polls/ i ciesz się:

![image](https://user-images.githubusercontent.com/12736759/40281765-aa3c08b0-5c65-11e8-93d1-29bff7c71e18.png)

Następnie dodajmy więcej widoków. Ponownie dodaj następujący kod do pliku _MyApp/views.py_:
```Python
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```
Połącz te nowe widoki z modułem _MyApp/urls.py_, dodając następujące wywołania url():
```Python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
```
Otwórz teraz odpowiednie strony w przeglądarce.

### Tworzenie szablonów Django
Jak widzisz, projektowanie tych stron jest zakodowane w widokach. Aby uczynić go bardziej czytelnym, musisz edytować odpowiedni kod w Pythonie. Oddzielmy wizualną reprezentację danych wyjściowych od Pythona - aby to zrobić, stwórzmy szablony.

Otwórz, plik _MyApp/views.py_ i zastąpić jego zawartość następującym kodem:
```Python
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```
Pierwszą rzeczą, którą zauważysz, jest nierozwiązane odniesienie do strony __index.html__:
![image](https://user-images.githubusercontent.com/12736759/40281994-54816200-5c68-11e8-87e4-fe28cc631366.png)

PyCharm sugeruje szybką naprawę: jeśli klikniesz żarówkę lub naciśniesz Alt + Enter, odpowiedni plik szablonu zostanie utworzony w folderze szablonów.

Plik _index.html_ jest już pusty. Dodaj do niego następujący kod:
```Python
{% load staticfiles %}
<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}"/>
{% if latest_question_list %}
    <ul>
        {% for question in latest_question_list %}
            <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
        {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```
W tagach HTML dostępne jest także uzupełnianie kodu.

Zwróć uwagę na ikony ![image](https://user-images.githubusercontent.com/12736759/40282031-0d24b2c6-5c69-11e8-95e3-33559cedb162.png) i ![image](https://user-images.githubusercontent.com/12736759/40282037-2a184cd0-5c69-11e8-88c4-c3bf2ec8276f.png), które pojawiają się na lewym marginesie odpowiednio plików _views.py_ i _index.html_. Ikony te umożliwiają natychmiastowe przejście między metodą widoku a jej szablonem.
### Korzystanie z arkusza stylów
Jak widać w pliku widoku _index.html_, istnieje odniesienie do arkusza stylów i jest ono niezdefiniowane:

1. Zdefiniuj to odniesienie w następujący sposób:
2. Utworzyć katalog w katalogu głównym o nazwie __static/polls__.
3. Następnie utwórz arkusz stylów w tym katalogu. 
4. Uzupełnij zawartość do utworzonego arkusza stylów, w zależności od twoich preferencji. Na przykład chcielibyśmy zobaczyć wypunktowaną listę pytań w kolorze zielonym:
```CSS
li a {
color: green;
}
```
W pliku _setings.py_ dopisz poniższy kod
```Python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```
Teraz sprawdźmy listę dostępnych ankiet(127.0.0.1:8888/polls). Nasza strona administratora już działa, a najprostszym sposobem odwiedzenia strony zawierającej listę pytań (stronę indeksu) jest określenie jej adresu URL.
![image](https://user-images.githubusercontent.com/12736759/40282818-0cf200b8-5c75-11e8-9139-01c196053a34.png)

### Sprawdź to…
Teraz zobaczmy, jak PyCharm pomaga uprościć testowanie aplikacji.

Istnieje już plik _tests.py_ w katalogu __MyApp__. Ten plik jest pusty. Naturalnie wskazane jest umieszczenie nowych testów w tym konkretnym pliku. Na przykład chcemy się upewnić, że nasza ankieta nie jest pusta:
```Python
import datetime
from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
from .models import Question


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionViewTests(TestCase):
    def test_index_view_with_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
```
Aby uruchomić ten test, kliknij prawym przyciskiem myszy tło pliku _tests.py_ w edytorze, wybierz opcję _Run_.
![image](https://user-images.githubusercontent.com/12736759/40282614-71ccd68c-5c72-11e8-815b-5679e8e6b9e5.png)

### Podsumowanie
Pomyślnie utworzyłeś i uruchomiłeś prostą aplikację Django. Powtórzmy to, co zostało zrobione przy pomocy PyCharm:
* Projekt i aplikacja Django zostały stworzone
* Uruchomiono serwer Django
* Baza danych skonfigurowana
* Utworzono modele, widoki i szablony
* Uruchomiono aplikację
* Testy stworzone i wykonane

![image](https://user-images.githubusercontent.com/12736759/40282621-89e71c46-5c72-11e8-9934-6f635cac153d.png)
