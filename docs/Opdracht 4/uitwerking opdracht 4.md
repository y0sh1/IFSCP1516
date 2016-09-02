# Opdracht 4

Schrijf een programma die binnen een directory m.b.v. metadata kan herkennen welke bestanden hier
aanwezig zijn. Laat de verschillende bestanden op soort kopieren naar een aparte directory per soort. Geef
ook een lijstje met aantallen verschillende soorten bestanden.
Voor bestandsherkenning kun je de standaard Python mime-types gebruiken, echter deze schakelt op
extensie. Een beter methode is gebruik te maken van de " Magic mime file". Hiervoor zijn aparte libraries
beschikbaar, of je gebruikt natuurlijk een linux-commando.
Schrijf daarnaast kleine programma' s die van de volgende bestanden metadata uitlezen en presenteren:
- pdf
- office (.doc, .xls, etc)

## Gebruik opdracht
Deze opdracht is middels python uit te voeren. Deze vereist de parameters ``-p <pad om te scannen>`` en ``-d <doel pad
om naar te kopieren>``.

Bij de kopieer actie, zal per type een submap in het doelpad aangemaakt worden, als het type
is aangestroffen in het te scannen pad.

Middels ``-h`` of ``--help`` kan de gebruiker eventueel zien welke parameters mogelijk en/of verplicht
zijn.

## Achtergrond informatie

### Sorting by type
Door de mimetypes van bestanden in te lezen, kunnen we bepalen welke bestand types aanwezig zijn.
Door tegengekomen bestanden te controlleren en voor de gevraagde mimetypes mappen aan te maken,
kunnen we duidelijk en snel deze sorteer en kopieer slag maken.

### Mime types
Mimetypes zijn waardes in bestanden, welke aangeven wat voor bestand men aan het
inlezen is. Deze mimetypes worden gebruikt door applicaties om te herkennen hoe de
applicatie het bestand moet benaderen. Diverse bestandstypes vereisen namelijk andere manieren
om ingelezen te worden, door verschillende standaarden in bestandsstructeren.

Door de mimetypes is de wijze van een bestand inlezen niet afhankelijk van de gegeven
extentie aan het bestand. Deze geeft namelijk alleen het systeem een indicatie met welke
applicatie het bestand gelezen kan worden, maar niet per definitie hoe deze ingeladen wordt.

### Kopieren
In de opdracht wordt gesteld dat betanden op een gesorteerde wijze uitgescheiden dienen te worden
opgeslagen. Dit houd in de praktijk in dat, wanneer bestanden gevonden zijn, mappen aangemaakt moeten
worden, welke betrekking hebben tot het gecontrolleerde bestandstype.

Met ``os.makedirs`` is het mogelijk om mappen aan te maken, op een specifieke lokatie. Vervolgens kunnen we
met ``shutil.copy2`` bestanden selecteren en naar de map kopieren. Het handige aan, specifiek, ``copy2`` is
dat deze geen doel bestandsnaam vereist, welke ons meer flexibiliteit kan leveren.

### Resources
- https://www.sitepoint.com/web-foundations/mime-types-complete-list/
- https://en.wikipedia.org/wiki/Media_type
- https://docs.python.org/3.0/library/mimetypes.html