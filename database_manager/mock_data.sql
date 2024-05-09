-- This file will generate some mock data for testing the software
-- You are more than welcome to change the data as you see fit

insert into inventory (id, name) values (1, 'Grocery 4 All');

insert into products (id, name, purchase_price, selling_price) values (1, 'Milk', 1.5, 2.5);
insert into products (id, name, purchase_price, selling_price) values (2, 'Bread', 1.0, 1.5);
insert into products (id, name, purchase_price, selling_price) values (3, 'Butter', 2.0, 3.0);
insert into products (id, name, purchase_price, selling_price) values (4, 'Cheese', 3.0, 4.0);
insert into products (id, name, purchase_price, selling_price) values (5, 'Eggs', 1.0, 1.5);
insert into products (id, name, purchase_price, selling_price) values (6, 'Chocolate', 5.0, 6.5);
insert into products (id, name, purchase_price, selling_price) values (7, 'Peanut Butter', 5.5, 6.5);
insert into products (id, name, purchase_price, selling_price) values (8, 'Cereal', 3.0, 4.0);
insert into products (id, name, purchase_price, selling_price) values (9, 'Tomatoes', 0.5, 1.0);
insert into products (id, name, purchase_price, selling_price) values (10, 'Coffee Beans', 7.0, 9.0);
insert into products (id, name, purchase_price, selling_price) values (11, 'Tea', 5.0, 6.5);
insert into products (id, name, purchase_price, selling_price) values (12, 'Cookies', 1.0, 1.5);
insert into products (id, name, purchase_price, selling_price) values (13, 'Cooking Oil', 2.0, 2.75);


insert into inventory_products (inventory_id, product_id, quantity) values (1, 1, 400);
insert into inventory_products (inventory_id, product_id, quantity) values (1, 2, 500);
insert into inventory_products (inventory_id, product_id, quantity) values (1, 3, 500);
insert into inventory_products (inventory_id, product_id, quantity) values (1, 4, 250);
insert into inventory_products (inventory_id, product_id, quantity) values (1, 5, 480);
insert into inventory_products (inventory_id, product_id, quantity) values (1, 6, 1500);
insert into inventory_products (inventory_id, product_id, quantity) values (1, 7, 1250);
insert into inventory_products (inventory_id, product_id, quantity) values (1, 8, 1000);
insert into inventory_products (inventory_id, product_id, quantity) values (1, 9, 750);
insert into inventory_products (inventory_id, product_id, quantity) values (1, 10, 600);
-- No Tea, Cookies and Oil in stock :(

