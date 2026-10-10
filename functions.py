import mysql.connector
import matplotlib.pyplot as plt

connection = mysql.connector.connect(
    host="localhost",
    username= "nayanuser",
    password = "Nayan@1234567890",
    database = "flipkart_db"
)

cursor = connection.cursor()

def yearsincomebargraph():
    cursor.execute("select year(delivery_date) as year, sum(total_amount) as networth from orders where payment_status= 'Paid' and year(delivery_date) is not null group by year(delivery_date) order by year(delivery_date) ;")
    data = cursor.fetchall()
    year = []
    income = []
    for i in data:
        year.append(i[0])
        income.append(i[1])

    # 1. Vibrant 7-color gradient palette (Deep Blue to Magenta Sunset)
    colors = ['#03045e', '#023e8a', '#0077b6', '#0096c7', '#00b4d8', '#48cae4', '#90e0ef']

    # 2. The optimized bar line for 7 items
    plt.bar(year, income, color=colors, width=0.55, edgecolor='white', linewidth=1.5, zorder=3)

    # 3. Clean, minimalist layout adjustments
    plt.grid(axis='y', linestyle=':', alpha=0.5, zorder=0)  # Subtle dotted background grid
    plt.gca().set_axisbelow(True)                           # Puts grid lines safely behind bars
    plt.gca().spines[['top', 'right', 'left']].set_visible(False) # Removes outer box borders
    plt.tick_params(axis='both', which='both', length=0)    # Removes rigid tick marks for a cleaner look
    plt.savefig("static/yearsofincome.jpg")

def totalofcustomers():
    cursor.execute("select gender,count(gender) Customer from customers group by gender;")
    data = cursor.fetchall()
    gender = []
    customer = []

    for i in data:
        gender.append(i[0])
        customer.append(i[1])

    plt.pie(customer,labels=gender,autopct='%1.2f%%')

    plt.savefig("static/countgender.jpg")        


def warehousesgraph():
    cursor.execute("with tb1 as (select w.warehouse_id, warehouse_name, courier_partner, status from warehouses w join shipments s on w.warehouse_id = s.warehouse_id) select status,count(status) from tb1 group by status;")
    data = cursor.fetchall()
    status = []
    warehouses = []

    for i in data:
        status.append(i[0])
        warehouses.append(i[1])

    colors = ['#03045e', '#023e8a', '#0077b6', '#0096c7', '#00b4d8', '#48cae4', '#90e0ef', '#00b4d8', '#48cae4', '#90e0ef']
    
    # 2. The optimized bar line for 7 items
    plt.bar(status, warehouses, color=colors, width=0.55, edgecolor='white', linewidth=1.5, zorder=3)

    # 3. Clean, minimalist layout adjustments
    plt.grid(axis='y', linestyle=':', alpha=0.5, zorder=0)  # Subtle dotted background grid
    plt.gca().set_axisbelow(True)                           # Puts grid lines safely behind bars
    plt.gca().spines[['top', 'right', 'left']].set_visible(False) # Removes outer box borders
    plt.tick_params(axis='both', which='both', length=0)    # Removes rigid tick marks for a cleaner look
    plt.savefig("static/yearsofincome.jpg")