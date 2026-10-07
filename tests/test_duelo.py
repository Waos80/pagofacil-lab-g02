"""MINI DUELO - Parte 2 del laboratorio.

Escribe aquí tus pruebas. El docente las ejecutará contra versiones del código
con defectos escondidos ("mutantes") y contará cuántos logran detectar.

REGLAS
  1. Solo puedes importar de `pytest` y de `pagofacil.comision`.
  2. TODAS tus pruebas deben PASAR con el código correcto (el que cumple
     ESPECIFICACION.md). Si una falla con el código correcto, no puntúas.
  3. Diseña desde la especificación (caja negra): particiones y valores límite.
  4. Evita montos cuyo resultado caiga justo en medio centavo (redondeo ambiguo).
  5. Trabaja SOLO en este archivo durante el duelo.
"""
import pytest

from pagofacil.comision import calcular_comision, calcular_total, validar_monto  # noqa: F401


def test_ejemplo_monto_bajo():  # ejemplo que ya pasa; puedes borrarlo o conservarlo
    assert calcular_comision(50) == 0


# --- Tus pruebas empiezan aquí ---
#Set de pruebas extra - Validando fronteras críticas de los tramos de comisión
@pytest.mark.parametrize("monto, esperado", [
    (1000,   15.0),   # límite superior del tramo 2 (incluye 1000)
    (1000.01, 10.0),  # primer centavo del tramo 3
    (2500,   25.0),   # exactamente donde se activa el tope
])
def test_comision_por_tramos(monto, esperado):
    assert calcular_comision(monto) == esperado


@pytest.mark.parametrize("monto, esperado", [
    (100.01, round(100.01 * 0.015, 2)),
])
def test_comision_por_tramos(monto, esperado):
    assert calcular_comision(monto) == esperado

def test_tipo_invalido():
    with pytest.raises(TypeError):
        calcular_comision("abc")