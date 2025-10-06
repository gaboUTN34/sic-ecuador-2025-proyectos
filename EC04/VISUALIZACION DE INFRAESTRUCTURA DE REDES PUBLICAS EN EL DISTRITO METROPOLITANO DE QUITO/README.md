# 📌 <VISUALIZACION_DE_INFRAESTRUCUTURA_DE_REDES_PUBLICAS_EN_EL_DISTRITO_METROPOLITANO_DE_QUITO>

**Curso:** Samsung Innovation Campus – Módulo de Python (Ecuador 2025)  
**Seccion:** EC04  
**Carpeta:** `/EC04/VISUALIZACION DE INFRAESTRUCTURA DE REDES PUBLICAS EN EL DISTRITO METROPOLITANO DE QUITO`

---

## 👥 Integrantes del Grupo
- Mario Anrrango
- Adriana Padilla
- Diego Montesdeoca
- Gabriel Andrade
- Camilo Vasquez 

---

## 📝 Descripción del Proyecto
Este proyecto es un programa de visualización y análisis de los puntos WiFi municipales del Distrito Metropolitano de Quito el cual facilita el acceso a información de conectividad pública con el propósito de identificar brechas de cobertura y optimizar recursos beneficiando a ciudadanos sin acceso a datos móviles y conexión a internet.

## ⚙️ Instrucciones de Instalación y Ejecución

### Requisitos
- Python 3.13.7 (recomendado)
- Git

### Pasos
1. Clonar el repositorio (o asegurarse de estar en la carpeta del proyecto):
   ```bash
   git clone <(https://github.com/fundestpuente/sic-ecuador-2025-proyectos.git)>
   cd <EC04/VISUALIZACION DE INSFRAESTRUCTURA DE REDES PUBLICAS EN EL DISTRITO METROPOLITANO DE QUITO>   # ej: cd ecuador03/proyecto-01-nombre
   ```

2. Actualizar pip e instalar dependencias:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. Ejecutar la aplicación:
   ```bash
   python dashboard_main.py
   ```

Nota: después de ejecutar la aplicación, abrir el dashboard accediendo a:
http://127.0.0.1:8050/

4. Ejecutar pruebas (si aplica):
   ```bash
   pytest
   ```

---

## 📂 Estructura del proyecto:
```
VISUALIZACION DE INFRAESTRUCTURA DE REDES PUBLICAS EN EL DISTRITO METROPOLITANO DE QUITO/
├── 📂 estadisticas/
│   ├── 📂 resultados                            # Carpeta que contiene los resultados estadísticos.
│   │   ├── cobertura_prioritaria.csv            # Declara como módulo a la carpeta para utilizar sus datos.
│   │   └── estadisticas_basicas.csv             # Declara como módulo a la carpeta para utilizar sus datos.
│   ├── __init__.py                              # Declara como módulo a la carpeta para utilizar sus datos.
│   ├── basic_stats.py                           # Script para calcular las estadísticas básicas.
│   └── coverage_calc.py                         # Script para calcular la cobertura prioritaria.
├── 📂 manejo_de_datos/
│   ├── __init__.py                              # Declara como módulo a la carpeta para utilizar sus datos.   
│   ├── datos_procesados.py                      # Script de procesamiento de los datos.
│   ├── extraccion_datos.py                      # Script de extracción de los datos desde la API.
│   ├── zonas_puntos_wifi.csv                    # Archivo CSV con los datos de la API (zonas wifi).
│   └── zonas_puntos_wifi_procesados.csv         # Archivo CSV con los datos procesados de las zonas wifi.
├── 📂 visualizacion/
│   ├── __init__.py                              # Declara como módulo a la carpeta para utilizar sus datos.              
│   └── visualizador.py                          # Gráficos de los resultados y mapa.
├── dashboard_main.py                            # Aplicación principal (dashboard)
├── requirements.txt                             # Dependencias del proyecto
└── README.md                                    # Este archivo.
```

---

## ✅ Herramientas Implementadas
- **Lenguaje:** Python 3.13.x
- **Librerías principales:** `<pandas, numpy, requests, matplotlib, seaborn, folium, dash, scipy>`
- **Otras herramientas:** `<pytest>`

---

## 💡 Buenas prácticas y reglas internas
- Trabajar únicamente dentro de la carpeta asignada al grupo.
- Realizar commits claros, por ejemplo: `feat: agrega función X`, `fix: corrige bug en Y`, `docs: actualiza README`.
- Mantener el README del proyecto actualizado con cambios importantes.
