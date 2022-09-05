# Wool Data Fetcher
Dies ist ein Projekt, das Beweisen soll, dass ich genau der richtige für MARKT-PILOT bin 😌😌😌😌 
Hier wurde Python 3.8.10 benutzt, für das Web-Scraping das Modul [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/). 
Im `notebooks` Ordner könnt ihr ausserdem nachgucken, wie mein Gedankengang so aussah :3

Verbrauchte Zeit: 2 Stunden 4 Minuten (inkl. Wartezeit des Scrapings)

## Modifizierte Beschreibung
Nachdem die Idee zu mir kam das ganze hier zu erstellen, bin ich schlafen gegangen. 
Am nächsten Morgen habe ich bemerkt, dass die Idee mit der begrenzten Artikelanzahl sehr doof ist! 
Ich liebe meine Oma über alles und will, dass sie möglichst viel spart! 
Deshalb beschloss ich anstatt von fünf Artikeln alle Artikeln durchzuscrapen, die es im Sortiment gibt! 🤩🤩🤩🤩
Da meine Oma eh nicht weiß, was ein Computer ist, und ich immer noch in der Prüfungsphase bin,
habe ich beschlossen die Daten einfach in einem .csv-File abzuspeichern und keinen UI zu benutzen. 
Die Datenbank finde ich auch überflüssig, so oft wird meine Oma keine Wolle kaufen wollen. 

## Vielleicht das nächste Mal?
Hier Paar Sachen, die ich machen würde, wenn ich keine Prüfung in paar Tagen hätte:
* [TQDM](https://github.com/tqdm/tqdm) benutzen, damit der User des Tools besser weiß, wie es mit dem Progress aussieht
* Tests für alle Methoden schreiben 🥲
* Den Teil mit dem Fetchen der Daten für jeden Artikel parallel laufen lassen
* die Möglichkeit implementieren Daten nach deren Eigenschaften zu sortieren (Verfügbarkeit, Preis, ...) 
* In der Methode `WoolDataFetcher.get_article_data()` doch `try: ... except: ...` nutzen, ist ja eher pythonic
* mehr git!
* Docstrings, aber nicht unbedingt hier, weil die Funktionen/Methoden sehr simpel sind
* Einige GitHub Actions wären auch nicht schlecht

## Feedback
Die coolste Software-Challenge, die ich bisher hatte! Fand die Idee mit der kleinen Story sehr cool. 
Würde mich auch für Feedback und auf die nächste Runde freuen :)