# 📄 Chatbot de Consulta de Currículum Vitae (CV) con Agentes

Este proyecto es un **chatbot interactivo** desarrollado con **Streamlit** que permite cargar **3 Currículums Vitae (CVs)** desde un directorio local, almacenarlos en **bases de datos vectoriales separadas** en **Pinecone**, y realizar consultas de forma dinámica utilizando un **Large Language Model (LLM)**, en este caso, **Llama 3 8B de Groq**.  

El objetivo principal es permitir una interacción ágil y eficiente con la información de múltiples CVs, proporcionando respuestas precisas a partir de preguntas en lenguaje natural.  

---

## 🚀 **Funcionalidades Principales**  

- **Carga de CVs**: El usuario puede subir 3 archivos de CV desde un directorio local.  
- **Vectorización de cada CV**: Cada CV se convierte en vectores y se almacena en una **base de datos vectorial separada** en **Pinecone**, permitiendo consultas específicas sobre cada uno de los CVs.  
- **Consultas sobre los CVs**: El usuario puede realizar preguntas personalizadas sobre el contenido de los CVs, como:  
  - _"¿En qué proyectos ha trabajado Claudia Ibañez?"_  
  - _"¿Cuántos años de experiencia tiene en Python la persona del CV de Juan?"_  
  - _"¿Qué certificaciones posee el candidato que cargué primero?"_  
- **IA para Consultas**: Utiliza una **LLM de Groq (Llama 3 8B)** para interpretar las preguntas y buscar la respuesta relevante en la base vectorial correspondiente.  
- **Consulta por Defecto**: Si la pregunta no especifica a cuál CV se refiere, se tomará por **defecto el de Claudia Ibañez**.  

---

## 🛠️ **Tecnologías Utilizadas**  

| **Tecnología**    | **Uso**                         |
|-------------------|---------------------------------|
| **Streamlit**     | Interfaz gráfica (UI) del chatbot |
| **Pinecone**      | Base de datos vectorial para almacenar los CVs |
| **Groq (Llama 3 8B)** | LLM para procesamiento y comprensión de texto |
| **Python**        | Lenguaje principal del proyecto |

---

## 📦 **Instalación**  

1️⃣ **Clonar el repositorio**  
```bash
git clone https://github.com/crisdavico/CEIA-LLMIAG-TP2.git
cd CEIA-LLMIAG-TP2
```

2️⃣ **Crear un entorno virtual**  
```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: .\venv\Scripts\activate
```

3️⃣ **Instalar las dependencias**  
```bash
pip install -r requirements.txt
```

4️⃣ **Configurar las claves de acceso**  
- **Pinecone API Key**: Necesitas crear una cuenta en [Pinecone.io](https://www.pinecone.io/) y obtener la clave API.  
- **Groq API Key**: Configura la clave para utilizar la LLM **Llama 3 8B**.  

Para facilitar la configuración, puedes crear un archivo `.env` en la raíz del proyecto:  
```
PINECONE_API_KEY=tu_api_key_aqui
GROQ_API_KEY=tu_api_key_aqui
```

Asegúrate de que tu entorno de desarrollo pueda leer variables de entorno.  

---

## ▶️ **Ejecución de la Aplicación**  

Para iniciar la aplicación, ejecuta:  
```bash
streamlit run main.py
```

Accede a la aplicación desde tu navegador en la URL **http://localhost:8501**.  

---

## 📚 **Uso de la Aplicación**  

**Realizar consultas**  
- Escribe preguntas relacionadas con los CVs en la interfaz.  
- Si no especificas a cuál CV se refiere la pregunta, el sistema tomará por **defecto el de Claudia Ibañez**.  
- Las respuestas se generarán en tiempo real mediante la LLM **Llama 3 8B**.  

Ejemplos de preguntas:  
- _"¿Cuáles son las habilidades técnicas más destacadas?"_ (se usará el CV de Claudia Ibañez)  
- _"¿Cuánto tiempo trabajó en su último empleo Joaquin?"_  
- _"¿Qué tipo de certificaciones posee Sergio?"_  

---

## 📈 **Flowchart del Proceso**  

En el repositorio se encuentra en formato de imagen el Flowchart de los distintos Agentes


---

## 📺 **Video Explicativo**  

En el repositorio se encuentra un video que muestra como funciona la aplicación.

---

## ⚙️ **Configuración Adicional**  

- **Personalización de la LLM**: Puedes cambiar el tamaño del modelo o modificar el prompt que se envía a la LLM.  
- **Almacenamiento en Pinecone**: Puedes ajustar la configuración de la base vectorial para almacenar más de 3 CVs o controlar el espacio de nombres (namespaces) para organizar la información.  

---

## 📜 **Requisitos Técnicos**  

- **Python 3.8 o superior**  
- **Acceso a Internet** (para la conexión con Pinecone y Groq)  
- **Claves API** de Pinecone y Groq  

---

## 🧠 **Conceptos Clave**  

### 🧮 **Vectorización**  
Cada CV se convierte en un vector para almacenarse en **Pinecone**, una base de datos vectorial. Cada oración, palabra o sección del CV se transforma en una representación numérica que permite realizar búsquedas de similitud de manera eficiente.  

### 🤖 **Modelo de Lenguaje Llama 3 8B (LLM)**  
El modelo Llama 3 8B es una red neuronal preentrenada que puede interpretar el lenguaje natural y generar respuestas. Usamos este modelo para comprender la pregunta del usuario y buscar la respuesta adecuada en la base vectorial correcta.  

### 📡 **Pinecone**  
Pinecone es una base de datos vectorial que permite realizar búsquedas de similitud de alta velocidad. Este sistema se utiliza para almacenar y recuperar representaciones vectoriales de los CVs.  

---

## 🛠️ **Personalización**  

- **Customización de Pinecone**: Cambiar la cantidad de dimensiones en la vectorización.  
- **Cambio de LLM**: Sustitución de la LLM de Groq por otra, como OpenAI o modelos open-source.  
- **Prompt Tuning**: Modificación del prompt de la LLM para personalizar las respuestas.  

---

## 💡 **Problemas Frecuentes**  

**1️⃣ Error de conexión con Pinecone**  
- Verifica la API Key de Pinecone.  
- Asegúrate de que el namespace esté configurado correctamente.  

**2️⃣ La LLM no responde correctamente**  
- Revisa la configuración del prompt.  
- Verifica la clave de API de Groq y su límite de uso.  

---

## ✉️ **Contacto**  

Si tienes preguntas o deseas colaborar, no dudes en contactarme a través de [crisdavico95@gmail.com](https://github.com/crisdavico/CEIA-LLMIAG-TP2).  

---

¡Gracias por usar el Chatbot de Consulta de CV! 🚀  

---

Si deseas realizar ajustes o agregar detalles adicionales, como el link al video o el flowchart, avísame y lo actualizaré.