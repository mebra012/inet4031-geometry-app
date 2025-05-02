# INET4031 Geometry Calculator App

This is a Python Flask web application built for INET4031. It calculates the volume of two 3D shapes:

- Cylinders
- Spheres

## Features

✅ Web interface using Flask  
✅ HTML templates for input forms  
✅ Volume calculation using Python  
✅ Unit tests for sphere volume  
✅ Command-line mode for both shapes

---

## How to Run the App

```bash
# 1. Create and activate a virtual environment (optional but recommended)
python3 -m venv .venv
source .venv/bin/activate

# 2. Install Flask
pip install Flask

# 3. Run the Flask app
flask --app GeometryCalcWeb.py run --port=5001

# 4. Open your browser and go to:
# http://127.0.0.1:5001
