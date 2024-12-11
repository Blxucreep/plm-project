USE `vnergy`;

INSERT INTO `plm_credit_cards` (`card`, `expiry_date`) VALUES 
('1234567891234567', '2025-12-31');

INSERT INTO `plm_clients` (`email`, `password`, `first_name`, `last_name`, `phone`, `address`, `postal_code`, `card`) VALUES
('john.doe@email.com', 'motdepasse1', 'John', 'Doe', '1234567890', '123 Rue des Fleurs', '75001', '1234567891234567'),
('jane.smith@email.com', 'motdepasse2', 'Jane', 'Smith', '9876543210', '456 Avenue des Étoiles', '75002', '1234567891234567'),
('alice.johnson@email.com', 'motdepasse3', 'Alice', 'Johnson', '5556667777', '789 Boulevard du Soleil', '75003', '1234567891234567'),
('bob.williams@email.com', 'motdepasse4', 'Bob', 'Williams', '3332221111', '1010 Rue de la Lune', '75004', '1234567891234567'),
('emma.martin@email.com', 'motdepasse5', 'Emma', 'Martin', '9998887777', '2020 Avenue des Nuages', '75005', '1234567891234567'),
('charlie.brown@email.com', 'motdepasse6', 'Charlie', 'Brown', '1110009999', '303 Rue des Montagnes', '75006', '1234567891234567'),
('olivia.white@email.com', 'motdepasse7', 'Olivia', 'White', '7776665555', '404 Avenue des Rivières', '75007', '1234567891234567'),
('michael.davis@email.com', 'motdepasse8', 'Michael', 'Davis', '4443332222', '505 Boulevard des Forêts', '75008', '1234567891234567'),
('sophia.thomas@email.com', 'motdepasse9', 'Sophia', 'Thomas', '2221110000', '606 Rue des Champs', '75009', '1234567891234567'),
('liam.jackson@email.com', 'motdepasse10', 'Liam', 'Jackson', '8887776666', '707 Avenue des Plaines', '75010', '1234567891234567');

INSERT INTO `plm_delivery_options` (`delivery_id`, `delivery_date`, `delivery_address`, `delivery_postal_code`, `option`) VALUES 
(1, '2021-01-03', '123 Rue des Fleurs', '75001', 'Express'),
(2, '2023-01-05', '2020 Avenue des Nuages', '75005', 'Standard'),
(3, '2022-04-30', '303 Rue des Montagnes', '75006', 'Standard'),
(4, '2022-10-17', '606 Rue des Champs', '75009', 'Standard'),
(5, '2021-12-26', '707 Avenue des Plaines', '75010', 'Standard');

INSERT INTO `plm_orders` (`order_id`, `order_date`, `total_price`, `status`, `email`, `card`, `delivery_id`) VALUES 
(1, '2021-01-01', 15.70, 'Delivered', 'john.doe@email.com', '1234567891234567', 1),
(2, '2023-01-01', 14.32, 'Delivered', 'emma.martin@email.com', '1234567891234567', 2),
(3, '2022-04-28', 12.50, 'Delivered', 'charlie.brown@email.com', '1234567891234567', 3),
(4, '2022-10-13', 34.12, 'Delivered', 'sophia.thomas@email.com', '1234567891234567', 4),
(5, '2021-12-24', 20.00, 'Delivered', 'liam.jackson@email.com', '1234567891234567', 5);

INSERT INTO `plm_items` (`item_id`, `name`, `price`) VALUES 
(1, 'Cannette 1', 2.55),
(2, 'Cannette 2', 2.55),
(3, 'Cannette 3', 2.87);

INSERT INTO `plm_is_composed` (`order_id`, `item_id`, `quantity`) VALUES 
(1, 1, 5),
(1, 2, 3),
(2, 1, 4),
(3, 3, 5),
(4, 1, 2),
(5, 3, 10);

INSERT INTO `plm_warehouses` (`warehouse_id`, `address`, `postal_code`, `max_capacity`) VALUES 
(1, '123 Rue des Fleurs', '75001', 3000),
(2, '2020 Avenue des Nuages', '75005', 2500),
(3, '303 Rue des Montagnes', '75006', 1000);

INSERT INTO `plm_stocked` (`item_id`, `warehouse_id`, `quantity`) VALUES 
(1, 1, 200),
(2, 1, 500),
(3, 1, 100),
(1, 2, 300),
(2, 2, 400),
(3, 2, 150),
(1, 3, 100),
(2, 3, 200),
(3, 3, 50);

INSERT INTO `plm_contact` (`contact_id`, `email`, `name`, `message`) VALUES
(1, 'bob.williams@email.com', 'Bob Williams', 'I would like to know if you have any discounts for large orders.');

INSERT INTO `plm_admins` (`username`, `password`, `role`) VALUES
('admin', 'admin', 'Admin');
