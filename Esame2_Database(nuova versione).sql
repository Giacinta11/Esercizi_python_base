-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versione server:              10.4.32-MariaDB - mariadb.org binary distribution
-- S.O. server:                  Win64
-- HeidiSQL Versione:            12.11.0.7065
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dump della struttura del database libreria
DROP DATABASE IF EXISTS `libreria`;
CREATE DATABASE IF NOT EXISTS `libreria` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `libreria`;

-- Dump della struttura di tabella libreria.addresses
DROP TABLE IF EXISTS `addresses`;
CREATE TABLE IF NOT EXISTS `addresses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) NOT NULL,
  `street` varchar(255) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `postal_code` varchar(20) DEFAULT NULL,
  `country` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `addresses_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dump dei dati della tabella libreria.addresses: ~10 rows (circa)
INSERT INTO `addresses` (`id`, `customer_id`, `street`, `city`, `postal_code`, `country`) VALUES
	(1, 1, 'Via Roma 12', 'Milano', '20100', 'Italia'),
	(2, 2, 'Corso Italia 45', 'Torino', '10100', 'Italia'),
	(3, 3, 'Via Garibaldi 8', 'Bologna', '40100', 'Italia'),
	(4, 4, 'Piazza Duomo 3', 'Firenze', '50100', 'Italia'),
	(5, 5, 'Via Napoli 22', 'Roma', '00100', 'Italia'),
	(6, 6, 'Via Verdi 5', 'Genova', '16100', 'Italia'),
	(7, 7, 'Via Mazzini 18', 'Verona', '37100', 'Italia'),
	(8, 8, 'Viale Venezia 9', 'Padova', '35100', 'Italia'),
	(9, 9, 'Via Po 11', 'Torino', '10100', 'Italia'),
	(10, 10, 'Via Dante 25', 'Bari', '70100', 'Italia'),
	(11, 11, 'via di qua', 'Roma', '00123', 'Italia'),
	(12, 12, 'Via Della Pace', 'Firenze', '00789', 'Italia');

-- Dump della struttura di tabella libreria.authors
DROP TABLE IF EXISTS `authors`;
CREATE TABLE IF NOT EXISTS `authors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dump dei dati della tabella libreria.authors: ~10 rows (circa)
INSERT INTO `authors` (`id`, `nome`) VALUES
	(1, 'Italo Calvino'),
	(2, 'Elena Ferrante'),
	(3, 'Umberto Eco'),
	(4, 'J.K. Rowling'),
	(5, 'Stephen King'),
	(6, 'Isabel Allende'),
	(7, 'George Orwell'),
	(8, 'Jane Austen'),
	(9, 'Haruki Murakami'),
	(10, 'Margaret Atwood');

-- Dump della struttura di tabella libreria.books
DROP TABLE IF EXISTS `books`;
CREATE TABLE IF NOT EXISTS `books` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `isbn` varchar(20) DEFAULT NULL,
  `author_id` int(11) DEFAULT NULL,
  `publisher` varchar(200) DEFAULT NULL,
  `price` decimal(8,2) NOT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `author_id` (`author_id`),
  KEY `idx_books_isbn` (`isbn`),
  CONSTRAINT `books_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `authors` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dump dei dati della tabella libreria.books: ~11 rows (circa)
INSERT INTO `books` (`id`, `title`, `isbn`, `author_id`, `publisher`, `price`, `created_at`) VALUES
	(1, 'Le città invisibili', '9788804498657', 1, 'Mondadori', 12.90, '2025-10-28 15:41:56'),
	(2, 'L\'amica geniale', '9788807881586', 2, 'E/O', 14.50, '2025-10-28 15:41:56'),
	(3, 'Il nome della rosa', '9788845259381', 3, 'Bompiani', 18.00, '2025-10-28 15:41:56'),
	(4, 'Harry Potter e la pietra filosofale', '9780747532699', 4, 'Bloomsbury', 9.99, '2025-10-28 15:41:56'),
	(5, 'Harry Potter e la camera dei segreti', '9780747538493', 4, 'Bloomsbury', 11.50, '2025-10-28 15:41:56'),
	(6, 'Shining', '9780450040184', 5, 'Anchor', 13.40, '2025-10-28 15:41:56'),
	(7, 'La casa degli spiriti', '9788807900430', 6, 'Feltrinelli', 15.00, '2025-10-28 15:41:56'),
	(8, '1984', '9780451524935', 7, 'Penguin', 10.99, '2025-10-28 15:41:56'),
	(9, 'Orgoglio e pregiudizio', '9780141439518', 8, 'Penguin', 8.50, '2025-10-28 15:41:56'),
	(10, 'Norwegian Wood', '9780099448822', 9, 'Vintage', 12.00, '2025-10-28 15:41:56'),
	(11, 'Il racconto dell\'ancella', '9788806220898', 10, 'Ponte alle Grazie', 13.00, '2025-10-28 15:41:56');

-- Dump della struttura di tabella libreria.customers
DROP TABLE IF EXISTS `customers`;
CREATE TABLE IF NOT EXISTS `customers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(250) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `idx_customers_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dump dei dati della tabella libreria.customers: ~12 rows (circa)
INSERT INTO `customers` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`) VALUES
	(1, 'Marco', 'Rossi', 'marco.rossi@email.com', '3204567890', '2025-10-28 15:42:54'),
	(2, 'Giulia', 'Bianchi', 'giulia.bianchi@email.com', '3335678901', '2025-10-28 15:42:54'),
	(3, 'Luca', 'Verdi', 'luca.verdi@email.com', '3401234567', '2025-10-28 15:42:54'),
	(4, 'Francesca', 'Neri', 'francesca.neri@email.com', '3312223344', '2025-10-28 15:42:54'),
	(5, 'Paolo', 'Conti', 'paolo.conti@email.com', '3299988776', '2025-10-28 15:42:54'),
	(6, 'Sara', 'Galli', 'sara.galli@email.com', '3205566778', '2025-10-28 15:42:54'),
	(7, 'Antonio', 'Russo', 'antonio.russo@email.com', '3471122334', '2025-10-28 15:42:54'),
	(8, 'Chiara', 'Ferrari', 'chiara.ferrari@email.com', '3393344556', '2025-10-28 15:42:54'),
	(9, 'Davide', 'Marini', 'davide.marini@email.com', '3456677889', '2025-10-28 15:42:54'),
	(10, 'Laura', 'Ricci', 'laura.ricci@email.com', '3334455667', '2025-10-28 15:42:54'),
	(11, 'Giacinta', 'Bernardi', 'giacintabernardi@gmail.com', '333 567894', '2025-10-28 16:17:57'),
	(12, 'Luigi', 'Olmati', 'luigiolmati.92@gmail.com', '334 4467890', '2025-10-28 18:11:23');

-- Dump della struttura di tabella libreria.sales
DROP TABLE IF EXISTS `sales`;
CREATE TABLE IF NOT EXISTS `sales` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) NOT NULL,
  `sale_date` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `customer_id` (`customer_id`),
  KEY `idx_sales_date` (`sale_date`),
  CONSTRAINT `sales_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dump dei dati della tabella libreria.sales: ~8 rows (circa)
INSERT INTO `sales` (`id`, `customer_id`, `sale_date`) VALUES
	(1, 1, '2025-10-23 15:44:56'),
	(2, 2, '2025-10-25 15:44:56'),
	(3, 3, '2025-10-26 15:44:56'),
	(4, 4, '2025-10-27 15:44:56'),
	(5, 5, '2025-10-27 15:44:56'),
	(6, 6, '2025-10-28 15:44:56'),
	(8, 3, '2025-10-28 16:55:57'),
	(9, 12, '2025-10-28 18:11:33');

-- Dump della struttura di tabella libreria.sale_items
DROP TABLE IF EXISTS `sale_items`;
CREATE TABLE IF NOT EXISTS `sale_items` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sales_id` int(11) NOT NULL,
  `book_id` int(11) DEFAULT NULL,
  `qty` int(11) NOT NULL,
  `price` decimal(8,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sales_id` (`sales_id`),
  KEY `book_id` (`book_id`),
  CONSTRAINT `sale_items_ibfk_1` FOREIGN KEY (`sales_id`) REFERENCES `sales` (`id`) ON DELETE CASCADE,
  CONSTRAINT `sale_items_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dump dei dati della tabella libreria.sale_items: ~9 rows (circa)
INSERT INTO `sale_items` (`id`, `sales_id`, `book_id`, `qty`, `price`) VALUES
	(1, 1, 1, 1, 12.90),
	(2, 1, 3, 1, 18.00),
	(3, 2, 4, 2, 9.99),
	(4, 3, 7, 1, 15.00),
	(5, 4, 8, 3, 10.99),
	(6, 4, 9, 1, 8.50),
	(7, 5, 6, 1, 13.40),
	(8, 6, 10, 2, 12.00),
	(9, 6, 11, 1, 13.00),
	(10, 8, 7, 4, 15.00),
	(11, 9, 11, 1, 13.00);

-- Dump della struttura di tabella libreria.stock
DROP TABLE IF EXISTS `stock`;
CREATE TABLE IF NOT EXISTS `stock` (
  `book_id` int(11) NOT NULL,
  `copies` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`book_id`),
  CONSTRAINT `stock_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Dump dei dati della tabella libreria.stock: ~11 rows (circa)
INSERT INTO `stock` (`book_id`, `copies`) VALUES
	(1, 12),
	(2, 8),
	(3, 5),
	(4, 15),
	(5, 10),
	(6, 7),
	(7, 5),
	(8, 20),
	(9, 14),
	(10, 6),
	(11, 10);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
