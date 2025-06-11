
ML EDA Starter: Titanic Survival Analysis
===========================================

This project performs Exploratory Data Analysis (EDA) on the Titanic dataset from Kaggle. It is structured for beginners to understand how to clean, explore, and prepare real-world data for machine learning models.

Project Structure
---------------------
ml-eda-starter/
├── data/              # Raw dataset files (e.g., train.csv, test.csv)
├── notebooks/         # Jupyter notebook for EDA
├── src/               # Python scripts for cleaning and reuse
├── README.md          # Project overview and instructions
├── .gitignore         # Files/folders excluded from Git tracking
└── requirements.txt   # Python dependencies

Data Cleaning Summary
-------------------------
The following steps were performed:

- Filled missing values in 'Age' with median
- Filled missing values in 'Embarked' with mode
- Dropped 'Cabin' due to excessive missing values
- Encoded 'Sex' as binary (0: female, 1: male)
- One-hot encoded 'Embarked'
- Dropped irrelevant columns ('Name', 'Ticket', 'PassengerId')

All cleaning logic is wrapped in a reusable Python function in 'src/data_cleaning.py'.

Exploratory Data Analysis (EDA)
-----------------------------------
Key insights from the data:

- Survival rate is higher for females and 1st class passengers
- Age distribution shows more younger passengers in 3rd class
- Embarkation port also shows survival variation

EDA is performed in 'notebooks/eda.ipynb' using pandas, seaborn, and matplotlib.

Getting Started
--------------------
To run the project:

1. Clone the repo:
   git clone https://github.com/your-username/ml-eda-starter.git
   cd ml-eda-starter

2. Install dependencies:
   pip install -r requirements.txt

3. Launch the notebook:
   jupyter notebook notebooks/eda.ipynb

Dependencies
----------------
- Python 3.10+
- pandas
- matplotlib
- seaborn
- jupyter

(See 'requirements.txt')

Git Commands Used to Push Code
----------------------------------
git init
git add .
git commit -m "Initial commit with cleaned data and structure"
git remote add origin https://github.com/your-username/ml-eda-starter.git
git branch -M main
git push -u origin main

Acknowledgments
-------------------
Dataset: https://www.kaggle.com/competitions/titanic

Author
----------
Priyanka
