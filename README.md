# Grocery 4 All

### Because everyone needs groceries, ours is just smarter +_+

[Link to the GitHub Repository](https://github.com/SaeeSaadat/Grocery4All-LMU-MMT.git)
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

The program will start in the main menu.
- Some of the commands will immediately produce an output such as `inventory`
- Some commands will start a sequence, such as `add` or `sell`.
  - In these sequences the user will be asked to provide the appropriate information regarding that operation.
  - These sequences can be cancelled using the `ctrl+c` keyboard interruption.
- Other commands such as `calculator` will redirect the user to a new menu with new available commands.
  - The user may go back to the main menu using the `back` command.



---

## Database Persistence:
For data persistence, the program uses an SQLite3 database, which is stored in the `database_manager` directory.

The first time the program is run, it will ask the user to initiate a new database. in this process
the inventory is given a name by the user. Then the user can add products to the inventory, and start selling and
restocking products.
The user can also choose to fill the database with mock data (using the mock_data.sql script in the database_manager
directory, which will add 13 products to the inventory.

If the user exists the program, the next time it's run, it will automatically load the last inventory that was used.
If you wish to clear the database, you may either run the `reset` command, or delete the `database.sqlite` file in
the `database_manager` directory.

There are `backup` and `restore` functionalities available as well!

---

## List of available commands

(available in the shell by running the `help` command):

**Commands**: Every command is a single word. Some of the commands take _optional_ arguments
- example: `transactions 30`, `history 5`, `history`

The following list explains the functionality of each command. 


### Common commands in all menus:
- **help**: Show help information
- **exit**: Exit the program
- **clear**: Clear the console

### Commands in the main menu
- **inventory**: Display inventory information, and the products _**available**_ in the inventory
- **products**: Display all products
- **transactions**: Displays the recent transactions
  - `transactions {n}`: shows the last `n` transactions. Defaults to 10
- **add**: Add a new type of product
- **sell**: record a sell transaction
- **restock**: record a restock transaction
- **history**: Display the command history
  - `history {n}`: shows the last `n` commands from history. Defaults to 10
- **calculator**: Go to the calculation mode

- **reset**: Reset to factory settings
- **backup**: Create a backup file of the database
- **restore**: Restore the database from the backup file
- **mock**: Fill the database with mock data



### Commands in the calculator menu
- **revenue**: Calculate the total revenue
- **cost**: Calculate the total cost
- **profit**: Calculate the total profit
- **inventory** value: Calculate the total value of the inventory

---
## Software Architecture

- **grocery4all.py**: The main file that runs the program, and contains the main loop of the program.

- **database_manager**: Contains the database manager class, which is responsible for all interactions with the database.
The database manager module is the only module that interacts with the database directly. 
Therefor in case we needed to change the database system, we would only need to update this module.
Each inventory module has a corresponding module in this directory, which contains the SQL queries that are used in that module.

- **inventory**: Contains the business logic, and all classes and models that are used to represent the inventory and its products.

- **menu**: Contains the classes that represent the different menus in the program, and the logic that is used to interact
with the user. All menus used in the program are subclasses of the `CommandMenu` class.
This design will improve the maintainability of the project and makes it easier to add new features in the future.

- **resources**: Contains the strings and messages that are used in the program.

- **logs**: Contains the log files that are generated by the program.

- **tests**: Contains the unit tests for the program. The tests are written using the `unittest` module in Python
and can be run using 
```shell
python3 -m unittest discover tests
```