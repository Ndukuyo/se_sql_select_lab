
# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')

# View employees table 
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")


# STEP 2
# Replace None with your code
df_first_five = pd.read_sql("""SELECT employeeNumber, lastName FROM employees""", conn)

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql("""SELECT lastName, employeeNumber FROM employees""", conn)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql("""SELECT lastName, employeeNumber AS ID FROM employees""", conn)

# STEP 5
# Replace None with your code
df_executive = pd.read_sql("""
    SELECT *, 
        CASE 
            WHEN jobTitle = 'President' OR jobTitle = 'VP Sales' OR jobTitle = 'VP Marketing' THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
""", conn)

# STEP 6
# Replace None with your code
df_name_length = pd.read_sql("""SELECT LENGTH(lastName) AS name_length FROM employees""", conn)

# STEP 7
# Replace None with your code
df_short_title = pd.read_sql("""SELECT SUBSTR(jobTitle, 1, 2) AS short_title FROM employees""", conn)

# View order details table (provided reference code)
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn) 
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")

# STEP 8
# Replace None with your code
sum_total_price = pd.read_sql("""
    SELECT SUM(ROUND(priceEach * quantityOrdered)) AS total_amount
    FROM orderDetails
""", conn).iloc[0]['total_amount']



# Close the connection
conn.close()