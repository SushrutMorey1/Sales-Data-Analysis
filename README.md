# Sales Data Dashboard

This is an interactive Sales Data Dashboard built with Streamlit and Plotly. It allows users to analyze and visualize key sales metrics, customer behavior, and insights from a retail dataset. The dashboard is designed for businesses or analysts who want an intuitive way to explore sales performance.

---

## Project Overview

The dashboard provides a simple interface to view total sales, profits, and order counts. Users can apply filters such as region, product category, customer segment, and date range to focus on specific subsets of data. It presents quarterly trends, state-level contributions, discount-profit relationships, and customer segmentation using clustering techniques.

---

## Features

The dashboard includes key performance indicators for total sales, profit, and order count.  
It visualizes quarterly sales and profit trends using bar charts.  
A treemap shows a hierarchical view of the top 20 states with categories and sub-categories.  
A scatter plot explores the relationship between discounts and profits.  
Customer segmentation is presented using PCA-based clustering.  
A customer details table provides easy access to individual performance metrics.

---

## Dataset

This project uses pre-processed datasets derived from the Superstore dataset:  

- full_sales_data.csv: Complete transaction data.  
- customer_df.csv: Aggregated customer-level data.  
- pca_df.csv: PCA-transformed data for clustering visualization.  
- ml_customer_data.csv: Includes customer clusters.  
- quarter_summary.csv: Quarterly sales and profit summary.  
- top_states_sales.csv, top_states_profit.csv, low_profit_states.csv: State-level insights.

---

## Technology Stack

The project uses Python for data processing and visualization.  
Streamlit provides the interactive user interface.  
Plotly is used for creating interactive charts.  
Pandas handles data manipulation, and scikit-learn was used for PCA and clustering.

---

## Running the Dashboard

1. Clone the repository.  
2. Install dependencies using `pip install -r requirements.txt`.  
3. Run the Streamlit app with `streamlit run app.py`.  
4. Open the browser and go to http://localhost:8501 to interact with the dashboard.

---

## Screenshots

### Dashboard Overview
*Insert dashboard overview screenshot here*

### Quarterly Sales and Profit
*Insert quarterly trends screenshot here*

### Treemap and Customer Segmentation
*Insert treemap and clustering screenshots here*

---

## Future Improvements

The dashboard can be extended with additional filters such as state and sub-category.  
Forecasting capabilities can be added using time-series models.  
Deployment to Streamlit Cloud would make it easily accessible online.  
A responsive layout can be implemented for better mobile experience.

---

## License

This project is open-source and licensed under the MIT License.
