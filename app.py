import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


#  Load Datasets

df = pd.read_csv("data/full_sales_data.csv")
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df = df.dropna(subset=['Order Date'])
ml_df = pd.read_csv("data/ml_customer_data.csv")


#  Page Config & Styling

st.set_page_config(page_title="Sales Analysis Dashboard", layout="wide")

st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
            background-color: #F4F6F8;
            color: #212529;
        }
        .stTabs [role="tab"] {
            background: #E9ECEF;
            border-radius: 12px;
            margin-right: 10px;
            padding: 14px 22px;
            font-weight: 600;
            color: #495057;
            transition: all 0.3s ease-in-out;
        }
        .stTabs [role="tab"][aria-selected="true"] {
            background: linear-gradient(90deg, #4C6EF5, #15AABF);
            color: #FFFFFF;
            box-shadow: 0 6px 20px rgba(0,0,0,0.15);
        }
        .metric {
            font-size: 21px;
            color: #4C6EF5;
        }
        .stPlotlyChart div {
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
            padding: 25px;
            background-color: #FFFFFF;
            transition: transform 0.4s ease;
        }
        .stPlotlyChart div:hover {
            transform: scale(1.03);
        }
    </style>
""", unsafe_allow_html=True)




#  App Title

st.title(" Sales Analysis Dashboard")
st.markdown("<p style='font-size:17px;'>A sleek, business-grade dashboard for impactful insights and reporting.</p>", unsafe_allow_html=True)


#  Sidebar Filters

st.sidebar.header(" Filters")
region_filter = st.sidebar.multiselect("Region(s)", df['Region'].unique(), default=df['Region'].unique())
category_filter = st.sidebar.multiselect("Category(s)", df['Category'].unique(), default=df['Category'].unique())
segment_filter = st.sidebar.multiselect("Segment(s)", df['Segment'].unique(), default=df['Segment'].unique())
min_date = df['Order Date'].min().date()
max_date = df['Order Date'].max().date()
date_range = st.sidebar.date_input("Date Range", [min_date, max_date])


#  Apply Filters

filtered_df = df[
    (df['Region'].isin(region_filter)) &
    (df['Category'].isin(category_filter)) &
    (df['Segment'].isin(segment_filter)) &
    (df['Order Date'].dt.date >= date_range[0]) &
    (df['Order Date'].dt.date <= date_range[1])
]


# Tabs Layout

tabs = st.tabs(["Overview", "State Insights", "Customer Segmentation"])


# Overview Tab

with tabs[0]:
    st.markdown("<h4 style='margin-bottom: 20px;'>Key Metrics</h4>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", f"${filtered_df['Sales'].sum():,.2f}")
    col2.metric("Total Profit", f"${filtered_df['Profit'].sum():,.2f}")
    col3.metric("Total Orders", f"{filtered_df['Order ID'].nunique()}")

    st.subheader("Quarterly Sales & Profit")

    # Create and sort quarters
    filtered_df['Quarter'] = filtered_df['Order Date'].dt.to_period('Q')
    quarterly_sales = filtered_df.groupby('Quarter')['Sales'].sum().sort_index()
    quarterly_profit = filtered_df.groupby('Quarter')['Profit'].sum().sort_index()
    x_vals = quarterly_sales.index.astype(str)

    # Plot
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.08)
    fig.add_trace(go.Bar(x=x_vals, y=quarterly_sales.values,
                         name='Sales', marker_color="#15AABF"), row=1, col=1)
    fig.add_trace(go.Bar(x=x_vals, y=quarterly_profit.values,
                         name='Profit', marker_color="#4C6EF5"), row=2, col=1)
    st.plotly_chart(fig, use_container_width=True)


# States Tab

with tabs[1]:
    st.subheader("Top States, Categories & Sub-Categories by Sales (Profit Highlighted)")
    top_states = filtered_df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(20).index
    top_state_data = filtered_df[filtered_df['State'].isin(top_states)]
    fig_treemap = px.treemap(top_state_data, path=['State', 'Category', 'Sub-Category'],
                             values='Sales', color='Profit', color_continuous_scale='Cividis')
    st.plotly_chart(fig_treemap, use_container_width=True)

    st.subheader("Discount vs Profit")
    fig_discount_profit = px.scatter(filtered_df, x='Discount', y='Profit', trendline="ols",
                                     color_discrete_sequence=["#FF922B"])
    fig_discount_profit.update_layout(template="plotly_white")
    st.plotly_chart(fig_discount_profit, use_container_width=True)


# Customers Tab

with tabs[2]:
    st.subheader("Customer Segmentation Clusters")
    fig_cluster = px.scatter(ml_df, x='PCA1', y='PCA2', color='Cluster',
                             hover_data=['Customer Name', 'Total Sales'],
                             color_continuous_scale='Viridis')
    fig_cluster.update_layout(template="plotly_white")
    st.plotly_chart(fig_cluster, use_container_width=True)

    st.subheader("Customer Data Table")
    st.dataframe(ml_df[['Customer Name', 'Total Sales', 'Total Profit', 'Cluster']]
                 .sort_values(by='Total Sales', ascending=False))


# Footer

st.markdown("---")
st.markdown("<center><p style='color:#868E96;'>Made with using Streamlit ❤️❤️ </p></center>", unsafe_allow_html=True)
