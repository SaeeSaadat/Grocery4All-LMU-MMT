create table if not exists inventory (
    name varchar(255) primary key,
    creation_date timestamp not null default current_timestamp
);


create table if not exists products (
    id INTEGER primary key,
    name varchar(255) not null unique,
    purchase_price decimal(10, 2) not null,
    selling_price decimal(10, 2) not null,
    quantity int not null default 0
);

create table if not exists transactions (
    id INTEGER primary key,
    type transaction_type not null,
    product_id int not null,
    quantity int not null,
    total_price decimal(10, 2) not null,
    transaction_time timestamp not null default current_timestamp,
    foreign key (product_id) references products(id),
    check ( type in ('Add', 'Sell', 'Restock') )
);


create table if not exists command_history (
    command varchar(255) not null,
    command_date timestamp not null default current_timestamp
);
