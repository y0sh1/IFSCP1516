# Opdracht 6

Ga op zoek naar verschillende libraries voor het encrypten/decrypten van bestanden. Schrijf een
programma waarin je deze libraries toepast. Doe ditzelfde voor steganografie.
Bestudeer de volgende site met tools gebouwd in Python:
https://www.volatilesystems.com/default/volatility

## Gebruik opdracht
Deze opdracht is middels python uit te voeren. De applicatie toont aan, hoe een text bestand aangemaakt kan worden,
gecodeert kan worden en vervolgens gedecodeert kan worden. Het eind resultaat wordt middels een MD5 hash gecontroleerd

Het is niet mogelijk om een eigen bestand mee te geven voor een codeer of decodeer actie.
## Achtergrond informatie

### Keuze van coderen
Voor deze opdracht heb ik gekozen voor symetrische codering, omdat deze relatief veilig is
en de toepassing hiervan goed te realiseren is met python. Er zijn veel voorbeelden te vinden, waarbij
kennis van de precieze techniek hierachter minder vereist is.

### AES in python
AES vereist een sleutel van 16 of 32 karakters. Dit heeft de bibliotheek die wij gebruiken ook als verplichting.
Deze verplichting wordt ook in de applicatie afgedwongen en niet automatisch met padding aangevult.

Als de gebruiker een te korte sleutel opgeeft, zal de versleuteling alsnog plaats vinden, door handmatige paddig
in het script zelf.

### Resources:
- http://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto

