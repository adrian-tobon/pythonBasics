while True:
    try:
        num1 = int(input("ingresa un numero: "))
        resultado = 100/num1
        print(resultado)       
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        break
    except ValueError:
        print("el valor ingresado no es valido")
        break
    except KeyboardInterrupt:
        print("ejecucion interrumpida") 
        break   
    finally:
        print("que tenga buen dia")