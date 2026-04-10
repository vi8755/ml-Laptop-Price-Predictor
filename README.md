# 💻 Smart Laptop Price Predictor

⭐ If you like this project, give it a star on GitHub!

An end-to-end Machine Learning web application that predicts laptop prices based on user-selected specifications like RAM, CPU, GPU, storage, and more.

---

## 🚀 Features

- 🎯 Predict laptop price based on custom requirements  
- 💻 Interactive UI built with React  
- ⚡ Real-time predictions using Flask API  
- 🧠 ML model trained on real-world dataset (Kaggle)  
- 🔍 Helps users choose laptops according to budget  

---

## 🛠 Tech Stack

**Frontend:**
- React.js  

**Backend:**
- Flask  

**Machine Learning:**
- Scikit-learn  
- Pandas  
- NumPy  

---

## 🤖 Machine Learning Model

- Multiple algorithms were tested  
- Final model selected based on **best R² Score**  
- Model trained on Kaggle dataset  

---

## 📊 Dataset

- Source: Kaggle  
- Contains laptop specifications like:
  - Company  
  - RAM  
  - CPU  
  - GPU  
  - Storage  
  - Display (PPI, IPS, Touchscreen)  

---

## 📸 Screenshots

<img width="1876" height="815" alt="Screenshot 2026-04-10 163426" src="https://github.com/user-attachments/assets/2a7d7bac-8a2b-4c26-abe2-6427c48eae42" />
<img width="1859" height="804" alt="Screenshot 2026-04-10 163443" src="https://github.com/user-attachments/assets/7b240492-9caf-4e54-a149-61f7e06ead4e" />

---

## ▶️ Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/vi8755/ml-Laptop-Price-Predictor.git
```
### 2. Backend setup
```bash
cd backend
pip install -r requirements.txt
python app.py
```
### 3. Frontend setup
```bash
cd frontend
npm install
npm start
```
## 📈 Performance
- Model evaluated using R² Score
- Best model selected after comparing multiple algorithms

## 🔮 Future Improvements
- 🌐 Deploy project online (Render / Vercel)
- 📊 Improve model accuracy with more data
- 🎨 Enhance UI/UX
