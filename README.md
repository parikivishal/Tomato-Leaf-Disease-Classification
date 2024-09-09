# Tomato Leaf Disease Classification



## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Model Architecture](#model-architecture)
- [Flask Application](#flask-application)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

Tomato is one of the most widely cultivated crops worldwide, but its production is often threatened by various leaf diseases. Early and accurate detection of these diseases is crucial for effective management and prevention of significant yield losses. This project leverages Convolutional Neural Networks (CNN) to classify tomato leaf diseases, providing an automated tool for farmers and agronomists to monitor plant health.

## Dataset

The dataset used in this project is sourced from Kaggle and contains images of healthy and diseased tomato leaves categorized into different classes based on the type of disease.

- **Dataset Link:** [Tomato Leaf Dataset](https://www.kaggle.com/datasets/kaustubhb999/tomatoleaf)

### Dataset Description

- **Classes:** The dataset includes images of various tomato leaf diseases such as Leaf Mold, Bacterial Spot, Early Blight, etc., along with healthy leaves.
- **Number of Images:** Approximately 10,000 images.
- **Image Resolution:** Varies, preprocessed to a standard size for model training.



## Model Architecture

The classification model is built using a Convolutional Neural Network (CNN), which is highly effective for image classification tasks. The architecture includes:

- **Input Layer:** Processes images resized to 224x224 pixels with 3 color channels (RGB).
- **Convolutional Layers:** Multiple convolutional layers with ReLU activation and max-pooling to extract features.
- **Fully Connected Layers:** Dense layers that interpret the extracted features for classification.
- **Output Layer:** Softmax activation function to output probability distribution over the disease classes.

### Model Training

- **Framework:** TensorFlow/Keras
- **Optimizer:** Adam
- **Loss Function:** Categorical Crossentropy
- **Metrics:** Accuracy
- **Epochs:** [Specify number]
- **Batch Size:** [Specify size]

## Flask Application

A user-friendly Flask web application is integrated into the project to provide an interface for uploading tomato leaf images and receiving disease classification results in real-time.

### Features

- **Image Upload:** Users can upload images of tomato leaves.
- **Prediction:** The app processes the image and displays the predicted disease.
- **User Interface:** Simple and intuitive UI built with HTML, CSS, and Bootstrap.

## Installation

Follow the steps below to set up the project locally.

### Prerequisites

- **Python 3.7 or higher**
- **pip (Python package manager)**
- **Git**

### Step 1: Clone the Repository

```bash
git clone https://github.com/parikivishal/tomato-leaf-disease-classification.git
cd tomato-leaf-disease-classification
```

### Step 2: Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv

venv\Scripts\activate
```
### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```
### Step 4: Download the Dataset
- Go to the Tomato Leaf Dataset on Kaggle.
- Click on the "Download" button to get the dataset.
- Extract the downloaded files and place them in the dataset/ directory of the project.
  
### Step 5: Train the CNN Model

```bash
start jupyter notebook
```
- Run the Tomato Leaf Disease Classification.ipynb

### Step 6:  Run the Flask Application
```bash
python app.py
```
## Usage
- Access the Web App: Navigate to http://127.0.0.1:5000/ in your browser.
- Upload Image: Click on the "Choose File" button to upload an image of a tomato leaf.
- View Prediction: After uploading, the app will display the predicted disease category along with the probability score.






