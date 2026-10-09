import time
from flask import Flask, request, render_template
import mysql.connector
from functions import yearsincomebargraph,totalofcustomers

import matplotlib
matplotlib.use("Agg")    
import matplotlib.pyplot as plt
connection = mysql.connector.connect(
    host="localhost",
    username= "nayanuser",
    password = "Nayan@1234567890",
    database = "flipkart_db"
)

cursor = connection.cursor()

app = Flask(__name__)

#route for homepage
@app.route("/",methods=["GET","POST"])
def home():
    return render_template("homepage.html")

# addemp route
@app.route("/addemp", methods=["GET","POST"])
def addemp():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        dept_id = request.form.get("dept_id")
        job_title = request.form.get("job_title")
        hire_date = request.form.get("hire_date")
        employment_type = request.form.get("employment_type")
        status = request.form.get("status")
        manager_id = request.form.get("manager_id")
        city = request.form.get("city")
        gender = request.form.get("gender")
        date_of_birth = request.form.get("date_of_birth")    
        query = ("Insert into employees (first_name,last_name,email,phone,dept_id,job_title,hire_date,employment_type,status,manager_id,city,gender,date_of_birth) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")    
        data = (first_name,last_name,email,phone,dept_id,job_title,hire_date,employment_type,status,manager_id,city,gender,date_of_birth)
        cursor.execute(query,data)
        connection.commit()
        status = "success"
        return render_template("addemp.html", status = status)
    else:
        return render_template("addemp.html")

    
@app.route("/addcus", methods=["GET","POST"])       
def addcus():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        gender = request.form.get("gender")
        date_of_birth = request.form.get("date_of_birth")
        registration_date = request.form.get("registration_date")
        loyalty_tier = request.form.get("loyalty_tier")
        is_active = request.form.get("is_active")
        referral_code = request.form.get("referral_code")
        query = ("insert into customers (first_name,last_name,email,phone,gender,date_of_birth,registration_date,loyalty_tier,is_active,referral_code) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        data = (first_name,last_name,email,phone,gender,date_of_birth,registration_date,loyalty_tier,is_active,referral_code)
        cursor.execute(query,data)
        connection.commit()
        status = "success"
        return render_template("addcus.html", status = status)
    else:
        return render_template("addcus.html")

@app.route("/delcus",methods=["GET","POST"])
def delcus():
    if request.method == "POST":
        customer_id = request.form.get("customer_id")

        cursor.execute(f"delete from customers where customer_id = '{customer_id}'")
        connection.commit()
        status = "success"
        return render_template("delcus.html", status = status)
    else:
        return render_template("delcus.html")
@app.route("/delcoup",methods=['GET','POST'])
def delcoup():
    if request.method == "POST":
        coupon_id = request.form.get("coupon_id")
        cursor.execute(f"delete from coupons where coupon_id ='{coupon_id}'")
        connection.commit()
        coupon = "coupon"
        return render_template("delcoup.html",coupon = coupon)
    else:
        return render_template("delcoup.html")

@app.route("/delprod",methods=["GET","POST"])
def delprod():
    if request.method== "POST":
        product_id = request.form.get(product_id)
        cursor.execute(f"delete from products product_id = '{product_id}'")
        connection.commit()
        product = "product"
        return render_template("delprod.html",product = product)
    else:
        return render_template("delprod.html")

@app.route("/addcate",methods=['GET','POST'])
def addcate():
    if request.method == "POST":
        category_name = request.form.get("category_name")
        parent_id = request.form.get("parent_id")
        description = request.form.get("description")

        query = ("insert into categories (category_name,parent_id,description) values (%s,%s,%s)")
        data = (category_name,parent_id,description)
        cursor.execute(query,data)
        connection.commit()
        addcate = "success"

        return render_template("addcate.html", addcate = addcate)
    else:
        return render_template("addcate.html")

@app.route("/addcus_add",methods=['GET','POST'])
def addcus_add():
    if request.method == "POST":
        customer_id = request.form.get("customer_id")
        address_type = request.form.get("address_type")
        address_line1 = request.form.get("address_line1")
        city = request.form.get("city")
        state = request.form.get("state")
        pincode = request.form.get("pincode")
        is_default = request.form.get("is_default")

        query = ("insert into customer_addresses (customer_id,address_type,address_line1,city,state,pincode,is_default) values (%s,%s,%s,%s,%s,%s,%s)")
        data = (customer_id,address_type,address_line1,city,state,pincode,is_default)
        cursor.execute(query,data)
        connection.commit()
        status = "status"
        return render_template("addcus_add.html", status = status)
    else:
        return render_template("addcus_add.html")
@app.route('/addorder',methods = ['GET','POST'])
def addorder():
    if request.method == "POST":
        customer_id = request.form.get("customer_id")
        order_date = request.form.get("order_date")
        status = request.form.get("status")
        shipping_address_id = request.form.get("shipping_address_id")
        coupon_id = request.form.get("coupon_id")
        subtotal = request.form.get("subtotal")
        discount_amt = request.form.get("discount_amt")
        shipping_charges = request.form.get("shipping_charges")
        tax_amt = request.form.get("tax_amt")
        total_amount = request.form.get("total_amount")
        payment_status = request.form.get("payment_status")
        delivery_date = request.form.get("delivery_date")
        warehouse_id = request.form.get("warehouse_id")
        channel = request.form.get("channel")

        query = ("insert into orders (customer_id, order_date, status, shipping_address_id, coupon_id, subtotal, discount_amt, shipping_charges, tax_amt, total_amount, payment_status, delivery_date, warehouse_id, channel) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        data = (customer_id, order_date, status, shipping_address_id, coupon_id, subtotal, discount_amt, shipping_charges, tax_amt, total_amount, payment_status, delivery_date, warehouse_id, channel)

        cursor.execute(query,data)
        connection.commit()
        status = "status" 
        return render_template("addorder.html",status = status)
    else:
        return render_template("addorder.html")

@app.route("/incomeanalysis")
def orders():
    yearsincomebargraph()
    return render_template("yearsofincome.html")

@app.route("/genderanalysis")    
def customer():
    totalofcustomers()
    return render_template("countofcustomers.html")



# lsit
ALLOWED_FIELDS = {
    "job_title": "Job Title",
    "status": "Status",
    "employment_type": "Employment Type",
    "city": "City",
    "gender": "Gender",
}


ORDER_FIELDS ={
    "payment_status":"Payment Status",
    "status":"Status"
}


import os

CHART_DIR = os.path.join(app.static_folder, "images")
os.makedirs(CHART_DIR, exist_ok=True)

def make_chart(rows, fieldtype):
    labels = [str(r[0]) for r in rows]
    totals = [r[1] for r in rows]

    fig, ax = plt.subplots(figsize=(7, max(3, 0.45 * len(labels) + 1)))
    colors = plt.cm.viridis([i / max(len(labels) - 1, 1) for i in range(len(labels))])
    bars = ax.barh(labels, totals, color=colors)

    ax.invert_yaxis()
    ax.bar_label(bars, padding=4)
    ax.set_xlabel("Employees")
    ax.set_title(f"Employees by {ALLOWED_FIELDS[fieldtype]}", fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()

    fig.savefig(os.path.join(CHART_DIR, f"analysis_{fieldtype}.png"), dpi=150)
    plt.close(fig)
    return f"images/analysis_{fieldtype}.png"

@app.route("/employeesanalyze", methods=["GET","POST"])
def empanalyze():
    rows = image = fieldtype = None

    if request.method == "POST":
        fieldtype = request.form.get("fieldtype")

        if fieldtype in ALLOWED_FIELDS:   # safe: only whitelisted column names reach the SQL
            query = (f"SELECT {fieldtype}, COUNT(*) FROM employees "
                     f"GROUP BY {fieldtype} ORDER BY COUNT(*) DESC")
            cursor.execute(query)
            rows = cursor.fetchall()
            image = make_chart(rows, fieldtype)

    return render_template(
        "employeesanalyze.html",
        rows=rows,
        selected=fieldtype,
        image=image,
        fields=ALLOWED_FIELDS,
        ts=int(time.time())
    )     

@app.route("/orderanalyze",methods=["GET","POST"])
def orderanalyze():
    rows = image = fieldtype = None
    if request.method == "POST":
        fieldtype = request.form.get("fieldtype")

        if fieldtype in ALLOWED_FIELDS:   # safe: only whitelisted column names reach the SQL
            query = (f"SELECT {fieldtype}, COUNT(*) FROM orders "
                     f"GROUP BY {fieldtype} ORDER BY COUNT(*) DESC")
            cursor.execute(query)
            rows = cursor.fetchall()
            image = make_chart(rows, fieldtype)
        
        return render_template(
        "orderananlyze.html",
        rows=rows,
        selected=fieldtype,
        image=image,
        fields=ALLOWED_FIELDS,
        ts=int(time.time())
    )  





if __name__ == "__main__":
    app.run(debug=True)