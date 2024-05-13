-- This file will generate some mock data for testing the software
-- You are more than welcome to change the data as you see fit

insert into inventory (name) values ('Grocery 4 All');

insert into products (id, name, purchase_price, selling_price, quantity) values (1, 'Milk', 1.5, 2.5, 400);
insert into products (id, name, purchase_price, selling_price, quantity) values (2, 'Bread', 1.0, 1.5, 500);
insert into products (id, name, purchase_price, selling_price, quantity) values (3, 'Butter', 2.0, 3.0, 500);
insert into products (id, name, purchase_price, selling_price, quantity) values (4, 'Cheese', 3.0, 4.0, 250);
insert into products (id, name, purchase_price, selling_price, quantity) values (5, 'Eggs', 1.0, 1.5, 480);
insert into products (id, name, purchase_price, selling_price, quantity) values (6, 'Chocolate', 5.0, 6.5, 1500);
insert into products (id, name, purchase_price, selling_price, quantity) values (7, 'Peanut Butter', 5.5, 6.5, 1250);
insert into products (id, name, purchase_price, selling_price, quantity) values (8, 'Cereal', 3.0, 4.0, 1000);
insert into products (id, name, purchase_price, selling_price, quantity) values (9, 'Tomatoes', 0.5, 1.0, 750);
insert into products (id, name, purchase_price, selling_price, quantity) values (10, 'Coffee Beans', 7.0, 9.0, 600);
insert into products (id, name, purchase_price, selling_price) values (11, 'Tea', 5.0, 6.5);
insert into products (id, name, purchase_price, selling_price) values (12, 'Cookies', 1.0, 1.5);
insert into products (id, name, purchase_price, selling_price) values (13, 'Cooking Oil', 2.0, 2.75);
-- No Tea, Cookies and Oil in stock :(

-- Each product must have been added via an `Add` Transaction
insert into transactions (type, product_id) values ('Add', 1);
insert into transactions (type, product_id) values ('Add', 2);
insert into transactions (type, product_id) values ('Add', 3);
insert into transactions (type, product_id) values ('Add', 4);
insert into transactions (type, product_id) values ('Add', 5);
insert into transactions (type, product_id) values ('Add', 6);
insert into transactions (type, product_id) values ('Add', 7);
insert into transactions (type, product_id) values ('Add', 8);
insert into transactions (type, product_id) values ('Add', 9);
insert into transactions (type, product_id) values ('Add', 10);
insert into transactions (type, product_id) values ('Add', 11);
insert into transactions (type, product_id) values ('Add', 12);
insert into transactions (type, product_id) values ('Add', 13);

-- The quantity of the products must have been set using `Restock` Transactions!
insert into transactions (type, product_id, quantity, total_value) values ('Restock', 1, 400, 400 * 1.5);
insert into transactions (type, product_id, quantity, total_value) values ('Restock', 2, 500, 500 * 1.0);
insert into transactions (type, product_id, quantity, total_value) values ('Restock', 3, 500, 500 * 2.0);
insert into transactions (type, product_id, quantity, total_value) values ('Restock', 4, 250, 250 * 3.0);
insert into transactions (type, product_id, quantity, total_value) values ('Restock', 5, 480, 480 * 1.0);
insert into transactions (type, product_id, quantity, total_value) values ('Restock', 6, 1500, 1500 * 5.0);
insert into transactions (type, product_id, quantity, total_value) values ('Restock', 7, 1250, 1250 * 5.5);
insert into transactions (type, product_id, quantity, total_value) values ('Restock', 8, 1000, 1000 * 3.0);
insert into transactions (type, product_id, quantity, total_value) values ('Restock', 9, 750, 750 * 0.5);
insert into transactions (type, product_id, quantity, total_value) values ('Restock', 10, 600, 600 * 7.0);

