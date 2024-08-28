# **Online Fraud Detection Using Machine Learning**

This project develops a machine learning-based system for detecting online fraud in multinational financial services. It offers real-time fraud detection by analyzing transaction patterns to enhance security and reduce false positives. The scalable and secure system includes a user-friendly interface and is designed for future AI and blockchain integration.

## **Project Description**
The project is focused on developing a robust and proactive system to identify and prevent fraudulent activities across diverse sectors, including investment banking, pension management, asset management, and payment services. By leveraging machine learning algorithms, the system enhances the accuracy of fraud detection compared to traditional methods, reduces false positives, and adapts to evolving threats. It ensures regulatory compliance, maintains customer trust, and optimizes operational efficiency, thereby fostering a secure and resilient financial environment.

## **Dataset**
The dataset used in this project is available on Kaggle: [Credit Card Fraud Detection Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud).

### **Dataset Overview**
The dataset contains credit card transactions over a two-day period in September 2013 by European cardholders. It includes a total of 284,807 transactions, of which 492 (0.172%) are fraudulent.

### **Data Composition**
- **PCA Transformed Features**: The majority of the features are numerical variables resulting from a Principal Component Analysis (PCA) transformation to maintain confidentiality.
- **Time**: Seconds elapsed between each transaction and the first transaction in the dataset.
- **Amount**: Transaction amount, which can be used for cost-sensitive learning.
- **Class**: The response variable indicating whether a transaction is fraudulent.

The dataset was collected and analyzed during a research collaboration between Worldline and the Machine Learning Group of Université Libre de Bruxelles (ULB) focused on big data mining and fraud detection.

## **Models**
This project applies various classification techniques, including:
- **Logistic Regression**
- **LightGBM**
- **K-Nearest Neighbors (KNN)**
- **Classification Trees**
- **Random Forest**
- **Support Vector Machine (SVM)**
- **XGBoost Classifier**

Each model has been evaluated to determine its effectiveness in detecting fraudulent transactions.

## **Future Scope**
Future enhancements could include the continuous improvement of machine learning models, the exploration of advanced technologies like AI and deep learning, the incorporation of behavioral analytics, and the integration of blockchain technology for heightened security. These improvements aim to maintain the system’s effectiveness in preventing online fraud as new challenges arise.
