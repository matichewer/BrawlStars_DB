# fecha mas reciente
SELECT 
	MAX(fecha) AS fecha_mas_reciente
FROM 
	jugadores;


# ultima vez que se registró al club
SELECT
	fecha AS fecha_mas_reciente,
	hora AS hora_mas_reciente, 
	tag, 
	copas 
FROM 
	jugadores
WHERE
	fecha = (	SELECT MAX(fecha)
				FROM jugadores
			)
ORDER BY
	copas 
DESC;
