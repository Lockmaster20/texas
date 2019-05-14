from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/curiosidades')
def p1():
    return render_template('p1.html')

@app.route('/localizacao')
def p2():
    return render_template('p2.html')

@app.route('/desporto')
def p3():
    return render_template('p3.html')

@app.route('/cultura')
def p4():
    return render_template('p4.html')

@app.route('/aeroespaco')
def p5():
    return render_template('p5.html')

@app.route('/gastronomia')
def p6():
    return render_template('p6.html')

@app.route('/musica')
def p7():
    return render_template('p7.html')

@app.route('/geografia')
def p8():
    return render_template('p8.html')

@app.route('/economia')
def p9():
    return render_template('p9.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/ec')
def ec():
    return render_template('ec.html')


if __name__ == '__main__':
    app.run(debug=True)
