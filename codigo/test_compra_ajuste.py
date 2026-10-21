# Casos de ajuste para completar la cobertura (CB-04 y CB-05)
from compra import validar_compra

def test_cb04_saldo_insuficiente():
    assert validar_compra(30, True, 100, 300) == "Compra rechazada"

def test_cb05_monto_cero():
    assert validar_compra(30, True, 500, 0) == "Compra rechazada"
