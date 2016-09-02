# Opdracht 7
Zoek uit welke api' s er beschikbaar zijn voor social media als twitter , facebook en instagram.
Schrijf een programma dat deze api's gebruikt en daarmee de relaties van een persoon laat zien.
Laat grafisch relaties , herkomst etc. zien

## Gebruik opdracht

### Installatie
Voordat aan de gang gegaan kan worden met deze opdracht, dient men eerst benodigde API
credentials bij twitter aan te vragen, via https://dev.twitter.com/oauth/overview/application-owner-access-tokens .

Men dient de volgende tokens en secrets aan te maken en in te voeren op de gewenste plek binnen het script:
-   consumer_key
-   consumer_secret
-   access_token
-   access_secret

### Uitvoeren
Deze opdracht is middels python uit te voeren. ``-h`` en ``--help`` kunnen gebruikt worden om parameters op te vragen,
welke verplicht danwel optioneel zijn.

De parameter ``-u <gebruikersnaam>`` is verplicht. Deze duid op de gebruiker, waarvan de volgers opgezocht dienen te worden.

Na het uitvoeren van het script, met valide API gegeven en een correcte gebruikersnaam,
zal een lijst weergegeven worden met ``<weergave naam> - <gebruikersnaam>``.

## Achtergrond informatie

### Twitter
Twitter bied een publieke API, welke gebruikt kan worden voor het ophalen van informatie
welke op twitter gedeeld is. Deze informatie vragen we, met authenticatie van de API key op.

Via de module python-twitter (ookwel twitter) kunnen we op twitter makkelijk api calls doen, en informatie die deze
terug geeft tevens gemakkelijk verwerken.

### Werking Applicatie
De applicatie zal bij het uitvoeren valideren of opgegeven API gegevens correct zijn. Vervolgens zal deze een lijst teruggeven met
alle volgers, voor zover de limieten van twitter dit toelaten.

### Resources:

- https://python-twitter.readthedocs.io/en/latest/