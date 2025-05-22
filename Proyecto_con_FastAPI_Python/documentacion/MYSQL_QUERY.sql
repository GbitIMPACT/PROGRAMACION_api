CREATE DATABASE dulceria_candice
USE dulceria_candice
SELECT * FROM trabajadores

ALTER TABLE productos ADD COLUMN unidad_medida VARCHAR(50);

ALTER TABLE productos ADD COLUMN trabajador_id INTEGER, ADD CONSTRAINT fk_trabajador FOREIGN KEY (trabajador_id) REFERENCES trabajadores(id);ALTER TABLE productos ADD COLUMN trabajador_id INTEGER, ADD CONSTRAINT fk_trabajador FOREIGN KEY (trabajador_id) REFERENCES trabajadores(id);
CREATE TABLE trabajadores (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) UNIQUE
);