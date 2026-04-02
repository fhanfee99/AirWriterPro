# AI Air Writing App

- Hand gesture drawing
- Color selection
- Pinch erase
- Wave clear
- Built with OpenCV + MediaPipe
- 
# -----------------------------
# 1️⃣ Create Project Folder
# -----------------------------
mkdir "D:\Website, FULL STACK\Python\Airwriterpro"
cd "D:\Website, FULL STACK\Python\Airwriterpro"

# -----------------------------
# 2️⃣ Create Python Virtual Environment
# -----------------------------
python -m venv venv310
venv310\Scripts\activate   # Windows PowerShell

# -----------------------------
# 3️⃣ Upgrade pip (optional)
# -----------------------------
python -m pip install --upgrade pip

# -----------------------------
# 4️⃣ Install Required Packages
# -----------------------------
pip install opencv-python mediapipe==0.10.8 numpy

# -----------------------------
# 5️⃣ Create Python Files
# -----------------------------
# main file
notepad AirWriterPro_all_in_one.py
# (Paste full code here from provided AirWriterPro_all_in_one.py)

# -----------------------------
# 6️⃣ Run the Project
# -----------------------------
python AirWriterPro_all_in_one.py

# -----------------------------
# 7️⃣ Git Commands to Push Full Project
# -----------------------------
git init
echo venv/ > .gitignore
echo *.pyc >> .gitignore
echo __pycache__/ >> .gitignore
echo .DS_Store >> .gitignore

git add .
git commit -m "Initial commit: AirWriterPro full project"

# Remove old remote if exists
git remote remove origin

# Add your GitHub repo remote (replace USERNAME)
git remote add origin https://github.com/USERNAME/AirWriterPro.git

# Rename branch to main and push
git branch -M main
git push -u origin main

# -----------------------------
# 8️⃣ Controls in App
# -----------------------------
# 'c' → clear drawing
# 'q' → quit
# Hands in front of webcam → draw in air
# Color picker on right → select color
# Plasma effect on fingers automatically
