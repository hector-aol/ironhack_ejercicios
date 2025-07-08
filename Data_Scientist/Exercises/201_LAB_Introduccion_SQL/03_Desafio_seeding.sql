USE lab_mysql;

-- Insertar datos en la tabla 'coches'
-- Nota: Corregido el VIN duplicado (último registro)
INSERT INTO coches (vin, fabricante, modelo, año, color) VALUES
('3K096I98581DHSNUP', 'Volkswagen', 'Tiguan', 2019, 'Azul'),
('ZM8G7BEUQZ97IH46V', 'Peugeot', 'Rifter', 2019, 'Rojo'),
('RKXVNNIHLVVZOUB4M', 'Ford', 'Fusion', 2018, 'Blanco'),
('HKNDGS7CU31E9Z7JW', 'Toyota', 'RAV4', 2018, 'Plata'),
('DAM41UDN3CHU2WVF6', 'Volvo', 'V60', 2019, 'Gris'),
('TMBBA41UDN3CHU2WX', 'Volvo', 'V60 Cross Country', 2019, 'Gris'); -- VIN corregido

-- Insertar datos en la tabla 'clientes'
-- Nota: Email como NULL en lugar de '-'
INSERT INTO clientes (cliente_id, nombre, telefono, email, direccion, ciudad, estado, pais, codigo_postal) VALUES
('10001', 'Pablo Picasso', '+34 636 17 63 82', NULL, 'Paseo de la Chopera, 14', 'Madrid', 'Madrid', 'España', '28045'),
('20001', 'Abraham Lincoln', '+1 305 907 7086', NULL, '120 SW 8th St', 'Miami', 'Florida', 'Estados Unidos', '33130'),
('30001', 'Napoléon Bonaparte', '+33 1 79 75 40 00', NULL, '40 Rue du Colisée', 'París', 'Île-de-France', 'Francia', '75008');

-- Insertar datos en la tabla 'vendedores'
-- Nota: Corregido "Mimia" -> "Miami"
INSERT INTO vendedores (vendedor_id, nombre, tienda) VALUES
('00001', 'Petey Cruiser', 'Madrid'),
('00002', 'Anna Sthesia', 'Barcelona'),
('00003', 'Paul Molive', 'Berlín'),
('00004', 'Gail Forcewind', 'París'),
('00005', 'Paige Turner', 'Miami'), -- Corregido Mimia->Miami
('00006', 'Bob Frapples', 'Ciudad de México'),
('00007', 'Walter Melon', 'Ámsterdam'),
('00008', 'Shonda Leer', 'São Paulo');

-- Insertar datos en la tabla 'facturas'
-- Nota: 
--  1. Fechas convertidas a formato MySQL (YYYY-MM-DD)
--  2. IDs de referencia basados en el orden de inserción:
--      Coches: VW Tiguan=1, Peugeot=2, Ford=3, Toyota=4, Volvo V60=5, Volvo Cross=6
--      Clientes: Picasso=1, Lincoln=2, Napoleon=3
--      Vendedores: Petey=1, Anna=2, Paul=3, Gail=4, Paige=5, Bob=6, Walter=7, Shonda=8
INSERT INTO facturas (factura_numero, fecha, coche_id, cliente_id, vendedor_id) VALUES
('852399038', '2018-08-22', 1, 2, 4),  -- Coche: VW Tiguan, Cliente: Lincoln, Vendedor: Gail
('731166526', '2018-12-31', 4, 1, 6),  -- Coche: Toyota, Cliente: Picasso, Vendedor: Bob
('271135104', '2019-01-22', 3, 3, 8);  -- Coche: Ford, Cliente: Napoleon, Vendedor: Shonda