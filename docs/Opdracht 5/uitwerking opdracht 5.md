# Opdracht 5
Schrijf een programma die de gps informatie uitleest uit verschillende plaatjes en deze plot in Google
maps. Geef daarnaast in een tijdlijn weer de verschillende creatiedatums en wijzigingsdatums van de
(plaatjes) bestanden. Geef de diverse exif informatie zoals grootte, resolutie, etc. op grafische wijze weer

## Gebruik opdracht
Deze opdracht is middels python uit te voeren.

Middels ``-h`` of ``--help`` kan de gebruiker opvragen, welke parameters mogelijk zijn.
``-p`` is een verplichte parameter, welke ingestelt dient te worden op de te scannen map.

Nadat een map gescant is, zal in de python console enige informatie die aangetroffen is weergegeven
worden.

Aan het einde van de scan, kan middels ``report.html``, een overzicht weergegeven worden van de
gevonden GPS lokaties. Deze vormt op basis van Google Maps een kaart met punten, welke de GPS inhoud van de foto's
inhouden.

## Achtergrond informatie

### GPS EXIF
JPEG afbeeldingen kunnen zogehete Exif metadata bevatten. Hierin wordt veel informatie opgeslagen over de afbeelding, oa:
- Waar deze gemaakt is
- Met welke camera deze gemaakt is
- Op wat voor stand de camera stond op het moment van fotograferen

### Werkwijze

Bestanden die in het te scannen pad staan, zullen automatisch gescant worden.
Deze bestanden worden een voor een door het programma ingelezen en relevante informatie wordt hiervan weergegeven.
Exif gegevens worden daarbij ook geextraheert. De GPS gegevens worden in ``places.json`` gezet, welke ``report.html``
kan geven voor de gebruiker


###Resources:

- http://www.geospatialexperts.com/sampledata.php
- https://gist.github.com/snakeye/fdc372dbf11370fe29eb
- http://stackoverflow.com/questions/23118546/google-maps-v3-api-key-wont-work-for-local-testing
- https://developers.google.com/maps/documentation/javascript/get-api-key#get-an-api-key
- http://geojsonlint.com/
- https://pypi.python.org/pypi/geojson/
- https://developers.google.com/maps/documentation/javascript/examples/layer-data-simple#try-it-yourself