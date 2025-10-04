from flask import Flask, render_template, request, jsonify, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "super_secret_hackathon_key"  # Needed for session


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mission', methods=['GET', 'POST'])
def mission():
    if request.method == 'POST': # Guarda lo elegido en la session
        session['mission'] = request.form['mission']
        return redirect(url_for('habitat')) # Al siguiente menu: habitat
    # Si el method es GET renderiza la pagina
    return render_template('mission.html')


@app.route('/habitat', methods=['GET', 'POST'])
def habitat():
    if request.method == 'POST': # Guarda lo elegido en la session
        session['habitat'] = request.form['habitat']
        if session['habitat'] == 'orbit':
            return redirect(url_for('editor'))
        return redirect(url_for('location')) # Al siguiente menu: location
    # Si el method es GET
    # Revisamos si eligio orbita u otro
    mission = session['mission']
    if mission in ['orbit', 'moon', 'mars']:
        return render_template('habitat.html', mission=mission)
    
    # Error: if the session var 'mission' is none of the expected
    # (which should not by any normal mean happen) then you
    # must go through mission choosing
    return redirect(url_for('mission'))


@app.route('/location', methods=['GET', 'POST'])
def location():
    if request.method == 'POST':
        session['location'] = request.form['location']
        # Now, pass all choices to the editor
        return redirect(url_for('editor'))

    mission = session['mission']
    if mission in ['moon', 'mars', 'orbit']: 
        # Pass mission to render only the locations for the intended mission
        return render_template('location.html', mission=session.get('mission'))

    return redirect(url_for('mission'))


@app.route('/editor')
def editor():
    return render_template('editor.html')


@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.json
    # Compute stats based on user input (e.g., modules layout)
    # For now, just echo back
    return jsonify({"status": "ok", "input": data})


@app.route('/view')
def view():
    return render_template('3dview.html')

if __name__ == '__main__':
    app.run(debug=True)
