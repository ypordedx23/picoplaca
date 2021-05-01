import numpy as np
import datetime
import core.utils as utils
import model.LicenceRequest as LicenceRequest

MORNING_START_TIME = datetime.time(7, 0, 0)
MORNING_FINISH_TIME = datetime.time(9, 30, 0)
EVENING_START_TIME = datetime.time(16, 0, 0)
EVENING_FINISH_TIME = datetime.time(19, 30, 0)



def can_be_on_the_road(licenceRequest):
    num_plate = utils.validate_ecuadorian_licence_plate(licenceRequest.licence)  
    print(licenceRequest.licence)
    print(licenceRequest.date)
    print(licenceRequest.time)
    if num_plate!="":
        if is_in_restriction_hour(licenceRequest.time):
            if is_restricted_to_drive(licenceRequest.licence[-1], utils.validate_date(licenceRequest.date).weekday()):
                return "No puede circular"
            else:
                return "Puede circular sin preocupaciones"
        else:
            return "Puede circular sin preocupaciones"
    else:
        return "Placa ingresada no válida"


def is_in_restriction_hour(hour):
    time = datetime.datetime.strptime(hour,'%H:%M').time()
    if time > MORNING_START_TIME and time< MORNING_FINISH_TIME:
        return True
    else:
        if time > EVENING_START_TIME and time < EVENING_FINISH_TIME:
            return True
        else:
            return False


def is_restricted_to_drive(last_digit, day):
    switcher={
        0: True if last_digit == '1' or last_digit == '2'  else False,
        1: True if last_digit == '3' or last_digit == '4'  else False,
        2: True if last_digit == '5' or last_digit == '6'  else False,
        3: True if last_digit == '7' or last_digit == '8'  else False,
        4: True if last_digit == '9' or last_digit == '0'  else False,
        5: False,
        6: False
    }
    val = switcher.get(day,"Valor no valido")
    return val