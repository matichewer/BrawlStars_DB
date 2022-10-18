CREATE DATABASE brawlstars;

USE brawlstars;

CREATE TABLE jugadores (
 	#id INT UNSIGNED NOT NULL AUTO_INCREMENT,
 	fecha DATE NOT NULL,
 	hora TIME NOT NULL,
	tag VARCHAR(15) NOT NULL,
	copas INT UNSIGNED,
 
 	CONSTRAINT pk_jugadores
 	PRIMARY KEY (fecha,hora,tag)

) ENGINE=InnoDB;

