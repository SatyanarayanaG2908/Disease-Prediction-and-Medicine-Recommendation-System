# 🩺 Disease Prediction and Medicine Recommendation System  

## 🚀 Overview  
The **Disease Prediction and Medicine Recommendation System** is an intelligent healthcare project designed to **predict diseases based on user-input symptoms** and **recommend suitable medicines**.  
It combines **Machine Learning** and **Healthcare Analytics** to provide accurate and interpretable medical insights.  

This system integrates multiple models — **Random Forest**, **SVM**, and **Gradient Boosting** — through an **ensemble voting mechanism** to achieve superior prediction performance.  

---

## 🧠 Key Features  
✨ Predicts disease based on multiple symptoms entered by the user  
✨ Ensemble learning (Random Forest + SVM + Gradient Boosting) for higher accuracy  
✨ Medicine recommendation system linked with disease prediction  
✨ Confidence score for predictions  
✨ Data preprocessing, feature encoding, and model evaluation  
✨ Interactive web integration-ready backend  

---

## 📂 Dataset Description  
The project uses a **symptom–disease dataset** where each row represents a combination of symptoms leading to a disease diagnosis.  

### Example Columns:
- `itching`, `skin_rash`, `joint_pain`, ... (symptom columns)
- `prognosis`: the target label (disease name)

### Dataset Highlights:
- Contains around **130+ disease types**  
- Each disease is mapped with **relevant symptoms**  
- Data is preprocessed to ensure clean, balanced input for ML models  

---

## 🧹 Data Preprocessing Steps  
1. Imported the dataset using **Pandas**  
2. Encoded categorical labels using **LabelEncoder**  
3. Handled missing values and duplicate entries  
4. Split the data into **train** and **test** sets using `train_test_split()`  
5. Standardized feature input for SVM and Gradient Boosting models  

---

## 🧩 Machine Learning Models Used  

| Model | Description | Key Strength |
|:------|:-------------|:--------------|
| **Random Forest Classifier** | Ensemble of decision trees | Handles feature interactions & non-linear data |
| **Support Vector Machine (SVM)** | Finds optimal hyperplane | High performance for complex classification |
| **Gradient Boosting Classifier** | Sequential ensemble learning | Reduces bias and variance |
| **Voting Classifier** | Combines outputs of above models | Produces final robust prediction |

✅ The final prediction is generated through **majority voting** across all three models.  

---

## 📊 Model Evaluation  
The models were evaluated using:  
- **Accuracy Score**  
- **Confusion Matrix**  
- **Classification Report (Precision, Recall, F1)**  
- **Cross-Validation Score**  

Average ensemble accuracy achieved: **~97-99%**, depending on dataset splits.  

---

## 💊 Medicine Recommendation  
Each predicted disease is mapped to its respective **set of recommended medicines** from a curated dictionary or CSV mapping file.  
Example:  

| Disease | Recommended Medicines |
|:--------:|:----------------------|
| Diabetes | Metformin, Glimepiride, Insulin |
| Hypertension | Amlodipine, Lisinopril |
| Migraine | Sumatriptan, Naproxen |

---

## ⚙️ Technologies Used  
- **Python 3.10+**  
- **NumPy**  
- **Pandas**  
- **Scikit-learn**  
- **Matplotlib / Seaborn** (for visualization)  
- **Streamlit / Flask (optional)** for frontend deployment  

---

## 🧪 How to Run  

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/Disease-Prediction-and-Medicine-Recommendation.git
   cd Disease-Prediction-and-Medicine-Recommendation
