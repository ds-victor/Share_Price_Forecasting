# 📈 Share Price Forecasting using ARIMA, SARIMA & Prophet

## 🔍 Project Overview
This project focuses on **time series forecasting of share prices** using historical stock market data.
The goal is to predict future price trends by applying both **classical statistical models** and a
**modern forecasting framework**, and to make the results accessible via a **Streamlit web application**.

The project demonstrates:
- End-to-end time series workflow
- Monthly aggregation of daily stock prices
- Model comparison using ARIMA, SARIMA, and Prophet
- Interactive forecasting using Streamlit

## url: https://sharepriceforecasting-ytjijjfbrexf3ke3sbsnev.streamlit.app/

## 📂 Folder Structure

```
Share_Price_Forecasting/
│
├── data/
│ └── yahoo_stock.csv
│
├── notebooks/
│ └── Share_Price_Forecasting.ipynb
│
├── app.py
├── requirements.txt
├── gitignore.bat
└── README.md
```


## 📊 Dataset
**Source:** Yahoo Stock Market Data  
**File:** `yahoo_stock.csv`

### Dataset Description
The dataset contains **daily stock prices** with the following columns:
- `Date`
- `Open`
- `High`
- `Low`
- `Close`
- `Volume`

To reduce daily noise and improve forecast stability, the data is **aggregated at a monthly level**
using the **average closing price**.


## 🧠 Methodology

1. Load and preprocess daily stock price data
2. Convert date column and sort chronologically
3. Aggregate daily prices into monthly averages
4. Perform Exploratory Data Analysis (EDA)
5. Check stationarity using the Augmented Dickey–Fuller (ADF) test
6. Analyze autocorrelation using ACF & PACF plots
7. Split data into training and testing sets (last 12 months)
8. Train forecasting models:
   - ARIMA
   - SARIMA (with yearly seasonality)
   - Prophet
9. Evaluate models using MAE and RMSE
10. Visualize and compare forecasts
11. Deploy forecasting logic using Streamlit


## 🤖 Models Used

### 🔹 ARIMA
- Captures short-term dependencies
- Suitable for non-seasonal time series

### 🔹 SARIMA
- Extends ARIMA to handle seasonality
- Models yearly patterns explicitly (12-month cycle)

### 🔹 Prophet
- Additive model developed by Meta
- Automatically handles trend and seasonality
- Robust to missing values and trend shifts


## 📈 Evaluation Metrics
The models are evaluated using:
- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**

These metrics help compare prediction accuracy on unseen data.


## 🌐 Streamlit Web Application
### Try Here : https://sharepriceforecasting-ytjijjfbrexf3ke3sbsnev.streamlit.app/

The project includes an interactive **Streamlit app** (`app.py`) that allows users to:
- Upload stock price data
- Visualize monthly trends
- Select forecast horizon
- View future price predictions

### ▶ To Run the app locally
bash
  - streamlit run app.py

## 🛠️ Tech Stack
- Python
- andas, NumPy
- Matplotlib
- Statsmodels
- Prophet
- Scikit-learn
- Streamlit


## 🚀 Future Enhancements
- Auto-ARIMA for automated parameter selection
- Rolling window cross-validation
- Support for multiple stocks
- Model persistence and versioning
- Cloud deployment with CI/CD

## 📌 Key Takeaways
- Monthly aggregation improves forecast stability
- SARIMA and Prophet outperform basic ARIMA
- Prophet provides better interpretability for business users
- Time series model choice depends on data granularity and seasonality
