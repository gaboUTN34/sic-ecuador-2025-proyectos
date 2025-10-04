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

3. Ejecutar la aplicación (ejemplo):
   ```bash
   python main.py
   ```
   O, si es una aplicación web:
   ```bash
   uvicorn app.main:app --reload   
   ```
   Reemplaza los comandos anteriores por los específicos de tu proyecto.

4. Ejecutar pruebas (si aplica):
   ```bash
   pytest
   ```

---

## 📂 Estructura del proyecto:
```
VISUALIZACION DE INFRAESTRUCTURA DE REDES PUBLICAS EN EL DISTRITO METROPOLITANO DE QUITO/
├── 📂 analisis_de_datos/
│   ├── raw_data.py             # Descarga de la API
│   └── processed_data.py       # Limpieza de los datos
├── 📂 dashboard/                   
│   ├── basic_stats.py          # Estadísticas básicas
│   └── coverage_calc.py        # Cálculo de la cobertura WIFI
├── 📂 manejo_de_datos/                   
│   ├── datos_procesados.py     # Gráficos estáticos
│   └── extraccion_datos.py     # Mapas interactivos
├── 📂 visualizacion/                   
│   └── visualizador.py         # Dashboard para mostrar los datos
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Este archivo.
```

---

## ✅ Herramientas Implementadas
- **Lenguaje:** Python 3.13.x
- **Librerías principales:** `<pandas, numpy, flask, fastapi, matplotlib, etc.>` (lista → reemplazar)
- **Otras herramientas:** `<Docker, GitHub Actions (CI), pytest, etc.>` (lista → reemplazar)

---

## 💡 Buenas prácticas y reglas internas
- Trabajar únicamente dentro de la carpeta asignada al grupo.
- Commits claros: `feat: agrega función X`, `fix: corrige bug en Y`, `docs: actualiza README`.
- Mantener el README del proyecto actualizado con cambios importantes.
