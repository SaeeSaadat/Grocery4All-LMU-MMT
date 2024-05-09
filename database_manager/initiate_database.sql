create table if not exists products (
    id serial primary key,
    name varchar(255) not null,
    purchase_price decimal(10, 2) not null,
    selling_price decimal(10, 2) not null
);

create table if not exists inventory (
    id serial primary key,
    name varchar(255),
    creation_date timestamp not null default current_timestamp
);

create table if not exists inventory_products (
    inventory_id int not null,
    product_id int not null,
    quantity int not null,
    foreign key (inventory_id) references inventory(id),
    foreign key (product_id) references products(id),
    primary key (inventory_id, product_id)
);

-- Type of transactions: Add, Sell, Restock
create type transaction_type as enum ('Add', 'Sell', 'Restock');

create table transactions (
    id serial primary key,
    type transaction_type not null,
    inventory_id int not null,
    product_id int not null,
    quantity int not null,
    total_price decimal(10, 2) not null,
    transaction_date timestamp not null default current_timestamp,
    foreign key (inventory_id) references inventory(id),
    foreign key (product_id) references products(id)
);


create table if not exists command_history (
    command varchar(255) not null,
    command_date timestamp not null default current_timestamp
);
)