from flask import Flask,render_template,request
 
app = Flask(__name__,template_folder='template')



@app.route('/', methods=['GET', 'POST'])
def validate_licence_plate():
    if request.method == 'POST':
        form_data = request.form
        if not form_data.get("licencePlate"):
            return render_template('index.html', msg='No has ingresado ninguna placa')
    elif request.method == 'GET':
        return render_template('index.html')
    else:
        return 'OK'

 
app.run(host='localhost', port=5000)


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    app.run()