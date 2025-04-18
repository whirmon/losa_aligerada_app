import sys
from PySide6.QtWidgets import QApplication
from viewmodels.main_vm import MainViewModel
from views.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    
    # Configurar MVVM
    viewmodel = MainViewModel()
    window = MainWindow(viewmodel)
    
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()