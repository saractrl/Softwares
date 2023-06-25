# SW-Keys

Es soll eine Software in Python erstellt werden, welche zur Speicherung von Software-Keys genutzt werden kann. Die Software-Keys werden in einer NoSQL Datenbank abgespeichert.

## Funktionale Anforderungen

Folgende Anforderungen müssen erfüllt werden:
1. Beim Starten der Applikation wird geprüft, ob auf dem Cluster die Datenbank "Softwares" und die Collection "Keys" existieren. Wenn die Datenbank und / oder Collections nicht existiert, wird der User gefragt, ob Datenbank und Collection erstellt werden sollen.
    - Wenn ja: Datenbank und / oder Collections werden erstellt.
    - Wenn nein: Die Applikation wird beendet.

2. In der Collection "Keys" werden Softwares inkl. derer Lizenzkeys gespeichert:
    - Name der Software
    - Hersteller
    - Array von Keys

3. Nach dem Starten werden alle enthaltenen Softwares mit einer Laufnummer angezeigt.

4. Mit "i" (insert) kann eine neue Software erfasst werden.
    - Name der Software und der Hersteller werden eingegeben.
    - Nach der Eingabe wird zum Punkt 3 zurückgekehrt.

5. Mit "k" (key) können die Keys der Software angezeigt werden.
    - Die Laufnummer der Software wird eingegeben.
    - Die Keys werden angezeigt.
    - Mit Enter wird zum Punkt 3 zurückgekehrt.

6. Mit "ik" (insert key) kann einer Software ein neuer Key hinterlegt werden.
    - Die Laufnummer der Software wird eingegeben.
    - Ein Key kann eingegeben werden.
    - Nach der Eingabe wird zum Punkt 3 zurückgekehrt.

7. Mit "q" (quit) kann die Software beendet werden.


## Anforderungen an Architektur

Zusätzlich sind folgende Vorgaben bezüglich des Programmierstils verlangt:
1. Interaktionen mit der Datenbank (Queries, Insert, usw.) sind in einer separaten Klasse programmiert.

2. Der Connection-String wird von der Umgebungsvariable  CS_MONGODB bezogen.
