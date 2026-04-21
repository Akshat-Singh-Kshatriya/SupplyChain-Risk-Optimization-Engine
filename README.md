## End-to-End Predictive Maintenance & Logistics Risk Analytics

## Executive Summary
This project demonstrates a "Strategy to Execution" approach by bridging the gap between manufacturing floor telemetry and global supply chain logistics. It utilizes a **Digital Twin** framework to predict machinery failure and quantify its downstream financial impact on order fulfillment, shipping penalties, and customer satisfaction. By integrating **Machine Learning (Python)**, **Relational Database Modeling (SQL)**, and **Business Intelligence (Power BI)**, this tool acts as a "Control Tower" for modern, connected supply chains.

## The Business Problem
In a "Smart Factory" environment, machine downtime is not just a maintenance issue; it’s a supply chain bottleneck. Unexpected failures lead to:
1. **Production Halts**: Direct loss in manufacturing capacity.
2. **Logistics Penalties**: Late-delivery fees and expedited shipping costs.
3. **Revenue Risk**: Potential loss of high-value customer orders.
   
## Technical Architecture
### Phase 1: Predictive Maintenance (Machine Learning)
* **Dataset**: **[AI4I 2020 Predictive Maintenance (UCI)](https://www.kaggle.com/datasets/stephanmatzka/predictive-maintenance-dataset-ai4i-2020)**
* **Modeling**: Trained a **Random Forest Classifier** with **Stratified 5-Fold Cross-Validation** to handle imbalanced failure data.
* **Key Insight**: Focused on thermodynamic metrics (Process vs. Air Temperature) to predict failures before they occur.

### Phase 2: Relational Mapping (PostgreSQL)
* **Dataset**: **[DataCo Smart Supply Chain](https://www.kaggle.com/datasets/shashwatwork/dataco-smart-supply-chain-for-big-data-analysis)**
* **Engineering**: Built a custom SQL View (`vw_SupplyChain_Risk_Assessment`) to link factory machine health to specific customer orders.
* **Logic**: Implemented a **15% late-delivery penalty** simulation and dynamic procurement cost logic ($150–$500 per part) based on failure probability.

### Phase 3: Executive Dashboard (Power BI)
* **Design**: Followed professional consulting aesthetics (Orange/Charcoal palette).
* **Functionality**: Developed interactive KPI cards and slicers to allow "diagnostic and benchmarking" of large data sets.

## Numerical Results
* **Model Reliability**: Achieved an **Average F1-Score of 94.2%**, ensuring high precision in maintenance scheduling to avoid unnecessary part orders.
* **Operational Impact**: The dashboard identifies the **Top 10 High-Risk Products** by revenue, allowing managers to prioritize maintenance on machines that affect the most profitable elements of the value chain.
* **Financial Visibility**: Quantified **Revenue at Risk** due to downtime, providing a data-driven basis for "Make-vs-Buy" and "Insource vs. Outsource" analysis.

## Tech Stack
* **Data Science**: Python (Scikit-Learn, Pandas, Numpy)
* **Data Engineering**: PostgreSQL (DDL, DML, Window Functions, Views) 
* **Analytics**: Microsoft Power BI (DAX, Slicers, Conditional Formatting) 
* **Methodologies**: Lean/Six Sigma Mindset, Industry 4.0, Supply Chain Planning
