from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/productos')
def lista_productos():
    lista_productos = ['Laptop', 'Mouse', 'Teclado', 'Ipad', 'Televisor','Tablet surface window']
    
    return render_template('productos.html', lista_productos=lista_productos)

@app.route('/usuarios')
def usuarios():
    lista_usuarios = ['Jhon', 'Luis', 'Carlos', 'Elena', 'Ana', 'Pepe']
    
    return render_template('user.html', usuarios=lista_usuarios)

if __name__ == '__main__':
    app.run(debug=True)
