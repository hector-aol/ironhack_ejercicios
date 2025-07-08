-- Seleccionar la base de datos
USE lab_mysql;

-- Eliminar tablas existentes (opcional, solo para desarrollo)
DROP TABLE IF EXISTS facturas;
DROP TABLE IF EXISTS coches;
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS vendedores;

-- Crear tabla de coches
CREATE TABLE coches (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vin VARCHAR(17) UNIQUE NOT NULL,
    fabricante VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    año SMALLINT NOT NULL,
    color VARCHAR(20)
);

-- Crear tabla de clientes
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id VARCHAR(20) UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    direccion VARCHAR(100) NOT NULL,
    ciudad VARCHAR(50) NOT NULL,
    estado VARCHAR(50) NOT NULL,
    pais VARCHAR(50) NOT NULL,
    codigo_postal VARCHAR(10) NOT NULL
);

-- Crear tabla de vendedores
CREATE TABLE vendedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vendedor_id VARCHAR(20) UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    tienda VARCHAR(50) NOT NULL
);

-- Crear tabla de facturas con relaciones
CREATE TABLE facturas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    factura_numero VARCHAR(20) UNIQUE NOT NULL,
    fecha DATE NOT NULL,
    coche_id INT NOT NULL,
    cliente_id INT NOT NULL,
    vendedor_id INT NOT NULL,
    FOREIGN KEY (coche_id) REFERENCES coches(id),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (vendedor_id) REFERENCES vendedores(id)
);