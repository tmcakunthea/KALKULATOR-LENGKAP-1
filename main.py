from flask import Flask, request, render_template
import math
from sympy import symbols, diff, sympify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/penjumlahan', methods=['GET', 'POST'])
def penjumlahan():
    if request.method == 'POST':
        angka1 = float(request.form['angka1'])
        angka2 = float(request.form['angka2'])
        hasil = angka1 + angka2
        return render_template('hasil.html', operasi='Penjumlahan', hasil=hasil)
    return render_template('penjumlahan.html')

@app.route('/pengurangan', methods=['GET', 'POST'])
def pengurangan():
    if request.method == 'POST':
        angka1 = float(request.form['angka1'])
        angka2 = float(request.form['angka2'])
        hasil = angka1 - angka2
        return render_template('hasil.html', operasi='Pengurangan', hasil=hasil)
    return render_template('pengurangan.html')

@app.route('/perkalian', methods=['GET', 'POST'])
def perkalian():
    if request.method == 'POST':
        angka1 = float(request.form['angka1'])
        angka2 = float(request.form['angka2'])
        hasil = angka1 * angka2
        return render_template('hasil.html', operasi='Perkalian', hasil=hasil)
    return render_template('perkalian.html')

@app.route('/pembagian', methods=['GET', 'POST'])
def pembagian():
    if request.method == 'POST':
        angka1 = float(request.form['angka1'])
        angka2 = float(request.form['angka2'])
        hasil = angka1 / angka2
        return render_template('hasil.html', operasi='Pembagian', hasil=hasil)
    return render_template('pembagian.html')

@app.route('/pemangkatan', methods=['GET', 'POST'])
def pemangkatan():
    if request.method == 'POST':
        basis = float(request.form['basis'])
        eksponen = float(request.form['eksponen'])
        hasil = math.pow(basis, eksponen)
        return render_template('hasil.html', operasi='Pemangkatan', hasil=hasil)
    return render_template('pemangkatan.html')

@app.route('/faktorial', methods=['GET', 'POST'])
def faktorial_route():
    if request.method == 'POST':
        bilangan = int(request.form['bilangan'])
        hasil = math.factorial(bilangan)
        return render_template('hasil.html', operasi='Faktorial', hasil=hasil)
    return render_template('faktorial.html')

if __name__ == '__main__':
    app.run(debug=True)
    