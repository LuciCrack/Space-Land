from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/editor')
def editor():
    return render_template('editor.html')

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.json
    # Compute stats based on user input (e.g., modules layout)
    # For now, just echo back
    return jsonify({"status": "ok", "input": data})

if __name__ == '__main__':
    app.run(debug=True)
