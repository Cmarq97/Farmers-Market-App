

######### TEST DATABASE ##################




-- Add Users
INSERT INTO users (email, password) VALUES ('admin@email.com', 'adminpass');
INSERT INTO users (email, password) VALUES ('cmarq97@gmail.com', 'password');


-- Add Markets

INSERT INTO markets (market_name, market_day, market_start, market_end, market_address)
VALUES ('Monterey', 'Tuesday', '16:00', '20:00', 'Alvarado St Monterey, CA 93940');

INSERT INTO markets (market_name, market_day, market_start, market_end, market_address)
VALUES ('Pleasonton', 'Saturday', '09:00', '13:00', '424 Main St. Pleasonton, CA');

INSERT INTO markets (market_name, market_day, market_start, market_end, market_address)
VALUES ('Danville', 'Saturday', '09:00', '13:00', '205 Railroad Ave. Danville, CA');


--Insert Vendors
INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity, map_icon)
VALUES ('Sunrise Nursery', '', 'Cut Flowers|Eggs', '/static/img/sunflower.png');

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity, map_icon)
VALUES ('La Vie', 'Drinklavie.com', 'Fresh Juice', '/static/img/healthy-food.png');

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity, map_icon)
VALUES ('Lone Oak Ranch', 'ThefarmerandtheDale.com', 'Fruit|Vegetables', '/static/img/vegetables.png');

--Sunrise Nursery
INSERT INTO marketvendors (market_id, vendor_id) VALUES (1,1);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (2,1);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (3,1);


--La Vie
INSERT INTO marketvendors (market_id, vendor_id) VALUES (2,2);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (3,2);


--Lone Oak Ranch
INSERT INTO marketvendors (market_id, vendor_id) VALUES (2,3);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (3,3);
