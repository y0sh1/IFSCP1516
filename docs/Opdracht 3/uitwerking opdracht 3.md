# Opdracht 3

Schrijf een programma waarmee je een schijf kunt benaderen. Zorg dat je een directory kunt selecteren
en laat vervolgens de namen van de bestanden zien. Sorteer deze namen op alfabet en/of extensie. Zorg
dat je ook onderliggende directories aan kan. Zorg dat je de bestanden mbv een OS-commando kunt
kopiëren naar een ander opgegeven directory.
Lees het volgende artikel:
http://simson.net/clips/academic/2009.SADFE.xml_forensics.pdf
Integreer deze techniek in een script.

## Gebruik opdracht
Deze opdracht is middels python uit te voeren, waarbij de parameter ``-p`` verplicht is. Voor
meer informatie kan het script uitgevoert worden met de ``-h`` of ``--help`` parameters.

De ``-p`` parameter geeft de gebruiker de mogelijkheid aan te duiden welke map er
gescant dient te worden. Een voorbeeld hiervan is ``python Opdracht3.py -p /home/peter``.

## Achtergrond informatie

### listing
Middels de OS module, zal van de vorige map, alle inhoud weergegeven worden.
Dit wordt gedaan middels de walk functie. Middels functies uit os.path kunnen
we controlleren of een gesteld pad een map of bestand is. Afhankelijk hiervan
kunnen we vervolgens bepalen deze weer te geven.

### Resources
- http://stackoverflow.com/questions/120656/directory-listing-in-python