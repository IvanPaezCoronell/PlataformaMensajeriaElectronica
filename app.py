from flask import Flask, render_template,request
import hashlib
import controlador

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("login.html")

@app.route("/validarUsuario" , methods=["GET","POST"])
def validarUsuario():
    if request.method == "POST":
        usu = request.form["txtusuario"]
        passw = request.form["txtpass"]
        passw2 = passw.encode()
        passw2 = hashlib.sha384(passw2).hexdigest()

        respuesta = controlador.validar_usuario(usu,passw2)
        if len(respuesta) == 0:
            mensaje = "Usuario o contraseña incorrectos"
            return render_template("informacion.html", datas=mensaje)
        else:
        #print("Usuario: " +usu)
        #print("Password: " +passw)
        #print("Password encrip: " +passw2)

            return render_template("principal.html")


@app.route("/registrarUsuario" , methods=["GET","POST"])
def registrarUsuario():
    if request.method == "POST":
        nombre = request.form["txtnombre"]
        email = request.form["txtusuarioregistro"]
        passw = request.form["txtpassregistro"]

        passw2 = passw.encode()
        passw2 = hashlib.sha384(passw2).hexdigest()

        respuesta = controlador.registrar_usuario(nombre,email,passw2)

        mensaje = "El usuario " + nombre + " ha sido registrado con éxito"
        return render_template("informacion.html",datas=mensaje)