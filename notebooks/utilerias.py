#I'm gonna use this file to write down some helpful routines
#That I'm gonna use always

#import section
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import trunc

#routines section

def missing_values_table(df):
    # Total missing values by column
    mis_val = df.isnull().sum()
        
    # Percentage of missing values by column
    mis_val_percent = 100 * df.isnull().sum() / len(df)
        
    # build a table with the thw columns
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
        
    # Rename the columns
    mis_val_table_ren_columns = mis_val_table.rename(
    columns = {0 : 'Missing Values', 1 : '% of Total Values'})
        
    # Sort the table by percentage of missing descending
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
        
    # Print some summary information
    print ('Sumary :')
    print ('========================================')
    print (f"Columns     :{str(df.shape[1])}")
    print (f"Null values :{str(mis_val_table_ren_columns.shape[0])}")
    print ('=========================================')
        
           
    return mis_val_table_ren_columns


def exact_values_table(df,fvalue):
    # Total zero values by column
    fval = df[(df == fvalue)].count()
        
    # Percentage of missing values by column
    fval_percent = 100 * df[(df == fvalue)].count() / len(df)
        
    # build a table with the thw columns
    f_val_table = pd.concat([fval, fval_percent], axis=1)
        
    # Rename the columns
    zero_val_table_ren_columns = f_val_table.rename(
    columns = {0 : 'f Values', 1 : '% of Total Values'})
        
    # Sort the table by percentage of zero descending
    zero_val_table_ren_columns = zero_val_table_ren_columns[
        zero_val_table_ren_columns.iloc[:,1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
        
    # Print some summary information
    print ('Sumary :')
    print ('========================================')
    print (f"Columns     :{str(df.shape[1])}")
    print (f"f values :{str(zero_val_table_ren_columns.shape[0])}")
    print ('=========================================')
        
    return zero_val_table_ren_columns

def features_by_type(df):
    # Count of column datatypes for the training dataset
    df_cols = pd.DataFrame(index = ['Features'], columns = ['Integer', 'Float', 'Object'])
    df_cols['Integer'] = len(df.columns[df.dtypes == 'int64'])
    df_cols['Float'] = len(df.columns[df.dtypes == 'float64'])
    df_cols['Object'] = len(df.columns[df.dtypes == 'object'])
    #print(f'shape param: {df.shape}')
    return df_cols

def plot_features_distribution(df):
    plt.figure(figsize=(15,70))
    plotnumber = 1

    num_rows=trunc(len(df.columns)/3)
    if (len(df.columns) % 3) != 0:
        num_rows += 1

    for col in df:
        if plotnumber <= df.shape[1]:
            ax1 = plt.subplot(num_rows,3,plotnumber)
            if df[col].dtypes == 'O':
                sns.countplot(data=df, y=col, palette='Dark2')
            else:
                sns.histplot(data= df, x=col ,palette='Light2')

            plt.xticks(fontsize=12)
            plt.yticks(fontsize=12)
            plt.title(col.title(), fontsize=14)
            plt.xlabel('')
            plt.ylabel('')
        plotnumber +=1
        plt.tight_layout()
    
    plt.show()
    
    return

def checking_skewness(df):
    table = df.skew()
    table = pd.concat([table, df.kurtosis()], axis=1)
    table = table.rename(columns = {0 : 'skewness', 1 : 'kurtosis'})

    # Sort the table by percentage of zero descending
    table = table[table.iloc[:,1] != 0].sort_values('skewness', ascending=False).round(1)
   

    #unpivot = pd.melt(df_bosson, df_bosson.describe().columns[0], df_bosson.describe().columns[1:])

    #g = sns.FacetGrid(unpivot, col="variable", col_wrap=3, sharex=False, sharey=False)
    #g.map(sns.kdeplot, "value")

    #plt.show()
    return table

def plot_outliers(df):

    plt.figure(figsize=(15,70))
    plotnumber = 1

    num_rows=trunc(len(df.columns)/3)
    if (len(df.columns) % 3) != 0:
        num_rows += 1

    for col in df:
        if plotnumber <= df.shape[1]:
            ax1 = plt.subplot(num_rows,3,plotnumber)

            if df[col].dtypes == 'O':
                sns.countplot(data=df, y=col, palette='Dark2')
            else:
                sns.boxplot(y=df[col],palette='Accent')

            plt.xticks(fontsize=12)
            plt.yticks(fontsize=12)
            plt.title(col.title(), fontsize=14)
            plt.xlabel('')
            plt.ylabel('')
        plotnumber +=1
        plt.tight_layout()
    
    plt.show()
    
    return

def drop_outliers_IQR(df,outliers_cols):
    df_to_erase=pd.DataFrame()
    for col in outliers_cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        df_nuevo =df[~(df[col]>= q1 - 1.5 * iqr) & (df[col]<= q3 + 1.5 * iqr)]
        if len(df_nuevo) != 0:
            df_to_erase = pd.concat([df_to_erase,df_nuevo],axis=0)
        
    return df_to_erase


def impute_outliers_IQR(df):
    for col in df.select_dtypes(include = ['float64', 'int64']).columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        upper = df[~(df>(q3+1.5*IQR))].max()
        lower = df[~(df<(q1-1.5*IQR))].min()
        df = df[(df[col] >= q1 - 1.5*iqr) & (df[col] <= q3 + 1.5*iqr)]
    
    q1=df.quantile(0.25)
    q3=df.quantile(0.75)
    IQR=q3-q1
    upper = df[~(df>(q3+1.5*IQR))].max()
    lower = df[~(df<(q1-1.5*IQR))].min()
    df = np.where(df > upper,df.mean(),
                  np.where(df < lower,df.mean(),df)
           )

    return df