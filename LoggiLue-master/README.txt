pip install Flask
pip install flask-mysqldb
pip install flask_login
pip install flask-bcrypt

Ovanstående bibliotek behöver installeras för att koden skall fungera.
Skriv kommandona i CMD på Windows eller Terminalen på OSX.
Python 3 behöver också finnas installerat.

En databas som kör MySQL behövs för att koden skall fungera.
När det finns en databas är det bara att importera database/LoggiLue.sql för att få tabeller och kolumner i databasen.
Om anslutningen mot databasen inte fungerar kan värden i "db.py" behöva ändras för att passa databasen som används.


För att starta en lokal-webbserver som kör applikationen öppnar man "main.py" och kör igång denna!

Skapa en ny användare på hemsidan för att kunna logga in och ta del av resten av funktionaliteten.