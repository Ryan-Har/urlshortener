# urlshortener
url shortener in flask

requirements.txt include the python software requirements.

Database connection needed, I have created a database called urlshortener with the following table.
CREATE TABLE `urlshortener`.`urls` (
  `ID` VARCHAR(6) NOT NULL,
  `url` VARCHAR(100) NOT NULL,
  `created` DATETIME NOT NULL,
  PRIMARY KEY (`ID`));


