🛍️ Customer Segmentation using K-Means Clustering

🔍 Project Overview

This project implements a customer segmentation system using K-Means clustering on real-world shopping behavior data.
The goal is to group customers into meaningful segments based on their purchasing patterns so that businesses can make data-driven marketing and pricing decisions.

The project follows a clean, production-style ML workflow:

Raw data preprocessing

Feature scaling

Unsupervised clustering

Cluster assignment and interpretation

🎯 Problem Statement

Businesses often treat all customers the same, which leads to inefficient marketing and poor personalization.

This project answers:

Can we group customers based on their shopping behavior?

Can these groups help in targeted marketing and customer strategy?

📊 Dataset

Real-world customer shopping dataset

Contains demographic and transactional information

Examples of attributes:

Age

Quantity purchased

Purchase price

🧠 Approach
1. Data Preprocessing

Removed non-informative identifiers

Selected behavior-based features

Handled missing values

Scaled numerical features using StandardScaler

2. Clustering

Applied K-Means clustering

Assigned each customer to a segment

Used a fixed random state for reproducibility

3. Output

Each customer is labeled with a cluster ID

These clusters represent different customer segments

🏗️ Project Structure
customer-segmentation-ml/
│
├── src/
│   ├── preprocess.py      # Data cleaning & scaling
│   ├── clustering.py      # K-Means clustering logic
│   └── evaluate.py        # (Optional) clustering evaluation
│
├── scripts/
│   ├── run_preprocessing.py
│   ├── run_clustering.py
│   └── run_evaluation.py
│
├── data/
│   ├── raw/               
│   └── processed/         
│
├── requirements.txt
├── .gitignore
└── README.md

▶️ How to Run the Project
1. Install dependencies
pip install -r requirements.txt

2. Preprocess the data
python scripts/run_preprocessing.py


This generates:

data/processed/processed_data.csv

3. Run K-Means clustering
python scripts/run_clustering.py


You will see cluster labels assigned to customers.

📈 Key Learnings

Feature scaling is critical for distance-based algorithms

K-Means is effective for discovering hidden customer groups

Clean separation of preprocessing and modeling improves reproducibility

Real-world datasets require careful feature selection

💼 Use Cases

Customer segmentation for marketing

Personalized offers and recommendations

Identifying high-value vs low-value customers

Business analytics and strategy planning

🧪 Technologies Used

Python

Pandas & NumPy

Scikit-learn

K-Means Clustering
