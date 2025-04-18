# 🧱 Calculadora de Losas Aligeradas (Vigueta y Bovedilla)

Aplicación 🐍 **Python** con 🖥️ interfaz gráfica para el 📐 cálculo de 🧱 losas aligeradas utilizando el patrón 🧩 **MVVM** (Model-View-ViewModel).

---

## ✨ Características principales

- 📐 Cálculo de área, volumen y peso de losas aligeradas  
- 🧱 Determinación del número de viguetas necesarias  
- ⚖️ Cálculo de cargas (vivas y muertas)  
- 🖥️ Interfaz intuitiva con actualización en tiempo real  
- 🧩 Implementación con patrón MVVM para mejor mantenibilidad  

---

## 💻 Requisitos del sistema

- Python 3.8 o superior  
- `pip` (gestor de paquetes de Python)  

---

## ⚙️ Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/whirmon/losa_aligerada_app.git
cd losa_aligerada_app

```

2.  Crea y activa un entorno virtual (recomendado):
    

```bash
python -m venv venv

```

-   En **Windows**:
    
    ```bash
    venv\Scripts\activate
    
    ```
    
-   En **Linux/Mac**:
    
    ```bash
    source venv/bin/activate
    
    ```
    

3.  Instala las dependencias:
    

```bash
pip install -r requirements.txt

```

----------

## ▶️ Ejecución

```bash
python main.py

```

----------

## 📦 Dependencias (`requirements.txt`)

```
PySide6>=6.4.0

```

----------

## 🗂️ Estructura del proyecto

```
losa_aligerada_app/
├── models/         # Modelos de datos y lógica
├── viewmodels/     # ViewModels (intermediarios)
├── views/          # Vistas (interfaz de usuario)
├── resources/      # Recursos gráficos (opcional)
└── main.py         # Punto de entrada de la aplicación

```

----------

## 🧪 Uso

1.  Ingrese las **dimensiones de la losa** (ancho y largo en metros)
2.  Especifique el **espesor** (por defecto 0.15 m)
3.  Defina las **cargas vivas y muertas** (en kg/m²)
4.  Los **resultados se calcularán automáticamente** en la interfaz

----------

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Ver el archivo `LICENSE` para más detalles.  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

----------

## 🤝 Contribuciones

Las contribuciones son bienvenidas.  
Por favor abre un **issue** o un **pull request** para sugerencias o mejoras.

----------

## 🗺️ Roadmap (Plan de Desarrollo)

### 🚀 **Fase 1: Versión Básica (Actual)** ✅

-   ✅ Interfaz gráfica funcional con PySide6
-   ✅ Cálculo de dimensiones básicas (área, volumen)
-   ✅ Estimación del número de viguetas
-   ✅ Cálculo de cargas totales
    

### 🧠 **Fase 2: Mejoras de Cálculo** 🚧

-   🧩 Selección de materiales (peso específico)
-   📏 Cálculo de resistencia según normas (ACI, NTCM)
-   🔁 Opción para diferentes separaciones de viguetas
-   🛡️ Validación de datos con rangos realistas
    

### 📈 **Fase 3: Visualización y Exportación**

-   📊 Gráficos de distribución de cargas
-   📄 Reportes PDF/Excel
-   🖨️ Vista previa de impresión
-   📱 Diseño responsive
    

### 🧰 **Fase 4: Funcionalidades Avanzadas**

-   💾 Guardar/cargar proyectos (JSON)
-   🌐 Versión web (Flask)
-   💸 Cálculo de costos (precios unitarios)
-   🤖 Auto-completado de valores típicos según uso
    

----------

### 📆 Calendario Tentativo

| Versión | Contenido Principal |
|--|--|
| v1.0 | Versión básica MVP |
| v1.5 | Mejoras de cálculo |
| v2.0 | Exportación y visualización |

----------

## 👨‍🔧 Cómo Contribuir

¿Quieres ayudar? ¡Abre un **issue** o envía un **PR**!

🔨 **Áreas prioritarias**:
-   💡 Mejoras en cálculos estructurales
-   🎨 Diseño de interfaz más intuitiva
-   🌍 Traducciones (español/inglés)