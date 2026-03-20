# ⚽ XScouting: Intelligent Football Analytics Engine

Este repositorio contiene el ecosistema completo de herramientas de **Data Scouting** y **Deep Learning** aplicadas al fútbol profesional. 

## 🏗️ Estructura del Proyecto

* **`/python`**: Pipeline de ingeniería de datos. Desde el scraping de portales oficiales hasta la creación de Dashboards interactivos.
* **`/pytorch`**: Motores de Inteligencia Artificial. Implementación de redes neuronales profundas con PyTorch para predicción de valor y rendimiento.

## 📈 Roadmap & Progreso

### **Fase 1: Data Engineering & ML Clásico (100% ✅)**
* **Scraping Pro**: Extracción de datos en tiempo real de LaLiga y Transfermarkt.
* **Analytics**: Procesamiento con Pandas y visualización de radares de rendimiento.
* **Machine Learning**: Clasificadores KNN y persistencia de modelos (.pkl).
* **Dashboard**: Interfaz de usuario con Streamlit para ojeadores.

### **Fase 2: Deep Learning con PyTorch (100% ✅)**
* **Arquitecturas Profundas**: Diseño de redes neuronales multicapa con funciones de activación ReLU para capturar relaciones no lineales en el mercado.
* **Optimización Avanzada**: Implementación de algoritmos Adam y descenso de gradiente para el ajuste preciso de pesos.
* **Big Data Ready**: Uso de `DataLoaders` y `TensorDatasets` para el procesamiento eficiente de grandes volúmenes de jugadores mediante minibatches.
* **Clasificación Táctica**: Motores de inferencia multiclase capaces de asignar roles (Muro, Motor, Finalizador) basados en KPIs de rendimiento.

### **Fase 3: Computer Vision - Tactical Video Analysis (En progreso ⏳)**
* [ ] **Nivel 17**: Implementación de **YOLO** para detección de futbolistas, árbitros y balón en clips de vídeo.
* [ ] **Nivel 18**: Algoritmos de seguimiento (**Object Tracking**) para asignar IDs únicos y mapear el movimiento.
* [ ] **Nivel 19**: Transformación de perspectiva (Homografía) para convertir vista de TV en mapa 2D.
* [ ] **EXAMEN CV**: Generación de **Heatmaps** automáticos basados puramente en análisis de vídeo.

## 🚀 Próximos Módulos de Especialización

### **Fase 4: Análisis de Series Temporales**
* Redes recurrentes (**LSTM**) para predecir cuándo un jugador necesita rotación por fatiga.
* Modelado de probabilidad de gol (Expected Goals - xG) avanzado.

### **Fase 5: Large Language Models**
* Integración con APIs de **Gemini/OpenAI** para automatizar reportes de ojeo.
* Creación de un asistente virtual táctico con conocimiento del historial del club.

## 🛠️ Stack Tecnológico
* **Lenguaje**: Python 3.11+
* **IA/ML**: PyTorch, Scikit-Learn, OpenCV, Ultralytics (YOLO).
* **Data**: Pandas, BeautifulSoup4, Requests.
* **UI**: Streamlit.