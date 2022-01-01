# AVT552 clock sync

Usługa do synchronizacji zegara w studiu z zegarem systemowym komputera

### Przeznaczenie

Zegar AVT5522 (https://serwis.avt.pl/manuals/AVT5522_2.pdf) posiada wejście RS232 do podłączenia odbiornika GPS, którego używa do synchronizacji czasu z timestampem GPS. Zegar jest kompatybilny z komendami NMEA i nasłuchuje komunikatu $GPSRMC, z którego pobiera datę i czas i aktualizuje zegar.

Przykładowa ramka (należy zakończyć ją znakami CR/LF):
```
$GPRMC,203700,A,0000.00,N,00000.00,W,0.0,0.0,051221,004.2,W*70
```
(co daje dzień 5. grudnia 2021 i godzinę 21:37:00, gdyż w ramce czas jest w UTC).

### Jak to działa

Skrypt "udaje" moduł i co 10 sekund:
* Pobiera czas systemowy (time.gmtime())
* Formatuje ramkę $GPSRMC - koordynaty są randomowe. Suma kontrolna ramki nie jest modyfikowana, ale firmware zegara jej nie sprawdza)
* Wysyła ramkę portem szeregowym do zegara.

### Instalacja i kofiguracja

Preferowanym miejscem do instalacji jest katalog `/opt`. Poniżej pełna procedura standardowej instalacji z roota z uwzględnieniem uruchomienia serwisu przy uruchomieniu:
```
cd /opt
git clone https://github.com/RadioAktywne/avt5522-sync.git
cd avt5522-sync
cp clock-sync.service /etc/systemd/system
systemctl enable clock-sync.service
systemctl start clock-sync.service
```

### Kastomizacja

Można zmienić domyślny port szeregowy (`/dev/ttyUSB0`) na inny zmieniając wartośc stałej `serial_port`, jeśli jest potrzeba.
