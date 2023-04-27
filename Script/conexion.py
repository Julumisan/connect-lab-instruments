# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 12:35:25 2023

@author: Julu

TODO ESTO ES SUPONIENDO QUE HAYA ENTENDIDO BIEN LO QUE TENGO QUE HACER
Parece que no pude soportar el estilo Neutrón

"""

import pyvisa as visa
import numpy as np

def connect_scope():
    """
    Función que establece la conexión con el osciloscopio.

    Returns:
    scope: objeto que representa la conexión con el osciloscopio.
    """
    rm = visa.ResourceManager()
    scope = rm.open_resource('DIRECCION OSCILOSCOPIO VISA')
    return scope

def configure_channel(scope):
    """
    Función que configura el canal ao0 de la tarjeta DAQ para generar una señal.

    Parameters:
    scope: objeto que representa la conexión con el osciloscopio.

    Returns:
    None
    """
    scope.write('MEASUrement:IMMed:SOUrce')
    scope.write('MEASUrement:MEAS<x>:SOUrce')
    scope.write('AUTOSet:VIEW')


def read_data(scope):
    """
    Función que lee los datos generados por la tarjeta DAQ en el canal ao0.

    Parameters:
    scope: objeto que representa la conexión con el osciloscopio.

    Returns:
    data: array de numpy que contiene los datos de la señal generada por la tarjeta DAQ en el canal ao0.
    """
    data = scope.query_ascii_values('CURVe') #Esto debería coger los valores y dibujarlos
    data = np.array(data)
    return data

def close_scope(scope):
    """
    Función que cierra la conexión con el osciloscopio.

    Parameters:
    scope: objeto que representa la conexión con el osciloscopio.

    Returns:
    None
    """
    scope.close()

def connect_multimeter():
    """
    Función que establece la conexión con el multímetro.

    Returns:
    multimeter: objeto que representa la conexión con el multímetro.
    """
    rm = visa.ResourceManager()
    multimeter = rm.open_resource('DIRECCION VISA MULTIMETRO')
    return multimeter

def configure_multimeter(multimeter):
    """
    Función que configura el multímetro para leer el voltaje.

    Parameters:
    multimeter: objeto que representa la conexión con el multímetro.

    Returns:
    None
    """
    multimeter.write('CONF:VOLT:DC')
    multimeter.write('VOLT:DC:NPLC 10')

def read_voltage(multimeter):
    """
    Función que lee el voltaje medido por el multímetro.

    Parameters:
    multimeter: objeto que representa la conexión con el multímetro.

    Returns:
    voltage: float que representa el voltaje medido por el multímetro.
    """
    voltage = multimeter.query_ascii_values('READ')
    voltage = voltage[0]
    return voltage

def close_multimeter(multimeter):
    """
    Función que cierra la conexión con el multímetro.

    Parameters:
    multimeter: objeto que representa la conexión con el multímetro.

    Returns:
    None
    """
    multimeter.close()

if __name__ == '__main__':
    # Establecer la conexión con el osciloscopio
    scope = connect_scope()

    # Configurar el canal ao0 de la tarjeta DAQ
    configure_channel(scope)
    # Leer los datos generados por la tarjeta DAQ
    data = read_data(scope)

    # Cerrar la conexión con el osciloscopio
    close_scope(scope)

    # Establecer la conexión con el multímetro
    multimeter = connect_multimeter()

    # Configurar el multímetro para leer el voltaje
    configure_multimeter(multimeter)

    # Leer el voltaje medido por el multímetro
    voltage = read_voltage(multimeter)

    # Cerrar la conexión con el multímetro
    close_multimeter(multimeter)

    print('Los datos generados por la tarjeta DAQ son:')
    print(data)
    print('El voltaje medido por el multímetro es:')
    print(voltage)