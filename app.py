from flask import Flask
from flask import render_template, request, redirect
from flaskext.mysql import MySQL
app=Flask(__name__)
mysql=MySQL()

app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='website_python'
mysql.init_app(app)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/estudios')
def estudios():
    return render_template('sitio/estudios.html')

@app.route('/admin')
def admin_index():
    return render_template('admin/index.html')

@app.route('/admin/login')
def admin_login():    
    return render_template('admin/login.html')
    

@app.route('/admin/estudios')
def admin_estudios():
    
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute("SELECT * FROM `estudios`")
    estudios=cursor.fetchall()
    conexion.commit()
    print(estudios)
    
    return render_template('admin/estudios.html')


@app.route('/admin/estudios/save', methods=['POST'])
def admin_estudios_save():
    
    _nombre=(request.form["textNombre"])
    _academia=(request.form["textAcademia"])
    _url=(request.form["urlAcademia"])
    _archivo=(request.files["myFile"])
    
    sql="INSERT INTO `estudios` (`id`, `nombre`, `imagen`, `academia`, `url`) VALUES (NULL,%s,%s,%s,%s);"
    datos=(_nombre,_archivo.filename,_academia,_url)
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()
    
    print(_nombre)
    print(_academia)
    print(_url)
    print(_archivo)
    
    print(request.form['textNombre'])
    return redirect('/admin/estudios')

if __name__ =='__main__':
    app.run(debug=True)
    
