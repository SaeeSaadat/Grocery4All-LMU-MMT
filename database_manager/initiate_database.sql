create table if not exists products (
    id serial primary key,
    name varchar(255) not null,
    quantity int not null default 0,
    purchase_price decimal(10, 2) not null,
    selling_price decimal(10, 2) not null
);

