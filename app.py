from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hitung', methods=['POST'])
def hitung():
    operasi = request.form.get('operasi')
    angka1 = float(request.form.get('angka1'))
    angka2 = float(request.form.get('angka2')) if 'angka2' in request.form else None
    
    if operasi == 'tambah':
        hasil = angka1 + angka2
    elif operasi == 'kurang':
        hasil = angka1 - angka2
    elif operasi == 'kali':
        hasil = angka1 * angka2
    elif operasi == 'bagi':
        hasil = angka1 / angka2
    elif operasi == 'pangkat':
        hasil = angka1 ** angka2
    elif operasi == 'faktorial':
        hasil = math.factorial(int(angka1))
    
    return render_template('index.html', hasil=hasil)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
