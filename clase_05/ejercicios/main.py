from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


libros = []


@app.route('/')
def index():
    return render_template('formulario.html')


@app.route('/formulario-libro', methods=['POST',])
def procesar_formulario_libro():
    titulo = request.form['titulo'] 
    autor = request.form['autor'] 
    genero = request.form['genero'] 
    print(titulo, autor, genero)
    libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero
    }
    libros.append(libro)
    return redirect(url_for("list_libros"))


@app.route('/libros/v1')
def list_libros():
    return render_template('list_libros.html', libros=libros)


@app.route('/hello/<string:name>')
def hello_world(name: str):
    return render_template('index.html', name=name)


@app.route('/formulario-nombre', methods=['POST',])
def procesar_formulario_nombre():
    nombre = request.form['nombre'] 
    email = request.form['email'] 
    # Lógica para procesar el formulario aquí 
    print("Accediendo")
    return f'Tu nombre es {nombre} y tu email es {email}' 


if __name__ == '__main__':
    app.run(debug=True)

