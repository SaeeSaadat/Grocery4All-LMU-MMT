# Grocery 4 All

### Because everyone needs groceries, ours is just smarter +_+

\
This project is part of the Ludwig Maximilians University's MMT program's essay assignment
for the winter semester of 2024/25
--- 

## Description of the project

This project is a new booking system for the retail company "Grocery4ALL", designed to keep track of the inventory,
revenue,
and costs regarding their business operations.
Written in Python, uses SQLite3 as its database system and has a Command Line interface.  
It is capable of the following:

- Managing a single inventory
    - One program will not support multiple inventories, as per the requirements listed in the proposal.
- Adding items to an inventory with attributes such as
    - ID
    - Name
    - Quantity
    - Purchasing Price
    - Selling Price
- Displaying the content inside each inventory
- Selling Products from the inventory
- Restocking products
- Showing the last interaction of the system
- Financial Calculations such as:
    - Total Revenue
    - Total Value of the Inventory
    - Total Cost
    - Total Profit

---

## How to use:

The program will start by either running the

```shell
 ./run.sh
 ```

script (Mac and Linux only) or by running the `grocery4all.py` file directly using

```shell
python3 grocery4all.py
```

The program will act as a shell, meaning once it's run, it will stay live in an infinite loop, and exits only after it
receives the `exit` command or the `ctrl+c` signal.

---

## Database Persistence:

The first time the program is run, it will ask the user to initiate a new database. in this process
the inventory is given a name by the user. Then the user can add products to the inventory, and start selling and
restocking products.
The user can also choose to fill the database with mock data (using the mock_data.sql script in the database_manager
directory, which will add 13 products to the inventory.

If the user exists the program, the next time it's run, it will automatically load the last inventory that was used.
If you wish to clear the database, you may either run the `reset` command, or delete the `database.sqlite` file in
the `database_manager` directory.
---

## List of available commands

(available in the shell by running the `help` command):

### Common commands in all menus:
- **help**: Show help information
- **exit**: Exit the program
- **clear**: Clear the console

### Commands in the main menu
- **inventory**: Display inventory information, and the products available in the inventory
- **products**: Display all products
- **new** product: Add a new type of product
- **sell**: record a sell transaction
- **restock**: record a restock transaction
- **history**: Display the transaction history
- **calculator**: Go to the calculation mode

- **reset**: Reset to factory settings
- **mock** data: Fill the database with mock data
- **manual** initiation: Manually initiate a new database


### Commands in the calculator menu
- **revenue**: Calculate the total revenue
- **cost**: Calculate the total cost
- **profit**: Calculate the total profit
- **inventory** value: Calculate the total value of the inventory