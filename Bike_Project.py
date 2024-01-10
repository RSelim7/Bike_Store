import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load data
st.set_page_config(page_title="Bike_Store🚴‍♂️🌎📊", page_icon="Capture.PNG", layout="wide")
st.image("Capture.PNGs.PNG", width=100)
df = pd.read_csv('sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Title

#Sidebar
st.sidebar.title("Data Exploration")

page = st.sidebar.selectbox("Choose a page", ["Home", "Data Overview","Customer Age Analysis","Order Quantity Analysis 1 ","Order Quantity Analysis 2","Order Quantity Analysis 3"
    ,"Order Quantity Analysis 4","Order Quantity Analysis 5","Sales Analysis","Geographical Analysis 1","Geographical Analysis 2"])
 #Page 1
if page == "Home":
    st.title("Streamlit Dashboard Demo")
    st.header("Introduction to Global Bike Store Sales Dataset")
    st.snow()    

# Introduction
    st.markdown(""" Welcome to the rich and diverse world of global bike store sales data! This dataset provides a comprehensive glimpse into the dynamics of bike sales across various countries, offering valuable insights into customer behaviors, sales trends, and regional preferences. Spanning the years 2011 to 2016, the dataset encompasses a treasure trove of information, including customer demographics, order quantities, sales revenue, and more.

""")

    if st.button("Let the exploration begin! 🚴‍♂️🌎📊"):
    # Move to the next page
     show_page = ("Data Overview")

# Sidebar

elif page == "Data Overview":
    st.title("Data Random Sample")
    st.markdown("""this dataframe consists of the folowings : Date,Customer Age, Country,State, Gender,Product Category, Sub Category,
                , Costs, Price , Profit, Costs & Revenues""")
    btn=st.button("Show Data")
    if btn:
       st.dataframe(df.sample(5))
    
    
# Streamlit App
    st.title('Sales Analysis per Year')

    df['Calculated_Date'] = df[['Year', 'Month', 'Day']].apply(lambda x: '{}-{}-{}'.format(x[0], x[1], x[2]), axis=1)
    df['Year'] = df['Year'].astype(str)
    #df['Month'] = df['Month'].astype(str)
    #df['Day'] = df['Day'].astype(str)
    df['Calculated_Date'] = pd.to_datetime(df['Calculated_Date'])
    
# Convert 'Year' column to string
    # Streamlit App
    #st.title('Sales Analysis per Year')

# Convert 'Year' column to string
   # df['Year'] = df['Year'].astype(str)

# Convert 'Your_Date_Column_Name' to datetime
   
    #df['Calculated_Date'] = pd.to_datetime(df['Calculated_Date'])

# Display the calculated date
    #st.subheader('Calculated Dates:')
    #st.write(df[['Calculated_Date']].head())
  

# Group by 'Your_Date_Column_Name' and calculate the count of sales
    sales_count_per_date = df.groupby('Calculated_Date')['Product'].count().reset_index()

# Display the sales count per date
   # st.subheader('Sales Count per Date:')
  #  st.write(sales_count_per_date)

# Plotting with Plotly
    fig = px.line(df.groupby(df['Calculated_Date'].dt.year)['Revenue'].sum().reset_index(),
              x='Calculated_Date', y='Revenue',
              labels={'Revenue': 'Sales', 'Calculated_Date': 'Year'},
              title='Sales per Year')

# Streamlit Display
    st.plotly_chart(fig)


# Load your data into Streamlit
    st.title("Dashboard Summary")

# Function to create styled metrics using st.markdown
    def styled_metric(label, value, bg_color, text_color='white', font_size='1.5em'):
        styled_text = f"<div style='background-color: {bg_color}; padding: 10px; border-radius: 5px; text-align: center;'><span style='color: {text_color}; font-size: {font_size};'><b>{label}:</b> {value}</span></div>"
        st.markdown(styled_text, unsafe_allow_html=True)

# 1. Total Number Of Countries
    total_countries = df['Country'].nunique()
    styled_metric("Total Number Of Countries", total_countries, '#3366cc')

# 2. Total Count Of Products
    total_products = df['Product'].nunique()
    styled_metric("Total Count Of Products", total_products, '#dc3912')

# 3. Total Sum Of Revenue
    total_revenue = df['Revenue'].sum()
    styled_metric("Total Sum Of Revenue", total_revenue, '#ff9900')

# 4. Total Sum Of Profit
    total_profit = df['Profit'].sum()
    styled_metric("Total Sum Of Profit", total_profit, '#109618')

# 5. Total Count Of Orders
    total_orders = df.shape[0]
    styled_metric("Total Count Of Orders", total_orders, '#990099')




# Page 3

elif page == "Customer Age Analysis":
    st.title("Customer Age Analysis")
    st.write("Explore the age distribution of customers.")

    
# Assuming df is your DataFrame

    
    # Create a KDE (Kernel Density Estimate) plot using Plotly Express (histogram)

    st.subheader("Kernel Density Estimate (KDE) Plot for Customer Age:")
    st.markdown("""the graph illustrate that the denisty in the age below 36 "mean""")
# Check if the DataFrame is not empty
    if not df.empty:
    # Create a KDE (Kernel Density Estimate) plot using Plotly Express
        fig = px.histogram(df, x='Customer_Age', marginal='box', 
                       title='Kernel Density Estimate (KDE) Plot for Customer Age',
                       labels={'Customer_Age': 'Customer Age'},
                       template='plotly', color_discrete_sequence=['lightblue'])

    # Add vertical lines for mean and median
        mean_line = df['Customer_Age'].mean()
        median_line = df['Customer_Age'].median()

        fig.add_shape(type='line', x0=mean_line, x1=mean_line,
                  y0=0, y1=1, line=dict(color='red', width=2), 
                  xref='x', yref='paper')

        fig.add_shape(type='line', x0=median_line, x1=median_line,
                  y0=0, y1=1, line=dict(color='green', width=2), 
                  xref='x', yref='paper')

    # Show the plot in Streamlit
        st.plotly_chart(fig)
    else:
        st.warning("The DataFrame is empty.")
        
    # Streamlit App
    st.title('Customer Age Analysis per Country')

# Create a grouped box plot with Plotly
    fig = px.box(df, x='Country', y='Customer_Age', color='Country',
             title='Grouped Box Plot: Customer Age per Country',
             labels={'Customer_Age': 'Customer Age'})
    fig.update_layout(xaxis_title='Country', yaxis_title='Customer Age')

# Streamlit Display
    st.plotly_chart(fig)
  
###Page 3
elif page == "Order Quantity Analysis 1":
     st.title("Order Quantity Analysis")
     st.write("Explore the order quantity distribution.")

    # Mean Order Quantity
     st.subheader("Mean Order Quantity:")
     st.write(df['Order_Quantity'].mean())

#   Histogram and Box Plot for Order Quantity
  
# Assuming df is your DataFrame
# Histogram
 # Assuming df is your DataFrame

 # Histogram
     st.title('Order Quantity Histogram')

# Sidebar for selecting options if needed
# You can customize this based on your requirements
# For example, you can add options to select different columns or filters
# st.sidebar.header('Options')
# selected_column = st.sidebar.selectbox('Select a column', df.columns)

# Plotting the histogram
     fig, ax = plt.subplots(figsize=(8, 6))
     ax.hist(df['Order_Quantity'], bins=32, color='lightblue', ec='black')
     ax.set_xlabel('Order Quantity')
     ax.set_ylabel('Order Frequency')
     ax.set_title('Order Quantity Histogram')
 
# Display the plot using Streamlit
     st.pyplot(fig)
     
     
    
elif page == "Order Quantity Analysis 2":    
     st.title('Order Quantity Box plot')

# Sidebar for selecting options if needed
# You can customize this based on your requirements
# For example, you can add options to select different columns or filters
# st.sidebar.header('Options')
# selected_column = st.sidebar.selectbox('Select a column', df.columns)

# Plotting the box plot
     fig, ax = plt.subplots(figsize=(8, 6))
     sns.boxplot(x=df['Order_Quantity'], color='lightblue', ax=ax)
     ax.set_title('Order Quantity Box plot')
   
# Display the plot using Streamlit
     st.pyplot(fig) 
elif page == "Order Quantity Analysis 3":
    st.title("Order Quantity Analysis")
   
# Streamlit App
    st.title('Order Quantity Analysis per Country and State')

# Order Quantity per Country and State
    order_quantity_per_location = df.groupby(['Country', 'State'])['Order_Quantity'].sum().reset_index()
    order_quantity_per_location = order_quantity_per_location.sort_values('Order_Quantity', ascending=True)

# Display Order Quantity per Country and State
    st.subheader('Order Quantity per Country and State:')
    st.write(order_quantity_per_location)

#Streamlit App (Box Plotting with Plotly)
    st.title('Order Quantity Analysis per Country')

    fig_box = px.box(df, x='Country', y='Order_Quantity', color='Country', points='all',
                     title='Order Quantity per Country Box Plot', labels={'Order_Quantity': 'Order Quantity'})
    fig_box.update_traces(marker=dict(color='blue'))
    fig_box.update_layout(xaxis_title='Country', yaxis_title='Order Quantity')

# Streamlit Display
    st.plotly_chart(fig_box)
    
    
    
elif page == "Order Quantity Analysis 4":
     st.title("Order Quantity Analysis")
# Group by 'Country' & 'State' and calculate the count of 'Product'
     orders_per_state = df.groupby(['Country', 'State'])['Product'].count().reset_index()

# Sort the DataFrame in descending order based on the 'Product' count
     orders_per_state_descending = orders_per_state.sort_values(by='Country', ascending=False)



# Display the result in Streamlit
     st.write(orders_per_state_descending)

# Filter rows where 'Country' is 'France' and sort the values
     filtered_orders_france = orders_per_state_descending[orders_per_state_descending['Country'] == 'France'].sort_values(by='Product', ascending=False)

# Display the result in Streamlit
     st.write(filtered_orders_france)
    
    
# Bar plot with Plotly Express
     fig = px.bar(filtered_orders_france, x='State', y='Product', color='State',
               labels={'Product': 'Count of Orders'},
               title='Orders Per Each State in France Using a Bar Plot')

# Streamlit Display
     st.plotly_chart(fig)
    
elif page == "Order Quantity Analysis 5":
     st.title('Orders Per State Analysis')
    
# Group by 'Product_Category' & 'Sub_Category' and calculate the count of 'Product'
     orders_per_subcategory = df.groupby(['Product_Category', 'Sub_Category'])['Product'].count().reset_index()

# Sort the DataFrame in descending order based on the 'Product' count
     orders_per_subcategory_descending = orders_per_subcategory.sort_values(by='Product_Category', ascending=False)

# Streamlit App
     st.title('Orders Per Sub-Category Analysis for Accessories Category')

# Display the result in Streamlit
     st.write(orders_per_subcategory_descending)

# Filter rows where 'Product_Category' is 'Accessories' and sort the values
     filtered_orders_accessories = orders_per_subcategory_descending[orders_per_subcategory_descending['Product_Category'] == 'Accessories'].sort_values(by='Product', ascending=False)

# Display the result in Streamlit
     st.write(filtered_orders_accessories)

# Bar plot with Plotly Express
     fig = px.bar(filtered_orders_accessories, x='Sub_Category', y='Product', color='Sub_Category',
               labels={'Product': 'Count of Orders'},
               title='Orders Per Each Sub-Category For Accessories Category Using a Bar Plot')

# Streamlit Display
     st.plotly_chart(fig)

# Filter rows where 'Product_Category' is 'Bikes' and sort the values
     filtered_orders_bikes = orders_per_subcategory_descending[orders_per_subcategory_descending['Product_Category'] == 'Bikes'].sort_values(by='Product', ascending=False)

# Streamlit App
     st.title('Orders Per Sub-Category Analysis for Bikes Category')

# Display the result in Streamlit
     st.write(filtered_orders_bikes)

# Pie plot with Plotly Express
     fig = px.pie(filtered_orders_bikes, values='Product', names='Sub_Category',
               title='Total Orders Per Bike Subcategory',
               labels={'Product': 'Count of Orders'},
               hole=0.3)

# Streamlit Display
     st.plotly_chart(fig)


elif page == "Sales Analysis":
    st.title("Sales Analysis")
    

    st.subheader("Sales by Year:")

# Group by Year and sum the Revenue
    sales_by_year = df.groupby('Year')['Revenue'].sum().reset_index()

# Create a pie chart using Plotly Express
    fig = px.pie(sales_by_year, values='Revenue', names='Year', title='Sales by Year', 
             labels={'Revenue': 'Revenue', 'Year': 'Year'}, 
             template='plotly', hole=0.3, 
             color_discrete_sequence=px.colors.sequential.Blues[::-1])
    st.plotly_chart(fig)
    
# Sales by Month Bar Plot
    st.subheader("Sales by Month:")
    sales_by_month = df.groupby('Month')['Revenue'].sum().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(sales_by_month['Month'], sales_by_month['Revenue'], color='skyblue')
    ax.set_ylabel('Sales')
    ax.set_xlabel('Month')
    ax.set_title('Sales Per Month Using a Bar Plot')
    ax.set_xticks(sales_by_month['Month'])
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    st.plotly_chart(fig)
    
    
    
# Sales per Country Bar Plot

# Assuming df is your DataFrame with columns 'Country' and 'Revenue'
# Make sure to load your data or replace df with your actual DataFrame

# Streamlit App
    st.title('Sales Analysis')

# Sales per Country
    st.subheader("Sales per Country:")
    sales_per_country = df.groupby('Country')['Revenue'].sum().reset_index()
    sales_per_country = sales_per_country.sort_values('Revenue', ascending=True)

# Plotting with Plotly
    fig = px.bar(sales_per_country, x='Country', y='Revenue', color='Revenue', color_continuous_scale='Blues', labels={'Revenue': 'Sales'})
    fig.update_layout(title='Sales per Country', xaxis_title='Country', yaxis_title='Sales')

# Streamlit Display
    st.plotly_chart(fig)


# Display unique products


# Sales per Product
    st.title('Product Sales Analysis')
# Sales per Product
    sales_per_product = df.groupby('Product')['Revenue'].sum().reset_index()
    sales_per_product = sales_per_product.sort_values('Revenue', ascending=True)
    top_10_sold_products = sales_per_product.head(10)

# Display top 10 sold products
    st.subheader('Top 10 Sold Products:')
    st.write(top_10_sold_products)

# Plotting with Plotly
    fig = px.bar(top_10_sold_products, x='Product', y='Revenue', color='Revenue', labels={'Revenue': 'Sales'})
    fig.update_layout(title='Top 10 Sold Products', xaxis_title='Product', yaxis_title='Sales', xaxis_tickangle=-45)

# Streamlit Display
    st.plotly_chart(fig)
# Assuming df is your DataFrame with columns 'Unit_Cost' and 'Unit_Price'
# Make sure to load your data or replace df with your actual DataFrame
    st.subheader("Relations")
# Streamlit App
    st.title('Scatter Plot: Unit_Cost vs. Unit_Price')

# Plotting with Plotly
    fig = px.scatter(df, x='Unit_Cost', y='Unit_Price', color=df.index, title='Scatter Plot: Unit_Cost vs. Unit_Price', labels={'Unit_Cost': 'Unit Cost', 'Unit_Price': 'Unit Price'})
    fig.update_traces(marker=dict(color='blue', symbol='circle'))

# Streamlit Display
    st.plotly_chart(fig)
    
# Assuming df is your DataFrame with columns 'Order_Quantity' and 'Profit'
# Make sure to load your data or replace df with your actual DataFrame

# Streamlit App
    st.title('Scatter Plot: Order_Quantity vs. Profit')
    st.text("""we found : 
            outliers but after digging, the reason is the Touring-1000-yellow 50 
            Order_Quantity below 5 is the hisghest profit !!""")
# Plotting with Plotly
    fig = px.scatter(df, x='Order_Quantity', y='Profit', title='Scatter Plot: Order_Quantity vs. Profit', labels={'Order_Quantity': 'Order Quantity', 'Profit': 'Profit'})
    fig.update_traces(marker=dict(symbol='x', size=10, color='blue'))

# Streamlit Display
    st.plotly_chart(fig)    
    
   # Assuming df is your DataFrame
# Make sure to load your data or replace df with your actual DataFrame

# Streamlit App
    st.title('Revenue and Revenue Adjustment Analysis per Year')

# Adding Revenue Adjustment column
    df['Revenue_Adjustment'] = df['Revenue'] + 50

# Group by 'Year' and calculate the sum of 'Revenue' and 'Revenue_Adjustment'
    revenue_per_year = df.groupby('Year')[['Revenue', 'Revenue_Adjustment']].sum().reset_index()

# Print or display the result
    st.subheader('Revenue per Year:')
    st.write(revenue_per_year)

# Plotting with Plotly
    fig = px.bar(revenue_per_year, x='Year', y=['Revenue', 'Revenue_Adjustment'],
             labels={'value': 'Total Revenue', 'variable': 'Metric'},
             title='Revenue & Revenue Adjustment Per Year Using a Bar Plot',
             color_discrete_map={'Revenue': 'skyblue', 'Revenue_Adjustment': 'orange'})

# Streamlit Display
    st.plotly_chart(fig) 
    
# Group by 'Customer_Gender' and calculate the sum of 'Revenue'
    sales_per_gender = df.groupby('Customer_Gender')['Revenue'].sum().reset_index()

# Sort the DataFrame in descending order based on the 'Revenue'
    sales_per_gender_descending = sales_per_gender.sort_values(by='Revenue', ascending=False)

# Plot Pie Chart using Plotly Express
    fig = px.pie(sales_per_gender_descending, values='Revenue', names='Customer_Gender', title='Sales Comparison by Gender')

# Display the Pie Chart in Streamlit app
    st.plotly_chart(fig)



# Group by 'Product_Category' and calculate the sum of 'Sales'
    sales_per_category = df.groupby('Product_Category')['Revenue'].sum().reset_index()

# Sort the DataFrame in descending order based on the 'Sales'
    sales_per_category_descending = sales_per_category.sort_values(by='Revenue', ascending=False)

# Streamlit App
    st.title('Sales Analysis Per Category')

# Display the result in Streamlit
    st.write(sales_per_category_descending)

# Pie plot with Plotly Express
    fig = px.pie(sales_per_category_descending, values='Revenue', names='Product_Category',
             title='Total Sales Per Category',
             labels={'Revenue': 'Total Revenue'},
             hole=0.3)

# Streamlit Display
    st.plotly_chart(fig)


# Sort the DataFrame in descending order based on 'Revenue' and get the top 5
    top_5_sales = df.sort_values('Revenue', ascending=False).head(5)

# Streamlit App
    st.title('Top-5 Sales with the Highest Revenue')

# Display the result in Streamlit
    st.write(top_5_sales)
    
# Find the sale with the highest revenue
    highest_revenue_sale = df[df['Revenue'] == df['Revenue'].max()]

# Streamlit App
    st.title('Highest Revenue Sale')

# Display the result in Streamlit
    st.write(highest_revenue_sale)


    
# PAge 4
elif page == "Geographical Analysis 1":
    st.title("Sales Analysis per country")
    st.write("Explore sales information.")
    st.title('Profit Analysis per Country')

# Profit per Country
    Profit_per_country = df.groupby('Country')['Profit'].sum().reset_index()
    Profit_per_country = Profit_per_country.sort_values('Profit', ascending=True)

# Display Profit per Country
    st.subheader('Profit per Country:')
    st.write(Profit_per_country)
  
# Plotting with Plotly Map
    fig = px.choropleth(Profit_per_country,
                         locations='Country',
                         locationmode='country names',
                         color='Profit',
                         color_continuous_scale='Blues',
                         title='Profit per Country Map',
                         labels={'Profit': 'Total Profit'})

# Streamlit Display
    st.plotly_chart(fig)


# Assuming df is your DataFrame with columns 'Country', 'Profit', and 'Customer_gender'
# Make sure to load your data or replace df with your actual DataFrame

# Streamlit App
    st.title('Profit Analysis per Country and Customer Gender')

# Multiselect for filtering countries
    selected_countries = st.multiselect('Select Countries', df['Country'].unique(), df['Country'].unique())

# Multiselect for filtering customer gender
    selected_gender = st.multiselect('Select Customer Gender', df['Customer_Gender'].unique(), df['Customer_Gender'].unique())

# Filter DataFrame based on selected countries and customer gender
    filtered_df = df[(df['Country'].isin(selected_countries)) & (df['Customer_Gender'].isin(selected_gender))]

# Profit per Country
    Profit_per_country = filtered_df.groupby(['Country', 'Customer_Gender'])['Profit'].sum().reset_index()
    Profit_per_country = Profit_per_country.sort_values('Profit', ascending=True)

# Display Profit per Country and Customer Gender
    st.subheader('Profit per Country and Customer Gender:')
    st.write(Profit_per_country)

# Plotting with Plotly Map
    fig = px.choropleth(Profit_per_country,
                    locations='Country',
                    locationmode='country names',
                    color='Profit',
                    color_continuous_scale='Blues',
                    title='Profit per Country Map',
                    labels={'Profit': 'Total Profit'},
                    facet_col='Customer_Gender')  # Use 'Customer_gender' instead of 'Customer_Gender'

# Streamlit Display
    st.plotly_chart(fig)
    
elif page == "Geographical Analysis 2":
# Streamlit App
    st.title('Profit Analysis per Country')

# Box Plotting with Plotly
    fig = px.box(df, x='Country', y='Profit', color='Country', points='all',
             title='Profit per Country Box Plot', labels={'Profit': 'Profit'})
    fig.update_traces(marker=dict(color='blue'))
    fig.update_layout(xaxis_title='Country', yaxis_title='Profit')

# Streamlit Display
    st.plotly_chart(fig)
    


# ...

# Finally, run the Streamlit app
# Save this script in a file named 'app.py' and run the following command in the terminal:
# streamlit run app.py
