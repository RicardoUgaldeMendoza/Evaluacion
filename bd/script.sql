CREATE DATABASE IF NOT EXISTS paquexpress_db;
USE paquexpress_db;

CREATE TABLE Agentes (
    id_agente INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50) UNIQUE NOT NULL,
    hash_contrasena VARCHAR(255) NOT NULL,
    nombre_completo VARCHAR(100),
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Paquetes (
    id_paquete INT AUTO_INCREMENT PRIMARY KEY,
    id_unico_rastreo VARCHAR(50) UNIQUE NOT NULL,
    direccion_destino VARCHAR(255) NOT NULL,
    id_agente_asignado INT,
    estado ENUM('ASIGNADO', 'EN_RUTA', 'ENTREGADO') DEFAULT 'ASIGNADO',
    FOREIGN KEY (id_agente_asignado) REFERENCES Agentes(id_agente)
);

CREATE TABLE Entregas (
    id_entrega INT AUTO_INCREMENT PRIMARY KEY,
    id_paquete INT UNIQUE NOT NULL,
    id_agente INT,
    latitud DECIMAL(10, 8) NOT NULL,
    longitud DECIMAL(11, 8) NOT NULL,
    ruta_foto_evidencia VARCHAR(255) NOT NULL,
    fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_paquete) REFERENCES Paquetes(id_paquete),
    FOREIGN KEY (id_agente) REFERENCES Agentes(id_agente)
);

INSERT INTO Agentes (nombre_usuario, hash_contrasena, nombre_completo) VALUES 
('agente01', MD5('password123'), 'Juan Pérez'),
('agente02', MD5('contrasena456'), 'María López');

INSERT INTO Paquetes (id_unico_rastreo, direccion_destino, id_agente_asignado) VALUES 
('PX1001', 'Calle Falsa 123, Ciudad de México', 1),
('PX1002', 'Avenida Siempre Viva 742, CDMX', 1),
('PX1003', 'Blvd. de los Sueños 500, Puebla', 2);
