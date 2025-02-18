# PFE_SmolVLM_and_Gaussian_Splatting_Mobile_2D_to_3D_Image_Transformation
# 📷 SmolVLM Image Description App  

Une application mobile Flutter qui utilise **SmolVLM** pour générer une description détaillée d'une image. L'application permet à l'utilisateur de choisir une image et d'envoyer la requête à un serveur FastAPI qui exécute **SmolVLM**.

---

## 📌 Fonctionnalités  
- 📸 **Sélectionner une image** depuis la galerie.  
- 🔄 **Envoyer l'image** à un serveur.  
- 📝 **Recevoir une description** détaillée de l'image générée par **SmolVLM**.  
- 🎯 **Déploiement simple** via FastAPI et Flutter.  

---

## 🏗️ **Technologies Utilisées**  
- **Flutter/Dart** → Application mobile  
- **FastAPI/Python** → Serveur backend  
- **SmolVLM** → Modèle d'analyse d'image  
- **Hugging Face Transformers** → Exécution du modèle  

---

## 🚀 **Installation et Configuration**  

### 1️⃣ **Pré-requis**  
Avant de commencer, assure-toi d'avoir installé :  
- [Flutter](https://flutter.dev/docs/get-started/install)  
- [Python 3.8+](https://www.python.org/downloads/)  
- [FastAPI](https://fastapi.tiangolo.com/)  

---

### 2️⃣ **Installation du Backend (FastAPI + SmolVLM)**  
1. **Cloner ce repository :**  
   ```bash
   git clone https://github.com/chamarb/PFE_SmolVLM_and_Gaussian_Splatting_Mobile_2D_to_3D_Image_Transformation.git
   cd PFE_SmolVLM_and_Gaussian_Splatting_Mobile_2D_to_3D_Image_Transformation

# SmolVLM and Gaussian Splatting: 2D to 3D Image Transformation

## Project Overview
This project transforms 2D images into 3D reconstructions using Gaussian Splatting and provides a detailed description of the image using SmolVLM.

## Steps to Run the Project
1. Clone the repository.
2. Set up the backend (Python server).
3. Set up the Flutter app on your mobile device.
4. Test the image upload and description feature.

## Backend
- The backend is implemented in Python and handles the communication with the SmolVLM API.

## Frontend
- The mobile frontend is developed in Flutter and handles image selection, communication with the SmolVLM API, and displaying results.

