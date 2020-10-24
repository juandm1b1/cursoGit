from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#MySql Conexión
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'contactosflask'
mysql = MySQL(app)

#Settings: Inicializar una sesión: datos q guarda la app para reutilizar
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('select * from contactos')
    data = cur.fetchall()
    return render_template('index.html', contacts = data)
    
@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']

        if ((fullname == "") or (phone == "") or (email == "")):
            flash('Falta diligenciar uno o varios campos')
            ctx = {"fullname": fullname, "phone": phone, "email": email}
            return render_template('index.html', contacts=ctx)  
        else:
            cur = mysql.connection.cursor()
            cur.execute('insert into contactos (fullname,phone,email) values (%s,%s,%s)', (fullname,phone,email))
            mysql.connection.commit()
            flash('Contacto agregado correctamente')

        
        return redirect(url_for('Index'))
        

@app.route('/edit/<id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('select * from contactos where id = %s', [id])
    data = cur.fetchall()
    return render_template('edit_contact.html', contact = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
        update contactos 
        set fullname = %s,
            phone = %s,
            email = %s
        where id = %s""", (fullname,phone,email,id))
        mysql.connection.commit()
        flash('Contacto actualizado correctamente')
        return redirect(url_for('Index'))


@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('delete from contactos where id={0}'.format(id))
    mysql.connection.commit()
    flash('Contacto eliminado correctamente')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)


#@app.route('prueba_git')

#@app.route('prueba2_git')