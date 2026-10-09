        # fieldtype = request.form.get("fieldtype")
        # if fieldtype == "job_title":
        #     query = "select job_title, count(job_title) from employees group by job_title;"
        #     cursor.execute(query)
        #     rows = cursor.fetchall()
        #     title = [i[0] for i in rows]
        #     total = [i[1] for i in rows]
        #     plt.pie(total, labels=title)
        #     plt.savefig("static/images/analysis.png")
        #     name = "analysis.png"
        # elif fieldtype == "gender":
        #     query = "select gender, count(gender) from employees group by gender;"
        #     cursor.execute(query)
        #     rows = cursor.fetchall()
        #     title = [i[0] for i in rows]
        #     total = [i[1] for i in rows]
        #     plt.pie(total, labels=title)
        #     plt.savefig("static/images/analysis.png")
        #     name = "analysis.png"    
        # elif fieldtype == "status":
        #     query = "select status,count(status) from employees group by status;"
        #     cursor.execute(query)
        #     rows = cursor.fetchall()
        #     title = [i[0] for i in rows]
        #     total = [i[1] for i in rows]
        #     plt.pie(total, labels=title)
        #     plt.savefig("static/images/analysis.png")
        #     name = "analysis.png"
        # elif fieldtype == "employment_type":
        #     query = "select employment_type,count(employment_type) from employees group by employment_type;"
        #     cursor.execute(query)
        #     rows = cursor.fetchall()
        #     title = [i[0] for i in rows]
        #     total = [i[1] for i in rows]
        #     plt.pie(total, labels=title)
        #     plt.savefig("static/images/analysis.png")
        #     name = "analysis.png"
        # elif fieldtype == "city":
        #     query = "select city,count(city) from employees group by city;"
        #     cursor.execute(query)
        #     rows = cursor.fetchall()
        #     title = [i[0] for i in rows]
        #     total = [i[1] for i in rows]
        #     plt.pie(total, labels=title)
        #     plt.savefig("static/images/analysis.png")
        #     name = "analysis.png"


        # return render_template("employeesanalyze.html", rows = rows, selected = fieldtype )

