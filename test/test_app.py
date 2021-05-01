import pytest
import numpy as np
import datetime
from core import utils
from core import validator


@pytest.mark.test
def test_case_valid_licence_plate():
    '''ValidarPlaca :: Ejecutar Prueba para verificar valides de placa:: ValidateEcuadorianLicencePlate'''
    num_plate = utils.validate_ecuadorian_licence_plate("PBM2942")  
    assert num_plate == "PBM2942"

@pytest.mark.test
def test_case_valid_licence_plate():
    '''ValidarFecha :: Ejecutar Prueba para validar Fecha Ingresada:: ValidateDate'''
    result = utils.validate_date("2020-02-15")
    assert result == datetime.datetime.strptime("2020-02-15", '%Y-%m-%d')


@pytest.mark.test
def test_case_valid_licence_plate():
    '''UltimoDigitoPicoPlaca :: Ejecuta prueba para verificar si puede circular un Lunes :: IsResctrictedToDrive'''
    result = validator.is_restricted_to_drive("2",0)  
    assert result == True