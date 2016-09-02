# IFSCP1516
Door: Joshua Beens - S1077749

## Installatie
De repository van IFSCP1516 bevat alle benodigde informatie, voor het installeren en uitvoeren
van de opdrachten die in het project aanwezig zijn.

Middels de python package manager ``pip`` is het mogelijk om de benodigde libraries van het internet
te downloaden en te installeren. Dit installatie proces kan middels het commando ``pip install -r requirements.txt``
gestart worden, als dit commando vanuit de root van het project gestart wordt.

Voor individuele opdrachten kan het mogelijk zijn dat er extra configuratie benodigd is. Hiervoor kan het beste
de documentatie van de betreffende opdracht geraadpleegd worden.

## Tests
Op alle opdrachten, met uitzondering van 8, worden testen gedaan op functionaliteit. Dit wordt gedaan middels
Travis CI, welke een test mogelijkheid bied, op een elke keer schoon systeem, met onze meegeven installatie parameters.

Alle scripts hebben 1 happy flow, waarvan de werking getest zal worden middels travis. Elke afwijking hiervan, resulteert mogelijk
in een negatief resultaat. De reden dat er maar 1 flow getest wordt, is omdat er niet meer flows zijn. De scripts gaan meer om
het bereiken van het doel, dan de perfectie afvanging van fouten. Hiervoor zijn het meer scripts, dan applicaties, waarvan
dit niveau wel verwacht kan worden.

### Travis CI
Wanneer er een commit gedaan wordt in de github repository van IFSCP1516, lanceert Travis CI 2 virtuele machines.
Deze virtuele machines draaien elk python, elk versie 2.7 of 3.2. Hierdoor kunne we op beide python versies
in 1 keer testen, met een schoon systeem.

In het bestand `.travis.yml` is te zien hoe deze test opgemaakt is.

Resultaten van deze tests zijn te zien op https://travis-ci.com/y0sh1/IFSCP1516/ (private repository) of
https://travis-ci.org/y0sh1/IFSCP1516/ (open source)

### Opdracht 1
De test van deze opdracht bestaat uit het uitvoeren van de applicatie. Deze heeft geen parameters en eigenlijk maar 1 flow.

### Opdracht 2
De test van deze opdracht bestaat uit het uitvoeren van de applicatie. Deze heeft geen parameters en eigenlijk maar 1 flow.

### Opdracht 3
De test van deze opdracht bestaat uit het uitvoeren van de applicatie met de parameter `-p ./` welke een scan zal starten in de
working directory. Standaard in travis is dit de root van de repository.

### Opdracht 4
De test van deze opdracht bestaat uit het uitvoeren van de applicatie met de parameter `-p ./` en `-d "./src/Opdracht 4/output"` welke een scan zal starten in de
working directory. Standaard in travis is dit de root van de repository. Vervolgens zullen gevonden documenten gekopieerd
worden naar `./src/Opdracht 4/output`.

### Opdracht 5
De test van deze opdracht bestaat uit het uitvoeren van de applicatie met de parameter `-p ./docs/samples/images` welke een scan zal starten in de
images directory. Vervolgens zullen relevante gegevens geprint worden van de afbeeldingen, welke
verkrijgbare informatie bevatten en places.json aangemaakt worden.

### Opdracht 6
De test van deze opdracht bestaat uit het uitvoeren van de applicatie. Deze heeft geen parameters en eigenlijk maar 1 flow.
Mochten er fouten optreden, zal het test resultaat negatief zijn door deze fout.

### Opdracht 7
De test van deze opdracht bestaat uit het uitvoeren van de applicatie.
Er zal geprobeert van de gebruiker, welke aangeduid is met parameter `-u <gebruikersnaam>`
zijn volgers op te halen. Als hier succesvol op gereageert wordt door de twitter API, zal de applicatie
de volgers weergeven. Als dit volledig gelukt is, zal het test resultaat positief zijn. Elke afwijking
zal resulteren in een negatief resultaat.