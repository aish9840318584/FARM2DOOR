from flask import Flask, request, render_template
import mysql.connector
import os

app = Flask(__name__)
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Dhanun@01',
    'database': 'food',

}


connection = mysql.connector.connect(**db_config)



@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')
@app.route('/dishes')
def dishes():
    return render_template('dishes.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/menu')
def menu():
    return render_template('menu.html')
@app.route('/review')
def review():
    return render_template('review.html')

@app.route('/submit_order', methods=['POST'])
def submit_order():
    name = request.form['name']
    phone_number = request.form['phone_number']
    order_name = request.form['order_name']
    additional_food = request.form.get('additional_food', '')
    quantity = request.form['quantity']
    order_date_time = request.form['order_date_time']
    address = request.form['address']
    message = request.form.get('message', '')

    cursor = connection.cursor()
    sql = """
        INSERT INTO orders (name, phone_number, order_name, additional_food, quantity, order_date_time, address, message)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (name, phone_number, order_name, additional_food, quantity, order_date_time, address, message)
    cursor.execute(sql, values)
    connection.commit()
    cursor.close()

    return render_template('order_confirmation.html', 
                           name=name, 
                           phone_number=phone_number, 
                           order_name=order_name, 
                           additional_food=additional_food, 
                           quantity=quantity, 
                           order_date_time=order_date_time, 
                           address=address, 
                           message=message)

if __name__ == '__main__':
    app.run(debug=True,port= 5001)
