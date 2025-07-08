UPDATE vendedores
SET tienda = 'Miami'  -- Corrige el error tipográfico
WHERE nombre = 'Paige Turner';  -- Identifica al vendedor específico

-- Actualiza cada cliente usando su nombre como identificador
UPDATE clientes SET email = 'ppicasso@gmail.com' WHERE nombre = 'Pablo Picasso';
UPDATE clientes SET email = 'lincoln@us.gov' WHERE nombre = 'Abraham Lincoln';
UPDATE clientes SET email = 'hello@napoleon.me' WHERE nombre = 'Napoléon Bonaparte';