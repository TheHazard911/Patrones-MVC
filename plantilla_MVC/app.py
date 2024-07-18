from MVC.modelo import Modelo
from MVC.vista import Vista
from MVC.controlador import Controlador

bd = Modelo() #Instanciamos el modelo
vista = Vista() #Instanciamos la vista
controlador = Controlador(bd) #Instanciamos el controlador y le pasamos el modelo
vista.set_controlador(controlador) #Establecemos el controlador para la vista

#Programa principal
if __name__ == '__main__':
    app = vista
    # el set_mostrar instancia a vista que a su vez es la primera
    # funcion constructora de la VIEW
    app.set_mostrar()
    
# nota: para mostrar y hacer pruebas en sus respectivos archivos
# se debe de instanciar dichos archivos, por otra parte realizar 
# desde el mismo Vista para no usar instancias