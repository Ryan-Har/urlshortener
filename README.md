# urlshortener
url shortener in flask

requirements.txt include the software requirements.
Database connection needed

CREATE TABLE `urlshortener`.`urls` (
  `ID` VARCHAR(6) NOT NULL,
  `url` VARCHAR(100) NOT NULL,
  `created` DATETIME NOT NULL,
  PRIMARY KEY (`ID`));


