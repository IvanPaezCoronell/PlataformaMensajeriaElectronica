import sqlite3

def validar_usuario(usuario, password):
    db = sqlite3.connect('mensajeria.s3db')
    db.row_factory = sqlite3.Row
    cursor=db.cursor()
    consulta="select * from usuarios where correo='"+usuario+"' and password='"+password+"'"
    cursor.execute(consulta)
    resultado=cursor.fetchall()
    return resultado

def registrar_usuario(nombre,correo, password):
    db = sqlite3.connect('mensajeria.s3db')
    db.row_factory = sqlite3.Row
    cursor=db.cursor()
    consulta="insert into usuarios (nombreusuario,correo,password,estado,codigoactivacion) values ('"+nombre+"','"+correo+"','"+password+"','0','0' )"
    cursor.execute(consulta)
    db.commit()
    return "1"