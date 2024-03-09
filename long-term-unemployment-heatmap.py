# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:39:27 2024

@author: java
"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Data\LongTermUnemployment.xlsx', sheet_name='Sheet1')
df['Period'] = pd.to_datetime(df['Period']).dt.strftime('%b-%Y')

# Convert period column to categorical data with custom sorting
period_order = ['Jan-2005',
                'Feb-2005',
                'Mar-2005',
                'Apr-2005',
                'May-2005',
                'Jun-2005',
                'Jul-2005',
                'Aug-2005',
                'Sep-2005',
                'Oct-2005',
                'Nov-2005',
                'Dec-2005',
                'Jan-2006',
                'Feb-2006',
                'Mar-2006',
                'Apr-2006',
                'May-2006',
                'Jun-2006',
                'Jul-2006',
                'Aug-2006',
                'Sep-2006',
                'Oct-2006',
                'Nov-2006',
                'Dec-2006',
                'Jan-2007',
                'Feb-2007',
                'Mar-2007',
                'Apr-2007',
                'May-2007',
                'Jun-2007',
                'Jul-2007',
                'Aug-2007',
                'Sep-2007',
                'Oct-2007',
                'Nov-2007',
                'Dec-2007',
                'Jan-2008',
                'Feb-2008',
                'Mar-2008',
                'Apr-2008',
                'May-2008',
                'Jun-2008',
                'Jul-2008',
                'Aug-2008',
                'Sep-2008',
                'Oct-2008',
                'Nov-2008',
                'Dec-2008',
                'Jan-2009',
                'Feb-2009',
                'Mar-2009',
                'Apr-2009',
                'May-2009',
                'Jun-2009',
                'Jul-2009',
                'Aug-2009',
                'Sep-2009',
                'Oct-2009',
                'Nov-2009',
                'Dec-2009',
                'Jan-2010',
                'Feb-2010',
                'Mar-2010',
                'Apr-2010',
                'May-2010',
                'Jun-2010',
                'Jul-2010',
                'Aug-2010',
                'Sep-2010',
                'Oct-2010',
                'Nov-2010',
                'Dec-2010',
                'Jan-2011',
                'Feb-2011',
                'Mar-2011',
                'Apr-2011',
                'May-2011',
                'Jun-2011',
                'Jul-2011',
                'Aug-2011',
                'Sep-2011',
                'Oct-2011',
                'Nov-2011',
                'Dec-2011',
                'Jan-2012',
                'Feb-2012',
                'Mar-2012',
                'Apr-2012',
                'May-2012',
                'Jun-2012',
                'Jul-2012',
                'Aug-2012',
                'Sep-2012',
                'Oct-2012',
                'Nov-2012',
                'Dec-2012',
                'Jan-2013',
                'Feb-2013',
                'Mar-2013',
                'Apr-2013',
                'May-2013',
                'Jun-2013',
                'Jul-2013',
                'Aug-2013',
                'Sep-2013',
                'Oct-2013',
                'Nov-2013',
                'Dec-2013',
                'Jan-2014',
                'Feb-2014',
                'Mar-2014',
                'Apr-2014',
                'May-2014',
                'Jun-2014',
                'Jul-2014',
                'Aug-2014',
                'Sep-2014',
                'Oct-2014',
                'Nov-2014',
                'Dec-2014',
                'Jan-2015',
                'Feb-2015'                
                 ]
df['Period'] = pd.Categorical(df['Period'], categories=period_order, ordered=True)

dff_men = df[df['Gender'] == 'Men'].copy()
dfff_men = dff_men.groupby(by=['Age', 'Period'], as_index=False)['Unemployed'].sum()

dfff = (
    dfff_men
    .pivot(columns=["Age"], index=["Period"], values="Unemployed")
)

dff_women = df[df['Gender'] == 'Women'].copy()
dfff_women = dff_women.groupby(by=['Age', 'Period'], as_index=False)['Unemployed'].sum()

dfff2 = (
    dfff_women
    .pivot(columns=["Age"], index=["Period"], values="Unemployed")
)

# Draw a heatmap with the numeric values in each cell
f, axes = plt.subplots(1, 2, figsize=(10, 12), sharey=True)
f.suptitle("Long Term Unemployment from Jan 2005 to Feb 2015", fontsize=14, fontweight='bold', ha='center')
sns.heatmap(dfff, annot=False, linewidths=.5, ax=axes[0], cbar=False)
sns.heatmap(dfff2, annot=False, linewidths=.5, ax=axes[1], cbar=True)
# f.subplots_adjust(left=0.4)
# axes[1].set_ylabel('')
# axes[0].set_ylabel('')
# axes[0].set_xlabel('')
# axes[1].set_xlabel('')
# axes[0].set_title("Age Group", fontsize=12, fontweight='bold')
# axes[1].set_title("Gender", fontsize=12, fontweight='bold')

# axes[1].tick_params(labelright=False)
# f.align_labels()
# plt.xticks(rotation=90)
# plt.subplots_adjust(wspace=0, hspace=0)

cbar = axes[1].collections[0].colorbar
cbar.set_ticks([500000, 1000000, 1500000, 2000000, 2500000, 3000000, 3500000, 4000000])
cbar.set_ticklabels(['500K', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M'])

# plt.savefig('heatmap.png', dpi=90)

plt.show()

