# Python Abfragescript zum lernen

### Fragen selber hinzufügen
Fragen können als liste wie folgt angelegt werden: <br>
```
name_der_kategorie = [
    ("warum ist die Banane krumm", "darum"),
]
```
Fragen können der "List of questions wie folgt" hinzugefügt werden:
```
l_o_q.append(name_der_kategorie)
```
Kategorien werden der "List of Categories" in derselben Reihenfolge
wie zur l_o_q hinzugefügt:
```
l_o_cat.append("name der Kategorie")
```

### Abfrage starten
Nach dem Starten des Programms mit:
```
python3 abfrage.py
```
wird man gefragt wie viele Fragen men gestellt bekommen will und dann gehts los.
```
-------------------------
11)
Question from the high performance computing category.
Latenz in HPC Zeiteinheit
nanosekunden

-------------------------
```
dam die Antwort natürlich richtig sein kann ohne das sie eins zu eins übereinstimmt, 
gibt es die Möglichkeit mit 1, y, oder yes zu bestätigen das man recht hatte.
```
The answer was:  nano Sekunden
Was the your answer actually correct? Then type 1, y or yes.
y
```
