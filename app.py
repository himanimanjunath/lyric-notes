from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from text_extraction import extract_text_from_pdf
from summarization import summarize_text
from lyrics_generation import generate_lyrics

# Check if PyTorch, TensorFlow, or Flax is installed
try:
    import torch
    backend = "PyTorch"
except ImportError:
    try:
        import tensorflow as tf
        backend = "TensorFlow"
    except ImportError:
        try:
            import flax
            backend = "Flax"
        except ImportError:
            raise ImportError(
                "None of PyTorch, TensorFlow >= 2.0, or Flax have been found. "
                "Please install one of these backends to use models."
            )

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Extract text from PDF
        text = extract_text_from_pdf(filepath)
        if not text:
            return "Error: No text could be extracted from the PDF.", 400
        
        # Summarize text
        try:
            summary = summarize_text(text)
        except Exception as e:
            return f"Error during summarization: {str(e)}", 500
        
        # Generate lyrics
        lyrics = generate_lyrics(summary)
        
        return render_template('lyrics.html', lyrics=lyrics)

if __name__ == '__main__':
    # Create uploads folder if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Run the app on port 5001
    app.run(debug=True, port=5001)