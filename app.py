from flask import Flask,render_template,request
import core.validator as validator
from model.LicenceRequest import LicenceRequest

app = Flask(__name__,template_folder='template')
 
app.run(host='localhost', port=5000)

#Metodo que obtiene el request del cliente
@app.route('/', methods=['GET', 'POST'])
def pico_placa_predictor():
    if request.method == 'POST':
        form_data = request.form
        licenceRequest = LicenceRequest(form_data.get("licencePlate"), form_data.get("date"), form_data.get("time"))
        result = validator.can_be_on_the_road(licenceRequest)
        return render_template('validator.html',show_result_modal = True, msg=result)
    elif request.method == 'GET':
        return render_template('validator.html')
    else:
        return 'OK'



if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    app.static_folder = 'static'
    app.run()