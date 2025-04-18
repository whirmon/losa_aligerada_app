from PySide6.QtCore import QObject, Signal, Slot
from models.calculo_losa import CalculoLosa

class MainViewModel(QObject):
    calculosActualizados = Signal(dict)
    
    def __init__(self):
        super().__init__()
        self.modelo = CalculoLosa()
    
    @Slot(float)
    def actualizar_ancho(self, value):
        self.modelo.ancho = value
        self._emitir_resultados()
    
    @Slot(float)
    def actualizar_largo(self, value):
        self.modelo.largo = value
        self._emitir_resultados()
    
    @Slot(float)
    def actualizar_espesor(self, value):
        self.modelo.espesor = value
        self._emitir_resultados()
    
    @Slot(float)
    def actualizar_carga_viva(self, value):
        self.modelo.carga_viva = value
        self._emitir_resultados()
    
    @Slot(float)
    def actualizar_carga_muerta(self, value):
        self.modelo.carga_muerta = value
        self._emitir_resultados()
    
    def _emitir_resultados(self):
        resultados = {
            'area': self.modelo.calcular_area(),
            'volumen': self.modelo.calcular_volumen(),
            'carga_total': self.modelo.calcular_carga_total(),
            'numero_viguetas': self.modelo.calcular_numero_viguetas(),
            'peso_total': self.modelo.calcular_peso_total()
        }
        self.calculosActualizados.emit(resultados) 