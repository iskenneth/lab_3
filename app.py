from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')  


@app.route('/works/toUpperCase', methods=['GET', 'POST'])
def to_uppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/works/areaOfCircle', methods=['GET', 'POST'])
def area_of_circle():
    result = None
    if request.method == 'POST':
        try: 
            radius = float(request.form.get('radius', 0))
            result = 3.1416 * (radius ** 2)
        except ValueError:
            result = "Invalid input"
    return render_template('areaOfCircle.html', result=result)

@app.route('/works/areaOfTriangle', methods=['GET', 'POST'])
def area_of_triangle():
    result = None
    if request.method == 'POST':
        try: 
            base = float(request.form.get('base', 0))
            height = float(request.form.get('height', 0))
            result = 0.5 * base * height
        except ValueError:
            result = "Invalid input"
    return render_template('areaOfTriangle.html', result=result)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    result = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        result = f"Thank you, {name}! Your message has been received."
    return render_template('contacts.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
