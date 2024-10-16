import pytest
from src.patentes import determinar_precio_patentes
from src.patentes import verificar_patente

# Pruebas por Tablas de Decisión
def test_auto_nuevo():
    assert determinar_precio_patentes('ABC123', '2020', '5600000') == 280000

def test_auto_semi_nuevo():
    assert determinar_precio_patentes('ABC123', '2017', '2600000') == 78000

def test_auto_casi_antiguo():
    assert determinar_precio_patentes('ABC123', '2012', '4220000') == 42200

def test_auto_antiguo():
    assert determinar_precio_patentes('ABC123', '1990', '13500000') == 0

def test_patente_valida():
    assert verificar_patente('ABC123')

def test_no_es_patente_valida():
    assert verificar_patente('') == 'Error en el numero de patente'

def test_modelo_invalido():
    assert determinar_precio_patentes('ABC123', '0', '13500000') == 'Error en la fecha del modelo'

def test_modelo_invalido2():
    assert determinar_precio_patentes('ABC123', '2025', '13500000') == 'Error en la fecha del modelo'

@pytest.mark.parametrize("pat1, year1, price1, expected",[
    ('ABC123', '2020', '13500000', 675000),
    ('ABC123', '2012', '13500000', 135000),
    ('ABC123', '1990', '13500000', 0),
    ('ABC123', '0', '13500000', 'Error en la fecha del modelo'),
    ('ABC123', '2020', '0', 'Error en el valor del auto'),
    ('ABC123', '', '13500000', 'Error en la fecha del modelo'),
    ('ABC123', '2020', '', 'Error en el valor del auto'),
    ('', '2020', '13400400', 'Error en el numero de patente')
])
def test_tabla(pat1, year1, price1, expected):
    assert determinar_precio_patentes(pat1, year1, price1) == expected

# Pruebas por Valores Límite
def test_valores_limite_5nuevo():
    assert determinar_precio_patentes('ABC123', '2019', '13500000') == 675000

def test_valores_limite_6seminuevo():
    assert determinar_precio_patentes('ABC123', '2018', '13500000') == 405000

def test_valores_limite_10seminuevo():
    assert determinar_precio_patentes('ABC123', '2014', '13500000') == 405000

def test_valores_limite_11casiantiguo():
    assert determinar_precio_patentes('ABC123', '2013', '13500000') == 135000

def test_valores_limite_25():
    assert determinar_precio_patentes('ABC123', '1999', '13500000') == 135000

def test_valores_limite_grande():
    assert determinar_precio_patentes('ABC123', '1900', '13500000') == 0