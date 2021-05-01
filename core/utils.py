import re
import numpy as np
import datetime


LICENCE_PLATE_REG_NEW = r"^(?:[A-C|E|G-N|O-Z][A-Z][A-Z][0-9]{4})$"
LICENCE_PLATE_REG_OLD = r"^(?:[A-C|E|G-N|O-Z][A-Z][A-Z][0-9]{3})$"
LICENCE_PLATE_REG_DIP = r"^(?:[C|O|A|I][C|D|I|T][0-9]{4})$"

def validate_ecuadorian_licence_plate(licence_plate):
    try:
        old_plate = re.compile(LICENCE_PLATE_REG_OLD)
        new_plate = re.compile(LICENCE_PLATE_REG_NEW)
        dip_plate = re.compile(LICENCE_PLATE_REG_DIP)
        licence_plate = validate_plate_length(licence_plate)
        if re.fullmatch(old_plate, licence_plate):
            #Valido para placa antigua
            return licence_plate
        else:
            if re.fullmatch(new_plate, licence_plate):
                #valido para placa nueva
                return licence_plate
            else:
                if re.fullmatch(dip_plate, licence_plate):
                    #valido para placa diplomatica o internacional
                    licence_plate = validate_diplomatic_plate(licence_plate)
                    return licence_plate
                else:
                    return ""
    except Exception:
        return ""

def validate_diplomatic_plate(licence_plate):
    valid_alpha_letters_switcher ={
        'CC':licence_plate,
        'CD':licence_plate,
        'OI':licence_plate,
        'AT':licence_plate,
        'IT':licence_plate
    }
    return valid_alpha_letters_switcher.get(licence_plate[0:2],"")


def validate_plate_length(licence_plate):
    if(len(licence_plate)==6 or len(licence_plate)==7):
        return licence_plate
    else:
        new_licence_plate=""
        counter=0
        for x in licence_plate:
            if(counter<3):
                if x.isalpha():
                    new_licence_plate += x
                counter+=1
            else:
                if(counter<7):
                    if x.digit():
                        new_licence_plate += x
                    counter+=1
        return new_licence_plate

def validate_date(date_text):
    try:
        return datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Formato de fecha incorrecto, el formato es Año-Mes-Dia")
        return ""

def day_of_week(date):
    day_of_week_switcher ={
        0:'Lunes',
        1:'Martes',
        2:'Miercoles',
        3:'Jueves',
        4:'Viernes',
        5:'Sabad0',
        6:'Domingo'
    }
    return day_of_week_switcher.get(date,"")

