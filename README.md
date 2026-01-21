# 📊 Vendor Performance Analysis | Inventory and sales

## 📌 One-Line Objective
Analyzed vendors and inventory performance to identify profitability drivers, strategic purchasing, inventory decision and optimization opportunities using SQL, Python, and data visualization.

---

## 📑 Table of Contents
- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Tools and Technologies](#tools-and-technologies)
- [Project Execution](#project-execution)
- [Dashboard](#dashboard)
- [How to Run This Project](#how-to-run-this-project)
- [Results and Conclusion](#results-and-conclusion)
- [Future Work](#future-work)
- [Author & Contact](#author--contact)

---

## 📖 Overview
This project focuses on analyzing vendor-level purchase and sales data to uncover key business insights related to profitability, inventory turnover, vendor dependency, and cost optimization. The analysis combines data cleaning, exploratory data analysis (EDA), statistical validation, and dashboard reporting to support data-driven decision-making.

---

## ❓ Problem Statement
Retail and wholesale businesses often face challenges such as:
- High dependency on a small number of vendors  
- Slow-moving inventory locking significant capital  
- Inefficient pricing and purchasing strategies  

This project aims to address these challenges by analyzing vendor performance, inventory movement, and pricing behavior to improve profitability and operational efficiency.

---

## 🗂 Dataset
- **Type:** Retail & Wholesale Transactional Data  
- **Records:** ~10,000+ rows  
- **Key Fields:**  
  - Vendor details  
  - Brand information  
  - Purchase price & quantity  
  - Sales price & quantity  
  - Freight cost  
  - Gross profit & profit margin  
- **Source:** Provided as CSV files (stored in the `/data` directory)

---

## 🛠 Tools and Technologies
- **SQL / MySQL** – Data extraction and aggregation  
- **Python** – Data cleaning and analysis  
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
- **Power BI / Tableau** – Dashboard creation  
- **GitHub** – Version control and project hosting  

---

## 🔄 Project Execution

### 1️⃣ Data Cleaning & Preparation
- Removed records with:
  - Gross profit ≤ 0
  - Profit margin ≤ 0
  - Zero sales quantity
- Handled extreme outliers in pricing and freight cost
- Ensured analysis focused only on profitable and valid transactions

### 2️⃣ Exploratory Data Analysis (EDA)
- Distribution analysis for pricing, sales, and inventory metrics
- Outlier detection in purchase price, freight cost, and profit margin
- Correlation analysis between:
  - Purchase quantity vs. sales quantity
  - Price vs. profit
  - Stock turnover vs. profitability

### 3️⃣ Research Questions & Key Findings
- **Vendor Concentration:**  
  Top 10 vendors contribute ~65.7% of total purchases (high supplier risk)
- **Inventory Efficiency:**  
  $2.71M worth of unsold inventory identified
- **Bulk Purchasing Impact:**  
  Large orders show ~72% lower unit cost compared to small orders
- **Profitability Patterns:**  
  Low-performing vendors have higher margins but lower sales volume
- **Statistical Validation:**  
  Hypothesis testing confirmed significant profit margin differences between vendor groups

---

## 📊 Dashboard
A vendor performance dashboard was created to visualize key insights, including:
- Total sales, purchases, gross profit, and profit margin
- Vendor contribution percentages
- Top vendors and brands by sales
- Low-performing vendors and brands
- Unsold inventory value

**Dashboard Screenshot Placeholder:**

![Dashboard Screenshot](images/dashboard.png)

> *(Replace this image once you upload your dashboard screenshot to the `images` folder)*

---

## ▶️ How to Run This Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/vendor-performance-analysis.git
