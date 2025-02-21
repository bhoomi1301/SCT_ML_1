# 🏡 House Price Prediction using Machine Learning & Flask

## 📌 Project Overview
This project predicts house prices based on various features such as square footage, number of bathrooms, and year built. It uses **Ridge Regression** for model training and serves predictions through a **Flask web application**.

---

## 🚀 Technologies Used
- **Python** (Data Processing & Model Training)
- **Pandas, NumPy** (Data Handling)
- **Scikit-Learn** (Machine Learning Model)
- **Flask** (Web Framework)
- **HTML, CSS** (Frontend)

---

## 📂 Project Structure
```
📁 house-price-predictor/
│── 📂 static/                # CSS & Images
│   ├── style.css            # Styles for index.html
│   ├── style1.css           # Styles for result.html
│   ├── background.png       # Background image for index.html
│── 📂 templates/             # HTML Files
│   ├── index.html           # Input Page
│   ├── result.html          # Prediction Output Page
│── 📂 model/                 # Machine Learning Model
│   ├── ridge_model.pkl      # Trained Ridge Regression Model
│   ├── scaler.pkl           # Standard Scaler for Data Normalization
│── app.py                   # Flask Web Application
│── requirements.txt         # Required Libraries
│── README.md                # Project Documentation
```

---

## 📊 Dataset
The model is trained on **Ames Housing Dataset**, which contains features such as:
- **GrLivArea** (Above ground living area)
- **BedroomAbvGr** (Number of bedrooms above ground)
- **TotalBathrooms** (Full + Half Baths)
- **TotalSF** (Total Square Footage)
- **HouseAge** (Years since built)

---

## ⚙️ Installation & Setup
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/house-price-predictor.git
cd house-price-predictor
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the Flask App**
```sh
python app.py
```
Visit **http://127.0.0.1:5000/** in your browser.

---

## 🖥️ How It Works
1️⃣ **Enter House Features** ➝ 2️⃣ **Model Predicts the Price** ➝ 3️⃣ **Displays Result**

---

## 📸 Screenshots
### **🏡 Input Page**
![Input Page](static/background.png)

### **💰 Prediction Output**
![Result Page](static/result_page.png)

---

## 📝 Future Improvements
✅ Improve UI with Bootstrap 🖌️  
✅ Add More Machine Learning Models 🤖  
✅ Deploy on Cloud (AWS/Heroku) ☁️  

---

## 💡 Contributing
Feel free to **fork** this repository, make improvements, and submit a **pull request**! 🚀

---

## 🏅 Acknowledgements
Dataset Source: [Ames Housing Dataset](https://www.kaggle.com/datasets)

📩 Connect with me on [LinkedIn](https://www.linkedin.com/in/bhoomikans/)
