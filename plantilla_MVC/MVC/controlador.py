from MVC.modelo import Modelo

class Controlador():
    def __init__(self, modelo):
        self.modelo = modelo

    def read(self):
        info = self.modelo.obtener_datos()
        # print(info) aca para probar
        return info


    

# esto para la instancia al modelo para realizar pruebas
modelo = Modelo()
controlador = Controlador(modelo)
controlador.read() #ojo cambiar funcion de mostrar



# -----------------------------------------------------------
    # controlador de muestra
    # def insertar_orden(self, id_orden, fec_orden, id_cliente):
    #     result = self.modelo.Insert(id_orden, fec_orden, id_cliente)
    #     return result