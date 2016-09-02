# Opdracht 2

In deze opdracht worden een aantal zaken gevraagt:

- Wat doet het inspringen van de code?
- Python Syntax
- het import commando, welke modules kent Python zoal?
- input en en output
- datatypes, values, arrays
- for/while/if statements
- functies

## Gebruik opdracht
Deze opdracht is middels python uit te voeren.

De applicatie zal een aantal funtionaliteiten van python uitlichten,
welke standaard meegelevert worden. Deze zullen direct bij het aanroepen
van het script uitgevoerd worden.
## Achtergrond informatie

### Inspringen

Resources:
- http://www.diveintopython.net/getting_to_know_python/indenting_code.html


Het inspringen, ook wel indents, van code heeft de bedoeling om blokken van code te maken.
Dit zorgt er voor dat, zoals bij andere talen, blokken en statements niet afgesloten hoeven te worden.
Het resultaat is als volgt:
```
Hoofd
    Blok 1
        Blok 1.1
            Blok 1.1.1
            Blok 1.1.2
        Blok 1.2
    Blok 2
        Blok 2.1
        Blok 2.2
            Blok 2.2.1
            Blok 2.2.2
Hoofd
```

Een voorbeeld van echte code zal zijn:
```python
class HelloWorld:
    greeting = ""

    def __init__(self):
        self.greeting = "hello world"

    def function1(self):
        if self.greeting == "hello world":
            print(self.greeting)
        return True

    def function2(self):
        if 1 == 1:
            print(self.greeting)
            return False
        else:
            return True

HelloWorld().function1()
HelloWorld().function2()
```

### Python Syntax

Resources:
    - http://www.tutorialspoint.com/python/python_basic_syntax.htm

De syntax van python is vrij uitgebreid. Om niet de complete
inhoud van de tutorialspoint.com pagina te kopieren,
adviseer ik hier te kijken. Deze geeft uitgebreide informatie.

### Imports en standard modules

Python geeft de programmeur de mogelijkheid bestaande code te gebruiken
binnen een nieuw programma. Dit geeft flexibiliteit aan taken die veel
projecten hetzelfde doen, voor bijvoorbeeld communicatie met protocollen
of het interpreteren van standaarden binnen computer systemen.

Imports kunnen voorkomen uit eigen code, of gedeelde code van andere
programmeurs. Deze kunnen met een programma als ``pip`` geinstalleerd worden.

Een import kan met de volgende code gedaan worden:

```
import <module>
```

Zoals eerder aangegeven kan er via het programma ``pip`` een installatie van bestaande
code van andere ontwikkelaars geinstalleerd worden. Dit programma kan vanaf internet, of een lokale server,
beschikbaar gestelde code ophalen en installeren.

Installeren van pip onder een windows systeem kan met de volgende commando's:

```
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
```

Vervolgens kan via het volgende commando een module geinstalleerd worden:

```
pip install <module>
```

Modules zijn o.a. te vinden op de website https://pypi.python.org/pypi .

### input en en output

Python heeft veel manieren om in- en output te doen. Dit kan middels de console,
 met bestanden die ingeladen worden en input via parameters.

### datatypes, values, arrays

Python heeft niet echt stricte datatypes, zoals talen als C, maar het heeft wel datatypes.
Deze kunnen vrij, als objecten, aangemaakt worden. Deze dienen ook als zo zijde
behandeld te woden.

### for/while/if statements

#### While
De eerste lus controle structuur is het while statement. Normaal gezien begint de interpreter bij het eerste statement en neemt dan het volgende. Controlestructuren veranderen de volgorde waarin statements uitgevoerd worden of beslissen of het al dan niet uitgevoerd moet worden. Het volgende programma maakt gebruikt van het while statement:
```
a = 0
while a < 10 :
    a += 1
    print a
print "Loop finished"
```

#### For
Een volgende manier om een lus te implementeren is met hulp van het for statement. Een voorbeeld analoog aan de while lus kan er alsvolgt uitzien:
```
onetoten = range(1,11)
for a in onetoten:
    print a
print "Loop finished"
```

De uitvoer is volkomen identiek aan het while-voorbeeld: de getallen van 1 tem 10, gevolgd door de string Loop finished. De code ziet er echter verschillend uit. De eerste regel maakt gebruik van de range(start,einde) functie. Dit genereert een array getallen:

```
>>> range (1,11)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
### functies

Functies worden gemaakt met het def-statement, met of zonder argumenten.

```
def kwadrateren(getal):
    return getal*getal

print(kwadrateren(6))
>> 36
```