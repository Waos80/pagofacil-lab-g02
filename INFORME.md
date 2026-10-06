# Informe del laboratorio · Pruebas y versionamiento

> Reemplaza **cada** `<<COMPLETAR>>` con tu respuesta. No borres los encabezados.
> Extensión esperada: 1.5 a 2 páginas. Se entrega haciendo `git push` de este archivo.

## 1. Datos del equipo

- **Equipo (gNN):** <<COMPLETAR>>
- **Repositorio (URL):** <<COMPLETAR>>

| Integrante | Carnet | Usuario de GitHub |
|------------|--------|-------------------|
<<<<<<< HEAD
| <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> |
| <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> |
=======
| Tony Balán | 1202124| TABALAN |
| Luis | 1090824| Waos80 |
| Juan Mazariegos | 1140024| MazaJP|
| Claudia Mejía | 1127224| Claudiaam18 |
| Rodrigo Peñate |1134324| joserodrigoSP |
>>>>>>> a7c9fc5 (docs(informe): documentacion del laboratorio parte 1)

## 2. Evidencia

Pega la salida real de estos comandos (bloque de código):

`python -m pytest -q`
```
<<<<<<< HEAD
<<COMPLETAR>>
=======
.F..FFF...FF                                                                                                                       [100%]
=============================================================== FAILURES ================================================================
________________________________________________ test_monto_exacto_100_no_paga_comision _________________________________________________

    def test_monto_exacto_100_no_paga_comision():
>       assert calcular_comision(100) == 0
E       assert 1.5 == 0
E        +  where 1.5 = calcular_comision(100)

tests\test_comision.py:15: AssertionError
_____________________________________________________ test_tope_maximo_de_q25[3000] _____________________________________________________

monto = 3000

    @pytest.mark.parametrize("monto", [3000, 10000, 1_000_000])
    def test_tope_maximo_de_q25(monto):
>       assert calcular_comision(monto) == 25
E       assert 30.0 == 25
E        +  where 30.0 = calcular_comision(3000)

tests\test_comision.py:25: AssertionError
____________________________________________________ test_tope_maximo_de_q25[10000] _____________________________________________________

monto = 10000

    @pytest.mark.parametrize("monto", [3000, 10000, 1_000_000])
    def test_tope_maximo_de_q25(monto):
>       assert calcular_comision(monto) == 25
E       assert 100.0 == 25
E        +  where 100.0 = calcular_comision(10000)

tests\test_comision.py:25: AssertionError
___________________________________________________ test_tope_maximo_de_q25[1000000] ____________________________________________________

monto = 1000000

    @pytest.mark.parametrize("monto", [3000, 10000, 1_000_000])
    def test_tope_maximo_de_q25(monto):
>       assert calcular_comision(monto) == 25
E       assert 10000.0 == 25
E        +  where 10000.0 = calcular_comision(1000000)

tests\test_comision.py:25: AssertionError
_______________________________________________ test_total_incluye_la_comision[200-203.0] _______________________________________________

monto = 200, esperado = 203.0

    @pytest.mark.parametrize("monto, esperado", [(200, 203.0), (500, 507.5)])
    def test_total_incluye_la_comision(monto, esperado):
>       assert calcular_total(monto) == esperado
E       assert 197.0 == 203.0
E        +  where 197.0 = calcular_total(200)

tests\test_total.py:16: AssertionError
_______________________________________________ test_total_incluye_la_comision[500-507.5] _______________________________________________

monto = 500, esperado = 507.5

    @pytest.mark.parametrize("monto, esperado", [(200, 203.0), (500, 507.5)])
    def test_total_incluye_la_comision(monto, esperado):
>       assert calcular_total(monto) == esperado
E       assert 492.5 == 507.5
E        +  where 492.5 = calcular_total(500)

tests\test_total.py:16: AssertionError
======================================================== short test summary info ========================================================
FAILED tests/test_comision.py::test_monto_exacto_100_no_paga_comision - assert 1.5 == 0
FAILED tests/test_comision.py::test_tope_maximo_de_q25[3000] - assert 30.0 == 25
FAILED tests/test_comision.py::test_tope_maximo_de_q25[10000] - assert 100.0 == 25
FAILED tests/test_comision.py::test_tope_maximo_de_q25[1000000] - assert 10000.0 == 25
FAILED tests/test_total.py::test_total_incluye_la_comision[200-203.0] - assert 197.0 == 203.0
FAILED tests/test_total.py::test_total_incluye_la_comision[500-507.5] - assert 492.5 == 507.5
6 failed, 6 passed in 0.18s
>>>>>>> a7c9fc5 (docs(informe): documentacion del laboratorio parte 1)
```

`git log v1.0.0..v1.0.1 --oneline --decorate`
```
<<<<<<< HEAD
<<COMPLETAR>>
=======
2aecb7f (tag: v1.0.1, origin/main, origin/HEAD, main) docs(changeLog) : registrar version 1.0.1
2285881 fix(comision): comision no mayor a 25
633fc4a tipo(comision): corregir el total que se debita al cliente
6bc332c fix(comision): incluir 100 exacto en el tramosin comision
346c82e test(pytest): incluir pruebas parametrizadas en test_edad.py
361ad6d fix(tarea-previa): incluir 18 años como mayor de edad
>>>>>>> a7c9fc5 (docs(informe): documentacion del laboratorio parte 1)
```

## 3. Bitácora de defectos

| # | Pruebas que fallaban | Síntoma (mensaje del error) | Causa raíz | Corrección (qué línea cambió) | Commit | Quién |
|---|----------------------|-----------------------------|------------|-------------------------------|--------|-------|
<<<<<<< HEAD
| 1 | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> |
| 2 | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> |
| 3 | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> |
=======
| 1 | tests/test_comision.py::test_monto_exacto_100_no_paga_comision | tests\test_comision.py:15: AssertionError | La condición del límite sin condición no incluye a 100, solo valores inferiores. | Se cambió el operador de la condición de < (menor que) a <= (menor o igual que) en la linea 30 de comision.py| 6bc332c | Waos80 |
| 2 | tests/test_comision.py::test_tope_maximo_de_q25[3000], tests/test_comision.py::test_tope_maximo_de_q25[10000], tests/test_comision.py::test_tope_maximo_de_q25[1000000] | tests\test_comision.py:25: AssertionError | El valor retornado por calcular_comision no toma en cuenta el valor de tope de la comisión. | Se agregó la función min en la línea 37 de comision.py para que se tome el valor de tope en caso que la comision supere el límite. | 2285881 | Claudia |
| 3 | tests/test_total.py::test_total_incluye_la_comision[200-203.0], tests/test_total.py::test_total_incluye_la_comision[500-507.5] | tests\test_total.py:16: AssertionError | El cálculo del total que se debita al cliente era incorrecto (monto - comision). | Se cambió la operación de (monto - comision) a (monto + comision) en la línea 44 de comision.py | 633fc4a | joserodrigoSP |
>>>>>>> a7c9fc5 (docs(informe): documentacion del laboratorio parte 1)

**Pregunta:** al inicio había 6 pruebas fallando pero solo 3 defectos. ¿Por qué? ¿Qué diferencia hay entre *síntoma* y *causa raíz*?

Una causa raiz puede causar multiples síntomas a lo largo de múltiples valores de prueba, por lo que un defecto puede causar múltiples fallos.

## 4. Versionamiento

1. Corrigieron 3 defectos sin cambiar la interfaz pública. ¿Por qué la nueva versión es `1.0.1` y no `1.1.0` ni `2.0.0`?
   Porque la nueva versión consiste en un parche que corrige errores de un código ya hecho, no se agregan nuevas funcionalidades ni cambian la estructura del proyecto sin hacer incompatible versiones anteriores.
2. Si agregaran la función nueva `calcular_comision_con_iva(monto)` sin tocar nada existente, ¿qué versión sería y por qué?
   Sería v1.1.0, ya que se agrega una nueva funcionalidad sin afectar la compatibilidad.
3. Si cambiaran `calcular_comision(monto)` para exigir un segundo parámetro obligatorio `moneda`, ¿qué versión sería y por qué?
   Sería v2.0.0, ya que al cambiar la cantidad de parámetros para la función implica que todas las demás secciones del código que la llamaban deben cambiar a la nueva cantidad de parámetros, haciendo el nuevo código incompatible con la anterior.
4. Ejecuten `git diff v1.0.0 v1.0.1 --stat`. ¿Qué archivos cambiaron y por qué es útil poder comparar dos versiones?
   Cambiaron:
   CHANGELOG.md              | 6 ++++++
   src/pagofacil/comision.py | 6 ++++--
   tarea_previa/edad.py      | 2 +-
   tarea_previa/test_edad.py 
   Esto es útil debido a que se puede conocer los archivos que podrían haber causado un fallo en una versión reciente y así poder arreglarlo con mayor facilidad.

## 5. Mini duelo

Tabla de casos que diseñaron (mínimo 6 filas; indiquen la técnica):

| Partición o límite que cubre | Entrada | Resultado esperado | Técnica |
|------------------------------|---------|--------------------|---------|
| <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> |
| <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> |
| <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> |
| <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> |
| <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> |
| <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> | <<COMPLETAR>> |

- **Resultado del marcador (mutantes detectados de 7):** <<COMPLETAR>>
- **¿Qué mutantes sobrevivieron (si alguno) y qué caso de prueba les habría faltado?** <<COMPLETAR>>

## 6. Reflexión (5 a 8 líneas)

Su suite visible quedó 100 % en verde y, aun así, el duelo puede encontrar defectos escondidos.
¿Qué implica eso para la estrategia de pruebas? Relaciónenlo con la pirámide de pruebas, con
qué conviene automatizar y con el caso Knight Capital de la clase.

<<COMPLETAR>>
