CREATE DATABASE brawlstars;

USE brawlstars;

CREATE TABLE jugadores (
 	#id INT UNSIGNED NOT NULL AUTO_INCREMENT,
 	fecha DATE NOT NULL,
 	hora TIME NOT NULL,
	tag VARCHAR(15) NOT NULL,
	copas INT,
 
 	CONSTRAINT pk_jugadores
 	PRIMARY KEY (fecha,hora,tag)

) ENGINE=InnoDB;



CREATE USER 'brawl-client'@'%' IDENTIFIED BY 'db-chewer-bs';
GRANT SELECT ON brawlstars.jugadores TO 'brawl-client'@'%';

