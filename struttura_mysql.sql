BEGIN;
--
-- Create model Canzone
--
CREATE TABLE "tributo_canzone" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "titolo" varchar(200) NOT NULL, "anno_uscita" integer NOT NULL, "testo" text NULL);
--
-- Create model Concerto
--
CREATE TABLE "tributo_concerto" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "luogo" varchar(200) NOT NULL, "citta" varchar(100) NOT NULL, "data" varchar(100) NOT NULL);
COMMIT;
