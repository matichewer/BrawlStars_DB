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


# diff de copas
SELECT
	j_actual.tag,
	j_7dias.fecha AS fecha_vieja,
	j_7dias.copas AS copas_viejas,
	j_actual.fecha AS fecha_actual,
	j_actual.copas AS copas_actuales,
	j_actual.copas - j_7dias.copas AS copas_diff

FROM (	SELECT *
		FROM jugadores
		WHERE fecha = (SELECT DATE(NOW()) - INTERVAL 7 DAY)) AS j_7dias 
JOIN (	SELECT *
		FROM jugadores
		WHERE fecha = (SELECT MAX(fecha) FROM jugadores)) AS j_actual
ON j_7dias.tag=j_actual.tag
ORDER BY copas_diff DESC;


# cant de horarios por dia
SELECT fecha, COUNT(hora) as cant
FROM (SELECT distinct fecha,hora FROM jugadores) AS tabla 
GROUP BY fecha;
