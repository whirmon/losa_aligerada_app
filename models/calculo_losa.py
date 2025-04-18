class CalculoLosa:
    """Modelo para cálculos de losa aligerada"""
    
    def __init__(self):
        self._ancho = 0.0
        self._largo = 0.0
        self._espesor = 0.15  # Valor por defecto 15cm
        self._carga_viva = 200  # kg/m2 por defecto
        self._carga_muerta = 100  # kg/m2 por defecto
    
    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, value):
        self._ancho = float(value)
    
    @property
    def largo(self):
        return self._largo
    
    @largo.setter
    def largo(self, value):
        self._largo = float(value)
    
    @property
    def espesor(self):
        return self._espesor
    
    @espesor.setter
    def espesor(self, value):
        self._espesor = float(value)
    
    @property
    def carga_viva(self):
        return self._carga_viva
    
    @carga_viva.setter
    def carga_viva(self, value):
        self._carga_viva = float(value)
    
    @property
    def carga_muerta(self):
        return self._carga_muerta
    
    @carga_muerta.setter
    def carga_muerta(self, value):
        self._carga_muerta = float(value)
    
    def calcular_area(self):
        return self.ancho * self.largo
    
    def calcular_volumen(self):
        return self.calcular_area() * self.espesor
    
    def calcular_carga_total(self):
        return self.carga_viva + self.carga_muerta
    
    def calcular_numero_viguetas(self, separacion=0.5):
        """Calcula el número de viguetas necesarias"""
        return int(self.ancho / separacion) + 1
    
    def calcular_peso_total(self, peso_unitario=1800):
        """Calcula el peso total en kg (peso_unitario en kg/m3)"""
        return self.calcular_volumen() * peso_unitario