from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.secret_key = "super_secret_hackathon_key"  # Needed for session

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mission', methods=['GET', 'POST'])
def mission():
    if request.method == 'POST':
        session['mission'] = request.form['mission']
        return redirect(url_for('habitat_type'))
    return render_template('mission.html')

@app.route('/habitat-type', methods=['GET', 'POST'])
def habitat_type():
    if request.method == 'POST':
        session['habitat_type'] = request.form['habitat_type']
        return redirect(url_for('location'))
    return render_template('habitat_type.html')

@app.route('/location', methods=['GET', 'POST'])
def location():
    if request.method == 'POST':
        session['location'] = request.form['location']
        # Now, pass all choices to the editor
        return redirect(url_for('editor'))
    # Optionally: pass mission/habitat_type to template to customize options
    return render_template('location.html', mission=session.get('mission'), habitat_type=session.get('habitat_type'))

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
