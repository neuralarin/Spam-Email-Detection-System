# Spam Email Detection System 📧

A **Machine Learning and NLP-based project** that helps users identify whether an email is **Spam or Ham (Legit)** before interacting with it.

## 🛡️ Industry Domain
**Cybersecurity**

## 🤨 Problem Statement
Users receive unwanted, suspicious, and potentially fraudulent emails every day. Identifying spam manually can be difficult and may expose users to scams, phishing attempts, or malicious content. An automated system can help users detect suspicious emails quickly.

## 🎯 Objective
Developed a machine learning-based system that analyzes email content and predicts whether an email is **Spam or Legit**, helping users make safer decisions before opening or interacting with suspicious messages.

## 🧠 Tech Stack
* **Python**
* **Pandas & NumPy**
* **Scikit-learn**
* **NLP**
* **Matplotlib & Seaborn**
* **Streamlit**

## 📊 Data Visualization
1. **Ham vs Spam email distribution**
<img src="https://github.com/neuralarin/Spam-Email-Detection-System/blob/main/images/1_ham_vs_spam_distributions.png" width="100%">

2. **Character distribution in data**
<img src="https://github.com/neuralarin/Spam-Email-Detection-System/blob/main/images/2_spam_vs_not_spam_character_distributions.png" width="100%">

3. **Word distribution in data**
<img src="https://github.com/neuralarin/Spam-Email-Detection-System/blob/main/images/3_spam_vs_not_spam_word_distributions.png" width="100%">

4. **Pairplot distribution of data**
<img src="https://github.com/neuralarin/Spam-Email-Detection-System/blob/main/images/4_pairplot_distributions.png" width="100%">

5. **Correlation heatmap of data**
<img src="https://github.com/neuralarin/Spam-Email-Detection-System/blob/main/images/5_correlation_heatmap.png" width="100%">

6. **Spam message word cloud**
<img src="https://github.com/neuralarin/Spam-Email-Detection-System/blob/main/images/6_spam_word_cloud.png" width="100%">

7. **Ham message word cloud**
<img src="https://github.com/neuralarin/Spam-Email-Detection-System/blob/main/images/7_ham_word_cloud.png" width="100%">

8. **Top 30 ham words in data**
<img src="https://github.com/neuralarin/Spam-Email-Detection-System/blob/main/images/8_top_30_ham_message.png" width="100%">

9. **Top 30 spam words in data**
<img src="https://github.com/neuralarin/Spam-Email-Detection-System/blob/main/images/9_top_30_spam_message.png" width="100%">


## 🤖 Machine Learning Models
* **Logistic Regression**
* **K-Nearest Neighbor**
* **Naive Bayes**
* **Support Vector Machine**
* **Random Forest**

## 🔄 Project Workflow

```text
Understanding Data
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Text Preprocessing
        ↓
Feature Extraction
        ↓
Baseline Model Training
        ↓
Precision-Based Hyperparameter Tuning
        ↓
F1-Score-Based Hyperparameter Tuning
        ↓
Final Model Selection
        ↓
Streamlit Deployment
        ↓
Spam / Legit Prediction
```

# ⚖️ Model Selection & Optimization

As spam detection involves a trade-off between **precision and recall**, the models were evaluated using different optimization objectives.

## Precision-Based Optimization

The first hyperparameter tuning process was done using **precision** to minimize false-positive spam classifications, where legit emails are incorrectly marked as spam.

### Selected Model: Support Vector Machine (SVM)

SVM provided a strong balance between precision and recall during precision-based optimization.

| Actual / Predicted | Predicted Ham | Predicted Spam |
| ------------------ | ------------: | -------------: |
| **Actual Ham**     |       **892** |          **4** |
| **Actual Spam**    |        **22** |        **116** |

### Key Observation

* Random Forest and KNN achieved **100% precision**, but their recall dropped significantly.
* Optimizing only for precision made some models too conservative and caused them to miss more spam emails.
* Therefore, precision alone was not sufficient for final model selection.

---

# F1-Score-Based Optimization

To achieve a better balance between **precision and recall**, The next hyperparameter tuning was performed using the **F1-score**.

### 🏆 Final Model: Random Forest

Random Forest achieved the best balance between precision and recall during F1-score-based optimization.

| Actual / Predicted | Predicted Legitimate | Predicted Spam |
| ------------------ | -------------------: | -------------: |
| **Actual Ham**     |              **889** |          **7** |
| **Actual Spam**    |               **13** |        **125** |

### Model Performance

| Metric        |      Score |
| ------------- | ---------: |
| **Precision** | **94.69%** |
| **Recall**    | **90.57%** |
| **F1-Score**  | **92.59%** |

### Interpretation

* **889** legit emails were correctly classified.
* **7** legit emails were incorrectly classified as Spam.
* **125** Spam emails were correctly detected.
* **13** Spam emails were missed.

# 📊 Precision vs Recall Trade-off

```text
Precision Optimization
        ↓
Fewer False Positives
        ↓
More Spam Emails Missed
        ↓
Lower Recall
        ↓
F1-Score Optimization
        ↓
Better Precision-Recall Balance
```

# 🏁 Conclusion
* Firstly, i performed hyperparameter tuning using **precision** to minimize false-positive spam classifications. But, precision-only optimization caused some models to have significantly lower recall. For example, Random Forest achieved **100% precision but only 15.9% recall** during this optimization.
* Then i performed hyperparameter tuning using **F1-score** to balance precision and recall. after F1-based optimization, **Random Forest** achieved **94.69% precision, 90.57% recall, and 92.59% F1-score** on the test data. based on this balance, **Random Forest was selected as the final model and deployed using Streamlit**.

# 🏭 Real-World Benefits
If integrated into an email platform, the system can automatically filter unwanted emails, reduce inbox junk, minimize incorrect spam classifications, save users' time, and provide an initial layer of protection against potentially suspicious messages.