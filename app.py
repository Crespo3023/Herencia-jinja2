from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/productos')
def lista_productos():
    lista_productos = ['Laptop', 'Mouse', 'Teclado', 'Ipad', 'Televisor','Tablet surface window']
    lista_precios = [1000, 50, 20, 500, 300, 800]
    
    # Apredi a usar el comando zip que permite combinar listas 
    # ya que jinja2 no puede manejar dos listas en una misma iterracion
    lista_combinada = zip(lista_productos,lista_precios)
    
    return render_template('productos.html', lista_combinada=lista_combinada)

@app.route('/usuarios')
def usuarios():
    lista_usuarios = ['Jhon', 'Luis', 'Carlos', 'Elena', 'Ana', 'Pepe']
    
    return render_template('user.html', usuarios=lista_usuarios)

if __name__ == '__main__':
    app.run(debug=True)
