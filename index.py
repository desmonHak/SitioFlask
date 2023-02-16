from flask import *
from consultas_sql import *
from sqlite3 import connect, OperationalError
from datetime import datetime
from os import mkdir
from os.path import exists

app = Flask(__name__) # para arranacar la aplicacion

@app.route("/") 
def index(): 
    return render_template("login.html")

@app.route('/guardar_archivo/', methods=['POST'])
def guardar_archivo():
    username = request.args.get('username')
    print(username)
    contenido = request.form['contenido']
    print(contenido)
    file = open(rutas_estaticos.format(username)+"/{}.html".format(username), "w")
    file.write(contenido)
    file.close()
    # procesar el contenido del archivo y guardarlo en el servidor
    return redirect(url_for('home2', username=username))

@app.route("/edit_my_site/<username>/<password>")
def edit_my_site(username, password):
    print("edit_my_site >> ", username, password)
    try:
        bd = connect(name_data_db)
        print("Base de datos abierta")
        
        cursor = bd.cursor()
        
        cursor.execute("SELECT user FROM users")
        users = cursor.fetchall()
        
        cursor.execute("SELECT password FROM users")
        _password = cursor.fetchall()

        if ('{}'.format(username),) in users:
            print("[*] Usuario {} existe".format(username))
            if _password[users.index(('{}'.format(username),))][0] == password:
                
                file = open(rutas_estaticos.format(username)+"/{}.html".format(username), "r")
                my_content = file.read()
                file.close()
                
                return render_template("edit_my_site.html", username=username, password=password, my_content=my_content)
        else:
            print("[*] Usuario {} no existe".format(username))
        
        print(users)
        print(_password)
        
        cursor.close()
        bd.close()
    except OperationalError as error:
        print("Error al abrir:", error)


@app.route('/home/<username>/<password>')
def home(username, password):
    """username = request.args.get('username')
    password = request.args.get('password')"""
    print("home >> ", username, password)
    return render_template("home.html", username=username, password=password)
"""@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if request.method == 'POST':
        name = request.form['User']
        password = request.form['Password']
        print(name, password)
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('home'))
    return render_template("formulario.html")"""

@app.route('/home/<username>')
def home2(username):
    print("home2 >> ", username)
    return render_template("{}/{}.html".format(username, username))

@app.route('/my_data')
def my_data():
    username = request.args.get('username')
    password = request.args.get('password')
    print("my_data>> ", username, password)

    try:
        bd = connect(name_data_db)
        print("Base de datos abierta")
        
        cursor = bd.cursor()
        
        cursor.execute("SELECT user FROM users")
        users = cursor.fetchall()
        
        cursor.execute("SELECT password FROM users")
        _password = cursor.fetchall()

        if ('{}'.format(username),) in users:
            print("[*] Usuario {} existe".format(username))
            if _password[users.index(('{}'.format(username),))][0] == password:
                print("[*] La contrasena es correcta, el usuario puede acceder.")
                date_time = cursor.execute("SELECT fecha_creacion FROM users").fetchall()[users.index(('{}'.format(username),))][0]
                print(date_time)
                return render_template("my_data.html", 
                                       username=username, 
                                       password=password,
                                       date_time=date_time
                                    )
        else:
            print("[*] Usuario {} no existe".format(username))
        
        print(users)
        print(_password)
        
        cursor.close()
        bd.close()
    except OperationalError as error:
        print("Error al abrir:", error)
    return redirect(url_for('index'))
    
      
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    try:
        bd = connect(name_data_db)
        print("Base de datos abierta")
        
        cursor = bd.cursor()
        
        cursor.execute("SELECT user FROM users")
        users = cursor.fetchall()
        
        cursor.execute("SELECT password FROM users")
        _password = cursor.fetchall()

        if ('{}'.format(username),) in users:
            print("[*] Usuario {} existe".format(username))
            if _password[users.index(('{}'.format(username),))][0] == password:
                print("[*] La contrasena es correcta, el usuario puede acceder.")
                if exists(rutas_estaticos.format(username)) == False:
                    mkdir(rutas_estaticos.format(username))
                    file = open(rutas_estaticos.format("default")+".html", "r")
                    my_content = file.read()
                    file.close()
                    
                    file = open(rutas_estaticos.format(username)+"/{}.html".format(username), "w")
                    file.write(my_content)
                    file.close()    
                return redirect(url_for('home', username=username, password=password))
        else:
            print("[*] Usuario {} no existe".format(username))
        
        print(users)
        print(_password)
        
        cursor.close()
        bd.close()
        
    except OperationalError as error:
        print("Error al abrir:", error)
    return redirect(url_for('index', username=username, ))

@app.route('/create_count', methods=['POST', 'GET'])
def create_count():
    return render_template("create_count.html")

@app.route('/create_count_', methods=['POST', 'GET'])
def create_count_():
        
    try:
        bd = connect(name_data_db)
        print("Base de datos abierta")
        
        cursor = bd.cursor()
        
        for tabla in tablas:
            cursor.execute(tabla)
        print("Tablas creadas correctamente")
    
        
        username = request.form['username']
        password = request.form['password']
        _datetime = datetime.now()
        values = [username, password, _datetime]
        print(values)
        
        cursor.execute(setencia_crear_user, values)
        
        bd.commit() #Guardamos los cambios al terminar el ciclo
        cursor.close()
        bd.close()
        
        if exists(rutas_estaticos.format(username)) == False:
            mkdir(rutas_estaticos.format(username))
            
            file = open(rutas_estaticos.format("default")+".html", "r")
            my_content = file.read()
            file.close()
            
            file = open(rutas_estaticos.format(username)+"/{}.html".format(username), "w")
            file.write(my_content)
            file.close()    
    
    except OperationalError as error:
        print("Error al abrir:", error)
    return redirect(url_for('index'))

@app.route("/about")# mi link about
def about():# mi funcion about
    return render_template("/about.html")
    #return "About page" # texto de mi link about
    
@app.route("/gato")
def gato():
    return render_template("/gato.html")

if __name__ == "__main__":# para arrancar la aplicacion
    app.run(debug = True) # esto arrancar la pagina y debugea el codigo
"""
    sudo pip install virtualenv : instalar virtual env
    estos archivo se suben a heroku, pagina de heroku(https://dashboard.heroku.com/apps)
    sudo snap install --classic heroku : para instalar heroku
    comando(heroku login) para registrate
"""
