from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('form_data.db')

@app.route('/submit', methods=['POST'])
def submit_form():
    # Extract data from form
    name = request.form.get('form_fields[name]')
    email = request.form.get('form_fields[email]')
    phone = request.form.get('form_fields[phone]')
    carpet_area = request.form.get('form_fields[crapet_area]')
    super_area = request.form.get('form_fields[super_area]')
    rent_carpet = request.form.get('form_fields[rent_carpet]')
    rent_super = request.form.get('form_fields[rent_super]')
    cam_area = request.form.get('form_fields[cam_area]')
    city_name = request.form.get('form_fields[city_name]')

    # Store data in SQLite database
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO form_submissions (name, email, phone, carpet_area, super_area, rent_carpet, rent_super, cam_area, city_name)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, email, phone, carpet_area, super_area, rent_carpet, rent_super, cam_area, city_name))
    conn.commit()
    conn.close()

    # Redirect back to the main page
    return redirect('http://127.0.0.1:5500/')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
