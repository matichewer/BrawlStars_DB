# fecha mas reciente
SELECT MAX(fecha) AS fecha_mas_reciente
FROM jugadores;


# Elimina todas las filas cuya hora no es a las 00hs
DELETE FROM jugadores
WHERE HOUR(hora) NOT IN (00);


# Tabla con ultimo registro
SELECT *
FROM jugadores
WHERE fecha = (	SELECT MAX(fecha)
				FROM jugadores)
ORDER BY copas DESC;


# Tabla con registro de hace 7 dias
SELECT *
FROM jugadores
WHERE fecha = (SELECT DATE(NOW()) - INTERVAL 7 DAY)
ORDER BY copas DESC;




# diff de copas - FALTA TERMINAR
SELECT j_7dias.fecha, j_actual.tag, (j_actual.copas - j_7dias.copas) AS copas
FROM jugadores AS j_7dias, jugadores AS j_actual;
WHERE