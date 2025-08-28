# 🐾 Cats vs Dogs Classifier

A simple **Flask web app** that uses a pre-trained deep learning model (TensorFlow/Keras) to classify uploaded images as either **Cat** or **Dog**.  
The app provides a clean UI built with **Bootstrap**, allowing users to upload an image, view the prediction, and see the uploaded image instantly.

---

## ✨ Features
- 📂 Upload an image (`.jpg`, `.jpeg`, `.png`) through the web UI.  
- 🤖 Deep learning model (CNN) trained to classify **Cats vs Dogs**.  
- 🖼️ Displays the uploaded image alongside the prediction.  
- 🎨 User-friendly interface with Bootstrap styling.  
- ⚡ Auto-clears uploaded files to keep the server clean.  

---

## 🚀 Tech Stack
- **Python 3.8+**
- **Flask** (for the web app)  
- **TensorFlow/Keras** (for deep learning model)  
- **Bootstrap 5** (for frontend styling)  

---

## 📂 Project Structure
```
cats-vs-dogs-classifier/
│
├── app.py                  # Main Flask application
├── models/
│   └── cats_dogs_model.h5  # Trained Keras model
├── static/
│   └── uploads/            # Stores uploaded images temporarily
├── templates/
│   └── index.html          # Frontend HTML template
└── README.md               # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/cats-vs-dogs-classifier.git
cd cats-vs-dogs-classifier
```

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Add your trained model
Place your trained Keras model (`cats_dogs_model.h5`) in the `models/` folder.  
*(You can train one using the Kaggle Cats vs Dogs dataset or use a pretrained one.)*

### 5️⃣ Run the Flask app
```bash
python app.py
```

App will be available at 👉 `http://127.0.0.1:5000/`

---

## 🖼️ Usage
1. Open the web app in your browser.  
2. Click **Choose File** and select a Cat or Dog image.  
3. Hit **Upload & Predict**.  
4. See the **prediction result** + the uploaded image on the page.  

---

## 📸 Demo
![Demo Screenshot](https://via.placeholder.com/700x400?text=Cats+vs+Dogs+Demo)

---

## 📦 Requirements
Add this in `requirements.txt`:
```
flask
tensorflow
numpy
```

*(Optional: add `gunicorn` if deploying to Heroku)*

---

## 🚀 Deployment
You can deploy this app on:
- **Heroku** (with `Procfile`)  
- **Render**  
- **AWS / GCP / Azure**  
- or host locally on your PC  

---

## 🛠️ Future Improvements
- ✅ Allow multiple image uploads at once  
- ✅ Add confidence score (%) for predictions  
- ✅ Support for more animal classes (not just cats & dogs)  
- ✅ Containerize with Docker  

---

## 👨‍💻 Author
Developed by Pratyay Patel 
