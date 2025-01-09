1. Jelenlegi helyzet leírása



A számításokhoz jelenleg különböző eszközöket használunk (pl. kézi számológép, Excel, mobilalkalmazások). Ezek gyakran nem nyújtanak testreszabott megoldást, bonyolultabb műveletek esetén pedig nehézkesen kezelhetők, vagy több lépésben kell az adatokat átalakítani. Az eszközök integrációja nincs megoldva.



2. Vágyálomrendszer leírása



A cél egy könnyen használható, platformfüggetlen számológép szoftver fejlesztése, amely:

• támogatja az alapvető (összeadás, kivonás, szorzás, osztás) és haladó matematikai műveleteket (pl. gyökvonás, hatványozás),

• rendelkezik felhasználóbarát kezelőfelülettel,

• mobil és asztali környezetben egyaránt működik,

• lehetővé teszi a műveletek mentését és visszakeresését.



3. Jelenlegi üzleti folyamatok modellje

1. Felhasználó kézzel beírja a műveleteket egy számológépbe vagy táblázatkezelőbe.

2. Az eredményt a felhasználó manuálisan más eszközökre viszi át, ha szükséges.

3. Hibák esetén újraszámításra van szükség.



Problémák:

• Időigényes manuális műveletek.

• Nehézkes visszakereshetőség.

• Nincs testreszabási lehetőség.



4. Igényelt üzleti folyamatok modellje

1. Felhasználó megnyitja az alkalmazást, és beírja a kívánt műveletet.

2. Az alkalmazás valós időben kiszámítja az eredményt, és megjeleníti azt.

3. A művelet elmenthető és kategorizálható (pl. „projekt X számításai”).

4. Az elmentett műveletek bármikor visszakereshetők és módosíthatók.



5. Követelménylista



Funkcionális követelmények:

• Alapvető műveletek támogatása (összeadás, kivonás, szorzás, osztás).

• Haladó matematikai műveletek (gyökvonás, hatványozás).

• Műveletek mentése és visszakeresése.

• Felhasználóbarát kezelőfelület.



Nem funkcionális követelmények:

• Platformfüggetlenség (web, mobil).

• Gyors válaszidő (<1 másodperc a számításokhoz).

• Felhasználói adatok biztonságos tárolása.



6. Használati esetek



Használati eset Leírás Résztvevők Előfeltétel Utófeltétel

1. Alapműveletek számítása A felhasználó beír egy alapműveletet (pl. 2+2), és az alkalmazás megjeleníti az eredményt. Felhasználó Az alkalmazás nyitva van. Az eredmény megjelenik a képernyőn.

2. Haladó műveletek számítása A felhasználó komplex műveletet ad meg (pl. 5^2), és az alkalmazás kiszámítja az eredményt. Felhasználó Az alkalmazás nyitva van. Az eredmény megjelenik a képernyőn.

3. Művelet mentése A felhasználó elment egy számítást. Felhasználó Egy számítás kész. A mentett művelet elérhető az archívumban.



7. Megfeleltetés



Használati esetek és követelmények kapcsolata:



Használati eset Kapcsolódó követelmények

1. Alapműveletek számítása Alapműveletek támogatása, felhasználóbarát kezelőfelület

2. Haladó műveletek számítása Haladó matematikai műveletek támogatása

3. Művelet mentése Műveletek mentése és visszakeresése



8. Képernyőtervek



Főképernyő:

• Számítási mező.

• Számgombok (0–9) és műveleti jelek (+, -, *, /).

• Haladó műveletek gombjai (pl. √, ^).

• Mentés gomb.



Archívum képernyő:

• Elmentett műveletek listája.

• Művelet részleteinek megtekintése.



9. Funkció-követelmény megfeleltetése



Funkció Kapcsolódó követelmény

Alapműveletek végrehajtása Alapműveletek támogatása

Haladó számítások Haladó műveletek támogatása

Adatok mentése és visszakeresése Műveletek mentése és visszakeresése



10. Fogalomszótár

• Alapműveletek: Az összeadás, kivonás, szorzás és osztás matematikai műveletek.

• Haladó műveletek: Olyan műveletek, mint a gyökvonás, hatványozás.

• Archívum: Az alkalmazásban mentett számítások listája.

• Platformfüggetlenség: Az alkalmazás használható böngészőben és mobileszközökön is.


