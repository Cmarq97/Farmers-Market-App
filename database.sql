-- Add Users
INSERT INTO users (email, password) VALUES ('admin@email.com', 'adminpass');
INSERT INTO users (email, password) VALUES ('cmarq97@gmail.com', 'password');

-- Add addresses

INSERT INTO addresses (address_id, address_street, address_city, address_zip)
VALUES (1, 'Alvarado St', 'Monterey', '93940');

INSERT INTO addresses (address_id, address_street, address_city)
VALUES (2, '424 Main St', 'Pleasonton');

INSERT INTO addresses (address_id, address_street, address_city)
VALUES (3, '205 Railroad Ave', 'Danville');

INSERT INTO addresses (address_id, address_street, address_city)
VALUES (4, '1326 9th Ave', 'San Francisco');

-- Add Markets

INSERT INTO markets (market_name, market_day, market_start, market_end, address_id)
VALUES ('Monterey', 'Tuesday', '16:00', '20:00', 1);

INSERT INTO markets (market_name, market_day, market_start, market_end, address_id)
VALUES ('Pleasonton', 'Saturday', '09:00', '13:00', 2);

INSERT INTO markets (market_name, market_day, market_start, market_end, address_id)
VALUES ('Danville', 'Saturday', '09:00', '13:00', 3);

INSERT INTO markets (market_name, market_day, market_start, market_end, address_id)
VALUES ('SF Inner Sunset', 'Sunday', '09:00', '13:00', 4);



--insert Vendors 

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity)
VALUES ('Sunrise Nursery', '', 'cut flowers, eggs');

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity)
VALUES ('La Vie', 'Drinklavie.com', 'Fresh Juice');

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity)
VALUES ('Lone Oak Ranch', 'ThefarmerandtheDale.com', 'Fruit, Vegetables');

--Market Vendors

--Sunrise Nursery
INSERT INTO marketvendors (market_id, vendor_id) VALUES (1,1);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (2,1);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (3,1);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (4,1);

--La Vie
INSERT INTO marketvendors (market_id, vendor_id) VALUES (2,2);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (3,2);

--Lone Oak Ranch
INSERT INTO marketvendors (market_id, vendor_id) VALUES (2,3);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (3,3);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (4,3);

-- Create some useful views

