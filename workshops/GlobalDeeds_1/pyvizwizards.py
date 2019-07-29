# Loading Mortality Rate data
def load_mr_data():
    import pandas as pd

    gdp_df = pd.read_csv("https://refactored.s3.amazonaws.com/data/MR_vs_GDP.csv")
    return gdp_df

# Loading Life Expectancy data
def load_le_data():
    import plotly.express as px
    gapminder = px.data.gapminder()
    
    return gapminder

# Mortality Rate Data Selector
def mr_data_selector(dframe, c_list, y_range):
    import pandas as pd
    dframe['comb'] = dframe['Country_or_Area']+dframe['Year'].astype('str')
    dframe.head()
    if len(y_range)==2:
        y_range = range(y_range[0],y_range[1]+1)
        y_range = [str(x) for x in y_range]
    elif len(y_range)==1:
        y_range = [str(x) for x in y_range]
    temp_df = pd.DataFrame(columns=dframe.columns)
    for i in c_list:
        for j in y_range:
            t=i+j
            temp_df = temp_df.append(dframe[dframe['comb']==t],ignore_index=True)
    temp_df = temp_df.drop(['comb'],axis=1)
    
    return temp_df

# Life Expectancy Data Selector
def le_data_selector(dframe, c_list, y_range):
    import pandas as pd
    dframe['comb'] = dframe['country']+dframe['year'].astype('str')
    dframe.head()
    if len(y_range)==2:
        y_range = range(y_range[0],y_range[1]+1)
        y_range = [str(x) for x in y_range]
    elif len(y_range)==1:
        y_range = [str(x) for x in y_range]
    temp_df = pd.DataFrame(columns=dframe.columns)
    for i in c_list:
        for j in y_range:
            t=i+j
            temp_df = temp_df.append(dframe[dframe['comb']==t],ignore_index=True)
    temp_df = temp_df.drop(['comb'],axis=1)
    temp_df['pop'] = temp_df["pop"].astype(str).astype(int)
    
    return temp_df

# Animated Bubble Chart
def animated_le_plot(sliced_df):
    import plotly.express as px
    my_plot = px.scatter(sliced_df, x="gdpPercap", y="lifeExp",
           animation_frame="year", size="pop", color="country",
           log_x=True, range_x=[10,100000], size_max=75,
           range_y=[sliced_df['lifeExp'].min()-10.0,sliced_df['lifeExp'].max()+10.0])
    
    return my_plot

# Trend Line Plot
def gdptrend_mr_plot(sliced_df):
    import plotly.express as px
    
    temp_viz = px.line(sliced_df, x="Year", y="GDP_Per_Capita(USD)", color="Country_or_Area",
              line_group="Country_or_Area", hover_name="Country_or_Area")
    
    return temp_viz

# Pie Chart
def pie_le_plot(sliced_df, yr):
    
    import plotly.offline as ofl
    import plotly.graph_objs as go
    import numpy as np

    ofl.init_notebook_mode()
    
    sliced_df2 = sliced_df.loc[sliced_df['year']==yr].copy()
    
    sliced_df2['GDP_in_bn']=(sliced_df2['gdpPercap']*sliced_df2['pop'])/1000000000
    
    temp_df = sliced_df2.groupby(['continent']).sum()
    
    temp_df = temp_df.sort_values(['continent'])
    
    # Creating labels
    labels = list(temp_df.index.values)

    # Creating values
    values = list(temp_df['GDP_in_bn'])

    # Creating the Pie plot object using the labels and values
    trace = go.Pie(labels=labels, values=values, marker={'colors': ['#EF963B', '#C93277', '#349600', '#EF533B', '#57D4F1']})

    # Visualizing the plot
    ofl.iplot([trace], filename='basic_pie_chart')

# Bar Plot
def bar_le_plot(sliced_df):
    
    import plotly.express as px

    fig = px.bar(sliced_df, x='country', y='lifeExp',
             hover_data=['lifeExp', 'gdpPercap'], color='country', height=400)
    fig.show()

# Map Chart
def map_le_plot(sliced_df):
    
    import plotly.express as px

    fig = px.choropleth(sliced_df, locations="iso_alpha",
                    color="gdpPercap", # lifeExp is a column of gapminder
                    hover_name="country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)
    fig.show()

# Animated Bubble Chart 2
def animated_mr_plot(sliced_df):
    import plotly.express as px
    my_plot = px.scatter(sliced_df, x="GDP_Per_Capita(USD)", y="Mortality_Rate(%)",
           animation_frame="Year", size="Population(mn)", color="Country_or_Area",
           log_x=True, range_x=[10,100000], size_max=75,
           range_y=[sliced_df['Mortality_Rate(%)'].min()-10.0,sliced_df['Mortality_Rate(%)'].max()+10.0])
    
    return my_plot
	
# Animated Bubble Chart 3
def animated_le_plot_grid(sliced_df):
    import plotly.express as px
    fig = px.scatter(sliced_df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country", facet_col="continent",
           log_x=True, size_max=45, range_x=[100,100000], range_y=[25,90])
    
    return fig











