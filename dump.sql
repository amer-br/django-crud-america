-- =======================================
-- Deshabilitar temporalmente las claves foráneas
-- =======================================
SET FOREIGN_KEY_CHECKS = 0;

-- =======================================
-- Tabla: Autor
-- =======================================
DROP TABLE IF EXISTS Autor;
CREATE TABLE Autor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE,
    nacionalidad VARCHAR(50)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Datos de ejemplo para Autores
INSERT INTO Autor (nombre, apellido, fecha_nacimiento, nacionalidad) VALUES
('Gabriel', 'García Márquez', '1927-03-06', 'Colombiano'),
('Isabel', 'Allende', '1942-08-02', 'Chilena'),
('J.K.', 'Rowling', '1965-07-31', 'Británica'),
('Mario', 'Vargas Llosa', '1936-03-28', 'Peruano'),
('Ernest', 'Hemingway', '1899-07-21', 'Estadounidense'),
('F. Scott', 'Fitzgerald', '1896-09-24', 'Estadounidense'),
('Leo', 'Tolstoy', '1828-09-09', 'Ruso'),
('Harper', 'Lee', '1926-04-28', 'Estadounidense'),
('Jane', 'Austen', '1775-12-16', 'Británica'),
('Mark', 'Twain', '1835-11-30', 'Estadounidense');

-- =======================================
-- Tabla: Libro
-- =======================================
DROP TABLE IF EXISTS Libro;
CREATE TABLE Libro (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    fechapublicacion DATE,
    precio DECIMAL(8,2),
    autor_id INT NOT NULL,
    FOREIGN KEY (autor_id) REFERENCES Autor(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Datos de ejemplo para Libros
INSERT INTO Libro (titulo, fechapublicacion, precio, autor_id) VALUES
('Cien años de soledad', '1967-05-30', 25.50, 1),
('El amor en los tiempos del cólera', '1985-09-15', 22.00, 1),
('La casa de los espíritus', '1982-01-01', 20.00, 2),
('Harry Potter y la piedra filosofal', '1997-06-26', 18.50, 3),
('La ciudad y los perros', '1963-01-01', 19.00, 4),
('El viejo y el mar', '1952-09-01', 15.50, 5),
('Adiós a las armas', '1929-01-01', 16.00, 5),
('El gran Gatsby', '1925-04-10', 18.00, 6),
('Anna Karenina', '1877-01-01', 22.50, 7),
('Guerra y paz', '1869-01-01', 24.00, 7),
('Matar a un ruiseñor', '1960-07-11', 17.50, 8),
('Orgullo y prejuicio', '1813-01-28', 19.00, 9),
('Emma', '1815-12-23', 18.50, 9),
('Sentido y sensibilidad', '1811-10-30', 18.00, 9),
('Las aventuras de Tom Sawyer', '1876-06-01', 16.50, 10),
('Las aventuras de Huckleberry Finn', '1884-12-10', 17.00, 10),
('El coronel no tiene quien le escriba', '1961-01-01', 20.00, 4),
('Paula', '1994-01-01', 19.50, 2),
('Harry Potter y la cámara secreta', '1998-07-02', 18.50, 3),
('Harry Potter y el prisionero de Azkaban', '1999-07-08', 18.50, 3),
('El amor en los tiempos modernos', '2020-01-01', 21.00, 1),
('Fiesta', '1926-01-01', 17.00, 6),
('El idiota', '1869-01-01', 22.00, 7),
('Homenaje a Cataluña', '1938-01-01', 16.50, 5),
('Cuentos completos', '1900-01-01', 18.00, 5),
('La tregua', '1960-01-01', 19.00, 4),
('Retrato de una dama', '1881-01-01', 20.50, 9),
('Harry Potter y el cáliz de fuego', '2000-07-08', 19.00, 3),
('Harry Potter y la orden del Fénix', '2003-06-21', 19.50, 3),
('Crónica de una muerte anunciada', '1981-01-01', 21.00, 1);

-- =======================================
-- Volver a habilitar las claves foráneas
-- =======================================
SET FOREIGN_KEY_CHECKS = 1;
