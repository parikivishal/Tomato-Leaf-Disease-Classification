import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
import tensorflow as tf
from PIL import Image
import numpy as np

app = Flask(__name__)
app.secret_key = 'b9f2e7a4f8c3481bb0f5439aa1d87ef7'

# Load the pre-trained model
model = tf.keras.models.load_model('model/light_tomato.h5')

# Class names for diseases
class_names = {
    0: 'bacterial spot',
    1: 'early blight',
    2: 'late blight',
    3: 'leaf mold',
    4: 'Septoria',
    5: 'spider mites',
    6: 'target spot',
    7: 'yellow leaf',
    8: 'mosaic',
    9: 'healthy'
}

# Allowed file extensions for uploads
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Check if the uploaded file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username and password are 'admin'
        if username == 'admin' and password == 'admin':
            session['logged_in'] = True
            return redirect(url_for('dashboard'))  # Redirect to dashboard after login success
        else:
            flash('Invalid username or password. Please try again.')
            return redirect(url_for('login'))

    return render_template('login.html')

# Dashboard route (for disease classification)
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'logged_in' not in session:
        return redirect(url_for('login'))  # Redirect to login if not logged in

    if request.method == 'POST':
        # Check if a file is uploaded
        if 'file' not in request.files or request.files['file'].filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)

        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join('uploads', filename)
            os.makedirs('uploads', exist_ok=True)  # Ensure the 'uploads' folder exists
            file.save(filepath)

            # Preprocess the uploaded image for prediction
            img = Image.open(filepath).resize((256, 256))  # Resize to the model's expected size
            img_array = np.array(img) / 255.0  # Normalize
            img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

            # Predict using the loaded model
            predictions = model.predict(img_array)
            predicted_label = predictions.argmax(axis=-1)[0]

            # Get the disease class name
            predicted_disease = class_names.get(predicted_label, 'Unknown Disease')

            return render_template('dashboard.html', predicted_disease=predicted_disease)
        else:
            flash('Invalid file format. Please upload a PNG, JPG, or JPEG image.')
            return redirect(url_for('dashboard'))

    return render_template('dashboard.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You have been logged out successfully.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
