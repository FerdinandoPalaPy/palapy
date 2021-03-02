import json
libreria={
    "Libro 1":'{"Titolo":"Il mondo nuovo – Ritorno al mondo nuovo","Autore":"Aldous Huxley","Genere":"Fantascienza, Narrativa distopica"}',
    "Libro 2":'{"Titolo":"10 piccoli indiani","Autore":"Agatha Christie","Genere":"Romanzo"}',
    "Libro 3":'{"Titolo":"1984","Autore":"George Orwell","Genere":"Fantascienza, Fantascienza sociologica, Fantapolitica, Narrativa distopica"}',
    "Libro 4":'{"Titolo":"I Fratelli Karamazov","Autore":"Fëdor Dostoevskij","Genere":"Romanzo"}',
    "Libro 5":'{"Titolo":"Cime tempestose","Autore":"Emily Bronte","Genere":"Romanzo, Fiction gotica, Romanzo rosa, Tragedia"}',
    "Libro 6":'{"Titolo":"Orgoglio e pregiudizio","Autore":"Jane Austen","Genere":"Romanzo rosa, Dramma, Letteratura per giovani adulti, Satira, Romanzo di costume"}',
    "Libro 7":'{"Titolo":"La storia infinita","Autore":"Michael Ende","Genere":"Romanzo, Letteratura per ragazzi, Narrativa fantasy, Fantasy epico"}',
    "Libro 8":'{"Titolo":"Il giovane Holden","Autore":"Salinger","Genere":"Romanzo"}',
    "Libro 9":'{"Titolo":"Il processo","Autore":"Kafka","Genere":"Romanzo, Narrativa filosofica, Narrativa distopica"}',
    "Libro 10":'{"Titolo":"Psycho","Autore":"Robert Bloch","Genere":"Romanzo, Horror fiction, Thriller, Suspense, Giallo"}'
    }

y=json.dumps(libreria)
print(y)
