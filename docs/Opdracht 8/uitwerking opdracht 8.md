# Opdracht 8

De Digitale Toets heeft betrekking op de combinatie van bovenstaande opdrachten. Nu is het zaak
documentatie te schrijven bij de ontstane applicatie/ het script.
Beargumenteer waarom je hebt gekozen voor deze implementatie. Beschrijf welke libraries je hebt
gebruikt.
Zorg voor helpfunctie en/of gebruikershandleiding, en een technische handleiding met betrekking tot de
installatie van de software, waaronder de gebruikte libraries.
De applicatie dient correct te werken.
Geef in de verslaglegging aan welke testactiviteiten je hebt uitgevoerd. Beschrijf ook waarom je deze tests
hebt uitgevoerd.
Tijdens deze module heb je zelfstandig Python eigen moeten maken, beschrijf het materiaal dat je hebt
gebruikt en geef jouw mening over dit materiaal.

## Gebruik opdracht
Deze opdracht is middels python uit te voeren. Er worden meerdere parameters geaccepteert, welke een opdracht kunnen
activeren. Mogelijk zijn hier parameters voor nodig. Dit kan middels ``-h`` of ``--help`` gecontroleerd worden.
Het programma controlleert hier zelf ook op en zal aangeven als er niet voldoende informatie
opgegeven is.

## Achtergrond informatie
Opdracht 8 is afhankelijk van de andere 7 opdrachten. Technisch worden deze namelijk letterlijk
met hun parameters gestart. De verdere werking is daarom het zelfde als de opdrachten los,
echter is er nu een centraal aanspreekpunt.

### Os.system
Via het commando ``os.system`` wordt in opdracht 8 een opdracht verstuurt naar het uitvoerende systeem,
waardoor python aangeroepen wordt op een van de andere 7 opdrachten.