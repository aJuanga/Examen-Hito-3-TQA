# Casos de caja blanca diseñados (CB-01 a CB-03)
from compra import validar_compra

def test_cb01_menor_de_edad():
    assert validar_compra(16, True, 500, 200) == "Compra no permitida: edad"

def test_cb02_cuenta_inactiva():
    assert validar_compra(25, False, 500, 200) == "Compra no permitida: cuenta"

def test_cb03_compra_aprobada():
    assert validar_compra(30, True, 500, 200) == "Compra aprobada"
