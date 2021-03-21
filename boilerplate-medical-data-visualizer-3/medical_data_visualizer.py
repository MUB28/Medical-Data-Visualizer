import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")



# Add 'overweight' column

df['BMI'] = df['weight']/((df['height']/100)**2)

DATA = np.array([])
for i in df['BMI']:
    if i < 25:
        np.append(DATA, 0)
    else:
        np.append(DATA, 1)

overweight_data = []
for i in df['BMI']:
    if i > 25:
        overweight_data.append(1)
    else:
        overweight_data.append(0)



df['overweight'] = overweight_data

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

cholesterol_data_normalised = []

for i in df['cholesterol']:
    if i == 1:
        cholesterol_data_normalised.append(0)
    elif i > 1:
        cholesterol_data_normalised.append(1)

df['cholesterol'] = cholesterol_data_normalised

gluc_data_normalised = []

for i in df['gluc']:
    if i == 1:
        gluc_data_normalised.append(0)
    elif i > 1:
        gluc_data_normalised.append(1)

df['gluc'] = gluc_data_normalised

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    
    global df

    new_df = df.transpose()

    new_df_cardio0 = df.loc[df['cardio'] == 0].transpose()

    new_df_cardio1 = df.loc[df['cardio'] == 1].transpose()

    # The following variables hold the values needed for the bar chart. They follow the format 'sns_ab' where 'a' is the cardio value and 'b' can be either 0 or 1 (where 0 is good and 1 is bad).  

    sns_00 = [
    
    len(new_df_cardio0.loc['cholesterol']) - new_df_cardio0.loc['cholesterol'].sum(),   
    
    len(new_df_cardio0.loc['gluc']) - new_df_cardio0.loc['gluc'].sum(), 
    
    len(new_df_cardio0.loc['smoke']) - new_df_cardio0.loc['smoke'].sum(),
    
    len(new_df_cardio0.loc['alco']) - new_df_cardio0.loc['alco'].sum(),    
    
    len(new_df_cardio0.loc['active']) - new_df_cardio0.loc['active'].sum(),
    
    len(new_df_cardio0.loc['overweight']) - new_df_cardio0.loc['overweight'].sum()]

    sns_01 = [
    
    new_df_cardio0.loc['cholesterol'].sum(),
    
    new_df_cardio0.loc['gluc'].sum(),
    
    new_df_cardio0.loc['smoke'].sum(),
    
    new_df_cardio0.loc['alco'].sum(),
    
    new_df_cardio0.loc['active'].sum(),
    
    new_df_cardio0.loc['overweight'].sum()]


    sns_10 = [
    
    len(new_df_cardio1.loc['cholesterol']) - new_df_cardio1.loc['cholesterol'].sum(),   
    
    len(new_df_cardio1.loc['gluc']) - new_df_cardio1.loc['gluc'].sum(), 
    
    len(new_df_cardio1.loc['smoke']) - new_df_cardio1.loc['smoke'].sum(),
    
    len(new_df_cardio1.loc['alco']) - new_df_cardio1.loc['alco'].sum(),    
    
    len(new_df_cardio1.loc['active']) - new_df_cardio1.loc['active'].sum(),
    
    len(new_df_cardio1.loc['overweight']) - new_df_cardio1.loc['overweight'].sum()]

    sns_11 = [
    
    
    new_df_cardio1.loc['cholesterol'].sum(),
    
    new_df_cardio1.loc['gluc'].sum(),
    
    new_df_cardio1.loc['smoke'].sum(),
    
    new_df_cardio1.loc['alco'].sum(),
    
    new_df_cardio1.loc['active'].sum(),
    
    new_df_cardio1.loc['overweight'].sum()]

    sns_df0 = new_df_cardio0.loc['cholesterol': 'active'].append(new_df_cardio0.loc['overweight'])

    sns_df1 = new_df_cardio1.loc['cholesterol': 'active'].append(new_df_cardio1.loc['overweight'])

    sns_df0['0'] = sns_00

    sns_df0['1'] = sns_01

    sns_df1['0'] = sns_10

    sns_df1['1'] = sns_11

    cleaned_up = sns_df0.drop(columns = sns_df0.columns[0:35021])

    cleaned_up1 = sns_df1.drop(columns = sns_df1.columns[0:34979])

    X = [4, 3, 0, 1, 5, 2]

    A = np.array([cleaned_up.index[i] for i in X ]) 
    B = np.array([int(cleaned_up['0'][i]) for i in X])
    C = np.array([int(cleaned_up['1'][i]) for i in X])

    D = np.array([cleaned_up1.index[i] for i in X ]) 
    E = np.array([int(cleaned_up1['0'][i]) for i in X]) 
    F = np.array([int(cleaned_up1['1'][i]) for i in X])

    my_data2 = np.stack((A, B, C), axis=1)

    my_data3 = np.stack((D, E, F), axis=1)

    refactored_data0 = pd.DataFrame(my_data2,            columns= ['variable', '0', '1'])

    refactored_data1 = pd.DataFrame(my_data3,
    columns= ['variable', '0', '1'])

    joint_dataframes =  pd.concat([refactored_data0, refactored_data1], axis=1)

    joint_dataframes.columns = ['variable', 'value = 0', 'value = 1', 'variable1', 'Value = 0', 'Value = 1']

    joint_dataframes = joint_dataframes.drop(columns=['variable1'])

    DF1 = pd.melt(joint_dataframes, id_vars = ['variable'], value_vars = ['value = 0', 'value = 1'], var_name= 'value', value_name='total')

    DF2 = pd.melt(joint_dataframes, id_vars = ['variable'], value_vars = ['value = 0', 'value = 1'], var_name= 'value', value_name='total')

    cardio_list = ['0' for i in range(12)] + ['1' for i in range(12)]

    all_dfs = [DF1, DF2]

    for j in all_dfs:
        j.columns = ['variable', 'value', 'total']
    all_dfs = pd.concat(all_dfs).reset_index(drop=True)

    all_dfs['total'] = all_dfs['total'].astype(float)

    all_dfs['cardio'] = cardio_list
    

    
    


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.

    #df_cat = None

    # Draw the catplot with 'sns.catplot()'

    g = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=all_dfs, kind='bar', height=6, aspect=0.8)

    fig = g.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():

    global df

    # Clean the data
    df_heat = df.loc[
    
    df['ap_lo'] <= df['ap_hi']
    
    ].loc[df['height'] >= df['height'].quantile(0.025)

    ].loc[
    df['height'] <= df['height'].quantile(0.975)
    ].loc[
    df['weight'] >= df['weight'].quantile(0.025)
    ].loc[
    df['weight'] <= df['weight'].quantile(0.975)]

    # Calculate the correlation matrix
    corr = df_heat.drop(columns=['BMI']).corr()  .round(1)

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(df_heat.drop(columns=['BMI']).corr().round(1), dtype=bool))



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(16, 8))
    cmap = sns.diverging_palette(230, 20, as_cmap=True, center = 'dark')

    # Draw the heatmap with 'sns.heatmap()'

    sns.heatmap(df_heat.drop(columns=['BMI']).corr().round(1), annot=True, fmt ='.1f',mask=mask, cmap=cmap, vmax=.3, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
