from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route untuk halaman utama (Menampilkan Form)
@app.route('/')
def home():
    # Ini akan memanggil file index.html di dalam folder templates
    return render_template('index.html')

# Route contoh API untuk menerima data dari tombol/form
@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    pesan = data.get("pesan", "")
    
    # Memberikan respon balik ke browser
    return jsonify({
        "status": "sukses",
        "pesan_diterima": f"Flask menerima: {pesan}"
    })

if __name__ == '__main__':

    app.run(debug=True, port=5000)