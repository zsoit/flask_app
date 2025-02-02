CREATE TABLE Kategoria (
    KAT_id INTEGER PRIMARY KEY,
    KAT_nazwa FLOAT
);

CREATE TABLE Produkt (
    PROD_id INTEGER PRIMARY KEY,
    PROD_Nazwa TEXT,
    PROD_Opis TEXT,
    PROD_Cena FLOAT,
    PROD_StanMagazynowy INTEGER,
    KAT_id INTEGER,
    SZ_id INTEGER,
    FOREIGN KEY (KAT_id) REFERENCES Kategoria(KAT_id)
);

CREATE TABLE Koszyk (
    KOS_id INTEGER PRIMARY KEY,
    UZ_id INTEGER,
    PROD_id INTEGER,
    KOS_Ilosc INTEGER,
    FOREIGN KEY (UZ_id) REFERENCES Uzytkownik(UZ_id),
    FOREIGN KEY (PROD_id) REFERENCES Produkt(PROD_id)
);

CREATE TABLE Uzytkownik (
    UZ_id INTEGER PRIMARY KEY,
    UZ_imie TEXT,
    UZ_Nazwisko TEXT,
    UZ_Email TEXT,
    UZ_Haslo TEXT,
    UZ_DataRejestracji DATETIME
);

CREATE TABLE Status (
    Status_id INTEGER PRIMARY KEY,
    data text
);

CREATE TABLE Zamowienie (
    ZAM_id INTEGER PRIMARY KEY,
    ZAM_Data DATETIME,
    Status_id INTEGER,
    UZ_id INTEGER,
    PL_id INTEGER,
    SZ_id INTEGER,
    FOREIGN KEY (Status_id) REFERENCES Status(Status_id),
    FOREIGN KEY (UZ_id) REFERENCES Uzytkownik(UZ_id),
    FOREIGN KEY (PL_id) REFERENCES Platnosc(PL_id)
);

CREATE TABLE SzczegolyZamowienia (
    SZ_id INTEGER PRIMARY KEY,
    ZAM_id INTEGER,
    PROD_id INTEGER,
    SZ_Ilosc INTEGER,
    SZ_CenaJednostkowa FLOAT,
    FOREIGN KEY (ZAM_id) REFERENCES Zamowienie(ZAM_id),
    FOREIGN KEY (PROD_id) REFERENCES Produkt(PROD_id)
);

CREATE TABLE Platnosc (
    PL_id INTEGER PRIMARY KEY,
    PL_Typ TEXT,
    PL_Status TEXT,
    PL_Data DATETIME
);
