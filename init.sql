-- Active: 1701813900343@@127.0.0.1@3306@vnergy
USE `vnergy`;

-- drop tables
DROP TABLE IF EXISTS `plm_stocked`;
DROP TABLE IF EXISTS `plm_warehouses`;
DROP TABLE IF EXISTS `plm_is_composed`;
DROP TABLE IF EXISTS `plm_items`;
DROP TABLE IF EXISTS `plm_orders`;
DROP TABLE IF EXISTS `plm_delivery_options`;
DROP TABLE IF EXISTS `plm_clients`;
DROP TABLE IF EXISTS `plm_credit_cards`;
DROP TABLE IF EXISTS `plm_contact`;
DROP TABLE IF EXISTS `plm_admins`;

-- create tables
CREATE TABLE IF NOT EXISTS `plm_credit_cards` (
    `card` VARCHAR(16) NOT NULL PRIMARY KEY,
    `expiry_date` DATE
);

CREATE TABLE IF NOT EXISTS `plm_clients` (
    `email` VARCHAR(50) NOT NULL PRIMARY KEY,
    `password` VARCHAR(50),
    `first_name` VARCHAR(30),
    `last_name` VARCHAR(30),
    `phone` VARCHAR(10),
    `address` VARCHAR(50),
    `postal_code` VARCHAR(5),
    `card` VARCHAR(16) NOT NULL
);

CREATE TABLE IF NOT EXISTS `plm_delivery_options` (
    `delivery_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `delivery_date` DATE,
    `delivery_address` VARCHAR(50),
    `delivery_postal_code` VARCHAR(5),
    `option` ENUM('Standard','Express')
);

CREATE TABLE IF NOT EXISTS `plm_orders` (
    `order_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `order_date` DATE,
    `total_price` DECIMAL(10,2),
    `status` ENUM('Pending','Confirmed','In transit','Delivered','Cancelled'),
    `email` VARCHAR(50) NOT NULL,
    `card` VARCHAR(16) NOT NULL,
    `delivery_id` INT NOT NULL
);

CREATE TABLE IF NOT EXISTS `plm_items` (
    `item_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(30),
    `price` DECIMAL(5,2)
);

CREATE TABLE IF NOT EXISTS `plm_is_composed` (
    `order_id` INT NOT NULL,
    `item_id` INT NOT NULL,
    `quantity` INT
);

CREATE TABLE IF NOT EXISTS `plm_warehouses` (
    `warehouse_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `address` VARCHAR(50),
    `postal_code` VARCHAR(5),
    `max_capacity` INT
);

CREATE TABLE IF NOT EXISTS `plm_stocked` (
    `item_id` INT NOT NULL,
    `warehouse_id` INT NOT NULL,
    `quantity` INT
);

CREATE TABLE IF NOT EXISTS `plm_contact` (
    `contact_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `email` VARCHAR(50),
    `name` VARCHAR(30),
    `message` VARCHAR(500)
);

CREATE TABLE IF NOT EXISTS `plm_admins` (
    `username` VARCHAR(30) NOT NULL PRIMARY KEY,
    `password` VARCHAR(50),
    `role` ENUM('Admin','Data Analyst', 'Manager', 'Employee')
);

-- add foreign keys
ALTER TABLE `plm_clients` ADD CONSTRAINT `fk_plm_clients_card` FOREIGN KEY (`card`) REFERENCES `plm_credit_cards`(`card`);

ALTER TABLE `plm_orders` ADD CONSTRAINT `fk_plm_orders_email` FOREIGN KEY (`email`) REFERENCES `plm_clients`(`email`);
ALTER TABLE `plm_orders` ADD CONSTRAINT `fk_plm_orders_card` FOREIGN KEY (`card`) REFERENCES `plm_credit_cards`(`card`);
ALTER TABLE `plm_orders` ADD CONSTRAINT `fk_plm_orders_delivery_id` FOREIGN KEY (`delivery_id`) REFERENCES `plm_delivery_options`(`delivery_id`);

ALTER TABLE `plm_is_composed` ADD CONSTRAINT `fk_plm_is_composed_order_id` FOREIGN KEY (`order_id`) REFERENCES `plm_orders`(`order_id`);
ALTER TABLE `plm_is_composed` ADD CONSTRAINT `fk_plm_is_composed_item_id` FOREIGN KEY (`item_id`) REFERENCES `plm_items`(`item_id`);

ALTER TABLE `plm_stocked` ADD CONSTRAINT `fk_plm_stocked_item_id` FOREIGN KEY (`item_id`) REFERENCES `plm_items`(`item_id`);
ALTER TABLE `plm_stocked` ADD CONSTRAINT `fk_plm_stocked_warehouse_id` FOREIGN KEY (`warehouse_id`) REFERENCES `plm_warehouses`(`warehouse_id`);
