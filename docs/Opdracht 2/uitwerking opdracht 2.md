# Opdracht 2

In deze opdracht worden een aantal zaken gevraagt:

- Wat doet het inspringen van de code?
- Python Syntax
- het import commando, welke modules kent Python zoal?
- input en en output
- datatypes, values, arrays
- for/while/if statements
- functies

## Inspringen

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