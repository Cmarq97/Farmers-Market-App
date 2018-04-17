-- Add Users
INSERT INTO users (email, password) VALUES ('admin@email.com', 'adminpass');
INSERT INTO users (email, password) VALUES ('cmarq97@gmail.com', 'password');


-- Add Markets

INSERT INTO markets (market_name, market_day, market_start, market_end, market_address, market_city)
VALUES ('Monterey Farmer''s Market', 'Tuesday', '16:00', '20:00', 'Alvarado St Monterey, CA 93940', 'Monterey');

INSERT INTO markets (market_name, market_day, market_start, market_end, market_address, market_city)
VALUES ('Pleasanton Farmer''s Market', 'Saturday', '09:00', '13:00', '424 Main St. Pleasonton, CA', 'Pleasanton');

INSERT INTO markets (market_name, market_day, market_start, market_end, market_address, market_city)
VALUES ('Danville Farmer''s Market', 'Saturday', '09:00', '13:00', '205 Railroad Ave. Danville, CA', 'Danville');

INSERT INTO markets (market_name, market_day, market_start, market_end, market_address, market_city)
VALUES ('Inner Sunset Farmer''s Market', 'Sunday', '09:00', '13:00', '1326 9th Ave. San Francisco, CA', 'San Francisco');

INSERT INTO markets (market_name, market_day, market_start, market_end, market_address, market_city)
VALUES ('Brentwood Farmer''s Market', 'Saturday', '08:00', '12:00','655 First St. Brentwood, CA', 'Brentwood');

INSERT INTO markets (market_name, market_day, market_start, market_end, market_address, market_city)
VALUES ('Concord Farmer''s Market', 'Tuesday', '10:00', '14:00', '2100 Salvio St. Concord, CA', 'Concord');

INSERT INTO markets (market_name, market_day, market_start, market_end, market_address, market_city)
VALUES ('Pittsburg Farmer''s Market', 'Saturday', '09:00', '13:00', '544 Railroad Ave. Pittsburg, CA', 'Pittsburg');

INSERT INTO markets (market_name, market_day, market_start, market_end, market_address, market_city)
VALUES ('Vallejo Farmer''s Market', 'Saturday', '09:00', '14:00', '400 Georgia St. Vallejo, CA', 'Vallejo');

INSERT INTO markets (market_name, market_day, market_start, market_end, market_address, market_city)
VALUES ('Evergreen Farmer''s Market', 'Sunday & Wednesday', '09:00', '13:00', '4055 Evergreen Village Sq. San Jose, CA', 'San Jose');

INSERT INTO markets (market_name, market_day, market_start, market_end, market_address, market_city)
VALUES ('Downtown San Leandro Farmer''s Market', 'Wednesday', '16:00', '20:00', '135 Parrott St. San Leandro, CA', 'San Leandro' );

INSERT INTO markets (market_name, market_day, market_start, market_end, market_address, market_city)
VALUES ('Contra Costa Farmer''s Market', 'Sunday', '09:00', '13:00', '1799 Locust St Walnut Creek, CA', 'Walnut Creek');

INSERT INTO markets (market_name, market_day, market_start, market_end, market_address, market_city)
VALUES ('Jack London Square Farmer''s Market', 'Sunday', '10:00', '15:00', 'Webster St & Embarcadero West Oakland, CA', 'Oakland');

INSERT INTO markets (market_name, market_day, market_start, market_end, market_address, market_city)
VALUES ('Old Oakland Farmer''s Market', 'Friday', '09:00', '14:00', '9th St. & Broadway Oakland, CA', 'Oakland');

INSERT INTO markets (market_name, market_day, market_start, market_end, market_address, market_city)
VALUES ('Willow Glen Farmer''s Market', 'Saturday', '09:00', '13:00', '2175 Lincoln Ave. San Jose, CA', 'San Jose');

INSERT INTO markets (market_name, market_day, market_start, market_end, market_address, market_city)
VALUES ('San Leandro Farmer''s Market at Bayfair', 'Saturday', '09:00', '13:00', '15555 E 14th St San Leandro, CA', 'San Leandro');

INSERT INTO markets (market_name, market_day, market_start, market_end, market_address, market_city)
VALUES ('Campbell Farmer''s Market', 'Sunday', '09:00', '13:00', 'Campbell Ave & Central Ave Campbell, CA', 'Campbell');

INSERT INTO markets (market_name, market_day, market_start, market_end, market_address, market_city)
VALUES ('Mountain View Farmer''s Market', 'Sunday', '09:00', '13:00', '600 W Evelyn Ave Mountain View, CA', 'Mountain View');

INSERT INTO markets (market_name, market_day, market_start, market_end, market_address, market_city)
VALUES ('Divisadero Farmer''s Market', 'Sunday', '10:00', '14:00', '1301-1315 Grove St San Francisco, CA', 'San Francisco');
--insert Vendors 

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity, map_icon)
VALUES ('Sunrise Nursery', '', 'Cut Flowers|Eggs', '/static/img/sunflower.png');

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity, map_icon)
VALUES ('La Vie', 'Drinklavie.com', 'Fresh Juice', '/static/img/healthy-food.png');

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity, map_icon)
VALUES ('Lone Oak Ranch', 'ThefarmerandtheDale.com', 'Fruit', '/static/img/vegetables.png');

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity, map_icon)
VALUES ('Shelly''s Farm', 'Facebook.com/shellysfarmfresh.com', 'Eggs', '/static/img/egg.png');

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity, map_icon)
VALUES ('Prather Ranch Meat Co.', 'PratherRanch.com', 'Meat', '/static/img/steak.png');

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity, map_icon)
VALUES ('Hummus Heaven', '', 'Hummus', '/static/img/hummus.png');

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity, map_icon)
VALUES ('Smit Farms', '', 'Apples|Berries|Cherries', '/static/img/apple.png');

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity, map_icon)
VALUES ('J&M Ibarra Farms', '', 'Vegetables', '/static/img/vegetables.png');

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity, map_icon)
VALUES ('Foustmans', 'Foustmans.com', 'Salami', '/static/img/sausage.png');

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity)
VALUES ('That Garlic Stuff', 'Facebook.com/ThatGarlicStuff', 'Sauces');

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity, map_icon)
VALUES ('Bella Fruit & Drinks', '', 'Cut Fruit|Juice', '/static/img/healthy-food.png');

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity, map_icon)
VALUES ('Jiquilipan Frutas y Aguas Frescas', '', 'Cut Fruit|Juice', '/static/img/healthy-food.png');

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity, map_icon)
VALUES ('Hall''s Organic Farm', '', 'Vegetables|Strawberries', '/static/img/vegetables.png');

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity)
VALUES ('Cipponeri Family Farms', '', 'Fruits|Nuts|Melons');

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity, map_icon)
VALUES ('Bistro Blends', 'BayAreaBistro.com', 'Olive Oil', '/static/img/olive-oil.png');

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity, map_icon)
VALUES ('Great Valley Poultry', '', 'Eggs', '/static/img/egg.png');

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity)
VALUES ('Alonso Baking & Foods', '', 'Baked Goods');

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity, map_icon)
VALUES ('Precious Puch Doggie Bakery', '', 'Dog Treats', '/static/img/snack.png');

INSERT INTO vendors (vendor_name, vendor_website, vendor_commodity, map_icon)
VALUES ('Home Maid Ravioli', '', 'Ravioli|Pasta|Sauces|Olives', '/static/img/ravioli.png');
--Market Vendors

--Sunrise Nursery
INSERT INTO marketvendors (market_id, vendor_id) VALUES (1,1);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (2,1);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (3,1);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (4,1);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (5,1);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (6,1);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (7,1);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (8,1);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (9,1);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (10,1);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (13,1);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (14,1);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (15,1);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (16,1);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (17,1);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (18,1);


--La Vie
INSERT INTO marketvendors (market_id, vendor_id) VALUES (2,2);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (3,2);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (12,2);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (16,2);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (17,2);

--Lone Oak Ranch
INSERT INTO marketvendors (market_id, vendor_id) VALUES (2,3);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (3,3);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (4,3);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (11,3);

--Shellys Farm
INSERT INTO marketvendors (market_id, vendor_id) VALUES (2,4);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (4,4);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (5,4);

--Prather Ranch
INSERT INTO marketvendors (market_id, vendor_id) VALUES (3,5);

--Hummus Heaven
INSERT INTO marketvendors (market_id, vendor_id) VALUES (3,6);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (4,6);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (5,6);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (6,6);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (8,6);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (9,6);

--Smit Farms
INSERT INTO marketvendors (market_id, vendor_id) VALUES (2,7);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (3,7);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (6,7);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (8,7);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (11,7);

--J&M Ibarra Farms
INSERT INTO marketvendors (market_id, vendor_id) VALUES (1,8);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (11,8);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (15,8);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (17,8);

--Foustmans
INSERT INTO marketvendors (market_id, vendor_id) VALUES (1,9);

--Garlic Stuff
INSERT INTO marketvendors (market_id, vendor_id) VALUES (1,10);

--Bella Fruit
INSERT INTO marketvendors (market_id, vendor_id) VALUES (1,11);

--Jiquilipan Fruit 
INSERT INTO marketvendors (market_id, vendor_id) VALUES (1,12);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (9,12);

--Hall Farms
INSERT INTO marketvendors (market_id, vendor_id) VALUES (1,13);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (6,13);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (13,13);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (16,13);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (17,13);

--Cipponeri
INSERT INTO marketvendors (market_id, vendor_id) VALUES (1,14);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (3,14);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (5,14);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (10,14);

--Bistro Blends
INSERT INTO marketvendors (market_id, vendor_id) VALUES (6,15);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (10,15);

--Great Valley Poultry
INSERT INTO marketvendors (market_id, vendor_id) VALUES (3,16);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (6,16);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (9,16);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (10,16);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (12,16);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (15,16);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (17,16);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (18,16);
--Alonso Baking
INSERT INTO marketvendors (market_id, vendor_id) VALUES (1,17);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (15,17);
--Precious Puch
INSERT INTO marketvendors (market_id, vendor_id) VALUES (10,18);

--Home Maid Ravioli
INSERT INTO marketvendors (market_id, vendor_id) VALUES (2,19);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (4,19);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (5,19);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (10,19);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (12,19);
INSERT INTO marketvendors (market_id, vendor_id) VALUES (18,19);



