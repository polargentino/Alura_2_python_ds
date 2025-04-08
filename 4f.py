# 7 - Función de división de columnas y manejo de excepciones:

def divide_columnas(lista_1: list, lista_2: list) -> list | None:
    """
    Divide los elementos de la lista_1 por los elementos correspondientes de la lista_2.

    Args:
        lista_1 (list): La lista del numerador.
        lista_2 (list): La lista del denominador.

    Returns:
        list | None: Una lista con los resultados de la división redondeados a dos decimales,
                     o None si ocurre un error (tamaños diferentes o división por cero).
    """
    try:
        if len(lista_1) != len(lista_2):  # Verificando si las listas tienen el mismo tamaño, si no, lanza una excepción
            raise ValueError("Las listas deben tener el mismo tamaño")

        # La función zip empareja los elementos de las listas y se genera una lista mediante la división entre las parejas
        resultado = [round(a / b, 2) for a, b in zip(lista_1, lista_2)]
        return resultado
    except ValueError as e:
        print(e)
        return None
    except ZeroDivisionError as e:
        print(f"{e}: La 2ª lista no puede tener un valor igual a 0")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

# Probando sin excepciones:

# Probando en el ejemplo que no lanza excepciones
print("Probando sin excepciones:")
presiones = [100, 120, 140, 160, 180]
temperaturas = [20, 25, 30, 35, 40]

resultado_sin_error = divide_columnas(presiones, temperaturas)
print(f"Resultado: {resultado_sin_error}")

# Probando con excepción (Caso 1):

# Probando en el ejemplo que lanza una excepción (ZeroDivisionError)
print("\nProbando con excepción (ZeroDivisionError):")
presiones_cero = [60, 120, 140, 160, 180]
temperaturas_cero = [0, 25, 30, 35, 40]

resultado_cero_error = divide_columnas(presiones_cero, temperaturas_cero)
print(f"Resultado: {resultado_cero_error}")

# Probando con excepción (Caso 2):

# Probando en el ejemplo que lanza una excepción (ValueError)
print("\nProbando con excepción (ValueError):")
presiones_tamano = [100, 120, 140, 160]
temperaturas_tamano = [20, 25, 30, 35, 40]

resultado_tamano_error = divide_columnas(presiones_tamano, temperaturas_tamano)
print(f"Resultado: {resultado_tamano_error}")

'''
Probando sin excepciones:
Resultado: [5.0, 4.8, 4.67, 4.57, 4.5]

Probando con excepción (ZeroDivisionError):
division by zero: La 2ª lista no puede tener un valor igual a 0
Resultado: None

Probando con excepción (ValueError):
Las listas deben tener el mismo tamaño
Resultado: None



Cambios y Explicación:
---------------------
Docstring Agregado: Se añadió un docstring al inicio de la función divide_columnas. Este docstring 
explica:

Qué hace la función.
Los argumentos que recibe (lista_1 y lista_2) y su tipo esperado.

Qué retorna la función (list | None) y las posibles razones para retornar None (error).

Anotación de Retorno Mejorada: La anotación de retorno se modificó a list | None para indicar 
explícitamente que la función puede devolver None en caso de error.

Retorno None en los Bloques except: Dentro de los bloques except ValueError y except 
ZeroDivisionError, se agregó la instrucción return None. Esto es una buena práctica para que la 
función indique explícitamente cuando ha ocurrido un error y no ha podido completar su tarea 
principal (devolver la lista de resultados).

Bloque except Exception: Se añadió un bloque except Exception as e: para capturar cualquier otro 
error inesperado que pudiera ocurrir durante la ejecución de la función. Esto proporciona una capa 
adicional de robustez al código. También retorna None en este caso.

Impresión de Resultados en las Pruebas: Se agregaron print() descriptivos alrededor de las llamadas a 
la función en las secciones de prueba para que la salida sea más clara y fácil de entender. 
También se imprime el valor retornado por la función en cada caso.

Con estas modificaciones, el código ahora tiene una documentación clara a través del docstring y 
maneja los errores de manera más explícita al retornar None cuando ocurren excepciones. La salida 
de las pruebas también es más informativa.
'''