
# 📊 Failed Banking Transaction Analysis

## 📌 Overview

This project aims to build a **scalable, cloud-native data pipeline** for analyzing failed banking transactions using **Google Cloud Platform (GCP)**. The pipeline supports ingesting, processing, cleaning, analyzing, and visualizing large volumes of transactional data collected from various bank branches across multiple cities.

**Author:** Mohamed Razeeth M  
**Date:** May 25  
**Tools & Platforms:** GCP, PySpark, Dataproc, Cloud SQL, BigQuery, Looker Studio

---

## 🎯 Objective

The primary goal is to:

- Identify and analyze **failed banking transactions**.
- Build a **scalable and automated pipeline** using GCP services.
- Enable **data-driven decisions** for improving banking operations and minimizing transaction failures.

---

## 📁 Data Description

- **Source:** Daily CSV files from 15 branches (3 cities × 5 branches)
- **Structure:** Each file contains transaction metadata including:
  - Transaction ID
  - Branch
  - Timestamp
  - Status
  - Failure Reason
  - Amount
- **Challenges:** The data is inconsistent with:
  - Missing values
  - Duplicates
  - Blank fields

---

## 🏗️ Architecture

```plaintext
GCS (raw CSVs)
   ↓
Dataproc (PySpark cleaning/filtering)
   ↓
Cloud SQL (store cleaned + failed transactions)
   ↓
BigQuery (query and transformation)
   ↓
Looker Studio (visual reporting)
```

---

## 🔄 Workflow Steps

### 1. Data Ingestion

- Created a Cloud Storage bucket:
  ```bash
  gsutil mb gs://your-bucket-name/
  ```
- Uploaded all CSV files into the `input/` directory:
  ```bash
  gsutil cp /local/path/*.csv gs://your-bucket-name/input/
  ```

---

### 2. Data Cleaning with PySpark (on Dataproc)

- Read all input CSV files using PySpark
- Cleaned the data by:
  - Removing rows with null or blank fields:
    ```python
    df.dropna()
    df.filter(trim(col("column")) != "")
    ```
- Saved cleaned data to:
  ```plaintext
  gs://my-bucket-rashid/cleaned-banking-transactions-data/
  ```

---

### 3. Extracting Failed Transactions

- Processed cleaned data to filter rows with failed transactions
- Exported failed transactions as a new CSV
- Loaded the result into **Cloud SQL (MySQL)**
- Connected Cloud SQL with **BigQuery** for seamless analysis

---

### 4. Analysis & Reporting with Looker Studio

Key visualizations include:

- 📉 Failure rate by branch  
- 🔍 Count of failed transactions by product category  
- 📊 Transaction failure percentage by payment mode  
- 🔁 Cross-analysis of product categories and failure modes

---

## 🧠 Key Insights

- Enabled **real-time monitoring** of failure trends  
- Improved visibility into **failure reasons and high-risk branches**  
- Built a **modular, scalable pipeline** ready for production workloads

---

## ✅ Technologies Used

- **Cloud Storage (GCS)** – File storage  
- **Dataproc + PySpark** – Data cleaning and processing  
- **Cloud SQL (MySQL)** – Processed data storage  
- **BigQuery** – Advanced querying  
- **Looker Studio** – Interactive dashboards

---

## 🙌 Acknowledgements

Special thanks to the GCP services and open-source PySpark community for enabling this scalable and flexible data solution.
