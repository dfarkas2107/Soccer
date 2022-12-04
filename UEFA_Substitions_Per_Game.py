#Importo paquetes que voy a usar
from operator import index
import pandas         as pd
import numpy          as np
import plotly.express as px
import seaborn        as sns
import plotly
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import matplotlib.pyplot as plt
#Traigo la informacion del CSV con las estadisiticas de La Liga

file_name = "C:/Users/diego/OneDrive/Facultad/Documents/Python/Uefa_Substitutions.xlsx"
sheet ="Pandas"
df = pd.read_excel(io=file_name, sheet_name=sheet)

print(df.head(15)) 

df['CambiosRealizados'] = df['CambiosRealizados'].astype(int)
df['Goles'] = df['Goles'].astype(int)

#Cambio nombre de las columnas
print(df['CambiosRealizados'].median())

Mediana_Cambios_Equipo=df.groupby('Equipo')['CambiosRealizados'].median()
print(Mediana_Cambios_Equipo)

SUM_Goles_Equipo=df.groupby('Equipo')['Goles'].sum()
print(SUM_Goles_Equipo)

sns.barplot(data=df,
            x='Equipo', 
            y='Goles', 
            hue='Equipo',  
            hue_order=None, 
            orient=None, 
            color=None, 
            palette=None
            )
plt.show()
sns.boxplot(data=df,
            x='Equipo', 
            y='CambiosRealizados', 
            hue='Equipo',  
            medianprops={"color": "coral"},
            hue_order=None, 
            orient=None, 
            color=None, 
            palette=None, 
            saturation=0.8, 
            width=8
            )
plt.show()
#print(df.head(15)) 
#Creo un dataframe que me traiga la informacion resumida,con Año,Equipo y sus estadisitcas(Goles Favor,Contra y Goleador del equipo)


