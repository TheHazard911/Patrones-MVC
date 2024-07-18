class Vista:
    def __init__(self):
        self.controlador = None

    def set_controlador(self, controlador):
        self.controlador = controlador
    
    #A partir de aca se pueden incluir mas constructores y usarlos
    def set_mostrar(self):
        print("Aqui va la vista del programa!")
        # llamando al controlador
        self.mostrar_read()
        
    def mostrar_read(self):
        # en los constructores se muestra el print!
        # los print desde la vista
        print(self.controlador.read())