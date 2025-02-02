import sqlite3

DB_NAME = "sklep.db"

# Połączenie z bazą
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# 📌 Tworzenie tabel
cursor.executescript("""
CREATE TABLE IF NOT EXISTS Kategoria (
    KAT_id INTEGER PRIMARY KEY,
    KAT_nazwa TEXT
);

CREATE TABLE IF NOT EXISTS Produkt (
    PROD_id INTEGER PRIMARY KEY,
    PROD_Nazwa TEXT,
    PROD_Opis TEXT,
    PROD_Cena FLOAT,
    PROD_StanMagazynowy INTEGER,
    KAT_id INTEGER,
    FOREIGN KEY (KAT_id) REFERENCES Kategoria(KAT_id)
);

CREATE TABLE IF NOT EXISTS Uzytkownik (
    UZ_id INTEGER PRIMARY KEY,
    UZ_imie TEXT,
    UZ_Nazwisko TEXT,
    UZ_Email TEXT,
    UZ_Haslo TEXT,
    UZ_DataRejestracji DATETIME
);
""")

# 📌 Dodanie przykładowych danych
cursor.executescript("""
INSERT INTO Kategoria (KAT_nazwa) VALUES ('Elektronika'), ('Odzież');

INSERT INTO Produkt (PROD_Nazwa, PROD_Opis, PROD_Cena, PROD_StanMagazynowy, KAT_id)
VALUES 
    ('Laptop Lenovo', 'Laptop z ekranem 15"', 3500, 10, 1),
    ('Smartfon Samsung', 'Telefon z Androidem', 2500, 20, 1),
    ('Koszulka Nike', 'Koszulka sportowa', 100, 50, 2);

INSERT INTO Uzytkownik (UZ_imie, UZ_Nazwisko, UZ_Email, UZ_Haslo, UZ_DataRejestracji)
VALUES 
    ('Jan', 'Kowalski', 'jan@wp.pl', 'haslo123', datetime('now')),
    ('Anna', 'Nowak', 'anna@o2.pl', 'pass456', datetime('now'));
""")

conn.commit()
conn.close()
print("✅ Baza danych została utworzona i uzupełniona!")