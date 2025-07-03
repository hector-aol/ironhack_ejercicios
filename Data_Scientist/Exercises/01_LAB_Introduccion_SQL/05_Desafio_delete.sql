-- Primero elimina facturas asociadas al coche ID #4
DELETE FROM facturas WHERE coche_id = 4;

-- Luego elimina el coche duplicado
DELETE FROM coches WHERE id = 4;