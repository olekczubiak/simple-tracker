# Simple-tracker-readme

## Backend:

Instalacja: 
```
#Zbuduj obraz w folderze backend
docker build -t backend .

#Uruchom kontener
docker run --name tracker -d -p 80:80 backend
```
Flaga **-d** odpowiada za działanie kontenera w tle.


Trzeba pamiętać o tym, że trzeba odkomentować aliasy do bazy danych na serwerze VPS.
