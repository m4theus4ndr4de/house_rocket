import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import geopandas
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
from datetime import datetime

st.set_page_config(layout='wide')

@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)
    return data

@st.cache(allow_output_mutation=True)
def get_geofile(url):
    geofile = geopandas.read_file(url)
    return geofile

def set_feature(data):
    data['price_m2'] = data['price'] / data['sqft_lot'] 
    return data

def overview_data(data):
    f_attributes = st.sidebar.multiselect('Enter columns', data.columns) 
    f_zipcode = st.sidebar.multiselect( 'Enter zipcode', data['zipcode'].unique())

    st.title('Data Overview')

    if f_zipcode != []:
        data_selection = data.loc[data['zipcode'].isin(f_zipcode)]

    else:
        data_selection = data.copy()

    if f_attributes != []:
        data_print = data_selection.loc[:, f_attributes]
    
    else:
        data_print = data_selection.copy()

    st.dataframe(data_print.head())

    c1, c2 = st.columns((1, 1))  

    # Average metrics
    df1 = data_selection[['id', 'zipcode']].groupby('zipcode').count().reset_index()
    df2 = data_selection[['price', 'zipcode']].groupby('zipcode').mean().reset_index()
    df3 = data_selection[['sqft_living', 'zipcode']].groupby('zipcode').mean().reset_index()
    df4 = data_selection[['price_m2', 'zipcode']].groupby('zipcode').mean().reset_index()


    # merge
    m1 = pd.merge(df1, df2, on='zipcode', how='inner')
    m2 = pd.merge(m1, df3, on='zipcode', how='inner')
    df = pd.merge(m2, df4, on='zipcode', how='inner')

    df.columns = ['ZIPCODE', 'TOTAL HOUSES', 'PRICE', 'SQRT LIVING','PRICE/M2']

    c1.header('Average Values')
    c1.dataframe(df, height=800)

    # Statistic Descriptive
    num_attributes = data_selection.select_dtypes( include=['int64', 'float64'])
    mean = pd.DataFrame(num_attributes.apply(np.mean))
    median = pd.DataFrame(num_attributes.apply(np.median))

    std = pd.DataFrame(num_attributes.apply(np.std))
    max_ = pd.DataFrame(num_attributes.apply(np.max)) 
    min_ = pd.DataFrame(num_attributes.apply(np.min)) 

    df1 = pd.concat([max_, min_, mean, median, std], axis=1).reset_index()

    df1.columns = ['attributes', 'max', 'min', 'mean', 'median', 'std'] 

    c2.header('Descriptive Analysis')
    c2.dataframe(df1, height=800)

    return None

def portfolio_density(data, geofile):
    st.title('Region Overview')

    c1, c2 = st.columns((1, 1))
    c1.header('Portfolio Density')


    df = data.copy().sample(100)

    # Base Map - Folium 
    density_map = folium.Map(location=[data['lat'].mean(), 
                            data['long'].mean()],
                            default_zoom_start=15) 

    marker_cluster = MarkerCluster().add_to(density_map)
    for name, row in df.iterrows():
        folium.Marker([row['lat'], row['long']], 
            popup='Sold R${0} on: {1}. Features: {2} sqft, {3} bedrooms, {4} bathrooms, year built: {5}'.format(
                row['price'],
                row['date'],
                row['sqft_living'],
                row['bedrooms'],
                row['bathrooms'],
                row['yr_built'])).add_to(marker_cluster)


    with c1:
        folium_static(density_map)


    # Region Price Map
    c2.header('Price Density')

    df = data[['price', 'zipcode']].groupby('zipcode').mean().reset_index()
    df.columns = ['ZIP', 'PRICE']

    geofile = geofile[geofile['ZIP'].isin( df['ZIP'].tolist())]

    region_price_map = folium.Map(location=[data['lat'].mean(), 
                                data['long'].mean() ],
                                default_zoom_start=15) 


    region_price_map.choropleth(data = df,
                                geo_data = geofile,
                                columns=['ZIP', 'PRICE'],
                                key_on='feature.properties.ZIP',
                                fill_color='YlOrRd',
                                fill_opacity = 0.7,
                                line_opacity = 0.2,
                                legend_name='AVG PRICE')

    with c2:
        folium_static(region_price_map)
    
    return None

def commercial_distribution(data):
    st.sidebar.title('Commercial Options')
    st.title('Commercial Attributes')

    # Average Price Per Year

    data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')

    # filters
    min_year_built = int(data['yr_built'].min())
    max_year_built = int(data['yr_built'].max())

    st.sidebar.subheader('Select Max Year Built')
    f_year_built = st.sidebar.slider('Year Built', min_year_built, max_year_built, min_year_built)

    st.header('Average Price per Year Built')

    # data selection
    df = data.loc[data['yr_built'] < f_year_built]
    df = df[['yr_built', 'price']].groupby('yr_built').mean().reset_index()

    # plot
    fig = px.line(df, x='yr_built', y='price')
    st.plotly_chart(fig, use_container_width=True)

    # Average Price Per Day
    st.header('Average Price per Day')
    st.sidebar.subheader("Select Max Date")

    # filters
    min_date = datetime.strptime(data['date'].min(), '%Y-%m-%d')
    max_date = datetime.strptime(data['date'].max(), '%Y-%m-%d')

    f_date = st.sidebar.slider('Date', min_date, max_date, min_date)

    # data selection
    data['date'] = pd.to_datetime(data['date'])
    df = data.loc[data['date'] < f_date]
    df = df[['date', 'price']].groupby('date').mean().reset_index()

    # plot
    fig = px.line(df, x='date', y='price')
    st.plotly_chart(fig, use_container_width=True)

    # Histograms
    st.header('Price Distribution')
    st.sidebar.subheader('Select Max Price')

    # filter
    min_price = int(data['price'].min())
    max_price = int(data['price'].max())
    avg_price = int(data['price'].mean())

    f_price = st.sidebar.slider('Price', min_price, max_price, avg_price)

    # data selection
    df = data.loc[data['price'] < f_price]

    # data plot
    fig = px.histogram(df, x='price', nbins=50)
    st.plotly_chart(fig, use_container_width=True)

    return None

def attributes_distribution(data):
    st.sidebar.title('Attributes Options')
    st.title('House Attributes')

    # filters
    f_bedrooms = st.sidebar.selectbox('Max Number of bedrooms', sorted(set(data['bedrooms'].unique())))
    f_bathrooms = st.sidebar.selectbox('Max Number of bathrooms', sorted(set(data['bathrooms'].unique())))
    f_floors = st.sidebar.selectbox('Max Number of floors', sorted(set(data['floors'].unique())))
    f_waterview = st.sidebar.checkbox('Only Houses with Waterview', sorted(set(data['bathrooms'].unique())))

    c1, c2 = st.columns((1, 1))
    c3, c4 = st.columns((1, 1))

    # house per bedrooms
    c1.header('Houses per Bedrooms')
    df = data[data['bedrooms'] < f_bedrooms]
    fig = px.histogram(df, x='bedrooms', nbins=19)
    c1.plotly_chart(fig, use_container_width=True)

    # house per bathrooms
    c2.header('Houses per Bathrooms')
    df = data[data['bathrooms'] < f_bathrooms]
    fig = px.histogram(df, x='bathrooms', nbins=19)
    c2.plotly_chart(fig, use_container_width=True)

    # house per floors
    c3.header('Houses per Floors')
    df = data[data['floors'] < f_floors]
    fig = px.histogram(df, x='floors', nbins=19)
    c3.plotly_chart(fig, use_container_width=True)

    # house per waterview
    c4.header('Houses per Waterview')

    if f_waterview:
        df = data[data['waterfront'] == 1]
    else:
        df = data.copy()

    fig = px.histogram(df, x='waterfront', nbins=19)
    c4.plotly_chart(fig, use_container_width=True)

    return None

def buy_and_sell(data):
    st.title('House to Buy and Sell')

    # creating new features
    data['sqft_price'] = data['price'] / data['sqft_living']
    data['date'] = pd.to_datetime(data['date'])
    data['year'] = data['date'].dt.year
    month_names = {1:'jan', 2:'feb', 3:'mar', 4:'apr', 5:'may', 6:'jun', 7:'jul', 8:'aug', 9:'sep', 10:'oct', 11:'nov', 12:'dec'}
    data['month'] = data['date'].dt.month.replace(month_names)
    data['season'] = data['date'].apply(lambda x: 'spring' if 3 <= x.month <= 5 else 'summer' if 6 <= x.month <= 8 else 'autumn' if 9 <= x.month <= 11 else 'winter')
    
    # creating a new dataframe that contains only the houses to buy
    data_median = data[['zipcode', 'sqft_price']].groupby('zipcode').median().reset_index()
    data_median.rename(columns={'sqft_price':'median_sqft_price'}, inplace=True)
    df = pd.merge(data[['id', 'date', 'season','price', 'condition', 'grade', 'zipcode', 'sqft_price']], data_median, on='zipcode', how='left')
    df['status'] = df[['sqft_price', 'median_sqft_price', 'condition', 'grade']].apply(lambda x: 'buy' if x.sqft_price < x.median_sqft_price and x.condition >= 3 and x.grade >= 7 else 'not buy', axis=1)
    df_buy = df.query("status == 'buy'")
    
    # setting the price at which houses should be sold
    df_buy_median = df_buy[['zipcode', 'season', 'sqft_price']].groupby(['zipcode', 'season']).median().reset_index()
    df_buy_median.rename(columns={'sqft_price':'median_sqft_price_sell'}, inplace=True)
    df_sell = pd.merge(df_buy, df_buy_median, on=['zipcode', 'season'], how='left')
    df_sell['sell_price'] = df_sell[['price', 'sqft_price', 'median_sqft_price_sell']].apply(lambda x: x.price * 1.3 if x.sqft_price < x.median_sqft_price_sell else x.price * 1.1, axis = 1)

    # showing the dataframes
    c1, c2 = st.columns((1, 1))
    c1.header('Houses to be Bought')
    c1.dataframe(df_buy, height=800)
    c2.header('Houses to be Sold')
    c2.dataframe(df_sell, height=800)

    return None

if __name__ == "__main__":
    # data extraction
    path = 'kc_house_data.csv'
    url = 'https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson'
    
    data = get_data(path)
    geofile = get_geofile(url)

    # transformation
    data = set_feature(data)

    overview_data(data)

    portfolio_density(data, geofile)

    commercial_distribution(data)

    attributes_distribution(data)

    buy_and_sell(data)