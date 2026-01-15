# 🛍️ Customer Segmentation using K-Means Clustering

## 📌 Overview
This project builds a **customer segmentation system** using **K-Means clustering** on real-world shopping behavior data.  
The objective is to group customers into meaningful segments based on their purchasing patterns, enabling businesses to make **data-driven marketing and personalization decisions**.

The project is designed with a **clean, modular, and production-style Machine Learning workflow**.

---

## 🎯 Problem Statement
Businesses often struggle to understand diverse customer behaviors. Treating all customers the same results in inefficient marketing strategies.

This project answers:
- How can customers be grouped based on shopping behavior?
- Can unsupervised learning identify meaningful customer segments?

---

## 📊 Dataset
- Real-world customer shopping dataset
- Contains demographic and transactional information such as:
  - Age
  - Quantity purchased
  - Purchase price



## 🧠 Methodology

### 1. Data Preprocessing
- Removed non-informative identifier columns
- Selected behavior-based numerical features
- Handled missing values
- Applied feature scaling using **StandardScaler**

### 2. Clustering
- Applied **K-Means clustering**
- Assigned each customer to a cluster
- Used a fixed random state for reproducibi
- - Assigned each customer to a cluster
- Used a fixed random state for reproducibility

### 3. Output
- Customers are labeled with cluster IDs
- Each cluster represents a distinct customer segment
📈 Key Learnings

Feature scaling is essential for distance-based algorithms

K-Means effectively identifies hidden customer groups

Clean separation of preprocessing and modeling improves reproducibility

Real-world datasets require careful feature selection

## 💼 Business Use Cases

Customer segmentation for targeted marketing

Personalized offers and recommendations

Identifying high-value vs low-value customers

Retail analytics and business strategy planning

## 🛠️ Technologies Used

Python

Pandas & NumPy

Scikit-learn

K-Means Clustering
