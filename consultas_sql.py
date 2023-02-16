tablas = [
	"""
		CREATE TABLE IF NOT EXISTS users(
			user TEXT NOT NULL,
			password TEXT NOT NULL,
            fecha_creacion TIMESTAMP NOT NULL
		);
	"""
]

name_data_db = "data_base.db"
select_all = "SELECT * FROM {}"
rutas_estaticos = "templates/{}"
setencia_crear_user = "INSERT INTO users(user, password, fecha_creacion) VALUES (?,?,?)"