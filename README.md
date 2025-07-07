# ⚡ AI-Driven Capacity Forecasting & Regional Monitoring Dashboard

A modular, production-grade system to forecast cloud infrastructure demands and monitor regional usage with anomaly detection, capacity forecasting, and mitigation simulations — built with **Prophet**, **Streamlit**, and **Python**, simulating real-world Azure/AWS cloud operations.

> 💼 Designed for roles in ML Engineering, Cloud Intelligence, and Infrastructure Forecasting.

---

## 🧠 Problem Statement

Cloud providers must dynamically predict regional resource demand to avoid outages, optimize scaling, and reduce operational costs. Manual heuristics or static thresholds often fail during usage spikes or regional anomalies.

Inspired by real industry scenarios (e.g., Microsoft's regional Azure planning or AWS capacity forecasting), this project tackles the core challenge:
> **How can we predict and monitor infrastructure demands with precision while offering simulation-based mitigation?**

---

This system is modular, scalable, and testable — structured to support CI/CD and extensibility.

---

📁 Designed for:

    - Modularity: Each component isolated and reusable.
    - Maintainability: Simple addition of new regions, models, or logic.
    - Version control & testing: Ideal for collaboration and CI workflows.

---

## 🔍 Core Features

| Feature                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| **📊 Forecasting**         | Prophet-based hourly capacity forecast for any region                      |
| **📉 Anomaly Detection**   | Z-score-based detection of demand spikes or drops                          |
| **🌐 Regional Drilldown**  | Visualize real usage vs. forecast per region with interactive charts       |
| **🧪 Testing Suite**       | Pytest-backed tests for forecast logic and input handling                  |
| **📁 Multi-page UI**       | Streamlit navigation with Forecast, Anomalies, Drilldown tabs              |
| **📈 Interactive Charts**  | Dynamic `plotly` graphs and real-time dropdown selection                   |
| **🧠 Designed for Cloud**   | Simulates Azure/AWS/GCP region capacity monitoring & predictive scaling   |

---
🗂️ Folder-Level Overview:

📁 notebooks/ (🔐 PRIVATE, not included in public repo except EDA)
    - Exploratory and visual analysis of simulated capacity data.
    - Includes model evaluation outputs, anomaly visualizations, and high-level experiment tracking.
    - Core ML algorithms are abstracted out — only results and workflows are shown.

📁 dashboard/pages/ 
    - Streamlit multi-page UI components: Forecast visualizer, anomaly dashboard, region drill-down, etc.
    - Safe to share — logic is presentation-focused only.

📁 src/ (🔐 PRIVATE, not included in public repo)
    - Contains forecasting algorithms (Prophet, XGBoost), anomaly detection logic (Z-score, Isolation Forest),
      mitigation strategies, auto-retraining simulations, and SHAP explainability logic.
    - Protected to preserve project IP.

📁 data/
    - Includes only a simulated CSV dataset (capacity usage) with timestamps and regions.
    - No real-world or client data is shared.

📁 .github/
    - Contains GitHub Actions for CI (e.g., linting, testing) — useful for showcasing engineering rigor.

> Complete code is maintained in a private repository. Contact: - [Form](https://forms.gle/4he63uTbjhTcTU5t5) for connect and more details
---



🔍 Inference Flow

This system simulates how a real-world cloud provider like Microsoft Azure or AWS might forecast capacity, detect anomalies, and recommend mitigations across data center regions. The full pipeline is built with reproducibility, scalability, and observability in mind — with each visual element in the app reflecting a key inference stage.

📈 1. Forecasting Future Demand (→ Forecast tab)

Once a region is selected (e.g., us-east), the app loads historical cpu_usage data and performs time series forecasting using Meta Prophet.

🛠️ Inputs:

Hourly metrics for cpu_usage per region.

🔮 Model:

Prophet — auto-tuned for the selected region.

📊 Visualization:
A dynamic line chart plots the predicted values with bounds:

    Identify plateaus or surges in demand.
    
    Anticipate potential resource constraints.
    
    Align provisioning and scaling plans in advance.

> ⚡ This mirrors how Microsoft intelligently forecasts Azure workload spikes using telemetry to pre-allocate compute capacity.


🔍 2. Regional Resource Drilldown (→ RegionDrilldown tab)

This tab enables deep inspection of each region’s actual resource usage against predicted demand.

💡 Use Cases:

Spot infrastructure saturation patterns.

Compare CPU vs memory usage across timelines.

Trace anomalies to raw data for RCA (Root Cause Analysis).

> 💡 Cloud teams at Microsoft rely on similar dashboards in Azure Monitor, Workbooks, or Log Analytics when diagnosing compute pressure, throttling, or under-utilized resources.

---

| Inference Component                  | Real-World Equivalent (Microsoft / AWS)                                                               |
|--------------------------|-----------------------------------------------------------------------------|
| **Prophet Forecasting**         | Azure Monitor-based capacity forecasting                      |
| **Z-Score Anomaly Detection**   | Azure Metrics Advisor / AWS DevOps Guru                         |
| **Region Drilldown**  | Azure Workbooks, AWS CloudWatch Dashboards       |

---

Outputs:

![1](https://github.com/user-attachments/assets/b5af52c2-1470-4d37-bea6-7585878b092c)


![2](https://github.com/user-attachments/assets/6b26b707-d556-4beb-82ad-5e1412defe4d)


![3](https://github.com/user-attachments/assets/aab047af-ae81-4f2f-b6bf-790cd7042088)


XGBoost RMSE: 3.87


![4](https://github.com/user-attachments/assets/7b7f4107-06b1-43f0-a976-61c47332af72)

![5](https://github.com/user-attachments/assets/c3024cf6-2c41-472a-8ce7-070cb4e26a00)

![6](https://github.com/user-attachments/assets/ca006d21-cce2-44d2-80ec-7383d3dcaccf)!
