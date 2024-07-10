from flask import Flask
from flask import render_template , request , redirect
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'notas'

mysql.init_app(app)

@app.route('/')
def index():
  conn = mysql.connect()
  cursor = conn.cursor()

  sql = "SELECT * FROM notas;"
  cursor.execute(sql)

  notas= cursor.fetchall()
  conn.commit()

  return render_template('notas/index.html', notas=notas)

@app.route('/nuevo')
def nuevo():
  return render_template('notas/nuevo.html')

@app.route('/notas', methods=["POST"])
def notas():
  _nombre = request.form['nombre']
  _asunto = request.form['asunto']
  _nota = request.form['nota']

  sql = "INSERT INTO notas(nombre, asunto, nota) values (%s,%s, %s);"
  datos = (_nombre, _asunto, _nota)

  conn = mysql.connect()
  cursor = conn.cursor()

  cursor.execute(sql, datos)

  conn.commit()

  return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
  sql = "DELETE FROM notas WHERE id=%s"
  conn = mysql.connect()
  cursor = conn.cursor()

  cursor.execute(sql, id)

  conn.commit()
  return redirect('/')

@app.route('/modify/<int:id>')
def modify(id):
  sql = "SELECT * FROM notas WHERE ID=%s"
  conn = mysql.connect()
  cursor = conn.cursor()

  cursor.execute(sql, id)
  notas = cursor.fetchone()

  conn.commit()
  return render_template('notas/editar.html', notas = notas)

@app.route('/actualizar', methods={"POST"})
def actualizar():
  _id = request.form['id'] 
  _nombre = request.form['nombre']
  _asunto = request.form['asunto']
  _nota = request.form['nota']

  datos = (_id, _nombre, _asunto, _nota)

  conn = mysql.connect()
  cursor = conn.cursor()

  sql = f'UPDATE notas SET nombre="{_nombre}", asunto="{_asunto}", nota="{_nota}" WHERE id="{_id}"'

  cursor.execute(sql)
  conn.commit()
  return redirect('/')


if __name__ == '__main__':
  app.run(debug=True)