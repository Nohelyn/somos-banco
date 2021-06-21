import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET']) #home
def home():
    return "<h1> SOMOS BANCO </h1> <p> TU GENTE, TU BANCO </p>"

@app.route('/login', methods=['GET']) #Log In
def login():
    return "<h1> SOMOS BANCO </h1> <p> EN CONSTRUCCION </p>"

@app.route('/consultar', methods=['GET']) #Consultar Cuentas (clientes y TCred)
def consultar():
    return "<h1> SOMOS BANCO </h1> <p> EN CONSTRUCCION </p>"  

@app.route('/pagar', methods=['GET']) #pagar tarjeta de credito
def pagar():
    return "<h1> SOMOS BANCO </h1> <p> EN CONSTRUCCION </p>"  

@app.route('/movimientos', methods=['GET']) #movimientos de cuentas 
def movimientos():
    return "<h1> SOMOS BANCO </h1> <p> EN CONSTRUCCION </p>"

#faltan tambien los de uso interno de la app

app.run()
