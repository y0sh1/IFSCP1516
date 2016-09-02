# Opdracht 5
Schrijf een programma die de gps informatie uitleest uit verschillende plaatjes en deze plot in Google
maps. Geef daarnaast in een tijdlijn weer de verschillende creatiedatums en wijzigingsdatums van de
(plaatjes) bestanden. Geef de diverse exif informatie zoals grootte, resolutie, etc. op grafische wijze weer

## GPS EXIF
JPEG afbeeldingen kunnen zogehete Exif metadata bevatten. Hierin wordt veel informatie opgeslagen over de afbeelding, oa:
- Waar deze gemaakt is
- Met welke camera deze gemaakt is
- Op wat voor stand de camera stond op het moment van fotograferen

## Werkwijze

Bestanden die in de images map geplaatst worden, zullen automatisch gescant worden.
Deze bestanden worden een voor een door het programma ingelezen en relevante informatie wordt hiervan weergegeven.
Exif gegevens worden daarbij ook geextraheert. De GPS gegevens worden in ``places.json`` gezet, welke ``report.html``
kan geven voor de gebruiker


##Resources:

- http://www.geospatialexperts.com/sampledata.php
- https://gist.github.com/snakeye/fdc372dbf11370fe29eb
- http://stackoverflow.com/questions/23118546/google-maps-v3-api-key-wont-work-for-local-testing
- https://developers.google.com/maps/documentation/javascript/get-api-key#get-an-api-key
- http://geojsonlint.com/
- https://pypi.python.org/pypi/geojson/
- https://developers.google.com/maps/documentation/javascript/examples/layer-data-simple#try-it-yourself