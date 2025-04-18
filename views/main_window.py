from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QFormLayout, QLabel, QDoubleSpinBox
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, viewmodel):
        super().__init__()
        self.viewmodel = viewmodel
        self.setWindowTitle("Calculadora de Losas Aligeradas")
        self.setMinimumSize(400, 500)
        
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        layout = QVBoxLayout(central_widget)
        
        # Formulario de entrada
        form_layout = QFormLayout()
        
        # Campos de entrada
        self.spin_ancho = QDoubleSpinBox()
        self.spin_ancho.setRange(0.1, 100.0)
        self.spin_ancho.setSuffix(" m")
        self.spin_ancho.setSingleStep(0.1)
        self.spin_ancho.valueChanged.connect(self.viewmodel.actualizar_ancho)
        
        self.spin_largo = QDoubleSpinBox()
        self.spin_largo.setRange(0.1, 100.0)
        self.spin_largo.setSuffix(" m")
        self.spin_largo.setSingleStep(0.1)
        self.spin_largo.valueChanged.connect(self.viewmodel.actualizar_largo)
        
        self.spin_espesor = QDoubleSpinBox()
        self.spin_espesor.setRange(0.1, 0.5)
        self.spin_espesor.setSuffix(" m")
        self.spin_espesor.setSingleStep(0.05)
        self.spin_espesor.setValue(0.15)
        self.spin_espesor.valueChanged.connect(self.viewmodel.actualizar_espesor)
        
        self.spin_carga_viva = QDoubleSpinBox()
        self.spin_carga_viva.setRange(50, 1000)
        self.spin_carga_viva.setSuffix(" kg/m²")
        self.spin_carga_viva.setValue(200)
        self.spin_carga_viva.valueChanged.connect(self.viewmodel.actualizar_carga_viva)
        
        self.spin_carga_muerta = QDoubleSpinBox()
        self.spin_carga_muerta.setRange(50, 1000)
        self.spin_carga_muerta.setSuffix(" kg/m²")
        self.spin_carga_muerta.setValue(100)
        self.spin_carga_muerta.valueChanged.connect(self.viewmodel.actualizar_carga_muerta)
        
        # Añadir campos al formulario
        form_layout.addRow("Ancho:", self.spin_ancho)
        form_layout.addRow("Largo:", self.spin_largo)
        form_layout.addRow("Espesor:", self.spin_espesor)
        form_layout.addRow("Carga Viva:", self.spin_carga_viva)
        form_layout.addRow("Carga Muerta:", self.spin_carga_muerta)
        
        # Sección de resultados
        self.label_area = QLabel("0.0 m²")
        self.label_volumen = QLabel("0.0 m³")
        self.label_carga_total = QLabel("0.0 kg/m²")
        self.label_num_viguetas = QLabel("0")
        self.label_peso_total = QLabel("0.0 kg")
        
        form_layout.addRow("Área:", self.label_area)
        form_layout.addRow("Volumen:", self.label_volumen)
        form_layout.addRow("Carga Total:", self.label_carga_total)
        form_layout.addRow("Número de Viguetas:", self.label_num_viguetas)
        form_layout.addRow("Peso Total:", self.label_peso_total)
        
        layout.addLayout(form_layout)
        
        # Conectar señales del ViewModel
        self.viewmodel.calculosActualizados.connect(self.actualizar_resultados)
    
    def actualizar_resultados(self, resultados):
        self.label_area.setText(f"{resultados['area']:.2f} m²")
        self.label_volumen.setText(f"{resultados['volumen']:.2f} m³")
        self.label_carga_total.setText(f"{resultados['carga_total']:.2f} kg/m²")
        self.label_num_viguetas.setText(f"{resultados['numero_viguetas']}")
        self.label_peso_total.setText(f"{resultados['peso_total']:.2f} kg")