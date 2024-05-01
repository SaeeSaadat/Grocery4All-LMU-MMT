# Grocery 4 All 
### Because everyone needs groceries, ours is just smarter +_+

\
This project is part of the Ludwig Maximilians University's MMT program's essay assignment 
for the winter semester of 2024/25
--- 

## Description of the project
This project is a new booking system for the retail company "Grocery4ALL", designed to keep track of the inventory, revenue,
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

The program will act as a shell, meaning once it's run using 
```shell
python3 grocery4all.py
```
it will stay live in an infinite loop, and exits only after it receives the `exit` command or the `ctrl+c` signal.

List of available commands: 
#TODO
