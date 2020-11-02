#!/usr/bin/env python3
import pandas as pd 
from matplotlib import pyplot as plt
import tensorflow as tf
from tensorflow import keras 
from tensorflow.keras import layers 
import numpy as np 
import tensorflow_docs as tfdocs
import tensorflow_docs.plots
import tensorflow_docs.modeling 


#Abottsford British Columbia
abottsfordbc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/abottsford_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_abottsfordbc = pd.DataFrame(abottsfordbc)
df_abottsfordbc["Feb"] = df_abottsfordbc["Feb"].replace(-9999.9, df_abottsfordbc["Feb"].median())
df_abottsfordbc["Oct"] = df_abottsfordbc["Oct"].replace(-9999.9, df_abottsfordbc["Oct"].median())


x1 = df_abottsfordbc["Year"]
y1 = df_abottsfordbc["Winter"]

plt.plot(x1,y1, label = "Winter", color ='b')

x2 = df_abottsfordbc["Year"]
y2 = df_abottsfordbc["Spring"]

plt.plot(x2,y2, label = "Spring", color = 'm')

x3 = df_abottsfordbc["Year"]
y3 = df_abottsfordbc["Summer"]

plt.plot(x3,y3, label = "Summer", color ='c')

x4 = df_abottsfordbc["Year"]
y4 = df_abottsfordbc["Autumn"]

plt.plot(x4,y4, label = "Autumn", color = 'y')

plt.xlabel("Year")
plt.ylabel("km/hour")
plt.title("Abottsford British Columbia")
plt.legend()
plt.show()

#Alert Nunavut
alert_nu = pd.read_csv('/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/alert_nu.csv', engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_alert_nu = pd.DataFrame(alert_nu)

df_alert_nu = pd.DataFrame(alert_nu)
df_alert_nu["Jan"] = df_alert_nu["Jan"].replace(-9999.9, df_alert_nu["Jan"].median())
df_alert_nu["Feb"] = df_alert_nu["Feb"].replace(-9999.9, df_alert_nu["Feb"].median())
df_alert_nu["Mar"] = df_alert_nu["Mar"].replace(-9999.9, df_alert_nu["Mar"].median())
df_alert_nu["Apr"] = df_alert_nu["Apr"].replace(-9999.9, df_alert_nu["Apr"].median())
df_alert_nu["May"] = df_alert_nu["May"].replace(-9999.9, df_alert_nu["May"].median())
df_alert_nu["Jun"] = df_alert_nu["Jun"].replace(-9999.9, df_alert_nu["Jun"].median())
df_alert_nu["Jul"] = df_alert_nu["Jul"].replace(-9999.9, df_alert_nu["Jul"].median())
df_alert_nu["Aug"] = df_alert_nu["Aug"].replace(-9999.9, df_alert_nu["Aug"].median())
df_alert_nu["Sep"] = df_alert_nu["Sep"].replace(-9999.9, df_alert_nu["Sep"].median())
df_alert_nu["Oct"] = df_alert_nu["Oct"].replace(-9999.9, df_alert_nu["Oct"].median())
df_alert_nu["Nov"] = df_alert_nu["Nov"].replace(-9999.9, df_alert_nu["Nov"].median())
df_alert_nu["Dec"] = df_alert_nu["Dec"].replace(-9999.9, df_alert_nu["Dec"].median())
df_alert_nu["Annual"] = df_alert_nu["Annual"].replace(-9999.9, df_alert_nu["Annual"].median())
df_alert_nu["Winter"] = df_alert_nu["Winter"].replace(-9999.9, df_alert_nu["Winter"].median())
df_alert_nu["Spring"] = df_alert_nu["Spring"].replace(-9999.9, df_alert_nu["Spring"].median())
df_alert_nu["Summer"] = df_alert_nu["Summer"].replace(-9999.9, df_alert_nu["Summer"].median())
df_alert_nu["Autumn"] = df_alert_nu["Autumn"].replace(-9999.9, df_alert_nu["Autumn"].median())



#Armstrong Ontario
armstrong_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/armstrong_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_armstrong_ont = pd.DataFrame(armstrong_ont)

df_armstrong_ont = pd.DataFrame(abottsfordbc)
df_armstrong_ont["Jan"] = df_armstrong_ont["Jan"].replace(-9999.9, df_armstrong_ont["Jan"].median())
df_armstrong_ont["Feb"] = df_armstrong_ont["Feb"].replace(-9999.9, df_armstrong_ont["Feb"].median())
df_armstrong_ont["Mar"] = df_armstrong_ont["Mar"].replace(-9999.9, df_armstrong_ont["Mar"].median())
df_armstrong_ont["Apr"] = df_armstrong_ont["Apr"].replace(-9999.9, df_armstrong_ont["Apr"].median())
df_armstrong_ont["May"] = df_armstrong_ont["May"].replace(-9999.9, df_armstrong_ont["May"].median())
df_armstrong_ont["Jun"] = df_armstrong_ont["Jun"].replace(-9999.9, df_armstrong_ont["Jun"].median())
df_armstrong_ont["Jul"] = df_armstrong_ont["Jul"].replace(-9999.9, df_armstrong_ont["Jul"].median())
df_armstrong_ont["Aug"] = df_armstrong_ont["Aug"].replace(-9999.9, df_armstrong_ont["Aug"].median())
df_armstrong_ont["Sep"] = df_armstrong_ont["Sep"].replace(-9999.9, df_armstrong_ont["Sep"].median())
df_armstrong_ont["Oct"] = df_armstrong_ont["Oct"].replace(-9999.9, df_armstrong_ont["Oct"].median())
df_armstrong_ont["Nov"] = df_armstrong_ont["Nov"].replace(-9999.9, df_armstrong_ont["Nov"].median())
df_armstrong_ont["Dec"] = df_armstrong_ont["Dec"].replace(-9999.9, df_armstrong_ont["Dec"].median())
df_armstrong_ont["Annual"] = df_armstrong_ont["Annual"].replace(-9999.9, df_armstrong_ont["Annual"].median())
df_armstrong_ont["Winter"] = df_armstrong_ont["Winter"].replace(-9999.9, df_armstrong_ont["Winter"].median())
df_armstrong_ont["Spring"] = df_armstrong_ont["Spring"].replace(-9999.9, df_armstrong_ont["Spring"].median())
df_armstrong_ont["Summer"] = df_armstrong_ont["Summer"].replace(-9999.9, df_armstrong_ont["Summer"].median())
df_armstrong_ont["Autumn"] = df_armstrong_ont["Autumn"].replace(-9999.9, df_armstrong_ont["Autumn"].median())



#Bagotville Quebec 
bagotville_queb = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/bagotville_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_bagotville_queb = pd.DataFrame(bagotville_queb)

df_bagotville_queb["Jan"] = df_bagotville_queb["Jan"].replace(-9999.9, df_bagotville_queb["Jan"].median())
df_bagotville_queb["Feb"] = df_bagotville_queb["Feb"].replace(-9999.9, df_bagotville_queb["Feb"].median())
df_bagotville_queb["Mar"] = df_bagotville_queb["Mar"].replace(-9999.9, df_bagotville_queb["Mar"].median())
df_bagotville_queb["Apr"] = df_bagotville_queb["Apr"].replace(-9999.9, df_bagotville_queb["Apr"].median())
df_bagotville_queb["May"] = df_bagotville_queb["May"].replace(-9999.9, df_bagotville_queb["May"].median())
df_bagotville_queb["Jun"] = df_bagotville_queb["Jun"].replace(-9999.9, df_bagotville_queb["Jun"].median())
df_bagotville_queb["Jul"] = df_bagotville_queb["Jul"].replace(-9999.9, df_bagotville_queb["Jul"].median())
df_bagotville_queb["Aug"] = df_bagotville_queb["Aug"].replace(-9999.9, df_bagotville_queb["Aug"].median())
df_bagotville_queb["Sep"] = df_bagotville_queb["Sep"].replace(-9999.9, df_bagotville_queb["Sep"].median())
df_bagotville_queb["Oct"] = df_bagotville_queb["Oct"].replace(-9999.9, df_bagotville_queb["Oct"].median())
df_bagotville_queb["Nov"] = df_bagotville_queb["Nov"].replace(-9999.9, df_bagotville_queb["Nov"].median())
df_bagotville_queb["Dec"] = df_bagotville_queb["Dec"].replace(-9999.9, df_bagotville_queb["Dec"].median())
df_bagotville_queb["Annual"] = df_bagotville_queb["Annual"].replace(-9999.9, df_bagotville_queb["Annual"].median())
df_bagotville_queb["Winter"] = df_bagotville_queb["Winter"].replace(-9999.9, df_bagotville_queb["Winter"].median())
df_bagotville_queb["Spring"] = df_bagotville_queb["Spring"].replace(-9999.9, df_bagotville_queb["Spring"].median())
df_bagotville_queb["Summer"] = df_bagotville_queb["Summer"].replace(-9999.9, df_bagotville_queb["Summer"].median())
df_bagotville_queb["Autumn"] = df_bagotville_queb["Autumn"].replace(-9999.9, df_bagotville_queb["Autumn"].median())


#Baiecomeau Quebec
baiecomeau_queb = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/baiecomeau_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_baiecomeau_queb = pd.DataFrame(baiecomeau_queb)

df_baiecomeau_queb["Jan"] = df_baiecomeau_queb["Jan"].replace(-9999.9, df_baiecomeau_queb["Jan"].median())
df_baiecomeau_queb["Feb"] = df_baiecomeau_queb["Feb"].replace(-9999.9, df_baiecomeau_queb["Feb"].median())
df_baiecomeau_queb["Mar"] = df_baiecomeau_queb["Mar"].replace(-9999.9, df_baiecomeau_queb["Mar"].median())
df_baiecomeau_queb["Apr"] = df_baiecomeau_queb["Apr"].replace(-9999.9, df_baiecomeau_queb["Apr"].median())
df_baiecomeau_queb["May"] = df_baiecomeau_queb["May"].replace(-9999.9, df_baiecomeau_queb["May"].median())
df_baiecomeau_queb["Jun"] = df_baiecomeau_queb["Jun"].replace(-9999.9, df_baiecomeau_queb["Jun"].median())
df_baiecomeau_queb["Jul"] = df_baiecomeau_queb["Jul"].replace(-9999.9, df_baiecomeau_queb["Jul"].median())
df_baiecomeau_queb["Aug"] = df_baiecomeau_queb["Aug"].replace(-9999.9, df_baiecomeau_queb["Aug"].median())
df_baiecomeau_queb["Sep"] = df_baiecomeau_queb["Sep"].replace(-9999.9, df_baiecomeau_queb["Sep"].median())
df_baiecomeau_queb["Oct"] = df_baiecomeau_queb["Oct"].replace(-9999.9, df_baiecomeau_queb["Oct"].median())
df_baiecomeau_queb["Nov"] = df_baiecomeau_queb["Nov"].replace(-9999.9, df_baiecomeau_queb["Nov"].median())
df_baiecomeau_queb["Dec"] = df_baiecomeau_queb["Dec"].replace(-9999.9, df_baiecomeau_queb["Dec"].median())
df_baiecomeau_queb["Annual"] = df_baiecomeau_queb["Annual"].replace(-9999.9, df_baiecomeau_queb["Annual"].median())
df_baiecomeau_queb["Winter"] = df_baiecomeau_queb["Winter"].replace(-9999.9, df_baiecomeau_queb["Winter"].median())
df_baiecomeau_queb["Spring"] = df_baiecomeau_queb["Spring"].replace(-9999.9, df_baiecomeau_queb["Spring"].median())
df_baiecomeau_queb["Summer"] = df_baiecomeau_queb["Summer"].replace(-9999.9, df_baiecomeau_queb["Summer"].median())
df_baiecomeau_queb["Autumn"] = df_baiecomeau_queb["Autumn"].replace(-9999.9, df_baiecomeau_queb["Autumn"].median())


#Bakerlake Nunanvut
bakerlake_nu = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/bakerlake_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_bakerlake_nu = pd.DataFrame(bakerlake_nu)

df_bakerlake_nu["Jan"] = df_bakerlake_nu["Jan"].replace(-9999.9, df_bakerlake_nu["Jan"].median())
df_bakerlake_nu["Feb"] = df_bakerlake_nu["Feb"].replace(-9999.9, df_bakerlake_nu["Feb"].median())
df_bakerlake_nu["Mar"] = df_bakerlake_nu["Mar"].replace(-9999.9, df_bakerlake_nu["Mar"].median())
df_bakerlake_nu["Apr"] = df_bakerlake_nu["Apr"].replace(-9999.9, df_bakerlake_nu["Apr"].median())
df_bakerlake_nu["May"] = df_bakerlake_nu["May"].replace(-9999.9, df_bakerlake_nu["May"].median())
df_bakerlake_nu["Jun"] = df_bakerlake_nu["Jun"].replace(-9999.9, df_bakerlake_nu["Jun"].median())
df_bakerlake_nu["Jul"] = df_bakerlake_nu["Jul"].replace(-9999.9, df_bakerlake_nu["Jul"].median())
df_bakerlake_nu["Aug"] = df_bakerlake_nu["Aug"].replace(-9999.9, df_bakerlake_nu["Aug"].median())
df_bakerlake_nu["Sep"] = df_bakerlake_nu["Sep"].replace(-9999.9, df_bakerlake_nu["Sep"].median())
df_bakerlake_nu["Oct"] = df_bakerlake_nu["Oct"].replace(-9999.9, df_bakerlake_nu["Oct"].median())
df_bakerlake_nu["Nov"] = df_bakerlake_nu["Nov"].replace(-9999.9, df_bakerlake_nu["Nov"].median())
df_bakerlake_nu["Dec"] = df_bakerlake_nu["Dec"].replace(-9999.9, df_bakerlake_nu["Dec"].median())
df_bakerlake_nu["Annual"] = df_bakerlake_nu["Annual"].replace(-9999.9, df_bakerlake_nu["Annual"].median())
df_bakerlake_nu["Winter"] = df_bakerlake_nu["Winter"].replace(-9999.9, df_bakerlake_nu["Winter"].median())
df_bakerlake_nu["Spring"] = df_bakerlake_nu["Spring"].replace(-9999.9, df_bakerlake_nu["Spring"].median())
df_bakerlake_nu["Summer"] = df_bakerlake_nu["Summer"].replace(-9999.9, df_bakerlake_nu["Summer"].median())
df_bakerlake_nu["Autumn"] = df_bakerlake_nu["Autumn"].replace(-9999.9, df_bakerlake_nu["Autumn"].median())


#Blueriver British Columbia 
blueriver_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/blueriver_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_blueriver_bc = pd.DataFrame(blueriver_bc)

df_blueriver_bc["Jan"] = df_blueriver_bc["Jan"].replace(-9999.9, df_blueriver_bc["Jan"].median())
df_blueriver_bc["Feb"] = df_blueriver_bc["Feb"].replace(-9999.9, df_blueriver_bc["Feb"].median())
df_blueriver_bc["Mar"] = df_blueriver_bc["Mar"].replace(-9999.9, df_blueriver_bc["Mar"].median())
df_blueriver_bc["Apr"] = df_blueriver_bc["Apr"].replace(-9999.9, df_blueriver_bc["Apr"].median())
df_blueriver_bc["May"] = df_blueriver_bc["May"].replace(-9999.9, df_blueriver_bc["May"].median())
df_blueriver_bc["Jun"] = df_blueriver_bc["Jun"].replace(-9999.9, df_blueriver_bc["Jun"].median())
df_blueriver_bc["Jul"] = df_blueriver_bc["Jul"].replace(-9999.9, df_blueriver_bc["Jul"].median())
df_blueriver_bc["Aug"] = df_blueriver_bc["Aug"].replace(-9999.9, df_blueriver_bc["Aug"].median())
df_blueriver_bc["Sep"] = df_blueriver_bc["Sep"].replace(-9999.9, df_blueriver_bc["Sep"].median())
df_blueriver_bc["Oct"] = df_blueriver_bc["Oct"].replace(-9999.9, df_blueriver_bc["Oct"].median())
df_blueriver_bc["Nov"] = df_blueriver_bc["Nov"].replace(-9999.9, df_blueriver_bc["Nov"].median())
df_blueriver_bc["Dec"] = df_blueriver_bc["Dec"].replace(-9999.9, df_blueriver_bc["Dec"].median())
df_blueriver_bc["Annual"] = df_blueriver_bc["Annual"].replace(-9999.9, df_blueriver_bc["Annual"].median())
df_blueriver_bc["Winter"] = df_blueriver_bc["Winter"].replace(-9999.9, df_blueriver_bc["Winter"].median())
df_blueriver_bc["Spring"] = df_blueriver_bc["Spring"].replace(-9999.9, df_blueriver_bc["Spring"].median())
df_blueriver_bc["Summer"] = df_blueriver_bc["Summer"].replace(-9999.9, df_blueriver_bc["Summer"].median())
df_blueriver_bc["Autumn"] = df_blueriver_bc["Autumn"].replace(-9999.9, df_blueriver_bc["Autumn"].median())


#Bonavista Newfoundland 
bonavista_nfld = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/bonavista_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_bonavista_nfld = pd.DataFrame(bonavista_nfld)    

df_bonavista_nfld["Jan"] = df_bonavista_nfld["Jan"].replace(-9999.9, df_bonavista_nfld["Jan"].median())
df_bonavista_nfld["Feb"] = df_bonavista_nfld["Feb"].replace(-9999.9, df_bonavista_nfld["Feb"].median())
df_bonavista_nfld["Mar"] = df_bonavista_nfld["Mar"].replace(-9999.9, df_bonavista_nfld["Mar"].median())
df_bonavista_nfld["Apr"] = df_bonavista_nfld["Apr"].replace(-9999.9, df_bonavista_nfld["Apr"].median())
df_bonavista_nfld["May"] = df_bonavista_nfld["May"].replace(-9999.9, df_bonavista_nfld["May"].median())
df_bonavista_nfld["Jun"] = df_bonavista_nfld["Jun"].replace(-9999.9, df_bonavista_nfld["Jun"].median())
df_bonavista_nfld["Jul"] = df_bonavista_nfld["Jul"].replace(-9999.9, df_bonavista_nfld["Jul"].median())
df_bonavista_nfld["Aug"] = df_bonavista_nfld["Aug"].replace(-9999.9, df_bonavista_nfld["Aug"].median())
df_bonavista_nfld["Sep"] = df_bonavista_nfld["Sep"].replace(-9999.9, df_bonavista_nfld["Sep"].median())
df_bonavista_nfld["Oct"] = df_bonavista_nfld["Oct"].replace(-9999.9, df_bonavista_nfld["Oct"].median())
df_bonavista_nfld["Nov"] = df_bonavista_nfld["Nov"].replace(-9999.9, df_bonavista_nfld["Nov"].median())
df_bonavista_nfld["Dec"] = df_bonavista_nfld["Dec"].replace(-9999.9, df_bonavista_nfld["Dec"].median())
df_bonavista_nfld["Annual"] = df_bonavista_nfld["Annual"].replace(-9999.9, df_bonavista_nfld["Annual"].median())
df_bonavista_nfld["Winter"] = df_bonavista_nfld["Winter"].replace(-9999.9, df_bonavista_nfld["Winter"].median())
df_bonavista_nfld["Spring"] = df_bonavista_nfld["Spring"].replace(-9999.9, df_bonavista_nfld["Spring"].median())
df_bonavista_nfld["Summer"] = df_bonavista_nfld["Summer"].replace(-9999.9, df_bonavista_nfld["Summer"].median())
df_bonavista_nfld["Autumn"] = df_bonavista_nfld["Autumn"].replace(-9999.9, df_bonavista_nfld["Autumn"].median())


#Brandon Manitoba
brandon_man = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh//brandon_man.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_brandon_man = pd.DataFrame(brandon_man)

df_brandon_man["Jan"] = df_brandon_man["Jan"].replace(-9999.9, df_brandon_man["Jan"].median())
df_brandon_man["Feb"] = df_brandon_man["Feb"].replace(-9999.9, df_brandon_man["Feb"].median())
df_brandon_man["Mar"] = df_brandon_man["Mar"].replace(-9999.9, df_brandon_man["Mar"].median())
df_brandon_man["Apr"] = df_brandon_man["Apr"].replace(-9999.9, df_brandon_man["Apr"].median())
df_brandon_man["May"] = df_brandon_man["May"].replace(-9999.9, df_brandon_man["May"].median())
df_brandon_man["Jun"] = df_brandon_man["Jun"].replace(-9999.9, df_brandon_man["Jun"].median())
df_brandon_man["Jul"] = df_brandon_man["Jul"].replace(-9999.9, df_brandon_man["Jul"].median())
df_brandon_man["Aug"] = df_brandon_man["Aug"].replace(-9999.9, df_brandon_man["Aug"].median())
df_brandon_man["Sep"] = df_brandon_man["Sep"].replace(-9999.9, df_brandon_man["Sep"].median())
df_brandon_man["Oct"] = df_brandon_man["Oct"].replace(-9999.9, df_brandon_man["Oct"].median())
df_brandon_man["Nov"] = df_brandon_man["Nov"].replace(-9999.9, df_brandon_man["Nov"].median())
df_brandon_man["Dec"] = df_brandon_man["Dec"].replace(-9999.9, df_brandon_man["Dec"].median())
df_brandon_man["Annual"] = df_brandon_man["Annual"].replace(-9999.9, df_brandon_man["Annual"].median())
df_brandon_man["Winter"] = df_brandon_man["Winter"].replace(-9999.9, df_brandon_man["Winter"].median())
df_brandon_man["Spring"] = df_brandon_man["Spring"].replace(-9999.9, df_brandon_man["Spring"].median())
df_brandon_man["Summer"] = df_brandon_man["Summer"].replace(-9999.9, df_brandon_man["Summer"].median())
df_brandon_man["Autumn"] = df_brandon_man["Autumn"].replace(-9999.9, df_brandon_man["Autumn"].median())

 
#Broadview Saskatchewan 
broadview_sask = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/broadview_sask.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_broadview_sask = pd.DataFrame(broadview_sask)

df_broadview_sask["Oct"] = df_broadview_sask["Oct"].replace(-9999.9, df_broadview_sask["Oct"].median())

#Burwash Yukon Territories 

burwash_yt = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/burwash_yt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_burwash_yt = pd.DataFrame(burwash_yt)

df_burwash_yt["Jan"] = df_burwash_yt["Jan"].replace(-9999.9, df_burwash_yt["Jan"].median())
df_burwash_yt["Feb"] = df_burwash_yt["Feb"].replace(-9999.9, df_burwash_yt["Feb"].median())
df_burwash_yt["Mar"] = df_burwash_yt["Mar"].replace(-9999.9, df_burwash_yt["Mar"].median())
df_burwash_yt["Apr"] = df_burwash_yt["Apr"].replace(-9999.9, df_burwash_yt["Apr"].median())
df_burwash_yt["May"] = df_burwash_yt["May"].replace(-9999.9, df_burwash_yt["May"].median())
df_burwash_yt["Jun"] = df_burwash_yt["Jun"].replace(-9999.9, df_burwash_yt["Jun"].median())
df_burwash_yt["Jul"] = df_burwash_yt["Jul"].replace(-9999.9, df_burwash_yt["Jul"].median())
df_burwash_yt["Aug"] = df_burwash_yt["Aug"].replace(-9999.9, df_burwash_yt["Aug"].median())
df_burwash_yt["Sep"] = df_burwash_yt["Sep"].replace(-9999.9, df_burwash_yt["Sep"].median())
df_burwash_yt["Oct"] = df_burwash_yt["Oct"].replace(-9999.9, df_burwash_yt["Oct"].median())
df_burwash_yt["Nov"] = df_burwash_yt["Nov"].replace(-9999.9, df_burwash_yt["Nov"].median())
df_burwash_yt["Dec"] = df_burwash_yt["Dec"].replace(-9999.9, df_burwash_yt["Dec"].median())
df_burwash_yt["Annual"] = df_burwash_yt["Annual"].replace(-9999.9, df_burwash_yt["Annual"].median())
df_burwash_yt["Winter"] = df_burwash_yt["Winter"].replace(-9999.9, df_burwash_yt["Winter"].median())
df_burwash_yt["Spring"] = df_burwash_yt["Spring"].replace(-9999.9, df_burwash_yt["Spring"].median())
df_burwash_yt["Summer"] = df_burwash_yt["Summer"].replace(-9999.9, df_burwash_yt["Summer"].median())
df_burwash_yt["Autumn"] = df_burwash_yt["Autumn"].replace(-9999.9, df_burwash_yt["Autumn"].median())


#Calgary Alberta

calgary_alber = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/calgary_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_calgary_alber = pd.DataFrame(calgary_alber)
 
#Cambridgebay Nunavut 
    
cambridgebay_nu = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/cambridgebay_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_cambridgebay_nu = pd.DataFrame(cambridgebay_nu)

#Capehooper Nunavut 
    
capehooper_nu = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/capehooper_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_capehooper_nu = pd.DataFrame(capehooper_nu)

df_capehooper_nu["Jan"] = df_capehooper_nu["Jan"].replace(-9999.9, df_capehooper_nu["Jan"].median())
df_capehooper_nu["Feb"] = df_capehooper_nu["Feb"].replace(-9999.9, df_capehooper_nu["Feb"].median())
df_capehooper_nu["Mar"] = df_capehooper_nu["Mar"].replace(-9999.9, df_capehooper_nu["Mar"].median())
df_capehooper_nu["Apr"] = df_capehooper_nu["Apr"].replace(-9999.9, df_capehooper_nu["Apr"].median())
df_capehooper_nu["May"] = df_capehooper_nu["May"].replace(-9999.9, df_capehooper_nu["May"].median())
df_capehooper_nu["Jun"] = df_capehooper_nu["Jun"].replace(-9999.9, df_capehooper_nu["Jun"].median())
df_capehooper_nu["Jul"] = df_capehooper_nu["Jul"].replace(-9999.9, df_capehooper_nu["Jul"].median())
df_capehooper_nu["Aug"] = df_capehooper_nu["Aug"].replace(-9999.9, df_capehooper_nu["Aug"].median())
df_capehooper_nu["Sep"] = df_capehooper_nu["Sep"].replace(-9999.9, df_capehooper_nu["Sep"].median())
df_capehooper_nu["Oct"] = df_capehooper_nu["Oct"].replace(-9999.9, df_capehooper_nu["Oct"].median())
df_capehooper_nu["Nov"] = df_capehooper_nu["Nov"].replace(-9999.9, df_capehooper_nu["Nov"].median())
df_capehooper_nu["Dec"] = df_capehooper_nu["Dec"].replace(-9999.9, df_capehooper_nu["Dec"].median())
df_capehooper_nu["Annual"] = df_capehooper_nu["Annual"].replace(-9999.9, df_capehooper_nu["Annual"].median())
df_capehooper_nu["Winter"] = df_capehooper_nu["Winter"].replace(-9999.9, df_capehooper_nu["Winter"].median())
df_capehooper_nu["Spring"] = df_capehooper_nu["Spring"].replace(-9999.9, df_capehooper_nu["Spring"].median())
df_capehooper_nu["Summer"] = df_capehooper_nu["Summer"].replace(-9999.9, df_capehooper_nu["Summer"].median())
df_capehooper_nu["Autumn"] = df_capehooper_nu["Autumn"].replace(-9999.9, df_capehooper_nu["Autumn"].median())


#Capeparry North West Territories 

 
capeparry_nwt = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/capeparry_nwt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_capeparry_nwt = pd.DataFrame(capeparry_nwt)

df_capeparry_nwt["Jan"] = df_capeparry_nwt["Jan"].replace(-9999.9, df_capeparry_nwt["Jan"].median())
df_capeparry_nwt["Feb"] = df_capeparry_nwt["Feb"].replace(-9999.9, df_capeparry_nwt["Feb"].median())
df_capeparry_nwt["Mar"] = df_capeparry_nwt["Mar"].replace(-9999.9, df_capeparry_nwt["Mar"].median())
df_capeparry_nwt["Apr"] = df_capeparry_nwt["Apr"].replace(-9999.9, df_capeparry_nwt["Apr"].median())
df_capeparry_nwt["May"] = df_capeparry_nwt["May"].replace(-9999.9, df_capeparry_nwt["May"].median())
df_capeparry_nwt["Jun"] = df_capeparry_nwt["Jun"].replace(-9999.9, df_capeparry_nwt["Jun"].median())
df_capeparry_nwt["Jul"] = df_capeparry_nwt["Jul"].replace(-9999.9, df_capeparry_nwt["Jul"].median())
df_capeparry_nwt["Aug"] = df_capeparry_nwt["Aug"].replace(-9999.9, df_capeparry_nwt["Aug"].median())
df_capeparry_nwt["Sep"] = df_capeparry_nwt["Sep"].replace(-9999.9, df_capeparry_nwt["Sep"].median())
df_capeparry_nwt["Oct"] = df_capeparry_nwt["Oct"].replace(-9999.9, df_capeparry_nwt["Oct"].median())
df_capeparry_nwt["Nov"] = df_capeparry_nwt["Nov"].replace(-9999.9, df_capeparry_nwt["Nov"].median())
df_capeparry_nwt["Dec"] = df_capeparry_nwt["Dec"].replace(-9999.9, df_capeparry_nwt["Dec"].median())
df_capeparry_nwt["Annual"] = df_capeparry_nwt["Annual"].replace(-9999.9, df_capeparry_nwt["Annual"].median())
df_capeparry_nwt["Winter"] = df_capeparry_nwt["Winter"].replace(-9999.9, df_capeparry_nwt["Winter"].median())
df_capeparry_nwt["Spring"] = df_capeparry_nwt["Spring"].replace(-9999.9, df_capeparry_nwt["Spring"].median())
df_capeparry_nwt["Summer"] = df_capeparry_nwt["Summer"].replace(-9999.9, df_capeparry_nwt["Summer"].median())
df_capeparry_nwt["Autumn"] = df_capeparry_nwt["Autumn"].replace(-9999.9, df_capeparry_nwt["Autumn"].median())


#Caperace Newfoundland 
    
caperace_nfld = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/caperace_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_caperace_nfld = pd.DataFrame(caperace_nfld)

df_caperace_nfld["Jan"] = df_caperace_nfld["Jan"].replace(-9999.9, df_caperace_nfld["Jan"].median())
df_caperace_nfld["Feb"] = df_caperace_nfld["Feb"].replace(-9999.9, df_caperace_nfld["Feb"].median())
df_caperace_nfld["Mar"] = df_caperace_nfld["Mar"].replace(-9999.9, df_caperace_nfld["Mar"].median())
df_caperace_nfld["Apr"] = df_caperace_nfld["Apr"].replace(-9999.9, df_caperace_nfld["Apr"].median())
df_caperace_nfld["May"] = df_caperace_nfld["May"].replace(-9999.9, df_caperace_nfld["May"].median())
df_caperace_nfld["Jun"] = df_caperace_nfld["Jun"].replace(-9999.9, df_caperace_nfld["Jun"].median())
df_caperace_nfld["Jul"] = df_caperace_nfld["Jul"].replace(-9999.9, df_caperace_nfld["Jul"].median())
df_caperace_nfld["Aug"] = df_caperace_nfld["Aug"].replace(-9999.9, df_caperace_nfld["Aug"].median())
df_caperace_nfld["Sep"] = df_caperace_nfld["Sep"].replace(-9999.9, df_caperace_nfld["Sep"].median())
df_caperace_nfld["Oct"] = df_caperace_nfld["Oct"].replace(-9999.9, df_caperace_nfld["Oct"].median())
df_caperace_nfld["Nov"] = df_caperace_nfld["Nov"].replace(-9999.9, df_caperace_nfld["Nov"].median())
df_caperace_nfld["Dec"] = df_caperace_nfld["Dec"].replace(-9999.9, df_caperace_nfld["Dec"].median())
df_caperace_nfld["Annual"] = df_caperace_nfld["Annual"].replace(-9999.9, df_caperace_nfld["Annual"].median())
df_caperace_nfld["Winter"] = df_caperace_nfld["Winter"].replace(-9999.9, df_caperace_nfld["Winter"].median())
df_caperace_nfld["Spring"] = df_caperace_nfld["Spring"].replace(-9999.9, df_caperace_nfld["Spring"].median())
df_caperace_nfld["Summer"] = df_caperace_nfld["Summer"].replace(-9999.9, df_caperace_nfld["Summer"].median())
df_caperace_nfld["Autumn"] = df_caperace_nfld["Autumn"].replace(-9999.9, df_caperace_nfld["Autumn"].median())


#Cartwright Newfoundland 

cartwright_nfld = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/cartwright_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_cartwright_nfld = pd.DataFrame(cartwright_nfld)

df_cartwright_nfld["Jan"] = df_cartwright_nfld["Jan"].replace(-9999.9, df_cartwright_nfld["Jan"].median())
df_cartwright_nfld["Feb"] = df_cartwright_nfld["Feb"].replace(-9999.9, df_cartwright_nfld["Feb"].median())
df_cartwright_nfld["Mar"] = df_cartwright_nfld["Mar"].replace(-9999.9, df_cartwright_nfld["Mar"].median())
df_cartwright_nfld["Apr"] = df_cartwright_nfld["Apr"].replace(-9999.9, df_cartwright_nfld["Apr"].median())
df_cartwright_nfld["May"] = df_cartwright_nfld["May"].replace(-9999.9, df_cartwright_nfld["May"].median())
df_cartwright_nfld["Jun"] = df_cartwright_nfld["Jun"].replace(-9999.9, df_cartwright_nfld["Jun"].median())
df_cartwright_nfld["Jul"] = df_cartwright_nfld["Jul"].replace(-9999.9, df_cartwright_nfld["Jul"].median())
df_cartwright_nfld["Aug"] = df_cartwright_nfld["Aug"].replace(-9999.9, df_cartwright_nfld["Aug"].median())
df_cartwright_nfld["Sep"] = df_cartwright_nfld["Sep"].replace(-9999.9, df_cartwright_nfld["Sep"].median())
df_cartwright_nfld["Oct"] = df_cartwright_nfld["Oct"].replace(-9999.9, df_cartwright_nfld["Oct"].median())
df_cartwright_nfld["Nov"] = df_cartwright_nfld["Nov"].replace(-9999.9, df_cartwright_nfld["Nov"].median())
df_cartwright_nfld["Dec"] = df_cartwright_nfld["Dec"].replace(-9999.9, df_cartwright_nfld["Dec"].median())
df_cartwright_nfld["Annual"] = df_cartwright_nfld["Annual"].replace(-9999.9, df_cartwright_nfld["Annual"].median())
df_cartwright_nfld["Winter"] = df_cartwright_nfld["Winter"].replace(-9999.9, df_cartwright_nfld["Winter"].median())
df_cartwright_nfld["Spring"] = df_cartwright_nfld["Spring"].replace(-9999.9, df_cartwright_nfld["Spring"].median())
df_cartwright_nfld["Summer"] = df_cartwright_nfld["Summer"].replace(-9999.9, df_cartwright_nfld["Summer"].median())
df_cartwright_nfld["Autumn"] = df_cartwright_nfld["Autumn"].replace(-9999.9, df_cartwright_nfld["Autumn"].median())


#Castlegar British Columbia 
    
castlegar_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/castlegar_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_castlegar_bc = pd.DataFrame(castlegar_bc)

df_castlegar_bc["Jan"] = df_castlegar_bc["Jan"].replace(-9999.9, df_castlegar_bc["Jan"].median())
df_castlegar_bc["Feb"] = df_castlegar_bc["Feb"].replace(-9999.9, df_castlegar_bc["Feb"].median())
df_castlegar_bc["Mar"] = df_castlegar_bc["Mar"].replace(-9999.9, df_castlegar_bc["Mar"].median())
df_castlegar_bc["Apr"] = df_castlegar_bc["Apr"].replace(-9999.9, df_castlegar_bc["Apr"].median())
df_castlegar_bc["May"] = df_castlegar_bc["May"].replace(-9999.9, df_castlegar_bc["May"].median())
df_castlegar_bc["Jun"] = df_castlegar_bc["Jun"].replace(-9999.9, df_castlegar_bc["Jun"].median())
df_castlegar_bc["Jul"] = df_castlegar_bc["Jul"].replace(-9999.9, df_castlegar_bc["Jul"].median())
df_castlegar_bc["Aug"] = df_castlegar_bc["Aug"].replace(-9999.9, df_castlegar_bc["Aug"].median())
df_castlegar_bc["Sep"] = df_castlegar_bc["Sep"].replace(-9999.9, df_castlegar_bc["Sep"].median())
df_castlegar_bc["Oct"] = df_castlegar_bc["Oct"].replace(-9999.9, df_castlegar_bc["Oct"].median())
df_castlegar_bc["Nov"] = df_castlegar_bc["Nov"].replace(-9999.9, df_castlegar_bc["Nov"].median())
df_castlegar_bc["Dec"] = df_castlegar_bc["Dec"].replace(-9999.9, df_castlegar_bc["Dec"].median())
df_castlegar_bc["Annual"] = df_castlegar_bc["Annual"].replace(-9999.9, df_castlegar_bc["Annual"].median())
df_castlegar_bc["Winter"] = df_castlegar_bc["Winter"].replace(-9999.9, df_castlegar_bc["Winter"].median())
df_castlegar_bc["Spring"] = df_castlegar_bc["Spring"].replace(-9999.9, df_castlegar_bc["Spring"].median())
df_castlegar_bc["Summer"] = df_castlegar_bc["Summer"].replace(-9999.9, df_castlegar_bc["Summer"].median())
df_castlegar_bc["Autumn"] = df_castlegar_bc["Autumn"].replace(-9999.9, df_castlegar_bc["Autumn"].median())


#Charlottetown PEI 
    
charlotte_town_pei = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/charlottetown_pei.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_charlotte_town_pei = pd.DataFrame(charlotte_town_pei)

df_charlotte_town_pei["Jan"] = df_charlotte_town_pei["Jan"].replace(-9999.9, df_charlotte_town_pei["Jan"].median())
df_charlotte_town_pei["Feb"] = df_charlotte_town_pei["Feb"].replace(-9999.9, df_charlotte_town_pei["Feb"].median())
df_charlotte_town_pei["Mar"] = df_charlotte_town_pei["Mar"].replace(-9999.9, df_charlotte_town_pei["Mar"].median())
df_charlotte_town_pei["Apr"] = df_charlotte_town_pei["Apr"].replace(-9999.9, df_charlotte_town_pei["Apr"].median())
df_charlotte_town_pei["May"] = df_charlotte_town_pei["May"].replace(-9999.9, df_charlotte_town_pei["May"].median())
df_charlotte_town_pei["Jun"] = df_charlotte_town_pei["Jun"].replace(-9999.9, df_charlotte_town_pei["Jun"].median())
df_charlotte_town_pei["Jul"] = df_charlotte_town_pei["Jul"].replace(-9999.9, df_charlotte_town_pei["Jul"].median())
df_charlotte_town_pei["Aug"] = df_charlotte_town_pei["Aug"].replace(-9999.9, df_charlotte_town_pei["Aug"].median())
df_charlotte_town_pei["Sep"] = df_charlotte_town_pei["Sep"].replace(-9999.9, df_charlotte_town_pei["Sep"].median())
df_charlotte_town_pei["Oct"] = df_charlotte_town_pei["Oct"].replace(-9999.9, df_charlotte_town_pei["Oct"].median())
df_charlotte_town_pei["Nov"] = df_charlotte_town_pei["Nov"].replace(-9999.9, df_charlotte_town_pei["Nov"].median())
df_charlotte_town_pei["Dec"] = df_charlotte_town_pei["Dec"].replace(-9999.9, df_charlotte_town_pei["Dec"].median())
df_charlotte_town_pei["Annual"] = df_charlotte_town_pei["Annual"].replace(-9999.9, df_charlotte_town_pei["Annual"].median())
df_charlotte_town_pei["Winter"] = df_charlotte_town_pei["Winter"].replace(-9999.9, df_charlotte_town_pei["Winter"].median())
df_charlotte_town_pei["Spring"] = df_charlotte_town_pei["Spring"].replace(-9999.9, df_charlotte_town_pei["Spring"].median())
df_charlotte_town_pei["Summer"] = df_charlotte_town_pei["Summer"].replace(-9999.9, df_charlotte_town_pei["Summer"].median())
df_charlotte_town_pei["Autumn"] = df_charlotte_town_pei["Autumn"].replace(-9999.9, df_charlotte_town_pei["Autumn"].median())


#Churchill Manitoba 
churchill_man = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/churchill_man.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_churchill_man = pd.DataFrame(churchill_man)


#Clyde Nunuvut 
clyde_nu = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/clyde_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_clyde_nu = pd.DataFrame(clyde_nu)

df_clyde_nu["Jan"] = df_clyde_nu["Jan"].replace(-9999.9, df_clyde_nu["Jan"].median())
df_clyde_nu["Feb"] = df_clyde_nu["Feb"].replace(-9999.9, df_clyde_nu["Feb"].median())
df_clyde_nu["Mar"] = df_clyde_nu["Mar"].replace(-9999.9, df_clyde_nu["Mar"].median())
df_clyde_nu["Apr"] = df_clyde_nu["Apr"].replace(-9999.9, df_clyde_nu["Apr"].median())
df_clyde_nu["May"] = df_clyde_nu["May"].replace(-9999.9, df_clyde_nu["May"].median())
df_clyde_nu["Jun"] = df_clyde_nu["Jun"].replace(-9999.9, df_clyde_nu["Jun"].median())
df_clyde_nu["Jul"] = df_clyde_nu["Jul"].replace(-9999.9, df_clyde_nu["Jul"].median())
df_clyde_nu["Aug"] = df_clyde_nu["Aug"].replace(-9999.9, df_clyde_nu["Aug"].median())
df_clyde_nu["Sep"] = df_clyde_nu["Sep"].replace(-9999.9, df_clyde_nu["Sep"].median())
df_clyde_nu["Oct"] = df_clyde_nu["Oct"].replace(-9999.9, df_clyde_nu["Oct"].median())
df_clyde_nu["Nov"] = df_clyde_nu["Nov"].replace(-9999.9, df_clyde_nu["Nov"].median())
df_clyde_nu["Dec"] = df_clyde_nu["Dec"].replace(-9999.9, df_clyde_nu["Dec"].median())
df_clyde_nu["Annual"] = df_clyde_nu["Annual"].replace(-9999.9, df_clyde_nu["Annual"].median())
df_clyde_nu["Winter"] = df_clyde_nu["Winter"].replace(-9999.9, df_clyde_nu["Winter"].median())
df_clyde_nu["Spring"] = df_clyde_nu["Spring"].replace(-9999.9, df_clyde_nu["Spring"].median())
df_clyde_nu["Summer"] = df_clyde_nu["Summer"].replace(-9999.9, df_clyde_nu["Summer"].median())
df_clyde_nu["Autumn"] = df_clyde_nu["Autumn"].replace(-9999.9, df_clyde_nu["Autumn"].median())


#Coldlake Alberta    
coldlake_alber = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/coldlake_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_coldlake_alber = pd.DataFrame(coldlake_alber)

df_coldlake_alber["Jan"] = df_coldlake_alber["Jan"].replace(-9999.9, df_coldlake_alber["Jan"].median())
df_coldlake_alber["Feb"] = df_coldlake_alber["Feb"].replace(-9999.9, df_coldlake_alber["Feb"].median())
df_coldlake_alber["Mar"] = df_coldlake_alber["Mar"].replace(-9999.9, df_coldlake_alber["Mar"].median())
df_coldlake_alber["Apr"] = df_coldlake_alber["Apr"].replace(-9999.9, df_coldlake_alber["Apr"].median())
df_coldlake_alber["May"] = df_coldlake_alber["May"].replace(-9999.9, df_coldlake_alber["May"].median())
df_coldlake_alber["Jun"] = df_coldlake_alber["Jun"].replace(-9999.9, df_coldlake_alber["Jun"].median())
df_coldlake_alber["Jul"] = df_coldlake_alber["Jul"].replace(-9999.9, df_coldlake_alber["Jul"].median())
df_coldlake_alber["Aug"] = df_coldlake_alber["Aug"].replace(-9999.9, df_coldlake_alber["Aug"].median())
df_coldlake_alber["Sep"] = df_coldlake_alber["Sep"].replace(-9999.9, df_coldlake_alber["Sep"].median())
df_coldlake_alber["Oct"] = df_coldlake_alber["Oct"].replace(-9999.9, df_coldlake_alber["Oct"].median())
df_coldlake_alber["Nov"] = df_coldlake_alber["Nov"].replace(-9999.9, df_coldlake_alber["Nov"].median())
df_coldlake_alber["Dec"] = df_coldlake_alber["Dec"].replace(-9999.9, df_coldlake_alber["Dec"].median())
df_coldlake_alber["Annual"] = df_coldlake_alber["Annual"].replace(-9999.9, df_coldlake_alber["Annual"].median())
df_coldlake_alber["Winter"] = df_coldlake_alber["Winter"].replace(-9999.9, df_coldlake_alber["Winter"].median())
df_coldlake_alber["Spring"] = df_coldlake_alber["Spring"].replace(-9999.9, df_coldlake_alber["Spring"].median())
df_coldlake_alber["Summer"] = df_coldlake_alber["Summer"].replace(-9999.9, df_coldlake_alber["Summer"].median())
df_coldlake_alber["Autumn"] = df_coldlake_alber["Autumn"].replace(-9999.9, df_coldlake_alber["Autumn"].median())


#Comox British Columbia

comox_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/comox_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding= 'utf-8-sig')
df_comox_bc = pd.DataFrame(comox_bc)


#Coral Harbour Nunavut 

coralharbour_nu = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/coralharbour_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding= 'utf-8-sig')
df_coralharbour_nu = pd.DataFrame(coralharbour_nu)

df_coralharbour_nu["Oct"] = df_coralharbour_nu["Oct"].replace(-9999.9, df_coralharbour_nu["Oct"].median())
df_coralharbour_nu["Nov"] = df_coralharbour_nu["Nov"].replace(-9999.9, df_coralharbour_nu["Nov"].median())
df_coralharbour_nu["Autumn"] = df_coralharbour_nu["Autumn"].replace(-9999.9, df_coralharbour_nu["Autumn"].median())


#Coronation Alberta 
    
coronation_alber = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/coronation_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding= 'utf-8-sig')
df_coronation_alber = pd.DataFrame(coronation_alber)

df_coronation_alber["Dec"] = df_coronation_alber["Dec"].replace(-9999.9, df_coronation_alber["Dec"].median())


#Cranbrook British Columbia 
        
cranbrook_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/cranbrook_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding= 'utf-8-sig')
df_cranbrook_bc = pd.DataFrame(cranbrook_bc)

df_cranbrook_bc["Jan"] = df_cranbrook_bc["Jan"].replace(-9999.9, df_cranbrook_bc["Jan"].median())
df_cranbrook_bc["Feb"] = df_cranbrook_bc["Feb"].replace(-9999.9, df_cranbrook_bc["Feb"].median())
df_cranbrook_bc["Mar"] = df_cranbrook_bc["Mar"].replace(-9999.9, df_cranbrook_bc["Mar"].median())
df_cranbrook_bc["Apr"] = df_cranbrook_bc["Apr"].replace(-9999.9, df_cranbrook_bc["Apr"].median())
df_cranbrook_bc["May"] = df_cranbrook_bc["May"].replace(-9999.9, df_cranbrook_bc["May"].median())
df_cranbrook_bc["Jun"] = df_cranbrook_bc["Jun"].replace(-9999.9, df_cranbrook_bc["Jun"].median())
df_cranbrook_bc["Jul"] = df_cranbrook_bc["Jul"].replace(-9999.9, df_cranbrook_bc["Jul"].median())
df_cranbrook_bc["Aug"] = df_cranbrook_bc["Aug"].replace(-9999.9, df_cranbrook_bc["Aug"].median())
df_cranbrook_bc["Sep"] = df_cranbrook_bc["Sep"].replace(-9999.9, df_cranbrook_bc["Sep"].median())
df_cranbrook_bc["Oct"] = df_cranbrook_bc["Oct"].replace(-9999.9, df_cranbrook_bc["Oct"].median())
df_cranbrook_bc["Nov"] = df_cranbrook_bc["Nov"].replace(-9999.9, df_cranbrook_bc["Nov"].median())
df_cranbrook_bc["Dec"] = df_cranbrook_bc["Dec"].replace(-9999.9, df_cranbrook_bc["Dec"].median())
df_cranbrook_bc["Annual"] = df_cranbrook_bc["Annual"].replace(-9999.9, df_cranbrook_bc["Annual"].median())
df_cranbrook_bc["Winter"] = df_cranbrook_bc["Winter"].replace(-9999.9, df_cranbrook_bc["Winter"].median())
df_cranbrook_bc["Spring"] = df_cranbrook_bc["Spring"].replace(-9999.9, df_cranbrook_bc["Spring"].median())
df_cranbrook_bc["Summer"] = df_cranbrook_bc["Summer"].replace(-9999.9, df_cranbrook_bc["Summer"].median())
df_cranbrook_bc["Autumn"] = df_cranbrook_bc["Autumn"].replace(-9999.9, df_cranbrook_bc["Autumn"].median())
 

#Danielsharbour Newfoundland 

danielsharbour_nfld = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/danielsharbour_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_danielsharbour_nfld = pd.DataFrame(danielsharbour_nfld)

df_danielsharbour_nfld.dropna(axis = 1, how='all', inplace = True)
df_danielsharbour_nfld.dropna(axis = 0, how='all', inplace = True)

df_danielsharbour_nfld["Jan"] = df_danielsharbour_nfld["Jan"].replace(-9999.9, df_danielsharbour_nfld["Jan"].median())
df_danielsharbour_nfld["Feb"] = df_danielsharbour_nfld["Feb"].replace(-9999.9, df_danielsharbour_nfld["Feb"].median())
df_danielsharbour_nfld["Mar"] = df_danielsharbour_nfld["Mar"].replace(-9999.9, df_danielsharbour_nfld["Mar"].median())
df_danielsharbour_nfld["Apr"] = df_danielsharbour_nfld["Apr"].replace(-9999.9, df_danielsharbour_nfld["Apr"].median())
df_danielsharbour_nfld["May"] = df_danielsharbour_nfld["May"].replace(-9999.9, df_danielsharbour_nfld["May"].median())
df_danielsharbour_nfld["Jun"] = df_danielsharbour_nfld["Jun"].replace(-9999.9, df_danielsharbour_nfld["Jun"].median())
df_danielsharbour_nfld["Jul"] = df_danielsharbour_nfld["Jul"].replace(-9999.9, df_danielsharbour_nfld["Jul"].median())
df_danielsharbour_nfld["Aug"] = df_danielsharbour_nfld["Aug"].replace(-9999.9, df_danielsharbour_nfld["Aug"].median())
df_danielsharbour_nfld["Sep"] = df_danielsharbour_nfld["Sep"].replace(-9999.9, df_danielsharbour_nfld["Sep"].median())
df_danielsharbour_nfld["Oct"] = df_danielsharbour_nfld["Oct"].replace(-9999.9, df_danielsharbour_nfld["Oct"].median())
df_danielsharbour_nfld["Nov"] = df_danielsharbour_nfld["Nov"].replace(-9999.9, df_danielsharbour_nfld["Nov"].median())
df_danielsharbour_nfld["Dec"] = df_danielsharbour_nfld["Dec"].replace(-9999.9, df_danielsharbour_nfld["Dec"].median())
df_danielsharbour_nfld["Annual"] = df_danielsharbour_nfld["Annual"].replace(-9999.9, df_danielsharbour_nfld["Annual"].median())
df_danielsharbour_nfld["Winter"] = df_danielsharbour_nfld["Winter"].replace(-9999.9, df_danielsharbour_nfld["Winter"].median())
df_danielsharbour_nfld["Spring"] = df_danielsharbour_nfld["Spring"].replace(-9999.9, df_danielsharbour_nfld["Spring"].median())
df_danielsharbour_nfld["Summer"] = df_danielsharbour_nfld["Summer"].replace(-9999.9, df_danielsharbour_nfld["Summer"].median())
df_danielsharbour_nfld["Autumn"] = df_danielsharbour_nfld["Autumn"].replace(-9999.9, df_danielsharbour_nfld["Autumn"].median())


#Dauphin Manitoba 

dauphin_man = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/dauphin_man.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_dauphin_man = pd.DataFrame(dauphin_man)

#Dawsoncreek British Columbia 

dawsoncreek_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/dawsoncreek_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_dawsoncreek_bc = pd.DataFrame(dawsoncreek_bc)


df_dawsoncreek_bc["Jan"] = df_dawsoncreek_bc["Jan"].replace(-9999.9, df_dawsoncreek_bc["Jan"].median())
df_dawsoncreek_bc["Feb"] = df_dawsoncreek_bc["Feb"].replace(-9999.9, df_dawsoncreek_bc["Feb"].median())
df_dawsoncreek_bc["Mar"] = df_dawsoncreek_bc["Mar"].replace(-9999.9, df_dawsoncreek_bc["Mar"].median())
df_dawsoncreek_bc["Apr"] = df_dawsoncreek_bc["Apr"].replace(-9999.9, df_dawsoncreek_bc["Apr"].median())
df_dawsoncreek_bc["May"] = df_dawsoncreek_bc["May"].replace(-9999.9, df_dawsoncreek_bc["May"].median())
df_dawsoncreek_bc["Jun"] = df_dawsoncreek_bc["Jun"].replace(-9999.9, df_dawsoncreek_bc["Jun"].median())
df_dawsoncreek_bc["Jul"] = df_dawsoncreek_bc["Jul"].replace(-9999.9, df_dawsoncreek_bc["Jul"].median())
df_dawsoncreek_bc["Aug"] = df_dawsoncreek_bc["Aug"].replace(-9999.9, df_dawsoncreek_bc["Aug"].median())
df_dawsoncreek_bc["Sep"] = df_dawsoncreek_bc["Sep"].replace(-9999.9, df_dawsoncreek_bc["Sep"].median())
df_dawsoncreek_bc["Oct"] = df_dawsoncreek_bc["Oct"].replace(-9999.9, df_dawsoncreek_bc["Oct"].median())
df_dawsoncreek_bc["Nov"] = df_dawsoncreek_bc["Nov"].replace(-9999.9, df_dawsoncreek_bc["Nov"].median())
df_dawsoncreek_bc["Dec"] = df_dawsoncreek_bc["Dec"].replace(-9999.9, df_dawsoncreek_bc["Dec"].median())
df_dawsoncreek_bc["Annual"] = df_dawsoncreek_bc["Annual"].replace(-9999.9, df_dawsoncreek_bc["Annual"].median())
df_dawsoncreek_bc["Winter"] = df_dawsoncreek_bc["Winter"].replace(-9999.9, df_dawsoncreek_bc["Winter"].median())
df_dawsoncreek_bc["Spring"] = df_dawsoncreek_bc["Spring"].replace(-9999.9, df_dawsoncreek_bc["Spring"].median())
df_dawsoncreek_bc["Summer"] = df_dawsoncreek_bc["Summer"].replace(-9999.9, df_dawsoncreek_bc["Summer"].median())
df_dawsoncreek_bc["Autumn"] = df_dawsoncreek_bc["Autumn"].replace(-9999.9, df_dawsoncreek_bc["Autumn"].median())


#Deaselake British Columbia 
    
deaselake_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/deaselake_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_deaselake_bc = pd.DataFrame(deaselake_bc)

df_deaselake_bc["Jan"] = df_deaselake_bc["Jan"].replace(-9999.9, df_deaselake_bc["Jan"].median())
df_deaselake_bc["Feb"] = df_deaselake_bc["Feb"].replace(-9999.9, df_deaselake_bc["Feb"].median())
df_deaselake_bc["Mar"] = df_deaselake_bc["Mar"].replace(-9999.9, df_deaselake_bc["Mar"].median())
df_deaselake_bc["Apr"] = df_deaselake_bc["Apr"].replace(-9999.9, df_deaselake_bc["Apr"].median())
df_deaselake_bc["May"] = df_deaselake_bc["May"].replace(-9999.9, df_deaselake_bc["May"].median())
df_deaselake_bc["Jun"] = df_deaselake_bc["Jun"].replace(-9999.9, df_deaselake_bc["Jun"].median())
df_deaselake_bc["Jul"] = df_deaselake_bc["Jul"].replace(-9999.9, df_deaselake_bc["Jul"].median())
df_deaselake_bc["Aug"] = df_deaselake_bc["Aug"].replace(-9999.9, df_deaselake_bc["Aug"].median())
df_deaselake_bc["Sep"] = df_deaselake_bc["Sep"].replace(-9999.9, df_deaselake_bc["Sep"].median())
df_deaselake_bc["Oct"] = df_deaselake_bc["Oct"].replace(-9999.9, df_deaselake_bc["Oct"].median())
df_deaselake_bc["Nov"] = df_deaselake_bc["Nov"].replace(-9999.9, df_deaselake_bc["Nov"].median())
df_deaselake_bc["Dec"] = df_deaselake_bc["Dec"].replace(-9999.9, df_deaselake_bc["Dec"].median())
df_deaselake_bc["Annual"] = df_deaselake_bc["Annual"].replace(-9999.9, df_deaselake_bc["Annual"].median())
df_deaselake_bc["Winter"] = df_deaselake_bc["Winter"].replace(-9999.9, df_deaselake_bc["Winter"].median())
df_deaselake_bc["Spring"] = df_deaselake_bc["Spring"].replace(-9999.9, df_deaselake_bc["Spring"].median())
df_deaselake_bc["Summer"] = df_deaselake_bc["Summer"].replace(-9999.9, df_deaselake_bc["Summer"].median())
df_deaselake_bc["Autumn"] = df_deaselake_bc["Autumn"].replace(-9999.9, df_deaselake_bc["Autumn"].median())

#Deerlake Newfoundland 
    
deerlake_nfld = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/deerlake_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_deerlake_nfld = pd.DataFrame(deerlake_nfld)

df_deerlake_nfld["Jan"] = df_deerlake_nfld["Jan"].replace(-9999.9, df_deerlake_nfld["Jan"].median())
df_deerlake_nfld["Feb"] = df_deerlake_nfld["Feb"].replace(-9999.9, df_deerlake_nfld["Feb"].median())
df_deerlake_nfld["Mar"] = df_deerlake_nfld["Mar"].replace(-9999.9, df_deerlake_nfld["Mar"].median())
df_deerlake_nfld["Apr"] = df_deerlake_nfld["Apr"].replace(-9999.9, df_deerlake_nfld["Apr"].median())
df_deerlake_nfld["May"] = df_deerlake_nfld["May"].replace(-9999.9, df_deerlake_nfld["May"].median())
df_deerlake_nfld["Jun"] = df_deerlake_nfld["Jun"].replace(-9999.9, df_deerlake_nfld["Jun"].median())
df_deerlake_nfld["Jul"] = df_deerlake_nfld["Jul"].replace(-9999.9, df_deerlake_nfld["Jul"].median())
df_deerlake_nfld["Aug"] = df_deerlake_nfld["Aug"].replace(-9999.9, df_deerlake_nfld["Aug"].median())
df_deerlake_nfld["Sep"] = df_deerlake_nfld["Sep"].replace(-9999.9, df_deerlake_nfld["Sep"].median())
df_deerlake_nfld["Oct"] = df_deerlake_nfld["Oct"].replace(-9999.9, df_deerlake_nfld["Oct"].median())
df_deerlake_nfld["Nov"] = df_deerlake_nfld["Nov"].replace(-9999.9, df_deerlake_nfld["Nov"].median())
df_deerlake_nfld["Dec"] = df_deerlake_nfld["Dec"].replace(-9999.9, df_deerlake_nfld["Dec"].median())
df_deerlake_nfld["Annual"] = df_deerlake_nfld["Annual"].replace(-9999.9, df_deerlake_nfld["Annual"].median())
df_deerlake_nfld["Winter"] = df_deerlake_nfld["Winter"].replace(-9999.9, df_deerlake_nfld["Winter"].median())
df_deerlake_nfld["Spring"] = df_deerlake_nfld["Spring"].replace(-9999.9, df_deerlake_nfld["Spring"].median())
df_deerlake_nfld["Summer"] = df_deerlake_nfld["Summer"].replace(-9999.9, df_deerlake_nfld["Summer"].median())
df_deerlake_nfld["Autumn"] = df_deerlake_nfld["Autumn"].replace(-9999.9, df_deerlake_nfld["Autumn"].median())
 

#Dewarlakes Nunuvut 

dewarlakes_nu = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/dewarlakes_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_dewarlakes_nu = pd.DataFrame(dewarlakes_nu)

df_dewarlakes_nu["Jan"] = df_dewarlakes_nu["Jan"].replace(-9999.9, df_dewarlakes_nu["Jan"].median())
df_dewarlakes_nu["Feb"] = df_dewarlakes_nu["Feb"].replace(-9999.9, df_dewarlakes_nu["Feb"].median())
df_dewarlakes_nu["Mar"] = df_dewarlakes_nu["Mar"].replace(-9999.9, df_dewarlakes_nu["Mar"].median())
df_dewarlakes_nu["Apr"] = df_dewarlakes_nu["Apr"].replace(-9999.9, df_dewarlakes_nu["Apr"].median())
df_dewarlakes_nu["May"] = df_dewarlakes_nu["May"].replace(-9999.9, df_dewarlakes_nu["May"].median())
df_dewarlakes_nu["Jun"] = df_dewarlakes_nu["Jun"].replace(-9999.9, df_dewarlakes_nu["Jun"].median())
df_dewarlakes_nu["Jul"] = df_dewarlakes_nu["Jul"].replace(-9999.9, df_dewarlakes_nu["Jul"].median())
df_dewarlakes_nu["Aug"] = df_dewarlakes_nu["Aug"].replace(-9999.9, df_dewarlakes_nu["Aug"].median())
df_dewarlakes_nu["Sep"] = df_dewarlakes_nu["Sep"].replace(-9999.9, df_dewarlakes_nu["Sep"].median())
df_dewarlakes_nu["Oct"] = df_dewarlakes_nu["Oct"].replace(-9999.9, df_dewarlakes_nu["Oct"].median())
df_dewarlakes_nu["Nov"] = df_dewarlakes_nu["Nov"].replace(-9999.9, df_dewarlakes_nu["Nov"].median())
df_dewarlakes_nu["Dec"] = df_dewarlakes_nu["Dec"].replace(-9999.9, df_dewarlakes_nu["Dec"].median())
df_dewarlakes_nu["Annual"] = df_dewarlakes_nu["Annual"].replace(-9999.9, df_dewarlakes_nu["Annual"].median())
df_dewarlakes_nu["Winter"] = df_dewarlakes_nu["Winter"].replace(-9999.9, df_dewarlakes_nu["Winter"].median())
df_dewarlakes_nu["Spring"] = df_dewarlakes_nu["Spring"].replace(-9999.9, df_dewarlakes_nu["Spring"].median())
df_dewarlakes_nu["Summer"] = df_dewarlakes_nu["Summer"].replace(-9999.9, df_dewarlakes_nu["Summer"].median())
df_dewarlakes_nu["Autumn"] = df_dewarlakes_nu["Autumn"].replace(-9999.9, df_dewarlakes_nu["Autumn"].median())
 

#Earlton Ontario 

earlton_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/earlton_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_earlton_ont = pd.DataFrame(earlton_ont)

df_earlton_ont["Feb"] = df_earlton_ont["Feb"].replace(-9999.9, df_earlton_ont["Feb"].median())
df_earlton_ont["Jul"] = df_earlton_ont["Jul"].replace(-9999.9, df_earlton_ont["Jul"].median())


#Edmonton Alberta

edmonton_alber = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/edmonton_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_edmonton_alber = pd.DataFrame(edmonton_alber)

df_edmonton_alber["Jan"] = df_edmonton_alber["Jan"].replace(-9999.9, df_edmonton_alber["Jan"].median())
df_edmonton_alber["Feb"] = df_edmonton_alber["Feb"].replace(-9999.9, df_edmonton_alber["Feb"].median())
df_edmonton_alber["Mar"] = df_edmonton_alber["Mar"].replace(-9999.9, df_edmonton_alber["Mar"].median())
df_edmonton_alber["Apr"] = df_edmonton_alber["Apr"].replace(-9999.9, df_edmonton_alber["Apr"].median())
df_edmonton_alber["May"] = df_edmonton_alber["May"].replace(-9999.9, df_edmonton_alber["May"].median())
df_edmonton_alber["Jun"] = df_edmonton_alber["Jun"].replace(-9999.9, df_edmonton_alber["Jun"].median())
df_edmonton_alber["Jul"] = df_edmonton_alber["Jul"].replace(-9999.9, df_edmonton_alber["Jul"].median())
df_edmonton_alber["Aug"] = df_edmonton_alber["Aug"].replace(-9999.9, df_edmonton_alber["Aug"].median())
df_edmonton_alber["Sep"] = df_edmonton_alber["Sep"].replace(-9999.9, df_edmonton_alber["Sep"].median())
df_edmonton_alber["Oct"] = df_edmonton_alber["Oct"].replace(-9999.9, df_edmonton_alber["Oct"].median())
df_edmonton_alber["Nov"] = df_edmonton_alber["Nov"].replace(-9999.9, df_edmonton_alber["Nov"].median())
df_edmonton_alber["Dec"] = df_edmonton_alber["Dec"].replace(-9999.9, df_edmonton_alber["Dec"].median())
df_edmonton_alber["Annual"] = df_edmonton_alber["Annual"].replace(-9999.9, df_edmonton_alber["Annual"].median())
df_edmonton_alber["Winter"] = df_edmonton_alber["Winter"].replace(-9999.9, df_edmonton_alber["Winter"].median())
df_edmonton_alber["Spring"] = df_edmonton_alber["Spring"].replace(-9999.9, df_edmonton_alber["Spring"].median())
df_edmonton_alber["Summer"] = df_edmonton_alber["Summer"].replace(-9999.9, df_edmonton_alber["Summer"].median())
df_edmonton_alber["Autumn"] = df_edmonton_alber["Autumn"].replace(-9999.9, df_edmonton_alber["Autumn"].median())
 

#Edmonton City Centre Alberta 

edmontoncitycentre_alber = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/edmontoncitycentre_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_edmontoncitycentre_alber = pd.DataFrame(edmontoncitycentre_alber)
   
#Edmontonnamao Alberta 

edmontonnamao_alber = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/edmontonnamao_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_edmontonnamao_alber = pd.DataFrame(edmontonnamao_alber)

df_edmontonnamao_alber["Jan"] = df_edmontonnamao_alber["Jan"].replace(-9999.9, df_edmontonnamao_alber["Jan"].median())
df_edmontonnamao_alber["Feb"] = df_edmontonnamao_alber["Feb"].replace(-9999.9, df_edmontonnamao_alber["Feb"].median())
df_edmontonnamao_alber["Mar"] = df_edmontonnamao_alber["Mar"].replace(-9999.9, df_edmontonnamao_alber["Mar"].median())
df_edmontonnamao_alber["Apr"] = df_edmontonnamao_alber["Apr"].replace(-9999.9, df_edmontonnamao_alber["Apr"].median())
df_edmontonnamao_alber["May"] = df_edmontonnamao_alber["May"].replace(-9999.9, df_edmontonnamao_alber["May"].median())
df_edmontonnamao_alber["Jun"] = df_edmontonnamao_alber["Jun"].replace(-9999.9, df_edmontonnamao_alber["Jun"].median())
df_edmontonnamao_alber["Jul"] = df_edmontonnamao_alber["Jul"].replace(-9999.9, df_edmontonnamao_alber["Jul"].median())
df_edmontonnamao_alber["Aug"] = df_edmontonnamao_alber["Aug"].replace(-9999.9, df_edmontonnamao_alber["Aug"].median())
df_edmontonnamao_alber["Sep"] = df_edmontonnamao_alber["Sep"].replace(-9999.9, df_edmontonnamao_alber["Sep"].median())
df_edmontonnamao_alber["Oct"] = df_edmontonnamao_alber["Oct"].replace(-9999.9, df_edmontonnamao_alber["Oct"].median())
df_edmontonnamao_alber["Nov"] = df_edmontonnamao_alber["Nov"].replace(-9999.9, df_edmontonnamao_alber["Nov"].median())
df_edmontonnamao_alber["Dec"] = df_edmontonnamao_alber["Dec"].replace(-9999.9, df_edmontonnamao_alber["Dec"].median())
df_edmontonnamao_alber["Annual"] = df_edmontonnamao_alber["Annual"].replace(-9999.9, df_edmontonnamao_alber["Annual"].median())
df_edmontonnamao_alber["Winter"] = df_edmontonnamao_alber["Winter"].replace(-9999.9, df_edmontonnamao_alber["Winter"].median())
df_edmontonnamao_alber["Spring"] = df_edmontonnamao_alber["Spring"].replace(-9999.9, df_edmontonnamao_alber["Spring"].median())
df_edmontonnamao_alber["Summer"] = df_edmontonnamao_alber["Summer"].replace(-9999.9, df_edmontonnamao_alber["Summer"].median())
df_edmontonnamao_alber["Autumn"] = df_edmontonnamao_alber["Autumn"].replace(-9999.9, df_edmontonnamao_alber["Autumn"].median())

 
#Estevan Saskatchewan 

estevan_sask = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/estevan_sask.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_estevan_sask = pd.DataFrame(estevan_sask)

#Eureka Nunavut 
    
eureka_nu= pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/eureka_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_eureka_nu = pd.DataFrame(eureka_nu)

df_eureka_nu["Jun"] = df_eureka_nu["Jun"].replace(-9999.9, df_eureka_nu["Jun"].median())
df_eureka_nu["Jul"] = df_eureka_nu["Jul"].replace(-9999.9, df_eureka_nu["Jul"].median())
df_eureka_nu["Summer"] = df_eureka_nu["Summer"].replace(-9999.9, df_eureka_nu["Summer"].median())

#Flinflon Manitoba 

flinflon_man = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/flinflon_man.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_flinflon_man = pd.DataFrame(flinflon_man)

df_flinflon_man["Jan"] = df_flinflon_man["Jan"].replace(-9999.9, df_flinflon_man["Jan"].median())
df_flinflon_man["Feb"] = df_flinflon_man["Feb"].replace(-9999.9, df_flinflon_man["Feb"].median())
df_flinflon_man["Mar"] = df_flinflon_man["Mar"].replace(-9999.9, df_flinflon_man["Mar"].median())
df_flinflon_man["Apr"] = df_flinflon_man["Apr"].replace(-9999.9, df_flinflon_man["Apr"].median())
df_flinflon_man["May"] = df_flinflon_man["May"].replace(-9999.9, df_flinflon_man["May"].median())
df_flinflon_man["Jun"] = df_flinflon_man["Jun"].replace(-9999.9, df_flinflon_man["Jun"].median())
df_flinflon_man["Jul"] = df_flinflon_man["Jul"].replace(-9999.9, df_flinflon_man["Jul"].median())
df_flinflon_man["Aug"] = df_flinflon_man["Aug"].replace(-9999.9, df_flinflon_man["Aug"].median())
df_flinflon_man["Sep"] = df_flinflon_man["Sep"].replace(-9999.9, df_flinflon_man["Sep"].median())
df_flinflon_man["Oct"] = df_flinflon_man["Oct"].replace(-9999.9, df_flinflon_man["Oct"].median())
df_flinflon_man["Nov"] = df_flinflon_man["Nov"].replace(-9999.9, df_flinflon_man["Nov"].median())
df_flinflon_man["Dec"] = df_flinflon_man["Dec"].replace(-9999.9, df_flinflon_man["Dec"].median())
df_flinflon_man["Annual"] = df_flinflon_man["Annual"].replace(-9999.9, df_flinflon_man["Annual"].median())
df_flinflon_man["Winter"] = df_flinflon_man["Winter"].replace(-9999.9, df_flinflon_man["Winter"].median())
df_flinflon_man["Spring"] = df_flinflon_man["Spring"].replace(-9999.9, df_flinflon_man["Spring"].median())
df_flinflon_man["Summer"] = df_flinflon_man["Summer"].replace(-9999.9, df_flinflon_man["Summer"].median())
df_flinflon_man["Autumn"] = df_flinflon_man["Autumn"].replace(-9999.9, df_flinflon_man["Autumn"].median())


#Fortmcmurray Alberta 

fortmcmurray_alber = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/fortmcmurray_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_fortmcmurray_alber = pd.DataFrame(fortmcmurray_alber)


#Fort Nelson British Columbia 

fortnelson_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/fortnelson_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_fortnelson_bc = pd.DataFrame(fortnelson_bc)

#Fort Simpson North West Territories 

fortsimpson_nwt = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/fortsimpson_nwt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_fortsimpson_nwt = pd.DataFrame(fortsimpson_nwt)

df_fortsimpson_nwt["Oct"] = df_fortsimpson_nwt["Oct"].replace(-9999.9, df_fortsimpson_nwt["Oct"].median())
df_fortsimpson_nwt["Nov"] = df_fortsimpson_nwt["Nov"].replace(-9999.9, df_fortsimpson_nwt["Nov"].median())
df_fortsimpson_nwt["Dec"] = df_fortsimpson_nwt["Dec"].replace(-9999.9, df_fortsimpson_nwt["Dec"].median())
df_fortsimpson_nwt["Autumn"] = df_fortsimpson_nwt["Autumn"].replace(-9999.9, df_fortsimpson_nwt["Autumn"].median())


#Fort Smith North West Territories 
    
fortsmith_nwt = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/fortsmith_nwt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_fortsmith_nwt = pd.DataFrame(fortsmith_nwt)

df_fortsmith_nwt["Oct"] = df_fortsmith_nwt["Oct"].replace(-9999.9, df_fortsmith_nwt["Oct"].median())
df_fortsmith_nwt["Nov"] = df_fortsmith_nwt["Nov"].replace(-9999.9, df_fortsmith_nwt["Nov"].median())
df_fortsmith_nwt["Dec"] = df_fortsmith_nwt["Dec"].replace(-9999.9, df_fortsmith_nwt["Dec"].median())


#Fort st. John British Columbia 

fortstjohn_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/fortstjohn_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_fortstjohn_bc = pd.DataFrame(fortstjohn_bc)

#Foxfive Nunuvut 

foxfive_nu = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/foxfive_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_foxfive_nu = pd.DataFrame(foxfive_nu)

df_foxfive_nu["Jan"] = df_foxfive_nu["Jan"].replace(-9999.9, df_foxfive_nu["Jan"].median())
df_foxfive_nu["Feb"] = df_foxfive_nu["Feb"].replace(-9999.9, df_foxfive_nu["Feb"].median())
df_foxfive_nu["Mar"] = df_foxfive_nu["Mar"].replace(-9999.9, df_foxfive_nu["Mar"].median())
df_foxfive_nu["Apr"] = df_foxfive_nu["Apr"].replace(-9999.9, df_foxfive_nu["Apr"].median())
df_foxfive_nu["May"] = df_foxfive_nu["May"].replace(-9999.9, df_foxfive_nu["May"].median())
df_foxfive_nu["Jun"] = df_foxfive_nu["Jun"].replace(-9999.9, df_foxfive_nu["Jun"].median())
df_foxfive_nu["Jul"] = df_foxfive_nu["Jul"].replace(-9999.9, df_foxfive_nu["Jul"].median())
df_foxfive_nu["Aug"] = df_foxfive_nu["Aug"].replace(-9999.9, df_foxfive_nu["Aug"].median())
df_foxfive_nu["Sep"] = df_foxfive_nu["Sep"].replace(-9999.9, df_foxfive_nu["Sep"].median())
df_foxfive_nu["Oct"] = df_foxfive_nu["Oct"].replace(-9999.9, df_foxfive_nu["Oct"].median())
df_foxfive_nu["Nov"] = df_foxfive_nu["Nov"].replace(-9999.9, df_foxfive_nu["Nov"].median())
df_foxfive_nu["Dec"] = df_foxfive_nu["Dec"].replace(-9999.9, df_foxfive_nu["Dec"].median())
df_foxfive_nu["Annual"] = df_foxfive_nu["Annual"].replace(-9999.9, df_foxfive_nu["Annual"].median())
df_foxfive_nu["Winter"] = df_foxfive_nu["Winter"].replace(-9999.9, df_foxfive_nu["Winter"].median())
df_foxfive_nu["Spring"] = df_foxfive_nu["Spring"].replace(-9999.9, df_foxfive_nu["Spring"].median())
df_foxfive_nu["Summer"] = df_foxfive_nu["Summer"].replace(-9999.9, df_foxfive_nu["Summer"].median())
df_foxfive_nu["Autumn"] = df_foxfive_nu["Autumn"].replace(-9999.9, df_foxfive_nu["Autumn"].median())


#Fredericton New Brunswick 

fredericton_nb = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/fredericton_nb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_fredericton_nb = pd.DataFrame(fredericton_nb)

#Ganderinternationalairport Newfoundland 
    
ganderinternationalairport_nfld = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/ganderinternationalairport_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_ganderinternationalairport_nfld = pd.DataFrame(ganderinternationalairport_nfld)

df_ganderinternationalairport_nfld["Jan"] = df_ganderinternationalairport_nfld["Jan"].replace(-9999.9, df_ganderinternationalairport_nfld["Jan"].median())
df_ganderinternationalairport_nfld["Feb"] = df_ganderinternationalairport_nfld["Feb"].replace(-9999.9, df_ganderinternationalairport_nfld["Feb"].median())
df_ganderinternationalairport_nfld["Mar"] = df_ganderinternationalairport_nfld["Mar"].replace(-9999.9, df_ganderinternationalairport_nfld["Mar"].median())
df_ganderinternationalairport_nfld["Apr"] = df_ganderinternationalairport_nfld["Apr"].replace(-9999.9, df_ganderinternationalairport_nfld["Apr"].median())
df_ganderinternationalairport_nfld["May"] = df_ganderinternationalairport_nfld["May"].replace(-9999.9, df_ganderinternationalairport_nfld["May"].median())
df_ganderinternationalairport_nfld["Jun"] = df_ganderinternationalairport_nfld["Jun"].replace(-9999.9, df_ganderinternationalairport_nfld["Jun"].median())
df_ganderinternationalairport_nfld["Jul"] = df_ganderinternationalairport_nfld["Jul"].replace(-9999.9, df_ganderinternationalairport_nfld["Jul"].median())
df_ganderinternationalairport_nfld["Aug"] = df_ganderinternationalairport_nfld["Aug"].replace(-9999.9, df_ganderinternationalairport_nfld["Aug"].median())
df_ganderinternationalairport_nfld["Sep"] = df_ganderinternationalairport_nfld["Sep"].replace(-9999.9, df_ganderinternationalairport_nfld["Sep"].median())
df_ganderinternationalairport_nfld["Oct"] = df_ganderinternationalairport_nfld["Oct"].replace(-9999.9, df_ganderinternationalairport_nfld["Oct"].median())
df_ganderinternationalairport_nfld["Nov"] = df_ganderinternationalairport_nfld["Nov"].replace(-9999.9, df_ganderinternationalairport_nfld["Nov"].median())
df_ganderinternationalairport_nfld["Dec"] = df_ganderinternationalairport_nfld["Dec"].replace(-9999.9, df_ganderinternationalairport_nfld["Dec"].median())
df_ganderinternationalairport_nfld["Annual"] = df_ganderinternationalairport_nfld["Annual"].replace(-9999.9, df_ganderinternationalairport_nfld["Annual"].median())
df_ganderinternationalairport_nfld["Winter"] = df_ganderinternationalairport_nfld["Winter"].replace(-9999.9, df_ganderinternationalairport_nfld["Winter"].median())
df_ganderinternationalairport_nfld["Spring"] = df_ganderinternationalairport_nfld["Spring"].replace(-9999.9, df_ganderinternationalairport_nfld["Spring"].median())
df_ganderinternationalairport_nfld["Summer"] = df_ganderinternationalairport_nfld["Summer"].replace(-9999.9, df_ganderinternationalairport_nfld["Summer"].median())
df_ganderinternationalairport_nfld["Autumn"] = df_ganderinternationalairport_nfld["Autumn"].replace(-9999.9, df_ganderinternationalairport_nfld["Autumn"].median())


#Gaspe Quebec

gaspe_que = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/gaspe_que.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_gaspe_que = pd.DataFrame(gaspe_que)

df_gaspe_que["Jan"] = df_gaspe_que["Jan"].replace(-9999.9, df_gaspe_que["Jan"].median())
df_gaspe_que["Feb"] = df_gaspe_que["Feb"].replace(-9999.9, df_gaspe_que["Feb"].median())
df_gaspe_que["Mar"] = df_gaspe_que["Mar"].replace(-9999.9, df_gaspe_que["Mar"].median())
df_gaspe_que["Apr"] = df_gaspe_que["Apr"].replace(-9999.9, df_gaspe_que["Apr"].median())
df_gaspe_que["May"] = df_gaspe_que["May"].replace(-9999.9, df_gaspe_que["May"].median())
df_gaspe_que["Jun"] = df_gaspe_que["Jun"].replace(-9999.9, df_gaspe_que["Jun"].median())
df_gaspe_que["Jul"] = df_gaspe_que["Jul"].replace(-9999.9, df_gaspe_que["Jul"].median())
df_gaspe_que["Aug"] = df_gaspe_que["Aug"].replace(-9999.9, df_gaspe_que["Aug"].median())
df_gaspe_que["Sep"] = df_gaspe_que["Sep"].replace(-9999.9, df_gaspe_que["Sep"].median())
df_gaspe_que["Oct"] = df_gaspe_que["Oct"].replace(-9999.9, df_gaspe_que["Oct"].median())
df_gaspe_que["Nov"] = df_gaspe_que["Nov"].replace(-9999.9, df_gaspe_que["Nov"].median())
df_gaspe_que["Dec"] = df_gaspe_que["Dec"].replace(-9999.9, df_gaspe_que["Dec"].median())
df_gaspe_que["Annual"] = df_gaspe_que["Annual"].replace(-9999.9, df_gaspe_que["Annual"].median())
df_gaspe_que["Winter"] = df_gaspe_que["Winter"].replace(-9999.9, df_gaspe_que["Winter"].median())
df_gaspe_que["Spring"] = df_gaspe_que["Spring"].replace(-9999.9, df_gaspe_que["Spring"].median())
df_gaspe_que["Summer"] = df_gaspe_que["Summer"].replace(-9999.9, df_gaspe_que["Summer"].median())
df_gaspe_que["Autumn"] = df_gaspe_que["Autumn"].replace(-9999.9, df_gaspe_que["Autumn"].median())


#Gillam Manitoba 
    
gillam_man = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/gillam_man.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_gillam_man = pd.DataFrame(gillam_man)

df_gillam_man["Jan"] = df_gillam_man["Jan"].replace(-9999.9, df_gillam_man["Jan"].median())
df_gillam_man["Feb"] = df_gillam_man["Feb"].replace(-9999.9, df_gillam_man["Feb"].median())
df_gillam_man["Mar"] = df_gillam_man["Mar"].replace(-9999.9, df_gillam_man["Mar"].median())
df_gillam_man["Apr"] = df_gillam_man["Apr"].replace(-9999.9, df_gillam_man["Apr"].median())
df_gillam_man["May"] = df_gillam_man["May"].replace(-9999.9, df_gillam_man["May"].median())
df_gillam_man["Jun"] = df_gillam_man["Jun"].replace(-9999.9, df_gillam_man["Jun"].median())
df_gillam_man["Jul"] = df_gillam_man["Jul"].replace(-9999.9, df_gillam_man["Jul"].median())
df_gillam_man["Aug"] = df_gillam_man["Aug"].replace(-9999.9, df_gillam_man["Aug"].median())
df_gillam_man["Sep"] = df_gillam_man["Sep"].replace(-9999.9, df_gillam_man["Sep"].median())
df_gillam_man["Oct"] = df_gillam_man["Oct"].replace(-9999.9, df_gillam_man["Oct"].median())
df_gillam_man["Nov"] = df_gillam_man["Nov"].replace(-9999.9, df_gillam_man["Nov"].median())
df_gillam_man["Dec"] = df_gillam_man["Dec"].replace(-9999.9, df_gillam_man["Dec"].median())
df_gillam_man["Annual"] = df_gillam_man["Annual"].replace(-9999.9, df_gillam_man["Annual"].median())
df_gillam_man["Winter"] = df_gillam_man["Winter"].replace(-9999.9, df_gillam_man["Winter"].median())
df_gillam_man["Spring"] = df_gillam_man["Spring"].replace(-9999.9, df_gillam_man["Spring"].median())
df_gillam_man["Summer"] = df_gillam_man["Summer"].replace(-9999.9, df_gillam_man["Summer"].median())
df_gillam_man["Autumn"] = df_gillam_man["Autumn"].replace(-9999.9, df_gillam_man["Autumn"].median())

#Goose Newfoundland

goose_nfld = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/goose_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_goose_nfld = pd.DataFrame(goose_nfld)

df_goose_nfld["Jan"] = df_goose_nfld["Jan"].replace(-9999.9, df_goose_nfld["Jan"].median())
df_goose_nfld["Feb"] = df_goose_nfld["Feb"].replace(-9999.9, df_goose_nfld["Feb"].median())
df_goose_nfld["Mar"] = df_goose_nfld["Mar"].replace(-9999.9, df_goose_nfld["Mar"].median())
df_goose_nfld["Apr"] = df_goose_nfld["Apr"].replace(-9999.9, df_goose_nfld["Apr"].median())
df_goose_nfld["May"] = df_goose_nfld["May"].replace(-9999.9, df_goose_nfld["May"].median())
df_goose_nfld["Jun"] = df_goose_nfld["Jun"].replace(-9999.9, df_goose_nfld["Jun"].median())
df_goose_nfld["Jul"] = df_goose_nfld["Jul"].replace(-9999.9, df_goose_nfld["Jul"].median())
df_goose_nfld["Aug"] = df_goose_nfld["Aug"].replace(-9999.9, df_goose_nfld["Aug"].median())
df_goose_nfld["Sep"] = df_goose_nfld["Sep"].replace(-9999.9, df_goose_nfld["Sep"].median())
df_goose_nfld["Oct"] = df_goose_nfld["Oct"].replace(-9999.9, df_goose_nfld["Oct"].median())
df_goose_nfld["Nov"] = df_goose_nfld["Nov"].replace(-9999.9, df_goose_nfld["Nov"].median())
df_goose_nfld["Dec"] = df_goose_nfld["Dec"].replace(-9999.9, df_goose_nfld["Dec"].median())
df_goose_nfld["Annual"] = df_goose_nfld["Annual"].replace(-9999.9, df_goose_nfld["Annual"].median())
df_goose_nfld["Winter"] = df_goose_nfld["Winter"].replace(-9999.9, df_goose_nfld["Winter"].median())
df_goose_nfld["Spring"] = df_goose_nfld["Spring"].replace(-9999.9, df_goose_nfld["Spring"].median())
df_goose_nfld["Summer"] = df_goose_nfld["Summer"].replace(-9999.9, df_goose_nfld["Summer"].median())
df_goose_nfld["Autumn"] = df_goose_nfld["Autumn"].replace(-9999.9, df_goose_nfld["Autumn"].median())

#Gorebay Ontario 
    
gorebay_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/gorebay_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_gorebay_ont = pd.DataFrame(gorebay_ont)

df_gorebay_ont["Jan"] = df_gorebay_ont["Jan"].replace(-9999.9, df_gorebay_ont["Jan"].median())
df_gorebay_ont["Feb"] = df_gorebay_ont["Feb"].replace(-9999.9, df_gorebay_ont["Feb"].median())
df_gorebay_ont["Mar"] = df_gorebay_ont["Mar"].replace(-9999.9, df_gorebay_ont["Mar"].median())
df_gorebay_ont["Apr"] = df_gorebay_ont["Apr"].replace(-9999.9, df_gorebay_ont["Apr"].median())
df_gorebay_ont["May"] = df_gorebay_ont["May"].replace(-9999.9, df_gorebay_ont["May"].median())
df_gorebay_ont["Jun"] = df_gorebay_ont["Jun"].replace(-9999.9, df_gorebay_ont["Jun"].median())
df_gorebay_ont["Jul"] = df_gorebay_ont["Jul"].replace(-9999.9, df_gorebay_ont["Jul"].median())
df_gorebay_ont["Aug"] = df_gorebay_ont["Aug"].replace(-9999.9, df_gorebay_ont["Aug"].median())
df_gorebay_ont["Sep"] = df_gorebay_ont["Sep"].replace(-9999.9, df_gorebay_ont["Sep"].median())
df_gorebay_ont["Oct"] = df_gorebay_ont["Oct"].replace(-9999.9, df_gorebay_ont["Oct"].median())
df_gorebay_ont["Nov"] = df_gorebay_ont["Nov"].replace(-9999.9, df_gorebay_ont["Nov"].median())
df_gorebay_ont["Dec"] = df_gorebay_ont["Dec"].replace(-9999.9, df_gorebay_ont["Dec"].median())
df_gorebay_ont["Annual"] = df_gorebay_ont["Annual"].replace(-9999.9, df_gorebay_ont["Annual"].median())
df_gorebay_ont["Winter"] = df_gorebay_ont["Winter"].replace(-9999.9, df_gorebay_ont["Winter"].median())
df_gorebay_ont["Spring"] = df_gorebay_ont["Spring"].replace(-9999.9, df_gorebay_ont["Spring"].median())
df_gorebay_ont["Summer"] = df_gorebay_ont["Summer"].replace(-9999.9, df_gorebay_ont["Summer"].median())
df_gorebay_ont["Autumn"] = df_gorebay_ont["Autumn"].replace(-9999.9, df_gorebay_ont["Autumn"].median())

#Grand Prarie Alberta

grandprairie_alber = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/grandprairie_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_grandprairie_alber = pd.DataFrame(grandprairie_alber)

#Greenwood Nova Scotia 

greenwood_ns = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/greenwood_ns.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_greenwood_ns = pd.DataFrame(greenwood_ns)

#Halifax Nova Scotia 

halifax_ns = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/halifax_ns.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_halifax_ns = pd.DataFrame(halifax_ns)

df_halifax_ns["Jan"] = df_halifax_ns["Jan"].replace(-9999.9, df_halifax_ns["Jan"].median())
df_halifax_ns["Feb"] = df_halifax_ns["Feb"].replace(-9999.9, df_halifax_ns["Feb"].median())
df_halifax_ns["Mar"] = df_halifax_ns["Mar"].replace(-9999.9, df_halifax_ns["Mar"].median())
df_halifax_ns["Apr"] = df_halifax_ns["Apr"].replace(-9999.9, df_halifax_ns["Apr"].median())
df_halifax_ns["May"] = df_halifax_ns["May"].replace(-9999.9, df_halifax_ns["May"].median())
df_halifax_ns["Jun"] = df_halifax_ns["Jun"].replace(-9999.9, df_halifax_ns["Jun"].median())
df_halifax_ns["Jul"] = df_halifax_ns["Jul"].replace(-9999.9, df_halifax_ns["Jul"].median())
df_halifax_ns["Aug"] = df_halifax_ns["Aug"].replace(-9999.9, df_halifax_ns["Aug"].median())
df_halifax_ns["Sep"] = df_halifax_ns["Sep"].replace(-9999.9, df_halifax_ns["Sep"].median())
df_halifax_ns["Oct"] = df_halifax_ns["Oct"].replace(-9999.9, df_halifax_ns["Oct"].median())
df_halifax_ns["Nov"] = df_halifax_ns["Nov"].replace(-9999.9, df_halifax_ns["Nov"].median())
df_halifax_ns["Dec"] = df_halifax_ns["Dec"].replace(-9999.9, df_halifax_ns["Dec"].median())
df_halifax_ns["Annual"] = df_halifax_ns["Annual"].replace(-9999.9, df_halifax_ns["Annual"].median())
df_halifax_ns["Winter"] = df_halifax_ns["Winter"].replace(-9999.9, df_halifax_ns["Winter"].median())
df_halifax_ns["Spring"] = df_halifax_ns["Spring"].replace(-9999.9, df_halifax_ns["Spring"].median())
df_halifax_ns["Summer"] = df_halifax_ns["Summer"].replace(-9999.9, df_halifax_ns["Summer"].median())
df_halifax_ns["Autumn"] = df_halifax_ns["Autumn"].replace(-9999.9, df_halifax_ns["Autumn"].median())

#Hallbeach Nunuvut 

hallbeach_nu = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/hallbeach_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_hallbeach_nu = pd.DataFrame(hallbeach_nu)

df_hallbeach_nu["Jan"] = df_hallbeach_nu["Jan"].replace(-9999.9, df_hallbeach_nu["Jan"].median())
df_hallbeach_nu["Feb"] = df_hallbeach_nu["Feb"].replace(-9999.9, df_hallbeach_nu["Feb"].median())
df_hallbeach_nu["Mar"] = df_hallbeach_nu["Mar"].replace(-9999.9, df_hallbeach_nu["Mar"].median())
df_hallbeach_nu["Apr"] = df_hallbeach_nu["Apr"].replace(-9999.9, df_hallbeach_nu["Apr"].median())
df_hallbeach_nu["May"] = df_hallbeach_nu["May"].replace(-9999.9, df_hallbeach_nu["May"].median())
df_hallbeach_nu["Jun"] = df_hallbeach_nu["Jun"].replace(-9999.9, df_hallbeach_nu["Jun"].median())
df_hallbeach_nu["Jul"] = df_hallbeach_nu["Jul"].replace(-9999.9, df_hallbeach_nu["Jul"].median())
df_hallbeach_nu["Aug"] = df_hallbeach_nu["Aug"].replace(-9999.9, df_hallbeach_nu["Aug"].median())
df_hallbeach_nu["Sep"] = df_hallbeach_nu["Sep"].replace(-9999.9, df_hallbeach_nu["Sep"].median())
df_hallbeach_nu["Oct"] = df_hallbeach_nu["Oct"].replace(-9999.9, df_hallbeach_nu["Oct"].median())
df_hallbeach_nu["Nov"] = df_hallbeach_nu["Nov"].replace(-9999.9, df_hallbeach_nu["Nov"].median())
df_hallbeach_nu["Dec"] = df_hallbeach_nu["Dec"].replace(-9999.9, df_hallbeach_nu["Dec"].median())
df_hallbeach_nu["Annual"] = df_hallbeach_nu["Annual"].replace(-9999.9, df_hallbeach_nu["Annual"].median())
df_hallbeach_nu["Winter"] = df_hallbeach_nu["Winter"].replace(-9999.9, df_hallbeach_nu["Winter"].median())
df_hallbeach_nu["Spring"] = df_hallbeach_nu["Spring"].replace(-9999.9, df_hallbeach_nu["Spring"].median())
df_hallbeach_nu["Summer"] = df_hallbeach_nu["Summer"].replace(-9999.9, df_hallbeach_nu["Summer"].median())
df_hallbeach_nu["Autumn"] = df_hallbeach_nu["Autumn"].replace(-9999.9, df_hallbeach_nu["Autumn"].median())

#Hamilton Ontario 

hamilton_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/hamilton_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_hamilton_ont = pd.DataFrame(hamilton_ont)

df_hamilton_ont["Jan"] = df_hamilton_ont["Jan"].replace(-9999.9, df_hamilton_ont["Jan"].median())
df_hamilton_ont["Feb"] = df_hamilton_ont["Feb"].replace(-9999.9, df_hamilton_ont["Feb"].median())
df_hamilton_ont["Mar"] = df_hamilton_ont["Mar"].replace(-9999.9, df_hamilton_ont["Mar"].median())
df_hamilton_ont["Apr"] = df_hamilton_ont["Apr"].replace(-9999.9, df_hamilton_ont["Apr"].median())
df_hamilton_ont["May"] = df_hamilton_ont["May"].replace(-9999.9, df_hamilton_ont["May"].median())
df_hamilton_ont["Jun"] = df_hamilton_ont["Jun"].replace(-9999.9, df_hamilton_ont["Jun"].median())
df_hamilton_ont["Jul"] = df_hamilton_ont["Jul"].replace(-9999.9, df_hamilton_ont["Jul"].median())
df_hamilton_ont["Aug"] = df_hamilton_ont["Aug"].replace(-9999.9, df_hamilton_ont["Aug"].median())
df_hamilton_ont["Sep"] = df_hamilton_ont["Sep"].replace(-9999.9, df_hamilton_ont["Sep"].median())
df_hamilton_ont["Oct"] = df_hamilton_ont["Oct"].replace(-9999.9, df_hamilton_ont["Oct"].median())
df_hamilton_ont["Nov"] = df_hamilton_ont["Nov"].replace(-9999.9, df_hamilton_ont["Nov"].median())
df_hamilton_ont["Dec"] = df_hamilton_ont["Dec"].replace(-9999.9, df_hamilton_ont["Dec"].median())
df_hamilton_ont["Annual"] = df_hamilton_ont["Annual"].replace(-9999.9, df_hamilton_ont["Annual"].median())
df_hamilton_ont["Winter"] = df_hamilton_ont["Winter"].replace(-9999.9, df_hamilton_ont["Winter"].median())
df_hamilton_ont["Spring"] = df_hamilton_ont["Spring"].replace(-9999.9, df_hamilton_ont["Spring"].median())
df_hamilton_ont["Summer"] = df_hamilton_ont["Summer"].replace(-9999.9, df_hamilton_ont["Summer"].median())
df_hamilton_ont["Autumn"] = df_hamilton_ont["Autumn"].replace(-9999.9, df_hamilton_ont["Autumn"].median())

#Hayriver North West Territories 

hayriver_nwt = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/hayriver_nwt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_hayriver_nwt = pd.DataFrame(hayriver_nwt)

df_hayriver_nwt["Sep"] = df_hayriver_nwt["Sep"].replace(-9999.9, df_hayriver_nwt["Sep"].median())
df_hayriver_nwt["Oct"] = df_hayriver_nwt["Oct"].replace(-9999.9, df_hayriver_nwt["Oct"].median())
df_hayriver_nwt["Nov"] = df_hayriver_nwt["Nov"].replace(-9999.9, df_hayriver_nwt["Nov"].median())
df_hayriver_nwt["Dec"] = df_hayriver_nwt["Dec"].replace(-9999.9, df_hayriver_nwt["Dec"].median())
df_hayriver_nwt["May"] = df_hayriver_nwt["May"].replace(-9999.9, df_hayriver_nwt["May"].median())
df_hayriver_nwt["Autumn"] = df_hayriver_nwt["Autumn"].replace(-9999.9, df_hayriver_nwt["Autumn"].median())


#Highlevel Alberta 

highlevel_alber = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/highlevel_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_highlevel_alber = pd.DataFrame(highlevel_alber)

df_highlevel_alber["Jan"] = df_highlevel_alber["Jan"].replace(-9999.9, df_highlevel_alber["Jan"].median())
df_highlevel_alber["Feb"] = df_highlevel_alber["Feb"].replace(-9999.9, df_highlevel_alber["Feb"].median())
df_highlevel_alber["Mar"] = df_highlevel_alber["Mar"].replace(-9999.9, df_highlevel_alber["Mar"].median())
df_highlevel_alber["Apr"] = df_highlevel_alber["Apr"].replace(-9999.9, df_highlevel_alber["Apr"].median())
df_highlevel_alber["May"] = df_highlevel_alber["May"].replace(-9999.9, df_highlevel_alber["May"].median())
df_highlevel_alber["Jun"] = df_highlevel_alber["Jun"].replace(-9999.9, df_highlevel_alber["Jun"].median())
df_highlevel_alber["Jul"] = df_highlevel_alber["Jul"].replace(-9999.9, df_highlevel_alber["Jul"].median())
df_highlevel_alber["Aug"] = df_highlevel_alber["Aug"].replace(-9999.9, df_highlevel_alber["Aug"].median())
df_highlevel_alber["Sep"] = df_highlevel_alber["Sep"].replace(-9999.9, df_highlevel_alber["Sep"].median())
df_highlevel_alber["Oct"] = df_highlevel_alber["Oct"].replace(-9999.9, df_highlevel_alber["Oct"].median())
df_highlevel_alber["Nov"] = df_highlevel_alber["Nov"].replace(-9999.9, df_highlevel_alber["Nov"].median())
df_highlevel_alber["Dec"] = df_highlevel_alber["Dec"].replace(-9999.9, df_highlevel_alber["Dec"].median())
df_highlevel_alber["Annual"] = df_highlevel_alber["Annual"].replace(-9999.9, df_highlevel_alber["Annual"].median())
df_highlevel_alber["Winter"] = df_highlevel_alber["Winter"].replace(-9999.9, df_highlevel_alber["Winter"].median())
df_highlevel_alber["Spring"] = df_highlevel_alber["Spring"].replace(-9999.9, df_highlevel_alber["Spring"].median())
df_highlevel_alber["Summer"] = df_highlevel_alber["Summer"].replace(-9999.9, df_highlevel_alber["Summer"].median())
df_highlevel_alber["Autumn"] = df_highlevel_alber["Autumn"].replace(-9999.9, df_highlevel_alber["Autumn"].median())


#Hopea British Columbia 

hopea_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/hopea_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_hopea_bc = pd.DataFrame(hopea_bc)

#Hopedale Newfoundland 

hopedale_nfld = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/hopedale_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_hopedale_nfld = pd.DataFrame(hopedale_nfld)

df_hopedale_nfld["Jan"] = df_hopedale_nfld["Jan"].replace(-9999.9, df_hopedale_nfld["Jan"].median())
df_hopedale_nfld["Feb"] = df_hopedale_nfld["Feb"].replace(-9999.9, df_hopedale_nfld["Feb"].median())
df_hopedale_nfld["Mar"] = df_hopedale_nfld["Mar"].replace(-9999.9, df_hopedale_nfld["Mar"].median())
df_hopedale_nfld["Apr"] = df_hopedale_nfld["Apr"].replace(-9999.9, df_hopedale_nfld["Apr"].median())
df_hopedale_nfld["May"] = df_hopedale_nfld["May"].replace(-9999.9, df_hopedale_nfld["May"].median())
df_hopedale_nfld["Jun"] = df_hopedale_nfld["Jun"].replace(-9999.9, df_hopedale_nfld["Jun"].median())
df_hopedale_nfld["Jul"] = df_hopedale_nfld["Jul"].replace(-9999.9, df_hopedale_nfld["Jul"].median())
df_hopedale_nfld["Aug"] = df_hopedale_nfld["Aug"].replace(-9999.9, df_hopedale_nfld["Aug"].median())
df_hopedale_nfld["Sep"] = df_hopedale_nfld["Sep"].replace(-9999.9, df_hopedale_nfld["Sep"].median())
df_hopedale_nfld["Oct"] = df_hopedale_nfld["Oct"].replace(-9999.9, df_hopedale_nfld["Oct"].median())
df_hopedale_nfld["Nov"] = df_hopedale_nfld["Nov"].replace(-9999.9, df_hopedale_nfld["Nov"].median())
df_hopedale_nfld["Dec"] = df_hopedale_nfld["Dec"].replace(-9999.9, df_hopedale_nfld["Dec"].median())
df_hopedale_nfld["Annual"] = df_hopedale_nfld["Annual"].replace(-9999.9, df_hopedale_nfld["Annual"].median())
df_hopedale_nfld["Winter"] = df_hopedale_nfld["Winter"].replace(-9999.9, df_hopedale_nfld["Winter"].median())
df_hopedale_nfld["Spring"] = df_hopedale_nfld["Spring"].replace(-9999.9, df_hopedale_nfld["Spring"].median())
df_hopedale_nfld["Summer"] = df_hopedale_nfld["Summer"].replace(-9999.9, df_hopedale_nfld["Summer"].median())
df_hopedale_nfld["Autumn"] = df_hopedale_nfld["Autumn"].replace(-9999.9, df_hopedale_nfld["Autumn"].median())


#Inukjuak Quebec 

inukjuak_queb = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/inukjuak_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_inukjuak_queb = pd.DataFrame(inukjuak_queb)

df_inukjuak_queb["Jan"] = df_inukjuak_queb["Jan"].replace(-9999.9, df_inukjuak_queb["Jan"].median())
df_inukjuak_queb["Feb"] = df_inukjuak_queb["Feb"].replace(-9999.9, df_inukjuak_queb["Feb"].median())
df_inukjuak_queb["Mar"] = df_inukjuak_queb["Mar"].replace(-9999.9, df_inukjuak_queb["Mar"].median())
df_inukjuak_queb["Apr"] = df_inukjuak_queb["Apr"].replace(-9999.9, df_inukjuak_queb["Apr"].median())
df_inukjuak_queb["May"] = df_inukjuak_queb["May"].replace(-9999.9, df_inukjuak_queb["May"].median())
df_inukjuak_queb["Jun"] = df_inukjuak_queb["Jun"].replace(-9999.9, df_inukjuak_queb["Jun"].median())
df_inukjuak_queb["Jul"] = df_inukjuak_queb["Jul"].replace(-9999.9, df_inukjuak_queb["Jul"].median())
df_inukjuak_queb["Aug"] = df_inukjuak_queb["Aug"].replace(-9999.9, df_inukjuak_queb["Aug"].median())
df_inukjuak_queb["Sep"] = df_inukjuak_queb["Sep"].replace(-9999.9, df_inukjuak_queb["Sep"].median())
df_inukjuak_queb["Oct"] = df_inukjuak_queb["Oct"].replace(-9999.9, df_inukjuak_queb["Oct"].median())
df_inukjuak_queb["Nov"] = df_inukjuak_queb["Nov"].replace(-9999.9, df_inukjuak_queb["Nov"].median())
df_inukjuak_queb["Dec"] = df_inukjuak_queb["Dec"].replace(-9999.9, df_inukjuak_queb["Dec"].median())
df_inukjuak_queb["Annual"] = df_inukjuak_queb["Annual"].replace(-9999.9, df_inukjuak_queb["Annual"].median())
df_inukjuak_queb["Winter"] = df_inukjuak_queb["Winter"].replace(-9999.9, df_inukjuak_queb["Winter"].median())
df_inukjuak_queb["Spring"] = df_inukjuak_queb["Spring"].replace(-9999.9, df_inukjuak_queb["Spring"].median())
df_inukjuak_queb["Summer"] = df_inukjuak_queb["Summer"].replace(-9999.9, df_inukjuak_queb["Summer"].median())
df_inukjuak_queb["Autumn"] = df_inukjuak_queb["Autumn"].replace(-9999.9, df_inukjuak_queb["Autumn"].median())

#Inuvik North West Territories 

inuvik_nwt = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/inuvik_nwt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_inuvik_nwt = pd.DataFrame(inuvik_nwt)

df_inuvik_nwt["Jan"] = df_inuvik_nwt["Jan"].replace(-9999.9, df_inuvik_nwt["Jan"].median())
df_inuvik_nwt["Feb"] = df_inuvik_nwt["Feb"].replace(-9999.9, df_inuvik_nwt["Feb"].median())
df_inuvik_nwt["Mar"] = df_inuvik_nwt["Mar"].replace(-9999.9, df_inuvik_nwt["Mar"].median())
df_inuvik_nwt["Apr"] = df_inuvik_nwt["Apr"].replace(-9999.9, df_inuvik_nwt["Apr"].median())
df_inuvik_nwt["May"] = df_inuvik_nwt["May"].replace(-9999.9, df_inuvik_nwt["May"].median())
df_inuvik_nwt["Jun"] = df_inuvik_nwt["Jun"].replace(-9999.9, df_inuvik_nwt["Jun"].median())
df_inuvik_nwt["Jul"] = df_inuvik_nwt["Jul"].replace(-9999.9, df_inuvik_nwt["Jul"].median())
df_inuvik_nwt["Aug"] = df_inuvik_nwt["Aug"].replace(-9999.9, df_inuvik_nwt["Aug"].median())
df_inuvik_nwt["Sep"] = df_inuvik_nwt["Sep"].replace(-9999.9, df_inuvik_nwt["Sep"].median())
df_inuvik_nwt["Oct"] = df_inuvik_nwt["Oct"].replace(-9999.9, df_inuvik_nwt["Oct"].median())
df_inuvik_nwt["Nov"] = df_inuvik_nwt["Nov"].replace(-9999.9, df_inuvik_nwt["Nov"].median())
df_inuvik_nwt["Dec"] = df_inuvik_nwt["Dec"].replace(-9999.9, df_inuvik_nwt["Dec"].median())
df_inuvik_nwt["Annual"] = df_inuvik_nwt["Annual"].replace(-9999.9, df_inuvik_nwt["Annual"].median())
df_inuvik_nwt["Winter"] = df_inuvik_nwt["Winter"].replace(-9999.9, df_inuvik_nwt["Winter"].median())
df_inuvik_nwt["Spring"] = df_inuvik_nwt["Spring"].replace(-9999.9, df_inuvik_nwt["Spring"].median())
df_inuvik_nwt["Summer"] = df_inuvik_nwt["Summer"].replace(-9999.9, df_inuvik_nwt["Summer"].median())
df_inuvik_nwt["Autumn"] = df_inuvik_nwt["Autumn"].replace(-9999.9, df_inuvik_nwt["Autumn"].median())


#Iqualuit Nunuvut 

iqualuit_nu = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/iqaluit_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_iqualuit_nu = pd.DataFrame(iqualuit_nu)


df_iqualuit_nu["Feb"] = df_iqualuit_nu["Feb"].replace(-9999.9, df_iqualuit_nu["Feb"].median())
df_iqualuit_nu["Mar"] = df_iqualuit_nu["Mar"].replace(-9999.9, df_iqualuit_nu["Mar"].median())
df_iqualuit_nu["Apr"] = df_iqualuit_nu["Apr"].replace(-9999.9, df_iqualuit_nu["Apr"].median())
df_iqualuit_nu["May"] = df_iqualuit_nu["May"].replace(-9999.9, df_iqualuit_nu["May"].median())
df_iqualuit_nu["Jun"] = df_iqualuit_nu["Jun"].replace(-9999.9, df_iqualuit_nu["Jun"].median())
df_iqualuit_nu["Jul"] = df_iqualuit_nu["Jul"].replace(-9999.9, df_iqualuit_nu["Jul"].median())
df_iqualuit_nu["Aug"] = df_iqualuit_nu["Aug"].replace(-9999.9, df_iqualuit_nu["Aug"].median())
df_iqualuit_nu["Sep"] = df_iqualuit_nu["Sep"].replace(-9999.9, df_iqualuit_nu["Sep"].median())
df_iqualuit_nu["Oct"] = df_iqualuit_nu["Oct"].replace(-9999.9, df_iqualuit_nu["Oct"].median())
df_iqualuit_nu["Nov"] = df_iqualuit_nu["Nov"].replace(-9999.9, df_iqualuit_nu["Nov"].median())
df_iqualuit_nu["Dec"] = df_iqualuit_nu["Dec"].replace(-9999.9, df_iqualuit_nu["Dec"].median())
df_iqualuit_nu["Annual"] = df_iqualuit_nu["Annual"].replace(-9999.9, df_iqualuit_nu["Annual"].median())
df_iqualuit_nu["Spring"] = df_iqualuit_nu["Spring"].replace(-9999.9, df_iqualuit_nu["Spring"].median())
df_iqualuit_nu["Summer"] = df_iqualuit_nu["Summer"].replace(-9999.9, df_iqualuit_nu["Summer"].median())
df_iqualuit_nu["Autumn"] = df_iqualuit_nu["Autumn"].replace(-9999.9, df_iqualuit_nu["Autumn"].median())

#Island Lake Manitoba 

islandlake_man = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/islandlake_man.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_islandlake_man = pd.DataFrame(islandlake_man)

df_islandlake_man["Jan"] = df_islandlake_man["Jan"].replace(-9999.9, df_islandlake_man["Jan"].median())
df_islandlake_man["Feb"] = df_islandlake_man["Feb"].replace(-9999.9, df_islandlake_man["Feb"].median())
df_islandlake_man["Mar"] = df_islandlake_man["Mar"].replace(-9999.9, df_islandlake_man["Mar"].median())
df_islandlake_man["Apr"] = df_islandlake_man["Apr"].replace(-9999.9, df_islandlake_man["Apr"].median())
df_islandlake_man["May"] = df_islandlake_man["May"].replace(-9999.9, df_islandlake_man["May"].median())
df_islandlake_man["Jun"] = df_islandlake_man["Jun"].replace(-9999.9, df_islandlake_man["Jun"].median())
df_islandlake_man["Jul"] = df_islandlake_man["Jul"].replace(-9999.9, df_islandlake_man["Jul"].median())
df_islandlake_man["Aug"] = df_islandlake_man["Aug"].replace(-9999.9, df_islandlake_man["Aug"].median())
df_islandlake_man["Sep"] = df_islandlake_man["Sep"].replace(-9999.9, df_islandlake_man["Sep"].median())
df_islandlake_man["Oct"] = df_islandlake_man["Oct"].replace(-9999.9, df_islandlake_man["Oct"].median())
df_islandlake_man["Nov"] = df_islandlake_man["Nov"].replace(-9999.9, df_islandlake_man["Nov"].median())
df_islandlake_man["Dec"] = df_islandlake_man["Dec"].replace(-9999.9, df_islandlake_man["Dec"].median())
df_islandlake_man["Annual"] = df_islandlake_man["Annual"].replace(-9999.9, df_islandlake_man["Annual"].median())
df_islandlake_man["Spring"] = df_islandlake_man["Spring"].replace(-9999.9, df_islandlake_man["Spring"].median())
df_islandlake_man["Summer"] = df_islandlake_man["Summer"].replace(-9999.9, df_islandlake_man["Summer"].median())
df_islandlake_man["Autumn"] = df_islandlake_man["Autumn"].replace(-9999.9, df_islandlake_man["Autumn"].median())
df_islandlake_man["Winter"] = df_islandlake_man["Winter"].replace(-9999.9, df_islandlake_man["Winter"].median())


#Jaspar Alberta 

jaspar_alber = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/jaspar_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_jaspar_alber = pd.DataFrame(jaspar_alber)

df_jaspar_alber["Feb"] = df_jaspar_alber["Feb"].replace(-9999.9, df_jaspar_alber["Feb"].median())
df_jaspar_alber["Jul"] = df_jaspar_alber["Jul"].replace(-9999.9, df_jaspar_alber["Jul"].median())
df_jaspar_alber["Aug"] = df_jaspar_alber["Aug"].replace(-9999.9, df_jaspar_alber["Aug"].median())
df_jaspar_alber["Sep"] = df_jaspar_alber["Sep"].replace(-9999.9, df_jaspar_alber["Sep"].median())
df_jaspar_alber["Summer"] = df_jaspar_alber["Summer"].replace(-9999.9, df_jaspar_alber["Summer"].median())


#Jean Lesage Airport Quebec 

jeanlesageairport_queb = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/jeanlesageairpot_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_jeanlesageairport_queb = pd.DataFrame(jeanlesageairport_queb)

#Kamloops British Columbia 

kamloops_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/kamloops_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_kamloops_bc = pd.DataFrame(kamloops_bc)


#Kapuskaking Ontario 

kapuskaking_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/kapuskaking_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_kapuskaking_ont = pd.DataFrame(kapuskaking_ont)

df_kapuskaking_ont["Sep"] = df_kapuskaking_ont["Sep"].replace(-9999.9, df_kapuskaking_ont["Sep"].median())
df_kapuskaking_ont["Oct"] = df_kapuskaking_ont["Oct"].replace(-9999.9, df_kapuskaking_ont["Oct"].median())
df_kapuskaking_ont["Nov"] = df_kapuskaking_ont["Nov"].replace(-9999.9, df_kapuskaking_ont["Nov"].median())
df_kapuskaking_ont["Dec"] = df_kapuskaking_ont["Dec"].replace(-9999.9, df_kapuskaking_ont["Dec"].median())
df_kapuskaking_ont["Autumn"] = df_kapuskaking_ont["Autumn"].replace(-9999.9, df_kapuskaking_ont["Autumn"].median())


#Kelowna British Columbia 

kelowna_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/kelowna_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_kelowna_bc = pd.DataFrame(kelowna_bc)

df_kelowna_bc["Jan"] = df_kelowna_bc["Jan"].replace(-9999.9, df_kelowna_bc["Jan"].median())
df_kelowna_bc["Feb"] = df_kelowna_bc["Feb"].replace(-9999.9, df_kelowna_bc["Feb"].median())
df_kelowna_bc["Mar"] = df_kelowna_bc["Mar"].replace(-9999.9, df_kelowna_bc["Mar"].median())
df_kelowna_bc["Apr"] = df_kelowna_bc["Apr"].replace(-9999.9, df_kelowna_bc["Apr"].median())
df_kelowna_bc["May"] = df_kelowna_bc["May"].replace(-9999.9, df_kelowna_bc["May"].median())
df_kelowna_bc["Jun"] = df_kelowna_bc["Jun"].replace(-9999.9, df_kelowna_bc["Jun"].median())
df_kelowna_bc["Jul"] = df_kelowna_bc["Jul"].replace(-9999.9, df_kelowna_bc["Jul"].median())
df_kelowna_bc["Aug"] = df_kelowna_bc["Aug"].replace(-9999.9, df_kelowna_bc["Aug"].median())
df_kelowna_bc["Sep"] = df_kelowna_bc["Sep"].replace(-9999.9, df_kelowna_bc["Sep"].median())
df_kelowna_bc["Oct"] = df_kelowna_bc["Oct"].replace(-9999.9, df_kelowna_bc["Oct"].median())
df_kelowna_bc["Nov"] = df_kelowna_bc["Nov"].replace(-9999.9, df_kelowna_bc["Nov"].median())
df_kelowna_bc["Dec"] = df_kelowna_bc["Dec"].replace(-9999.9, df_kelowna_bc["Dec"].median())
df_kelowna_bc["Annual"] = df_kelowna_bc["Annual"].replace(-9999.9, df_kelowna_bc["Annual"].median())
df_kelowna_bc["Winter"] = df_kelowna_bc["Winter"].replace(-9999.9, df_kelowna_bc["Winter"].median())
df_kelowna_bc["Spring"] = df_kelowna_bc["Spring"].replace(-9999.9, df_kelowna_bc["Spring"].median())
df_kelowna_bc["Summer"] = df_kelowna_bc["Summer"].replace(-9999.9, df_kelowna_bc["Summer"].median())
df_kelowna_bc["Autumn"] = df_kelowna_bc["Autumn"].replace(-9999.9, df_kelowna_bc["Autumn"].median())


#Kenora Ontario

kenora_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/kenora_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_kenora_ont = pd.DataFrame(kenora_ont)

df_kenora_ont["Oct"] = df_kenora_ont["Oct"].replace(-9999.9, df_kenora_ont["Oct"].median())


#Kingston Ontario 

kingston_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/kingston_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_kingston_ont = pd.DataFrame(kingston_ont)

df_kingston_ont["Jan"] = df_kingston_ont["Jan"].replace(-9999.9, df_kingston_ont["Jan"].median())
df_kingston_ont["Feb"] = df_kingston_ont["Feb"].replace(-9999.9, df_kingston_ont["Feb"].median())
df_kingston_ont["Mar"] = df_kingston_ont["Mar"].replace(-9999.9, df_kingston_ont["Mar"].median())
df_kingston_ont["Apr"] = df_kingston_ont["Apr"].replace(-9999.9, df_kingston_ont["Apr"].median())
df_kingston_ont["May"] = df_kingston_ont["May"].replace(-9999.9, df_kingston_ont["May"].median())
df_kingston_ont["Jun"] = df_kingston_ont["Jun"].replace(-9999.9, df_kingston_ont["Jun"].median())
df_kingston_ont["Jul"] = df_kingston_ont["Jul"].replace(-9999.9, df_kingston_ont["Jul"].median())
df_kingston_ont["Aug"] = df_kingston_ont["Aug"].replace(-9999.9, df_kingston_ont["Aug"].median())
df_kingston_ont["Sep"] = df_kingston_ont["Sep"].replace(-9999.9, df_kingston_ont["Sep"].median())
df_kingston_ont["Oct"] = df_kingston_ont["Oct"].replace(-9999.9, df_kingston_ont["Oct"].median())
df_kingston_ont["Nov"] = df_kingston_ont["Nov"].replace(-9999.9, df_kingston_ont["Nov"].median())
df_kingston_ont["Dec"] = df_kingston_ont["Dec"].replace(-9999.9, df_kingston_ont["Dec"].median())
df_kingston_ont["Annual"] = df_kingston_ont["Annual"].replace(-9999.9, df_kingston_ont["Annual"].median())
df_kingston_ont["Winter"] = df_kingston_ont["Winter"].replace(-9999.9, df_kingston_ont["Winter"].median())
df_kingston_ont["Spring"] = df_kingston_ont["Spring"].replace(-9999.9, df_kingston_ont["Spring"].median())
df_kingston_ont["Summer"] = df_kingston_ont["Summer"].replace(-9999.9, df_kingston_ont["Summer"].median())
df_kingston_ont["Autumn"] = df_kingston_ont["Autumn"].replace(-9999.9, df_kingston_ont["Autumn"].median())


#Kujjuuarapik Quebec

kujjuuarapik_queb = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/kujjuuarapik_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_kujjuuarapik_queb = pd.DataFrame(kujjuuarapik_queb)

df_kujjuuarapik_queb["Jan"] = df_kujjuuarapik_queb["Jan"].replace(-9999.9, df_kujjuuarapik_queb["Jan"].median())
df_kujjuuarapik_queb["Feb"] = df_kujjuuarapik_queb["Feb"].replace(-9999.9, df_kujjuuarapik_queb["Feb"].median())
df_kujjuuarapik_queb["Mar"] = df_kujjuuarapik_queb["Mar"].replace(-9999.9, df_kujjuuarapik_queb["Mar"].median())
df_kujjuuarapik_queb["Apr"] = df_kujjuuarapik_queb["Apr"].replace(-9999.9, df_kujjuuarapik_queb["Apr"].median())
df_kujjuuarapik_queb["May"] = df_kujjuuarapik_queb["May"].replace(-9999.9, df_kujjuuarapik_queb["May"].median())
df_kujjuuarapik_queb["Jun"] = df_kujjuuarapik_queb["Jun"].replace(-9999.9, df_kujjuuarapik_queb["Jun"].median())
df_kujjuuarapik_queb["Jul"] = df_kujjuuarapik_queb["Jul"].replace(-9999.9, df_kujjuuarapik_queb["Jul"].median())
df_kujjuuarapik_queb["Aug"] = df_kujjuuarapik_queb["Aug"].replace(-9999.9, df_kujjuuarapik_queb["Aug"].median())
df_kujjuuarapik_queb["Sep"] = df_kujjuuarapik_queb["Sep"].replace(-9999.9, df_kujjuuarapik_queb["Sep"].median())
df_kujjuuarapik_queb["Oct"] = df_kujjuuarapik_queb["Oct"].replace(-9999.9, df_kujjuuarapik_queb["Oct"].median())
df_kujjuuarapik_queb["Nov"] = df_kujjuuarapik_queb["Nov"].replace(-9999.9, df_kujjuuarapik_queb["Nov"].median())
df_kujjuuarapik_queb["Dec"] = df_kujjuuarapik_queb["Dec"].replace(-9999.9, df_kujjuuarapik_queb["Dec"].median())
df_kujjuuarapik_queb["Annual"] = df_kujjuuarapik_queb["Annual"].replace(-9999.9, df_kujjuuarapik_queb["Annual"].median())
df_kujjuuarapik_queb["Winter"] = df_kujjuuarapik_queb["Winter"].replace(-9999.9, df_kujjuuarapik_queb["Winter"].median())
df_kujjuuarapik_queb["Spring"] = df_kujjuuarapik_queb["Spring"].replace(-9999.9, df_kujjuuarapik_queb["Spring"].median())
df_kujjuuarapik_queb["Summer"] = df_kujjuuarapik_queb["Summer"].replace(-9999.9, df_kujjuuarapik_queb["Summer"].median())
df_kujjuuarapik_queb["Autumn"] = df_kujjuuarapik_queb["Autumn"].replace(-9999.9, df_kujjuuarapik_queb["Autumn"].median())


#Langara British Columbia 

langara_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/langara_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_langara_bc = pd.DataFrame(langara_bc)

df_langara_bc["Jan"] = df_langara_bc["Jan"].replace(-9999.9, df_langara_bc["Jan"].median())
df_langara_bc["Feb"] = df_langara_bc["Feb"].replace(-9999.9, df_langara_bc["Feb"].median())
df_langara_bc["Mar"] = df_langara_bc["Mar"].replace(-9999.9, df_langara_bc["Mar"].median())
df_langara_bc["Apr"] = df_langara_bc["Apr"].replace(-9999.9, df_langara_bc["Apr"].median())
df_langara_bc["May"] = df_langara_bc["May"].replace(-9999.9, df_langara_bc["May"].median())
df_langara_bc["Jun"] = df_langara_bc["Jun"].replace(-9999.9, df_langara_bc["Jun"].median())
df_langara_bc["Jul"] = df_langara_bc["Jul"].replace(-9999.9, df_langara_bc["Jul"].median())
df_langara_bc["Aug"] = df_langara_bc["Aug"].replace(-9999.9, df_langara_bc["Aug"].median())
df_langara_bc["Sep"] = df_langara_bc["Sep"].replace(-9999.9, df_langara_bc["Sep"].median())
df_langara_bc["Oct"] = df_langara_bc["Oct"].replace(-9999.9, df_langara_bc["Oct"].median())
df_langara_bc["Nov"] = df_langara_bc["Nov"].replace(-9999.9, df_langara_bc["Nov"].median())
df_langara_bc["Dec"] = df_langara_bc["Dec"].replace(-9999.9, df_langara_bc["Dec"].median())
df_langara_bc["Annual"] = df_langara_bc["Annual"].replace(-9999.9, df_langara_bc["Annual"].median())
df_langara_bc["Winter"] = df_langara_bc["Winter"].replace(-9999.9, df_langara_bc["Winter"].median())
df_langara_bc["Spring"] = df_langara_bc["Spring"].replace(-9999.9, df_langara_bc["Spring"].median())
df_langara_bc["Summer"] = df_langara_bc["Summer"].replace(-9999.9, df_langara_bc["Summer"].median())
df_langara_bc["Autumn"] = df_langara_bc["Autumn"].replace(-9999.9, df_langara_bc["Autumn"].median())

#Laronge Saskatchewan 

laronge_sask = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/laronge_sask.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_laronge_sask = pd.DataFrame(laronge_sask)

df_laronge_sask["Jan"] = df_laronge_sask["Jan"].replace(-9999.9, df_laronge_sask["Jan"].median())
df_laronge_sask["Feb"] = df_laronge_sask["Feb"].replace(-9999.9, df_laronge_sask["Feb"].median())
df_laronge_sask["Mar"] = df_laronge_sask["Mar"].replace(-9999.9, df_laronge_sask["Mar"].median())
df_laronge_sask["Apr"] = df_laronge_sask["Apr"].replace(-9999.9, df_laronge_sask["Apr"].median())
df_laronge_sask["May"] = df_laronge_sask["May"].replace(-9999.9, df_laronge_sask["May"].median())
df_laronge_sask["Jun"] = df_laronge_sask["Jun"].replace(-9999.9, df_laronge_sask["Jun"].median())
df_laronge_sask["Jul"] = df_laronge_sask["Jul"].replace(-9999.9, df_laronge_sask["Jul"].median())
df_laronge_sask["Aug"] = df_laronge_sask["Aug"].replace(-9999.9, df_laronge_sask["Aug"].median())
df_laronge_sask["Sep"] = df_laronge_sask["Sep"].replace(-9999.9, df_laronge_sask["Sep"].median())
df_laronge_sask["Oct"] = df_laronge_sask["Oct"].replace(-9999.9, df_laronge_sask["Oct"].median())
df_laronge_sask["Nov"] = df_laronge_sask["Nov"].replace(-9999.9, df_laronge_sask["Nov"].median())
df_laronge_sask["Dec"] = df_laronge_sask["Dec"].replace(-9999.9, df_laronge_sask["Dec"].median())
df_laronge_sask["Annual"] = df_laronge_sask["Annual"].replace(-9999.9, df_laronge_sask["Annual"].median())
df_laronge_sask["Winter"] = df_laronge_sask["Winter"].replace(-9999.9, df_laronge_sask["Winter"].median())
df_laronge_sask["Spring"] = df_laronge_sask["Spring"].replace(-9999.9, df_laronge_sask["Spring"].median())
df_laronge_sask["Summer"] = df_laronge_sask["Summer"].replace(-9999.9, df_laronge_sask["Summer"].median())
df_laronge_sask["Autumn"] = df_laronge_sask["Autumn"].replace(-9999.9, df_laronge_sask["Autumn"].median())


#Lethbridge Alberta 

lethbridge_alber = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/lethbridge_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_lethbridge_alber = pd.DataFrame(lethbridge_alber)

#London Ontario

london_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/london_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_london_ont = pd.DataFrame(london_ont)


#Longstaff Bluff Nunuvut 

longstaffbluff_nu = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/longstaffbluff_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_longstaffbluff_nu = pd.DataFrame(longstaffbluff_nu)

df_longstaffbluff_nu["Jan"] = df_longstaffbluff_nu["Jan"].replace(-9999.9, df_longstaffbluff_nu["Jan"].median())
df_longstaffbluff_nu["Feb"] = df_longstaffbluff_nu["Feb"].replace(-9999.9, df_longstaffbluff_nu["Feb"].median())
df_longstaffbluff_nu["Mar"] = df_longstaffbluff_nu["Mar"].replace(-9999.9, df_longstaffbluff_nu["Mar"].median())
df_longstaffbluff_nu["Apr"] = df_longstaffbluff_nu["Apr"].replace(-9999.9, df_longstaffbluff_nu["Apr"].median())
df_longstaffbluff_nu["May"] = df_longstaffbluff_nu["May"].replace(-9999.9, df_longstaffbluff_nu["May"].median())
df_longstaffbluff_nu["Jun"] = df_longstaffbluff_nu["Jun"].replace(-9999.9, df_longstaffbluff_nu["Jun"].median())
df_longstaffbluff_nu["Jul"] = df_longstaffbluff_nu["Jul"].replace(-9999.9, df_longstaffbluff_nu["Jul"].median())
df_longstaffbluff_nu["Aug"] = df_longstaffbluff_nu["Aug"].replace(-9999.9, df_longstaffbluff_nu["Aug"].median())
df_longstaffbluff_nu["Sep"] = df_longstaffbluff_nu["Sep"].replace(-9999.9, df_longstaffbluff_nu["Sep"].median())
df_longstaffbluff_nu["Oct"] = df_longstaffbluff_nu["Oct"].replace(-9999.9, df_longstaffbluff_nu["Oct"].median())
df_longstaffbluff_nu["Nov"] = df_longstaffbluff_nu["Nov"].replace(-9999.9, df_longstaffbluff_nu["Nov"].median())
df_longstaffbluff_nu["Dec"] = df_longstaffbluff_nu["Dec"].replace(-9999.9, df_longstaffbluff_nu["Dec"].median())
df_longstaffbluff_nu["Annual"] = df_longstaffbluff_nu["Annual"].replace(-9999.9, df_longstaffbluff_nu["Annual"].median())
df_longstaffbluff_nu["Winter"] = df_longstaffbluff_nu["Winter"].replace(-9999.9, df_longstaffbluff_nu["Winter"].median())
df_longstaffbluff_nu["Spring"] = df_longstaffbluff_nu["Spring"].replace(-9999.9, df_longstaffbluff_nu["Spring"].median())
df_longstaffbluff_nu["Summer"] = df_longstaffbluff_nu["Summer"].replace(-9999.9, df_longstaffbluff_nu["Summer"].median())
df_longstaffbluff_nu["Autumn"] = df_longstaffbluff_nu["Autumn"].replace(-9999.9, df_longstaffbluff_nu["Autumn"].median())


#Mayo Yukon Territories 

mayo_yt = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/mayo_yt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_mayo_yt = pd.DataFrame(mayo_yt)

df_mayo_yt["Apr"] = df_mayo_yt["Apr"].replace(-9999.9, df_mayo_yt["Apr"].median())
df_mayo_yt["May"] = df_mayo_yt["May"].replace(-9999.9, df_mayo_yt["Apr"].median())
df_mayo_yt["Oct"] = df_mayo_yt["Oct"].replace(-9999.9, df_mayo_yt["Oct"].median())
df_mayo_yt["Spring"] = df_mayo_yt["Spring"].replace(-9999.9, df_mayo_yt["Spring"].median())


#McInessisland British Columbia 

mcinessisland_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/mcinessisland_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_mcinessisland_bc = pd.DataFrame(mcinessisland_bc)

df_mcinessisland_bc["Jan"] = df_mcinessisland_bc["Jan"].replace(-9999.9, df_mcinessisland_bc["Jan"].median())
df_mcinessisland_bc["Feb"] = df_mcinessisland_bc["Feb"].replace(-9999.9, df_mcinessisland_bc["Feb"].median())
df_mcinessisland_bc["Mar"] = df_mcinessisland_bc["Mar"].replace(-9999.9, df_mcinessisland_bc["Mar"].median())
df_mcinessisland_bc["Apr"] = df_mcinessisland_bc["Apr"].replace(-9999.9, df_mcinessisland_bc["Apr"].median())
df_mcinessisland_bc["May"] = df_mcinessisland_bc["May"].replace(-9999.9, df_mcinessisland_bc["May"].median())
df_mcinessisland_bc["Jun"] = df_mcinessisland_bc["Jun"].replace(-9999.9, df_mcinessisland_bc["Jun"].median())
df_mcinessisland_bc["Jul"] = df_mcinessisland_bc["Jul"].replace(-9999.9, df_mcinessisland_bc["Jul"].median())
df_mcinessisland_bc["Aug"] = df_mcinessisland_bc["Aug"].replace(-9999.9, df_mcinessisland_bc["Aug"].median())
df_mcinessisland_bc["Sep"] = df_mcinessisland_bc["Sep"].replace(-9999.9, df_mcinessisland_bc["Sep"].median())
df_mcinessisland_bc["Oct"] = df_mcinessisland_bc["Oct"].replace(-9999.9, df_mcinessisland_bc["Oct"].median())
df_mcinessisland_bc["Nov"] = df_mcinessisland_bc["Nov"].replace(-9999.9, df_mcinessisland_bc["Nov"].median())
df_mcinessisland_bc["Dec"] = df_mcinessisland_bc["Dec"].replace(-9999.9, df_mcinessisland_bc["Dec"].median())
df_mcinessisland_bc["Annual"] = df_mcinessisland_bc["Annual"].replace(-9999.9, df_mcinessisland_bc["Annual"].median())
df_mcinessisland_bc["Winter"] = df_mcinessisland_bc["Winter"].replace(-9999.9, df_mcinessisland_bc["Winter"].median())
df_mcinessisland_bc["Spring"] = df_mcinessisland_bc["Spring"].replace(-9999.9, df_mcinessisland_bc["Spring"].median())
df_mcinessisland_bc["Summer"] = df_mcinessisland_bc["Summer"].replace(-9999.9, df_mcinessisland_bc["Summer"].median())
df_mcinessisland_bc["Autumn"] = df_mcinessisland_bc["Autumn"].replace(-9999.9, df_mcinessisland_bc["Autumn"].median())


#Medicinehat Alberta 

medicinehat_alber = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/medicinehat_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_medicinehat_alber = pd.DataFrame(medicinehat_alber)

df_medicinehat_alber.dropna(axis = 1, how='all', inplace = True)
df_medicinehat_alber.dropna(axis = 0, how='all', inplace = True)
df_medicinehat_alber.dropna(axis = 0, how='any', inplace = True)

df_medicinehat_alber["Jan"] = df_medicinehat_alber["Jan"].replace(-9999.9, df_medicinehat_alber["Jan"].median())
df_medicinehat_alber["Feb"] = df_medicinehat_alber["Feb"].replace(-9999.9, df_medicinehat_alber["Feb"].median())
df_medicinehat_alber["Mar"] = df_medicinehat_alber["Mar"].replace(-9999.9, df_medicinehat_alber["Mar"].median())
df_medicinehat_alber["Apr"] = df_medicinehat_alber["Apr"].replace(-9999.9, df_medicinehat_alber["Apr"].median())
df_medicinehat_alber["May"] = df_medicinehat_alber["May"].replace(-9999.9, df_medicinehat_alber["May"].median())
df_medicinehat_alber["Jun"] = df_medicinehat_alber["Jun"].replace(-9999.9, df_medicinehat_alber["Jun"].median())
df_medicinehat_alber["Jul"] = df_medicinehat_alber["Jul"].replace(-9999.9, df_medicinehat_alber["Jul"].median())
df_medicinehat_alber["Aug"] = df_medicinehat_alber["Aug"].replace(-9999.9, df_medicinehat_alber["Aug"].median())
df_medicinehat_alber["Sep"] = df_medicinehat_alber["Sep"].replace(-9999.9, df_medicinehat_alber["Sep"].median())
df_medicinehat_alber["Oct"] = df_medicinehat_alber["Oct"].replace(-9999.9, df_medicinehat_alber["Oct"].median())
df_medicinehat_alber["Nov"] = df_medicinehat_alber["Nov"].replace(-9999.9, df_medicinehat_alber["Nov"].median())
df_medicinehat_alber["Dec"] = df_medicinehat_alber["Dec"].replace(-9999.9, df_medicinehat_alber["Dec"].median())
df_medicinehat_alber["Annual"] = df_medicinehat_alber["Annual"].replace(-9999.9, df_medicinehat_alber["Annual"].median())
df_medicinehat_alber["Winter"] = df_medicinehat_alber["Winter"].replace(-9999.9, df_medicinehat_alber["Winter"].median())
df_medicinehat_alber["Spring"] = df_medicinehat_alber["Spring"].replace(-9999.9, df_medicinehat_alber["Spring"].median())
df_medicinehat_alber["Summer"] = df_medicinehat_alber["Summer"].replace(-9999.9, df_medicinehat_alber["Summer"].median())
df_medicinehat_alber["Autumn"] = df_medicinehat_alber["Autumn"].replace(-9999.9, df_medicinehat_alber["Autumn"].median())


#Miramichi New Brunswick 

miramichi_nb = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/miramichi_nb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_miramichi_nb = pd.DataFrame(miramichi_nb)

df_miramichi_nb["Jan"] = df_miramichi_nb["Jan"].replace(-9999.9, df_miramichi_nb["Jan"].median())
df_miramichi_nb["Feb"] = df_miramichi_nb["Feb"].replace(-9999.9, df_miramichi_nb["Feb"].median())
df_miramichi_nb["Mar"] = df_miramichi_nb["Mar"].replace(-9999.9, df_miramichi_nb["Mar"].median())
df_miramichi_nb["Apr"] = df_miramichi_nb["Apr"].replace(-9999.9, df_miramichi_nb["Apr"].median())
df_miramichi_nb["May"] = df_miramichi_nb["May"].replace(-9999.9, df_miramichi_nb["May"].median())
df_miramichi_nb["Jun"] = df_miramichi_nb["Jun"].replace(-9999.9, df_miramichi_nb["Jun"].median())
df_miramichi_nb["Jul"] = df_miramichi_nb["Jul"].replace(-9999.9, df_miramichi_nb["Jul"].median())
df_miramichi_nb["Aug"] = df_miramichi_nb["Aug"].replace(-9999.9, df_miramichi_nb["Aug"].median())
df_miramichi_nb["Sep"] = df_miramichi_nb["Sep"].replace(-9999.9, df_miramichi_nb["Sep"].median())
df_miramichi_nb["Oct"] = df_miramichi_nb["Oct"].replace(-9999.9, df_miramichi_nb["Oct"].median())
df_miramichi_nb["Nov"] = df_miramichi_nb["Nov"].replace(-9999.9, df_miramichi_nb["Nov"].median())
df_miramichi_nb["Dec"] = df_miramichi_nb["Dec"].replace(-9999.9, df_miramichi_nb["Dec"].median())
df_miramichi_nb["Annual"] = df_miramichi_nb["Annual"].replace(-9999.9, df_miramichi_nb["Annual"].median())
df_miramichi_nb["Winter"] = df_miramichi_nb["Winter"].replace(-9999.9, df_miramichi_nb["Winter"].median())
df_miramichi_nb["Spring"] = df_miramichi_nb["Spring"].replace(-9999.9, df_miramichi_nb["Spring"].median())
df_miramichi_nb["Summer"] = df_miramichi_nb["Summer"].replace(-9999.9, df_miramichi_nb["Summer"].median())
df_miramichi_nb["Autumn"] = df_miramichi_nb["Autumn"].replace(-9999.9, df_miramichi_nb["Autumn"].median())


#Miscousisland New Brunswick 

miscouisland_nb= pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/miscouisland_nb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_miscouisland_nb = pd.DataFrame(miscouisland_nb)

df_miscouisland_nb["Jan"] = df_miscouisland_nb["Jan"].replace(-9999.9, df_miscouisland_nb["Jan"].median())
df_miscouisland_nb["Feb"] = df_miscouisland_nb["Feb"].replace(-9999.9, df_miscouisland_nb["Feb"].median())
df_miscouisland_nb["Mar"] = df_miscouisland_nb["Mar"].replace(-9999.9, df_miscouisland_nb["Mar"].median())
df_miscouisland_nb["Apr"] = df_miscouisland_nb["Apr"].replace(-9999.9, df_miscouisland_nb["Apr"].median())
df_miscouisland_nb["May"] = df_miscouisland_nb["May"].replace(-9999.9, df_miscouisland_nb["May"].median())
df_miscouisland_nb["Jun"] = df_miscouisland_nb["Jun"].replace(-9999.9, df_miscouisland_nb["Jun"].median())
df_miscouisland_nb["Jul"] = df_miscouisland_nb["Jul"].replace(-9999.9, df_miscouisland_nb["Jul"].median())
df_miscouisland_nb["Aug"] = df_miscouisland_nb["Aug"].replace(-9999.9, df_miscouisland_nb["Aug"].median())
df_miscouisland_nb["Sep"] = df_miscouisland_nb["Sep"].replace(-9999.9, df_miscouisland_nb["Sep"].median())
df_miscouisland_nb["Oct"] = df_miscouisland_nb["Oct"].replace(-9999.9, df_miscouisland_nb["Oct"].median())
df_miscouisland_nb["Nov"] = df_miscouisland_nb["Nov"].replace(-9999.9, df_miscouisland_nb["Nov"].median())
df_miscouisland_nb["Dec"] = df_miscouisland_nb["Dec"].replace(-9999.9, df_miscouisland_nb["Dec"].median())
df_miscouisland_nb["Annual"] = df_miscouisland_nb["Annual"].replace(-9999.9, df_miscouisland_nb["Annual"].median())
df_miscouisland_nb["Winter"] = df_miscouisland_nb["Winter"].replace(-9999.9, df_miscouisland_nb["Winter"].median())
df_miscouisland_nb["Spring"] = df_miscouisland_nb["Spring"].replace(-9999.9, df_miscouisland_nb["Spring"].median())
df_miscouisland_nb["Summer"] = df_miscouisland_nb["Summer"].replace(-9999.9, df_miscouisland_nb["Summer"].median())
df_miscouisland_nb["Autumn"] = df_miscouisland_nb["Autumn"].replace(-9999.9, df_miscouisland_nb["Autumn"].median())


#Moncton New Brusnwick 

moncton_nb= pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/moncton_nb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_moncton_nb = pd.DataFrame(moncton_nb)


#Montjoli Quebec 

montjoli_queb = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/montjoli_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding ='utf-8-sig')
df_montjoli_queb = pd.DataFrame(montjoli_queb)

df_montjoli_queb["Oct"] = df_montjoli_queb["Oct"].replace(-9999.9, df_montjoli_queb["Oct"].median())


#Montreal Quebec 

montrealpet_queb = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/montrealpet_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_montrealpet_queb = pd.DataFrame(montrealpet_queb)

#Moosejaw Saskatchewan

moosejaw_sask = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/moosejaw_sask.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_moosejaw_sask = pd.DataFrame(moosejaw_sask)

df_moosejaw_sask["Jan"] = df_moosejaw_sask["Jan"].replace(-9999.9, df_moosejaw_sask["Jan"].median())
df_moosejaw_sask["Feb"] = df_moosejaw_sask["Feb"].replace(-9999.9, df_moosejaw_sask["Feb"].median())
df_moosejaw_sask["Mar"] = df_moosejaw_sask["Mar"].replace(-9999.9, df_moosejaw_sask["Mar"].median())
df_moosejaw_sask["Apr"] = df_moosejaw_sask["Apr"].replace(-9999.9, df_moosejaw_sask["Apr"].median())
df_moosejaw_sask["May"] = df_moosejaw_sask["May"].replace(-9999.9, df_moosejaw_sask["May"].median())
df_moosejaw_sask["Jun"] = df_moosejaw_sask["Jun"].replace(-9999.9, df_moosejaw_sask["Jun"].median())
df_moosejaw_sask["Jul"] = df_moosejaw_sask["Jul"].replace(-9999.9, df_moosejaw_sask["Jul"].median())
df_moosejaw_sask["Aug"] = df_moosejaw_sask["Aug"].replace(-9999.9, df_moosejaw_sask["Aug"].median())
df_moosejaw_sask["Sep"] = df_moosejaw_sask["Sep"].replace(-9999.9, df_moosejaw_sask["Sep"].median())
df_moosejaw_sask["Oct"] = df_moosejaw_sask["Oct"].replace(-9999.9, df_moosejaw_sask["Oct"].median())
df_moosejaw_sask["Nov"] = df_moosejaw_sask["Nov"].replace(-9999.9, df_moosejaw_sask["Nov"].median())
df_moosejaw_sask["Dec"] = df_moosejaw_sask["Dec"].replace(-9999.9, df_moosejaw_sask["Dec"].median())
df_moosejaw_sask["Annual"] = df_moosejaw_sask["Annual"].replace(-9999.9, df_moosejaw_sask["Annual"].median())
df_moosejaw_sask["Winter"] = df_moosejaw_sask["Winter"].replace(-9999.9, df_moosejaw_sask["Winter"].median())
df_moosejaw_sask["Spring"] = df_moosejaw_sask["Spring"].replace(-9999.9, df_moosejaw_sask["Spring"].median())
df_moosejaw_sask["Summer"] = df_moosejaw_sask["Summer"].replace(-9999.9, df_moosejaw_sask["Summer"].median())
df_moosejaw_sask["Autumn"] = df_moosejaw_sask["Autumn"].replace(-9999.9, df_moosejaw_sask["Autumn"].median())


#Mossonee Ontario 

mossonee_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/mossonee_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_mossonee_ont = pd.DataFrame(mossonee_ont)

df_mossonee_ont["Jan"] = df_mossonee_ont["Jan"].replace(-9999.9, df_mossonee_ont["Jan"].median())
df_mossonee_ont["Feb"] = df_mossonee_ont["Feb"].replace(-9999.9, df_mossonee_ont["Feb"].median())
df_mossonee_ont["Mar"] = df_mossonee_ont["Mar"].replace(-9999.9, df_mossonee_ont["Mar"].median())
df_mossonee_ont["Apr"] = df_mossonee_ont["Apr"].replace(-9999.9, df_mossonee_ont["Apr"].median())
df_mossonee_ont["May"] = df_mossonee_ont["May"].replace(-9999.9, df_mossonee_ont["May"].median())
df_mossonee_ont["Jun"] = df_mossonee_ont["Jun"].replace(-9999.9, df_mossonee_ont["Jun"].median())
df_mossonee_ont["Jul"] = df_mossonee_ont["Jul"].replace(-9999.9, df_mossonee_ont["Jul"].median())
df_mossonee_ont["Aug"] = df_mossonee_ont["Aug"].replace(-9999.9, df_mossonee_ont["Aug"].median())
df_mossonee_ont["Sep"] = df_mossonee_ont["Sep"].replace(-9999.9, df_mossonee_ont["Sep"].median())
df_mossonee_ont["Oct"] = df_mossonee_ont["Oct"].replace(-9999.9, df_mossonee_ont["Oct"].median())
df_mossonee_ont["Nov"] = df_mossonee_ont["Nov"].replace(-9999.9, df_mossonee_ont["Nov"].median())
df_mossonee_ont["Dec"] = df_mossonee_ont["Dec"].replace(-9999.9, df_mossonee_ont["Dec"].median())
df_mossonee_ont["Annual"] = df_mossonee_ont["Annual"].replace(-9999.9, df_mossonee_ont["Annual"].median())
df_mossonee_ont["Winter"] = df_mossonee_ont["Winter"].replace(-9999.9, df_mossonee_ont["Winter"].median())
df_mossonee_ont["Spring"] = df_mossonee_ont["Spring"].replace(-9999.9, df_mossonee_ont["Spring"].median())
df_mossonee_ont["Summer"] = df_mossonee_ont["Summer"].replace(-9999.9, df_mossonee_ont["Summer"].median())
df_mossonee_ont["Autumn"] = df_mossonee_ont["Autumn"].replace(-9999.9, df_mossonee_ont["Autumn"].median())

#Mouldbay North West Territories 

mouldbay_nwt = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/mouldbay_nwt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_mouldbay_nwt = pd.DataFrame(mouldbay_nwt)

df_mouldbay_nwt["Jan"] = df_mouldbay_nwt["Jan"].replace(-9999.9, df_mouldbay_nwt["Jan"].median())
df_mouldbay_nwt["Feb"] = df_mouldbay_nwt["Feb"].replace(-9999.9, df_mouldbay_nwt["Feb"].median())
df_mouldbay_nwt["Mar"] = df_mouldbay_nwt["Mar"].replace(-9999.9, df_mouldbay_nwt["Mar"].median())
df_mouldbay_nwt["Apr"] = df_mouldbay_nwt["Apr"].replace(-9999.9, df_mouldbay_nwt["Apr"].median())
df_mouldbay_nwt["May"] = df_mouldbay_nwt["May"].replace(-9999.9, df_mouldbay_nwt["May"].median())
df_mouldbay_nwt["Jun"] = df_mouldbay_nwt["Jun"].replace(-9999.9, df_mouldbay_nwt["Jun"].median())
df_mouldbay_nwt["Jul"] = df_mouldbay_nwt["Jul"].replace(-9999.9, df_mouldbay_nwt["Jul"].median())
df_mouldbay_nwt["Aug"] = df_mouldbay_nwt["Aug"].replace(-9999.9, df_mouldbay_nwt["Aug"].median())
df_mouldbay_nwt["Sep"] = df_mouldbay_nwt["Sep"].replace(-9999.9, df_mouldbay_nwt["Sep"].median())
df_mouldbay_nwt["Oct"] = df_mouldbay_nwt["Oct"].replace(-9999.9, df_mouldbay_nwt["Oct"].median())
df_mouldbay_nwt["Nov"] = df_mouldbay_nwt["Nov"].replace(-9999.9, df_mouldbay_nwt["Nov"].median())
df_mouldbay_nwt["Dec"] = df_mouldbay_nwt["Dec"].replace(-9999.9, df_mouldbay_nwt["Dec"].median())
df_mouldbay_nwt["Annual"] = df_mouldbay_nwt["Annual"].replace(-9999.9, df_mouldbay_nwt["Annual"].median())
df_mouldbay_nwt["Winter"] = df_mouldbay_nwt["Winter"].replace(-9999.9, df_mouldbay_nwt["Winter"].median())
df_mouldbay_nwt["Spring"] = df_mouldbay_nwt["Spring"].replace(-9999.9, df_mouldbay_nwt["Spring"].median())
df_mouldbay_nwt["Summer"] = df_mouldbay_nwt["Summer"].replace(-9999.9, df_mouldbay_nwt["Summer"].median())
df_mouldbay_nwt["Autumn"] = df_mouldbay_nwt["Autumn"].replace(-9999.9, df_mouldbay_nwt["Autumn"].median())


#Muskoka Ontario

muskoka_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/muskoka_ont.csv",engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_muskoka_ont = pd.DataFrame(muskoka_ont)


df_muskoka_ont["Jul"] = df_muskoka_ont["Jul"].replace(-9999.9, df_muskoka_ont["Jul"].median())
df_muskoka_ont["Aug"] = df_muskoka_ont["Aug"].replace(-9999.9, df_muskoka_ont["Aug"].median())
df_muskoka_ont["Summer"] = df_muskoka_ont["Summer"].replace(-9999.9, df_muskoka_ont["Summer"].median())
df_muskoka_ont["Autumn"] = df_muskoka_ont["Autumn"].replace(-9999.9, df_muskoka_ont["Autumn"].median())
df_muskoka_ont["Oct"] = df_muskoka_ont["Oct"].replace(-9999.9, df_muskoka_ont["Oct"].median())
df_muskoka_ont["Nov"] = df_muskoka_ont["Nov"].replace(-9999.9, df_muskoka_ont["Nov"].median())

#Nanaimo British Columbia 

nanaimo_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/nanaimo_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_nanaimo_bc = pd.DataFrame(nanaimo_bc)

df_nanaimo_bc["Jan"] = df_nanaimo_bc["Jan"].replace(-9999.9, df_nanaimo_bc["Jan"].median())
df_nanaimo_bc["Feb"] = df_nanaimo_bc["Feb"].replace(-9999.9, df_nanaimo_bc["Feb"].median())
df_nanaimo_bc["Mar"] = df_nanaimo_bc["Mar"].replace(-9999.9, df_nanaimo_bc["Mar"].median())
df_nanaimo_bc["Apr"] = df_nanaimo_bc["Apr"].replace(-9999.9, df_nanaimo_bc["Apr"].median())
df_nanaimo_bc["May"] = df_nanaimo_bc["May"].replace(-9999.9, df_nanaimo_bc["May"].median())
df_nanaimo_bc["Jun"] = df_nanaimo_bc["Jun"].replace(-9999.9, df_nanaimo_bc["Jun"].median())
df_nanaimo_bc["Jul"] = df_nanaimo_bc["Jul"].replace(-9999.9, df_nanaimo_bc["Jul"].median())
df_nanaimo_bc["Aug"] = df_nanaimo_bc["Aug"].replace(-9999.9, df_nanaimo_bc["Aug"].median())
df_nanaimo_bc["Sep"] = df_nanaimo_bc["Sep"].replace(-9999.9, df_nanaimo_bc["Sep"].median())
df_nanaimo_bc["Oct"] = df_nanaimo_bc["Oct"].replace(-9999.9, df_nanaimo_bc["Oct"].median())
df_nanaimo_bc["Nov"] = df_nanaimo_bc["Nov"].replace(-9999.9, df_nanaimo_bc["Nov"].median())
df_nanaimo_bc["Dec"] = df_nanaimo_bc["Dec"].replace(-9999.9, df_nanaimo_bc["Dec"].median())
df_nanaimo_bc["Annual"] = df_nanaimo_bc["Annual"].replace(-9999.9, df_nanaimo_bc["Annual"].median())
df_nanaimo_bc["Winter"] = df_nanaimo_bc["Winter"].replace(-9999.9, df_nanaimo_bc["Winter"].median())
df_nanaimo_bc["Spring"] = df_nanaimo_bc["Spring"].replace(-9999.9, df_nanaimo_bc["Spring"].median())
df_nanaimo_bc["Summer"] = df_nanaimo_bc["Summer"].replace(-9999.9, df_nanaimo_bc["Summer"].median())
df_nanaimo_bc["Autumn"] = df_nanaimo_bc["Autumn"].replace(-9999.9, df_nanaimo_bc["Autumn"].median())


#Natashquan Quebec 

natashquan_queb = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/natashquan_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_natashquan_queb = pd.DataFrame(natashquan_queb)

df_natashquan_queb["Jan"] = df_natashquan_queb["Jan"].replace(-9999.9, df_natashquan_queb["Jan"].median())
df_natashquan_queb["Feb"] = df_natashquan_queb["Feb"].replace(-9999.9, df_natashquan_queb["Feb"].median())
df_natashquan_queb["Mar"] = df_natashquan_queb["Mar"].replace(-9999.9, df_natashquan_queb["Mar"].median())
df_natashquan_queb["Apr"] = df_natashquan_queb["Apr"].replace(-9999.9, df_natashquan_queb["Apr"].median())
df_natashquan_queb["May"] = df_natashquan_queb["May"].replace(-9999.9, df_natashquan_queb["May"].median())
df_natashquan_queb["Jun"] = df_natashquan_queb["Jun"].replace(-9999.9, df_natashquan_queb["Jun"].median())
df_natashquan_queb["Jul"] = df_natashquan_queb["Jul"].replace(-9999.9, df_natashquan_queb["Jul"].median())
df_natashquan_queb["Aug"] = df_natashquan_queb["Aug"].replace(-9999.9, df_natashquan_queb["Aug"].median())
df_natashquan_queb["Sep"] = df_natashquan_queb["Sep"].replace(-9999.9, df_natashquan_queb["Sep"].median())
df_natashquan_queb["Oct"] = df_natashquan_queb["Oct"].replace(-9999.9, df_natashquan_queb["Oct"].median())
df_natashquan_queb["Nov"] = df_natashquan_queb["Nov"].replace(-9999.9, df_natashquan_queb["Nov"].median())
df_natashquan_queb["Dec"] = df_natashquan_queb["Dec"].replace(-9999.9, df_natashquan_queb["Dec"].median())
df_natashquan_queb["Annual"] = df_natashquan_queb["Annual"].replace(-9999.9, df_natashquan_queb["Annual"].median())
df_natashquan_queb["Winter"] = df_natashquan_queb["Winter"].replace(-9999.9, df_natashquan_queb["Winter"].median())
df_natashquan_queb["Spring"] = df_natashquan_queb["Spring"].replace(-9999.9, df_natashquan_queb["Spring"].median())
df_natashquan_queb["Summer"] = df_natashquan_queb["Summer"].replace(-9999.9, df_natashquan_queb["Summer"].median())
df_natashquan_queb["Autumn"] = df_natashquan_queb["Autumn"].replace(-9999.9, df_natashquan_queb["Autumn"].median())


#Normalwells North West Territories 

normalwells_nwt = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/normalwells_nwt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_normalwells_nwt = pd.DataFrame(normalwells_nwt)


df_normalwells_nwt["Oct"] = df_normalwells_nwt["Oct"].replace(-9999.9, df_normalwells_nwt["Oct"].median())


#Northbattleford Saskatchewan 

northbattleford_sask = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/northbattleford_sask.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_northbattleford_sask = pd.DataFrame(northbattleford_sask)

df_northbattleford_sask["Sep"] = df_northbattleford_sask["Sep"].replace(-9999.9, df_northbattleford_sask["Sep"].median())
df_northbattleford_sask["Oct"] = df_northbattleford_sask["Oct"].replace(-9999.9, df_northbattleford_sask["Oct"].median())
df_northbattleford_sask["Autumn"] = df_northbattleford_sask["Autumn"].replace(-9999.9, df_northbattleford_sask["Autumn"].median())


#North Bay Ontario

northbay_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/northbay_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_northbay_ont = pd.DataFrame(northbay_ont)


#Ottawa Ontario

ottawa_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/ottawa_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_ottawa_ont = pd.DataFrame(ottawa_ont)


#Peace River Alberta 
peaceriver_alber = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/peaceriver_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_peaceriver_alber = pd.DataFrame(peaceriver_alber)

df_peaceriver_alber["Jan"] = df_peaceriver_alber["Jan"].replace(-9999.9, df_peaceriver_alber["Jan"].median())
df_peaceriver_alber["Feb"] = df_peaceriver_alber["Feb"].replace(-9999.9, df_peaceriver_alber["Feb"].median())
df_peaceriver_alber["Mar"] = df_peaceriver_alber["Mar"].replace(-9999.9, df_peaceriver_alber["Mar"].median())
df_peaceriver_alber["Apr"] = df_peaceriver_alber["Apr"].replace(-9999.9, df_peaceriver_alber["Apr"].median())
df_peaceriver_alber["May"] = df_peaceriver_alber["May"].replace(-9999.9, df_peaceriver_alber["May"].median())
df_peaceriver_alber["Jun"] = df_peaceriver_alber["Jun"].replace(-9999.9, df_peaceriver_alber["Jun"].median())
df_peaceriver_alber["Jul"] = df_peaceriver_alber["Jul"].replace(-9999.9, df_peaceriver_alber["Jul"].median())
df_peaceriver_alber["Aug"] = df_peaceriver_alber["Aug"].replace(-9999.9, df_peaceriver_alber["Aug"].median())
df_peaceriver_alber["Sep"] = df_peaceriver_alber["Sep"].replace(-9999.9, df_peaceriver_alber["Sep"].median())
df_peaceriver_alber["Oct"] = df_peaceriver_alber["Oct"].replace(-9999.9, df_peaceriver_alber["Oct"].median())
df_peaceriver_alber["Nov"] = df_peaceriver_alber["Nov"].replace(-9999.9, df_peaceriver_alber["Nov"].median())
df_peaceriver_alber["Dec"] = df_peaceriver_alber["Dec"].replace(-9999.9, df_peaceriver_alber["Dec"].median())
df_peaceriver_alber["Annual"] = df_peaceriver_alber["Annual"].replace(-9999.9, df_peaceriver_alber["Annual"].median())
df_peaceriver_alber["Winter"] = df_peaceriver_alber["Winter"].replace(-9999.9, df_peaceriver_alber["Winter"].median())
df_peaceriver_alber["Spring"] = df_peaceriver_alber["Spring"].replace(-9999.9, df_peaceriver_alber["Spring"].median())
df_peaceriver_alber["Summer"] = df_peaceriver_alber["Summer"].replace(-9999.9, df_peaceriver_alber["Summer"].median())
df_peaceriver_alber["Autumn"] = df_peaceriver_alber["Autumn"].replace(-9999.9, df_peaceriver_alber["Autumn"].median())


#Penticton British Columbia 

penticton_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/penticton_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_penticton_bc = pd.DataFrame(penticton_bc)


#Pilot Mound Manitoba 

pilotmound_man = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/pilotmound_man.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_pilotmound_man = pd.DataFrame(pilotmound_man)

df_pilotmound_man["Jan"] = df_pilotmound_man["Jan"].replace(-9999.9, df_pilotmound_man["Jan"].median())
df_pilotmound_man["Feb"] = df_pilotmound_man["Feb"].replace(-9999.9, df_pilotmound_man["Feb"].median())
df_pilotmound_man["Mar"] = df_pilotmound_man["Mar"].replace(-9999.9, df_pilotmound_man["Mar"].median())
df_pilotmound_man["Apr"] = df_pilotmound_man["Apr"].replace(-9999.9, df_pilotmound_man["Apr"].median())
df_pilotmound_man["May"] = df_pilotmound_man["May"].replace(-9999.9, df_pilotmound_man["May"].median())
df_pilotmound_man["Jun"] = df_pilotmound_man["Jun"].replace(-9999.9, df_pilotmound_man["Jun"].median())
df_pilotmound_man["Jul"] = df_pilotmound_man["Jul"].replace(-9999.9, df_pilotmound_man["Jul"].median())
df_pilotmound_man["Aug"] = df_pilotmound_man["Aug"].replace(-9999.9, df_pilotmound_man["Aug"].median())
df_pilotmound_man["Sep"] = df_pilotmound_man["Sep"].replace(-9999.9, df_pilotmound_man["Sep"].median())
df_pilotmound_man["Oct"] = df_pilotmound_man["Oct"].replace(-9999.9, df_pilotmound_man["Oct"].median())
df_pilotmound_man["Nov"] = df_pilotmound_man["Nov"].replace(-9999.9, df_pilotmound_man["Nov"].median())
df_pilotmound_man["Dec"] = df_pilotmound_man["Dec"].replace(-9999.9, df_pilotmound_man["Dec"].median())
df_pilotmound_man["Annual"] = df_pilotmound_man["Annual"].replace(-9999.9, df_pilotmound_man["Annual"].median())
df_pilotmound_man["Winter"] = df_pilotmound_man["Winter"].replace(-9999.9, df_pilotmound_man["Winter"].median())
df_pilotmound_man["Spring"] = df_pilotmound_man["Spring"].replace(-9999.9, df_pilotmound_man["Spring"].median())
df_pilotmound_man["Summer"] = df_pilotmound_man["Summer"].replace(-9999.9, df_pilotmound_man["Summer"].median())
df_pilotmound_man["Autumn"] = df_pilotmound_man["Autumn"].replace(-9999.9, df_pilotmound_man["Autumn"].median())


#Port Aux Basque Newfoundland 

portauxbasque_nfld = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/portauxbasque_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_portauxbasque_nfld = pd.DataFrame(portauxbasque_nfld)


df_portauxbasque_nfld["Jan"] = df_portauxbasque_nfld["Jan"].replace(-9999.9, df_portauxbasque_nfld["Jan"].median())
df_portauxbasque_nfld["Feb"] = df_portauxbasque_nfld["Feb"].replace(-9999.9, df_portauxbasque_nfld["Feb"].median())
df_portauxbasque_nfld["Mar"] = df_portauxbasque_nfld["Mar"].replace(-9999.9, df_portauxbasque_nfld["Mar"].median())
df_portauxbasque_nfld["Apr"] = df_portauxbasque_nfld["Apr"].replace(-9999.9, df_portauxbasque_nfld["Apr"].median())
df_portauxbasque_nfld["May"] = df_portauxbasque_nfld["May"].replace(-9999.9, df_portauxbasque_nfld["May"].median())
df_portauxbasque_nfld["Jun"] = df_portauxbasque_nfld["Jun"].replace(-9999.9, df_portauxbasque_nfld["Jun"].median())
df_portauxbasque_nfld["Jul"] = df_portauxbasque_nfld["Jul"].replace(-9999.9, df_portauxbasque_nfld["Jul"].median())
df_portauxbasque_nfld["Aug"] = df_portauxbasque_nfld["Aug"].replace(-9999.9, df_portauxbasque_nfld["Aug"].median())
df_portauxbasque_nfld["Sep"] = df_portauxbasque_nfld["Sep"].replace(-9999.9, df_portauxbasque_nfld["Sep"].median())
df_portauxbasque_nfld["Oct"] = df_portauxbasque_nfld["Oct"].replace(-9999.9, df_portauxbasque_nfld["Oct"].median())
df_portauxbasque_nfld["Nov"] = df_portauxbasque_nfld["Nov"].replace(-9999.9, df_portauxbasque_nfld["Nov"].median())
df_portauxbasque_nfld["Dec"] = df_portauxbasque_nfld["Dec"].replace(-9999.9, df_portauxbasque_nfld["Dec"].median())
df_portauxbasque_nfld["Annual"] = df_portauxbasque_nfld["Annual"].replace(-9999.9, df_portauxbasque_nfld["Annual"].median())
df_portauxbasque_nfld["Winter"] = df_portauxbasque_nfld["Winter"].replace(-9999.9, df_portauxbasque_nfld["Winter"].median())
df_portauxbasque_nfld["Spring"] = df_portauxbasque_nfld["Spring"].replace(-9999.9, df_portauxbasque_nfld["Spring"].median())
df_portauxbasque_nfld["Summer"] = df_portauxbasque_nfld["Summer"].replace(-9999.9, df_portauxbasque_nfld["Summer"].median())
df_portauxbasque_nfld["Autumn"] = df_portauxbasque_nfld["Autumn"].replace(-9999.9, df_portauxbasque_nfld["Autumn"].median())

#Port Hardy

porthardy_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/porthardy_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_porthardy_bc = pd.DataFrame(porthardy_bc)


df_porthardy_bc.dropna(axis = 1, how='all', inplace = True)
df_porthardy_bc.dropna(axis = 0, how='all', inplace = True)

df_porthardy_bc["Jan"] = df_porthardy_bc["Jan"].replace(-9999.9, df_porthardy_bc["Jan"].median())
df_porthardy_bc["Feb"] = df_porthardy_bc["Feb"].replace(-9999.9, df_porthardy_bc["Feb"].median())
df_porthardy_bc["Mar"] = df_porthardy_bc["Mar"].replace(-9999.9, df_porthardy_bc["Mar"].median())
df_porthardy_bc["Apr"] = df_porthardy_bc["Apr"].replace(-9999.9, df_porthardy_bc["Apr"].median())
df_porthardy_bc["May"] = df_porthardy_bc["May"].replace(-9999.9, df_porthardy_bc["May"].median())
df_porthardy_bc["Jun"] = df_porthardy_bc["Jun"].replace(-9999.9, df_porthardy_bc["Jun"].median())
df_porthardy_bc["Jul"] = df_porthardy_bc["Jul"].replace(-9999.9, df_porthardy_bc["Jul"].median())
df_porthardy_bc["Aug"] = df_porthardy_bc["Aug"].replace(-9999.9, df_porthardy_bc["Aug"].median())
df_porthardy_bc["Sep"] = df_porthardy_bc["Sep"].replace(-9999.9, df_porthardy_bc["Sep"].median())
df_porthardy_bc["Oct"] = df_porthardy_bc["Oct"].replace(-9999.9, df_porthardy_bc["Oct"].median())
df_porthardy_bc["Nov"] = df_porthardy_bc["Nov"].replace(-9999.9, df_porthardy_bc["Nov"].median())
df_porthardy_bc["Dec"] = df_porthardy_bc["Dec"].replace(-9999.9, df_porthardy_bc["Dec"].median())
df_porthardy_bc["Annual"] = df_porthardy_bc["Annual"].replace(-9999.9, df_porthardy_bc["Annual"].median())
df_porthardy_bc["Winter"] = df_porthardy_bc["Winter"].replace(-9999.9, df_porthardy_bc["Winter"].median())
df_porthardy_bc["Spring"] = df_porthardy_bc["Spring"].replace(-9999.9, df_porthardy_bc["Spring"].median())
df_porthardy_bc["Summer"] = df_porthardy_bc["Summer"].replace(-9999.9, df_porthardy_bc["Summer"].median())
df_porthardy_bc["Autumn"] = df_porthardy_bc["Autumn"].replace(-9999.9, df_porthardy_bc["Autumn"].median())


#Prince Albert Saskatchewan 

princealbert_sask = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/princealbert_sask.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_princealbert_sask = pd.DataFrame(princealbert_sask)

df_princealbert_sask["Oct"] = df_princealbert_sask["Oct"].replace(-9999.9, df_princealbert_sask["Oct"].median())


#Prince George British Columbia 

princegeorge_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/princegeorge_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_princegeorge_bc = pd.DataFrame(princegeorge_bc)

df_princegeorge_bc["Feb"] = df_princegeorge_bc["Feb"].replace(-9999.9, df_princegeorge_bc["Feb"].median())


#Prince Rupert British Columbia 

princerupert_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/princerupert_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_princerupert_bc = pd.DataFrame(princerupert_bc)

df_princerupert_bc["Jan"] = df_princerupert_bc["Jan"].replace(-9999.9, df_princerupert_bc["Jan"].median())
df_princerupert_bc["Feb"] = df_princerupert_bc["Feb"].replace(-9999.9, df_princerupert_bc["Feb"].median())
df_princerupert_bc["Mar"] = df_princerupert_bc["Mar"].replace(-9999.9, df_princerupert_bc["Mar"].median())
df_princerupert_bc["Apr"] = df_princerupert_bc["Apr"].replace(-9999.9, df_princerupert_bc["Apr"].median())
df_princerupert_bc["May"] = df_princerupert_bc["May"].replace(-9999.9, df_princerupert_bc["May"].median())
df_princerupert_bc["Jun"] = df_princerupert_bc["Jun"].replace(-9999.9, df_princerupert_bc["Jun"].median())
df_princerupert_bc["Jul"] = df_princerupert_bc["Jul"].replace(-9999.9, df_princerupert_bc["Jul"].median())
df_princerupert_bc["Aug"] = df_princerupert_bc["Aug"].replace(-9999.9, df_princerupert_bc["Aug"].median())
df_princerupert_bc["Sep"] = df_princerupert_bc["Sep"].replace(-9999.9, df_princerupert_bc["Sep"].median())
df_princerupert_bc["Oct"] = df_princerupert_bc["Oct"].replace(-9999.9, df_princerupert_bc["Oct"].median())
df_princerupert_bc["Nov"] = df_princerupert_bc["Nov"].replace(-9999.9, df_princerupert_bc["Nov"].median())
df_princerupert_bc["Dec"] = df_princerupert_bc["Dec"].replace(-9999.9, df_princerupert_bc["Dec"].median())
df_princerupert_bc["Annual"] = df_princerupert_bc["Annual"].replace(-9999.9, df_princerupert_bc["Annual"].median())
df_princerupert_bc["Winter"] = df_princerupert_bc["Winter"].replace(-9999.9, df_princerupert_bc["Winter"].median())
df_princerupert_bc["Spring"] = df_princerupert_bc["Spring"].replace(-9999.9, df_princerupert_bc["Spring"].median())
df_princerupert_bc["Summer"] = df_princerupert_bc["Summer"].replace(-9999.9, df_princerupert_bc["Summer"].median())
df_princerupert_bc["Autumn"] = df_princerupert_bc["Autumn"].replace(-9999.9, df_princerupert_bc["Autumn"].median())


#Princeton British Columbia 

princeton_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/princeton_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_princeton_bc = pd.DataFrame(princeton_bc)

df_princeton_bc["Dec"] = df_princeton_bc["Dec"].replace(-9999.9, df_princeton_bc["Dec"].median())

#Quesnel British Columbia 

quesnel_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/quesnel_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_quesnel_bc = pd.DataFrame(quesnel_bc)

df_quesnel_bc["Jan"] = df_quesnel_bc["Jan"].replace(-9999.9, df_quesnel_bc["Jan"].median())
df_quesnel_bc["Feb"] = df_quesnel_bc["Feb"].replace(-9999.9, df_quesnel_bc["Feb"].median())
df_quesnel_bc["Mar"] = df_quesnel_bc["Mar"].replace(-9999.9, df_quesnel_bc["Mar"].median())
df_quesnel_bc["Apr"] = df_quesnel_bc["Apr"].replace(-9999.9, df_quesnel_bc["Apr"].median())
df_quesnel_bc["May"] = df_quesnel_bc["May"].replace(-9999.9, df_quesnel_bc["May"].median())
df_quesnel_bc["Jun"] = df_quesnel_bc["Jun"].replace(-9999.9, df_quesnel_bc["Jun"].median())
df_quesnel_bc["Jul"] = df_quesnel_bc["Jul"].replace(-9999.9, df_quesnel_bc["Jul"].median())
df_quesnel_bc["Aug"] = df_quesnel_bc["Aug"].replace(-9999.9, df_quesnel_bc["Aug"].median())
df_quesnel_bc["Sep"] = df_quesnel_bc["Sep"].replace(-9999.9, df_quesnel_bc["Sep"].median())
df_quesnel_bc["Oct"] = df_quesnel_bc["Oct"].replace(-9999.9, df_quesnel_bc["Oct"].median())
df_quesnel_bc["Nov"] = df_quesnel_bc["Nov"].replace(-9999.9, df_quesnel_bc["Nov"].median())
df_quesnel_bc["Dec"] = df_quesnel_bc["Dec"].replace(-9999.9, df_quesnel_bc["Dec"].median())
df_quesnel_bc["Annual"] = df_quesnel_bc["Annual"].replace(-9999.9, df_quesnel_bc["Annual"].median())
df_quesnel_bc["Winter"] = df_quesnel_bc["Winter"].replace(-9999.9, df_quesnel_bc["Winter"].median())
df_quesnel_bc["Spring"] = df_quesnel_bc["Spring"].replace(-9999.9, df_quesnel_bc["Spring"].median())
df_quesnel_bc["Summer"] = df_quesnel_bc["Summer"].replace(-9999.9, df_quesnel_bc["Summer"].median())
df_quesnel_bc["Autumn"] = df_quesnel_bc["Autumn"].replace(-9999.9, df_quesnel_bc["Autumn"].median())


#Reddeer Alberta 

reddeer_alber = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/reddeer_alber.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_reddeer_alber = pd.DataFrame(reddeer_alber)

df_reddeer_alber["May"] = df_reddeer_alber["May"].replace(-9999.9, df_reddeer_alber["May"].median())
df_reddeer_alber["Jun"] = df_reddeer_alber["Jun"].replace(-9999.9, df_reddeer_alber["Jun"].median())
df_reddeer_alber["Jul"] = df_reddeer_alber["Jul"].replace(-9999.9, df_reddeer_alber["Jul"].median())
df_reddeer_alber["Aug"] = df_reddeer_alber["Aug"].replace(-9999.9, df_reddeer_alber["Aug"].median())
df_reddeer_alber["Sep"] = df_reddeer_alber["Sep"].replace(-9999.9, df_reddeer_alber["Sep"].median())
df_reddeer_alber["Oct"] = df_reddeer_alber["Oct"].replace(-9999.9, df_reddeer_alber["Oct"].median())
df_reddeer_alber["Nov"] = df_reddeer_alber["Nov"].replace(-9999.9, df_reddeer_alber["Nov"].median())
df_reddeer_alber["Dec"] = df_reddeer_alber["Dec"].replace(-9999.9, df_reddeer_alber["Dec"].median())
df_reddeer_alber["Summer"] = df_reddeer_alber["Summer"].replace(-9999.9, df_reddeer_alber["Summer"].median())
df_reddeer_alber["Autumn"] = df_reddeer_alber["Autumn"].replace(-9999.9, df_reddeer_alber["Autumn"].median())
df_reddeer_alber["Annual"] = df_reddeer_alber["Annual"].replace(-9999.9, df_reddeer_alber["Annual"].median())

#Redlake Ontario

redlake_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/redlake_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_redlake_ont = pd.DataFrame(redlake_ont)

df_redlake_ont["Jan"] = df_redlake_ont["Jan"].replace(-9999.9, df_redlake_ont["Jan"].median())
df_redlake_ont["Feb"] = df_redlake_ont["Feb"].replace(-9999.9, df_redlake_ont["Feb"].median())
df_redlake_ont["Mar"] = df_redlake_ont["Mar"].replace(-9999.9, df_redlake_ont["Mar"].median())
df_redlake_ont["Apr"] = df_redlake_ont["Apr"].replace(-9999.9, df_redlake_ont["Apr"].median())
df_redlake_ont["May"] = df_redlake_ont["May"].replace(-9999.9, df_redlake_ont["May"].median())
df_redlake_ont["Jun"] = df_redlake_ont["Jun"].replace(-9999.9, df_redlake_ont["Jun"].median())
df_redlake_ont["Jul"] = df_redlake_ont["Jul"].replace(-9999.9, df_redlake_ont["Jul"].median())
df_redlake_ont["Aug"] = df_redlake_ont["Aug"].replace(-9999.9, df_redlake_ont["Aug"].median())
df_redlake_ont["Sep"] = df_redlake_ont["Sep"].replace(-9999.9, df_redlake_ont["Sep"].median())
df_redlake_ont["Oct"] = df_redlake_ont["Oct"].replace(-9999.9, df_redlake_ont["Oct"].median())
df_redlake_ont["Nov"] = df_redlake_ont["Nov"].replace(-9999.9, df_redlake_ont["Nov"].median())
df_redlake_ont["Dec"] = df_redlake_ont["Dec"].replace(-9999.9, df_redlake_ont["Dec"].median())
df_redlake_ont["Annual"] = df_redlake_ont["Annual"].replace(-9999.9, df_redlake_ont["Annual"].median())
df_redlake_ont["Winter"] = df_redlake_ont["Winter"].replace(-9999.9, df_redlake_ont["Winter"].median())
df_redlake_ont["Spring"] = df_redlake_ont["Spring"].replace(-9999.9, df_redlake_ont["Spring"].median())
df_redlake_ont["Summer"] = df_redlake_ont["Summer"].replace(-9999.9, df_redlake_ont["Summer"].median())
df_redlake_ont["Autumn"] = df_redlake_ont["Autumn"].replace(-9999.9, df_redlake_ont["Autumn"].median())

#Regina Saskatchewan 

regina_sask = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/regina_sask.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_regina_sask = pd.DataFrame(regina_sask)

#Resolutecars Nunuvut

resolutecars_nu = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/resolutecars_nu.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_resolutecars_nu = pd.DataFrame(resolutecars_nu)

df_resolutecars_nu["Nov"] = df_resolutecars_nu["Nov"].replace(-9999.9, df_resolutecars_nu["Nov"].median())
df_resolutecars_nu["Dec"] = df_resolutecars_nu["Dec"].replace(-9999.9, df_resolutecars_nu["Dec"].median())

#Rouyn Quebec 

rouyn_queb = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/rouyn_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_rouyn_queb = pd.DataFrame(rouyn_queb)

df_rouyn_queb["Jan"] = df_rouyn_queb["Jan"].replace(-9999.9, df_rouyn_queb["Jan"].median())
df_rouyn_queb["Feb"] = df_rouyn_queb["Feb"].replace(-9999.9, df_rouyn_queb["Feb"].median())
df_rouyn_queb["Mar"] = df_rouyn_queb["Mar"].replace(-9999.9, df_rouyn_queb["Mar"].median())
df_rouyn_queb["Apr"] = df_rouyn_queb["Apr"].replace(-9999.9, df_rouyn_queb["Apr"].median())
df_rouyn_queb["May"] = df_rouyn_queb["May"].replace(-9999.9, df_rouyn_queb["May"].median())
df_rouyn_queb["Jun"] = df_rouyn_queb["Jun"].replace(-9999.9, df_rouyn_queb["Jun"].median())
df_rouyn_queb["Jul"] = df_rouyn_queb["Jul"].replace(-9999.9, df_rouyn_queb["Jul"].median())
df_rouyn_queb["Aug"] = df_rouyn_queb["Aug"].replace(-9999.9, df_rouyn_queb["Aug"].median())
df_rouyn_queb["Sep"] = df_rouyn_queb["Sep"].replace(-9999.9, df_rouyn_queb["Sep"].median())
df_rouyn_queb["Oct"] = df_rouyn_queb["Oct"].replace(-9999.9, df_rouyn_queb["Oct"].median())
df_rouyn_queb["Nov"] = df_rouyn_queb["Nov"].replace(-9999.9, df_rouyn_queb["Nov"].median())
df_rouyn_queb["Dec"] = df_rouyn_queb["Dec"].replace(-9999.9, df_rouyn_queb["Dec"].median())
df_rouyn_queb["Annual"] = df_rouyn_queb["Annual"].replace(-9999.9, df_rouyn_queb["Annual"].median())
df_rouyn_queb["Winter"] = df_rouyn_queb["Winter"].replace(-9999.9, df_rouyn_queb["Winter"].median())
df_rouyn_queb["Spring"] = df_rouyn_queb["Spring"].replace(-9999.9, df_rouyn_queb["Spring"].median())
df_rouyn_queb["Summer"] = df_rouyn_queb["Summer"].replace(-9999.9, df_rouyn_queb["Summer"].median())
df_rouyn_queb["Autumn"] = df_rouyn_queb["Autumn"].replace(-9999.9, df_rouyn_queb["Autumn"].median())

#Roverbal Quebec

roverbal_queb = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/roverbal_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_roverbal_queb = pd.DataFrame(roverbal_queb)

df_roverbal_queb["Jan"] = df_roverbal_queb["Jan"].replace(-9999.9, df_roverbal_queb["Jan"].median())
df_roverbal_queb["Feb"] = df_roverbal_queb["Feb"].replace(-9999.9, df_roverbal_queb["Feb"].median())
df_roverbal_queb["Mar"] = df_roverbal_queb["Mar"].replace(-9999.9, df_roverbal_queb["Mar"].median())
df_roverbal_queb["Apr"] = df_roverbal_queb["Apr"].replace(-9999.9, df_roverbal_queb["Apr"].median())
df_roverbal_queb["May"] = df_roverbal_queb["May"].replace(-9999.9, df_roverbal_queb["May"].median())
df_roverbal_queb["Jun"] = df_roverbal_queb["Jun"].replace(-9999.9, df_roverbal_queb["Jun"].median())
df_roverbal_queb["Jul"] = df_roverbal_queb["Jul"].replace(-9999.9, df_roverbal_queb["Jul"].median())
df_roverbal_queb["Aug"] = df_roverbal_queb["Aug"].replace(-9999.9, df_roverbal_queb["Aug"].median())
df_roverbal_queb["Sep"] = df_roverbal_queb["Sep"].replace(-9999.9, df_roverbal_queb["Sep"].median())
df_roverbal_queb["Oct"] = df_roverbal_queb["Oct"].replace(-9999.9, df_roverbal_queb["Oct"].median())
df_roverbal_queb["Nov"] = df_roverbal_queb["Nov"].replace(-9999.9, df_roverbal_queb["Nov"].median())
df_roverbal_queb["Dec"] = df_roverbal_queb["Dec"].replace(-9999.9, df_roverbal_queb["Dec"].median())
df_roverbal_queb["Annual"] = df_roverbal_queb["Annual"].replace(-9999.9, df_roverbal_queb["Annual"].median())
df_roverbal_queb["Winter"] = df_roverbal_queb["Winter"].replace(-9999.9, df_roverbal_queb["Winter"].median())
df_roverbal_queb["Spring"] = df_roverbal_queb["Spring"].replace(-9999.9, df_roverbal_queb["Spring"].median())
df_roverbal_queb["Summer"] = df_roverbal_queb["Summer"].replace(-9999.9, df_roverbal_queb["Summer"].median())
df_roverbal_queb["Autumn"] = df_roverbal_queb["Autumn"].replace(-9999.9, df_roverbal_queb["Autumn"].median())

#Sableisland Nova Scotia

sableisland_ns = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/sableisland_ns.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_sableisland_ns = pd.DataFrame(sableisland_ns)

df_sableisland_ns.dropna(axis = 1, how='all', inplace = True)
df_sableisland_ns.dropna(axis = 0, how='all', inplace = True)

df_sableisland_ns["Jan"] = df_sableisland_ns["Jan"].replace(-9999.9, df_sableisland_ns["Jan"].median())
df_sableisland_ns["Feb"] = df_sableisland_ns["Feb"].replace(-9999.9, df_sableisland_ns["Feb"].median())
df_sableisland_ns["Mar"] = df_sableisland_ns["Mar"].replace(-9999.9, df_sableisland_ns["Mar"].median())
df_sableisland_ns["Apr"] = df_sableisland_ns["Apr"].replace(-9999.9, df_sableisland_ns["Apr"].median())
df_sableisland_ns["May"] = df_sableisland_ns["May"].replace(-9999.9, df_sableisland_ns["May"].median())
df_sableisland_ns["Jun"] = df_sableisland_ns["Jun"].replace(-9999.9, df_sableisland_ns["Jun"].median())
df_sableisland_ns["Jul"] = df_sableisland_ns["Jul"].replace(-9999.9, df_sableisland_ns["Jul"].median())
df_sableisland_ns["Aug"] = df_sableisland_ns["Aug"].replace(-9999.9, df_sableisland_ns["Aug"].median())
df_sableisland_ns["Sep"] = df_sableisland_ns["Sep"].replace(-9999.9, df_sableisland_ns["Sep"].median())
df_sableisland_ns["Oct"] = df_sableisland_ns["Oct"].replace(-9999.9, df_sableisland_ns["Oct"].median())
df_sableisland_ns["Nov"] = df_sableisland_ns["Nov"].replace(-9999.9, df_sableisland_ns["Nov"].median())
df_sableisland_ns["Dec"] = df_sableisland_ns["Dec"].replace(-9999.9, df_sableisland_ns["Dec"].median())
df_sableisland_ns["Annual"] = df_sableisland_ns["Annual"].replace(-9999.9, df_sableisland_ns["Annual"].median())
df_sableisland_ns["Winter"] = df_sableisland_ns["Winter"].replace(-9999.9, df_sableisland_ns["Winter"].median())
df_sableisland_ns["Spring"] = df_sableisland_ns["Spring"].replace(-9999.9, df_sableisland_ns["Spring"].median())
df_sableisland_ns["Summer"] = df_sableisland_ns["Summer"].replace(-9999.9, df_sableisland_ns["Summer"].median())
df_sableisland_ns["Autumn"] = df_sableisland_ns["Autumn"].replace(-9999.9, df_sableisland_ns["Autumn"].median())

#Sachsharbour North West Territories 

sachsharbour_nwt = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/sachsharbour_nwt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig' )
df_sachsharbour_nwt = pd.DataFrame(sachsharbour_nwt)

df_sachsharbour_nwt["Jan"] = df_sachsharbour_nwt["Jan"].replace(-9999.9, df_sachsharbour_nwt["Jan"].median())
df_sachsharbour_nwt["Feb"] = df_sachsharbour_nwt["Feb"].replace(-9999.9, df_sachsharbour_nwt["Feb"].median())
df_sachsharbour_nwt["Mar"] = df_sachsharbour_nwt["Mar"].replace(-9999.9, df_sachsharbour_nwt["Mar"].median())
df_sachsharbour_nwt["Apr"] = df_sachsharbour_nwt["Apr"].replace(-9999.9, df_sachsharbour_nwt["Apr"].median())
df_sachsharbour_nwt["May"] = df_sachsharbour_nwt["May"].replace(-9999.9, df_sachsharbour_nwt["May"].median())
df_sachsharbour_nwt["Jun"] = df_sachsharbour_nwt["Jun"].replace(-9999.9, df_sachsharbour_nwt["Jun"].median())
df_sachsharbour_nwt["Jul"] = df_sachsharbour_nwt["Jul"].replace(-9999.9, df_sachsharbour_nwt["Jul"].median())
df_sachsharbour_nwt["Aug"] = df_sachsharbour_nwt["Aug"].replace(-9999.9, df_sachsharbour_nwt["Aug"].median())
df_sachsharbour_nwt["Sep"] = df_sachsharbour_nwt["Sep"].replace(-9999.9, df_sachsharbour_nwt["Sep"].median())
df_sachsharbour_nwt["Oct"] = df_sachsharbour_nwt["Oct"].replace(-9999.9, df_sachsharbour_nwt["Oct"].median())
df_sachsharbour_nwt["Nov"] = df_sachsharbour_nwt["Nov"].replace(-9999.9, df_sachsharbour_nwt["Nov"].median())
df_sachsharbour_nwt["Dec"] = df_sachsharbour_nwt["Dec"].replace(-9999.9, df_sachsharbour_nwt["Dec"].median())
df_sachsharbour_nwt["Annual"] = df_sachsharbour_nwt["Annual"].replace(-9999.9, df_sachsharbour_nwt["Annual"].median())
df_sachsharbour_nwt["Winter"] = df_sachsharbour_nwt["Winter"].replace(-9999.9, df_sachsharbour_nwt["Winter"].median())
df_sachsharbour_nwt["Spring"] = df_sachsharbour_nwt["Spring"].replace(-9999.9, df_sachsharbour_nwt["Spring"].median())
df_sachsharbour_nwt["Summer"] = df_sachsharbour_nwt["Summer"].replace(-9999.9, df_sachsharbour_nwt["Summer"].median())
df_sachsharbour_nwt["Autumn"] = df_sachsharbour_nwt["Autumn"].replace(-9999.9, df_sachsharbour_nwt["Autumn"].median())


#Saint John New Brunswick 

saintjohn_nb = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/saintjohn_nb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_saintjohn_nb = pd.DataFrame(saintjohn_nb)

#Sandspit British Columbia 

sandspit_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/sandspit_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_sandspit_bc  = pd.DataFrame(sandspit_bc)

df_sandspit_bc["Jun"] = df_sandspit_bc["Jun"].replace(-9999.9, df_sandspit_bc["Jun"].median())
df_sandspit_bc["Sep"] = df_sandspit_bc["Sep"].replace(-9999.9, df_sandspit_bc["Sep"].median())
df_sandspit_bc["Oct"] = df_sandspit_bc["Oct"].replace(-9999.9, df_sandspit_bc["Oct"].median())
df_sandspit_bc["Autumn"] = df_sandspit_bc["Autumn"].replace(-9999.9, df_sandspit_bc["Autumn"].median())


#Saskatoon Diefenbaker Saskatchewan 

saskatoondiefenbaker_sask = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/saskatoondiefenbaker_sask.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_saskatoondiefenbaker_sask  = pd.DataFrame(saskatoondiefenbaker_sask)


#Saulstemarie Ontario

saulstemarie_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/saulstemarie_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_saulstemarie_ont  = pd.DataFrame(saulstemarie_ont)

df_saulstemarie_ont["Jan"] = df_saulstemarie_ont["Jan"].replace(-9999.9, df_saulstemarie_ont["Jan"].median())
df_saulstemarie_ont["Feb"] = df_saulstemarie_ont["Feb"].replace(-9999.9, df_saulstemarie_ont["Feb"].median())
df_saulstemarie_ont["Mar"] = df_saulstemarie_ont["Mar"].replace(-9999.9, df_saulstemarie_ont["Mar"].median())
df_saulstemarie_ont["Apr"] = df_saulstemarie_ont["Apr"].replace(-9999.9, df_saulstemarie_ont["Apr"].median())
df_saulstemarie_ont["May"] = df_saulstemarie_ont["May"].replace(-9999.9, df_saulstemarie_ont["May"].median())
df_saulstemarie_ont["Jun"] = df_saulstemarie_ont["Jun"].replace(-9999.9, df_saulstemarie_ont["Jun"].median())
df_saulstemarie_ont["Jul"] = df_saulstemarie_ont["Jul"].replace(-9999.9, df_saulstemarie_ont["Jul"].median())
df_saulstemarie_ont["Aug"] = df_saulstemarie_ont["Aug"].replace(-9999.9, df_saulstemarie_ont["Aug"].median())
df_saulstemarie_ont["Sep"] = df_saulstemarie_ont["Sep"].replace(-9999.9, df_saulstemarie_ont["Sep"].median())
df_saulstemarie_ont["Oct"] = df_saulstemarie_ont["Oct"].replace(-9999.9, df_saulstemarie_ont["Oct"].median())
df_saulstemarie_ont["Nov"] = df_saulstemarie_ont["Nov"].replace(-9999.9, df_saulstemarie_ont["Nov"].median())
df_saulstemarie_ont["Dec"] = df_saulstemarie_ont["Dec"].replace(-9999.9, df_saulstemarie_ont["Dec"].median())
df_saulstemarie_ont["Annual"] = df_saulstemarie_ont["Annual"].replace(-9999.9, df_saulstemarie_ont["Annual"].median())
df_saulstemarie_ont["Winter"] = df_saulstemarie_ont["Winter"].replace(-9999.9, df_saulstemarie_ont["Winter"].median())
df_saulstemarie_ont["Spring"] = df_saulstemarie_ont["Spring"].replace(-9999.9, df_saulstemarie_ont["Spring"].median())
df_saulstemarie_ont["Summer"] = df_saulstemarie_ont["Summer"].replace(-9999.9, df_saulstemarie_ont["Summer"].median())
df_saulstemarie_ont["Autumn"] = df_saulstemarie_ont["Autumn"].replace(-9999.9, df_saulstemarie_ont["Autumn"].median())


#Schefferville Quebec 

schefferville_queb = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/schefferville_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_schefferville_queb = pd.DataFrame(schefferville_queb)

df_schefferville_queb["Nov"] = df_schefferville_queb["Nov"].replace(-9999.9, df_schefferville_queb["Nov"].median())
df_schefferville_queb["Sep"] = df_schefferville_queb["Sep"].replace(-9999.9, df_schefferville_queb["Sep"].median())
df_schefferville_queb["Oct"] = df_schefferville_queb["Oct"].replace(-9999.9, df_schefferville_queb["Oct"].median())
df_schefferville_queb["Autumn"] = df_schefferville_queb["Autumn"].replace(-9999.9, df_schefferville_queb["Autumn"].median())


#Septiles Quebec 

septiles_queb = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/septiles_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_septiles_queb = pd.DataFrame(septiles_queb)

df_septiles_queb["Apr"] = df_septiles_queb["Apr"].replace(-9999.9, df_septiles_queb["Apr"].median())
df_septiles_queb["May"] = df_septiles_queb["May"].replace(-9999.9, df_septiles_queb["May"].median())
df_septiles_queb["Jun"] = df_septiles_queb["Jun"].replace(-9999.9, df_septiles_queb["Jun"].median())
df_septiles_queb["Jul"] = df_septiles_queb["Jul"].replace(-9999.9, df_septiles_queb["Jul"].median())
df_septiles_queb["Aug"] = df_septiles_queb["Aug"].replace(-9999.9, df_septiles_queb["Aug"].median())
df_septiles_queb["Sep"] = df_septiles_queb["Sep"].replace(-9999.9, df_septiles_queb["Sep"].median())
df_septiles_queb["Oct"] = df_septiles_queb["Oct"].replace(-9999.9, df_septiles_queb["Oct"].median())
df_septiles_queb["Nov"] = df_septiles_queb["Nov"].replace(-9999.9, df_septiles_queb["Nov"].median())
df_septiles_queb["Dec"] = df_septiles_queb["Dec"].replace(-9999.9, df_septiles_queb["Dec"].median())
df_septiles_queb["Annual"] = df_septiles_queb["Annual"].replace(-9999.9, df_septiles_queb["Annual"].median())
df_septiles_queb["Winter"] = df_septiles_queb["Winter"].replace(-9999.9, df_septiles_queb["Winter"].median())
df_septiles_queb["Spring"] = df_septiles_queb["Spring"].replace(-9999.9, df_septiles_queb["Spring"].median())
df_septiles_queb["Summer"] = df_septiles_queb["Summer"].replace(-9999.9, df_septiles_queb["Summer"].median())
df_septiles_queb["Autumn"] = df_septiles_queb["Autumn"].replace(-9999.9, df_septiles_queb["Autumn"].median())


#Shearwater Nova Scotia 

shearwater_ns = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/shearwater_ns.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_shearwater_ns = pd.DataFrame(shearwater_ns)

df_shearwater_ns["Jan"] = df_shearwater_ns["Jan"].replace(-9999.9, df_shearwater_ns["Jan"].median())
df_shearwater_ns["Feb"] = df_shearwater_ns["Feb"].replace(-9999.9, df_shearwater_ns["Feb"].median())
df_shearwater_ns["Mar"] = df_shearwater_ns["Mar"].replace(-9999.9, df_shearwater_ns["Mar"].median())
df_shearwater_ns["Apr"] = df_shearwater_ns["Apr"].replace(-9999.9, df_shearwater_ns["Apr"].median())
df_shearwater_ns["May"] = df_shearwater_ns["May"].replace(-9999.9, df_shearwater_ns["May"].median())
df_shearwater_ns["Jun"] = df_shearwater_ns["Jun"].replace(-9999.9, df_shearwater_ns["Jun"].median())
df_shearwater_ns["Jul"] = df_shearwater_ns["Jul"].replace(-9999.9, df_shearwater_ns["Jul"].median())
df_shearwater_ns["Aug"] = df_shearwater_ns["Aug"].replace(-9999.9, df_shearwater_ns["Aug"].median())
df_shearwater_ns["Sep"] = df_shearwater_ns["Sep"].replace(-9999.9, df_shearwater_ns["Sep"].median())
df_shearwater_ns["Oct"] = df_shearwater_ns["Oct"].replace(-9999.9, df_shearwater_ns["Oct"].median())
df_shearwater_ns["Nov"] = df_shearwater_ns["Nov"].replace(-9999.9, df_shearwater_ns["Nov"].median())
df_shearwater_ns["Dec"] = df_shearwater_ns["Dec"].replace(-9999.9, df_shearwater_ns["Dec"].median())
df_shearwater_ns["Annual"] = df_shearwater_ns["Annual"].replace(-9999.9, df_shearwater_ns["Annual"].median())
df_shearwater_ns["Winter"] = df_shearwater_ns["Winter"].replace(-9999.9, df_shearwater_ns["Winter"].median())
df_shearwater_ns["Spring"] = df_shearwater_ns["Spring"].replace(-9999.9, df_shearwater_ns["Spring"].median())
df_shearwater_ns["Summer"] = df_shearwater_ns["Summer"].replace(-9999.9, df_shearwater_ns["Summer"].median())
df_shearwater_ns["Autumn"] = df_shearwater_ns["Autumn"].replace(-9999.9, df_shearwater_ns["Autumn"].median())


#Sherbrooke Quebec 

sherbrooke_queb = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/sherbrooke_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_sherbrooke_queb = pd.DataFrame(sherbrooke_queb)


df_sherbrooke_queb["Jan"] = df_sherbrooke_queb["Jan"].replace(-9999.9, df_sherbrooke_queb["Jan"].median())
df_sherbrooke_queb["Feb"] = df_sherbrooke_queb["Feb"].replace(-9999.9, df_sherbrooke_queb["Feb"].median())
df_sherbrooke_queb["Mar"] = df_sherbrooke_queb["Mar"].replace(-9999.9, df_sherbrooke_queb["Mar"].median())
df_sherbrooke_queb["Apr"] = df_sherbrooke_queb["Apr"].replace(-9999.9, df_sherbrooke_queb["Apr"].median())
df_sherbrooke_queb["May"] = df_sherbrooke_queb["May"].replace(-9999.9, df_sherbrooke_queb["May"].median())
df_sherbrooke_queb["Jun"] = df_sherbrooke_queb["Jun"].replace(-9999.9, df_sherbrooke_queb["Jun"].median())
df_sherbrooke_queb["Jul"] = df_sherbrooke_queb["Jul"].replace(-9999.9, df_sherbrooke_queb["Jul"].median())
df_sherbrooke_queb["Aug"] = df_sherbrooke_queb["Aug"].replace(-9999.9, df_sherbrooke_queb["Aug"].median())
df_sherbrooke_queb["Sep"] = df_sherbrooke_queb["Sep"].replace(-9999.9, df_sherbrooke_queb["Sep"].median())
df_sherbrooke_queb["Oct"] = df_sherbrooke_queb["Oct"].replace(-9999.9, df_sherbrooke_queb["Oct"].median())
df_sherbrooke_queb["Nov"] = df_sherbrooke_queb["Nov"].replace(-9999.9, df_sherbrooke_queb["Nov"].median())
df_sherbrooke_queb["Dec"] = df_sherbrooke_queb["Dec"].replace(-9999.9, df_sherbrooke_queb["Dec"].median())
df_sherbrooke_queb["Annual"] = df_sherbrooke_queb["Annual"].replace(-9999.9, df_sherbrooke_queb["Annual"].median())
df_sherbrooke_queb["Winter"] = df_sherbrooke_queb["Winter"].replace(-9999.9, df_sherbrooke_queb["Winter"].median())
df_sherbrooke_queb["Spring"] = df_sherbrooke_queb["Spring"].replace(-9999.9, df_sherbrooke_queb["Spring"].median())
df_sherbrooke_queb["Summer"] = df_sherbrooke_queb["Summer"].replace(-9999.9, df_sherbrooke_queb["Summer"].median())
df_sherbrooke_queb["Autumn"] = df_sherbrooke_queb["Autumn"].replace(-9999.9, df_sherbrooke_queb["Autumn"].median())

#Siouxlookout Ontario 

siouxlookout_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/siouxlookout_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_siouxlookout_ont = pd.DataFrame(siouxlookout_ont)

df_siouxlookout_ont["Oct"] = df_siouxlookout_ont["Oct"].replace(-9999.9, df_siouxlookout_ont["Oct"].median())
df_siouxlookout_ont["Nov"] = df_siouxlookout_ont["Nov"].replace(-9999.9, df_siouxlookout_ont["Nov"].median())
df_siouxlookout_ont["Autumn"] = df_siouxlookout_ont["Autumn"].replace(-9999.9, df_siouxlookout_ont["Autumn"].median())

#Smithers British Columbia 

smithers_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/smithers_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_smithers_bc = pd.DataFrame(smithers_bc)

#Stephenville Newfoundland 

stephenville_nfld = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/stephenville_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_stephenville_nfld = pd.DataFrame(stephenville_nfld)

df_stephenville_nfld["Jan"] = df_stephenville_nfld["Jan"].replace(-9999.9, df_stephenville_nfld["Jan"].median())
df_stephenville_nfld["Feb"] = df_stephenville_nfld["Feb"].replace(-9999.9, df_stephenville_nfld["Feb"].median())
df_stephenville_nfld["Mar"] = df_stephenville_nfld["Mar"].replace(-9999.9, df_stephenville_nfld["Mar"].median())
df_stephenville_nfld["Apr"] = df_stephenville_nfld["Apr"].replace(-9999.9, df_stephenville_nfld["Apr"].median())
df_stephenville_nfld["May"] = df_stephenville_nfld["May"].replace(-9999.9, df_stephenville_nfld["May"].median())
df_stephenville_nfld["Jun"] = df_stephenville_nfld["Jun"].replace(-9999.9, df_stephenville_nfld["Jun"].median())
df_stephenville_nfld["Jul"] = df_stephenville_nfld["Jul"].replace(-9999.9, df_stephenville_nfld["Jul"].median())
df_stephenville_nfld["Aug"] = df_stephenville_nfld["Aug"].replace(-9999.9, df_stephenville_nfld["Aug"].median())
df_stephenville_nfld["Sep"] = df_stephenville_nfld["Sep"].replace(-9999.9, df_stephenville_nfld["Sep"].median())
df_stephenville_nfld["Oct"] = df_stephenville_nfld["Oct"].replace(-9999.9, df_stephenville_nfld["Oct"].median())
df_stephenville_nfld["Nov"] = df_stephenville_nfld["Nov"].replace(-9999.9, df_stephenville_nfld["Nov"].median())
df_stephenville_nfld["Dec"] = df_stephenville_nfld["Dec"].replace(-9999.9, df_stephenville_nfld["Dec"].median())
df_stephenville_nfld["Annual"] = df_stephenville_nfld["Annual"].replace(-9999.9, df_stephenville_nfld["Annual"].median())
df_stephenville_nfld["Winter"] = df_stephenville_nfld["Winter"].replace(-9999.9, df_stephenville_nfld["Winter"].median())
df_stephenville_nfld["Spring"] = df_stephenville_nfld["Spring"].replace(-9999.9, df_stephenville_nfld["Spring"].median())
df_stephenville_nfld["Summer"] = df_stephenville_nfld["Summer"].replace(-9999.9, df_stephenville_nfld["Summer"].median())
df_stephenville_nfld["Autumn"] = df_stephenville_nfld["Autumn"].replace(-9999.9, df_stephenville_nfld["Autumn"].median())

#St Johns Newfoundland 

stjohns_nfld = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/stjohns_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_stjohns_nfld = pd.DataFrame(stjohns_nfld)

df_stjohns_nfld["Jan"] = df_stjohns_nfld["Jan"].replace(-9999.9, df_stjohns_nfld["Jan"].median())
df_stjohns_nfld["Feb"] = df_stjohns_nfld["Feb"].replace(-9999.9, df_stjohns_nfld["Feb"].median())
df_stjohns_nfld["Mar"] = df_stjohns_nfld["Mar"].replace(-9999.9, df_stjohns_nfld["Mar"].median())
df_stjohns_nfld["Apr"] = df_stjohns_nfld["Apr"].replace(-9999.9, df_stjohns_nfld["Apr"].median())
df_stjohns_nfld["May"] = df_stjohns_nfld["May"].replace(-9999.9, df_stjohns_nfld["May"].median())
df_stjohns_nfld["Jun"] = df_stjohns_nfld["Jun"].replace(-9999.9, df_stjohns_nfld["Jun"].median())
df_stjohns_nfld["Jul"] = df_stjohns_nfld["Jul"].replace(-9999.9, df_stjohns_nfld["Jul"].median())
df_stjohns_nfld["Aug"] = df_stjohns_nfld["Aug"].replace(-9999.9, df_stjohns_nfld["Aug"].median())
df_stjohns_nfld["Sep"] = df_stjohns_nfld["Sep"].replace(-9999.9, df_stjohns_nfld["Sep"].median())
df_stjohns_nfld["Oct"] = df_stjohns_nfld["Oct"].replace(-9999.9, df_stjohns_nfld["Oct"].median())
df_stjohns_nfld["Nov"] = df_stjohns_nfld["Nov"].replace(-9999.9, df_stjohns_nfld["Nov"].median())
df_stjohns_nfld["Dec"] = df_stjohns_nfld["Dec"].replace(-9999.9, df_stjohns_nfld["Dec"].median())
df_stjohns_nfld["Annual"] = df_stjohns_nfld["Annual"].replace(-9999.9, df_stjohns_nfld["Annual"].median())
df_stjohns_nfld["Winter"] = df_stjohns_nfld["Winter"].replace(-9999.9, df_stjohns_nfld["Winter"].median())
df_stjohns_nfld["Spring"] = df_stjohns_nfld["Spring"].replace(-9999.9, df_stjohns_nfld["Spring"].median())
df_stjohns_nfld["Summer"] = df_stjohns_nfld["Summer"].replace(-9999.9, df_stjohns_nfld["Summer"].median())
df_stjohns_nfld["Autumn"] = df_stjohns_nfld["Autumn"].replace(-9999.9, df_stjohns_nfld["Autumn"].median())

#Sudbury Ontario

sudbury_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/sudbury_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_sudbury_ont = pd.DataFrame(sudbury_ont)

df_sudbury_ont["Jan"] = df_sudbury_ont["Jan"].replace(-9999.9, df_sudbury_ont["Jan"].median())
df_sudbury_ont["Feb"] = df_sudbury_ont["Feb"].replace(-9999.9, df_sudbury_ont["Feb"].median())
df_sudbury_ont["Mar"] = df_sudbury_ont["Mar"].replace(-9999.9, df_sudbury_ont["Mar"].median())
df_sudbury_ont["Apr"] = df_sudbury_ont["Apr"].replace(-9999.9, df_sudbury_ont["Apr"].median())
df_sudbury_ont["May"] = df_sudbury_ont["May"].replace(-9999.9, df_sudbury_ont["May"].median())
df_sudbury_ont["Jun"] = df_sudbury_ont["Jun"].replace(-9999.9, df_sudbury_ont["Jun"].median())
df_sudbury_ont["Jul"] = df_sudbury_ont["Jul"].replace(-9999.9, df_sudbury_ont["Jul"].median())
df_sudbury_ont["Aug"] = df_sudbury_ont["Aug"].replace(-9999.9, df_sudbury_ont["Aug"].median())
df_sudbury_ont["Sep"] = df_sudbury_ont["Sep"].replace(-9999.9, df_sudbury_ont["Sep"].median())
df_sudbury_ont["Oct"] = df_sudbury_ont["Oct"].replace(-9999.9, df_sudbury_ont["Oct"].median())
df_sudbury_ont["Nov"] = df_sudbury_ont["Nov"].replace(-9999.9, df_sudbury_ont["Nov"].median())
df_sudbury_ont["Dec"] = df_sudbury_ont["Dec"].replace(-9999.9, df_sudbury_ont["Dec"].median())
df_sudbury_ont["Annual"] = df_sudbury_ont["Annual"].replace(-9999.9, df_sudbury_ont["Annual"].median())
df_sudbury_ont["Winter"] = df_sudbury_ont["Winter"].replace(-9999.9, df_sudbury_ont["Winter"].median())
df_sudbury_ont["Spring"] = df_sudbury_ont["Spring"].replace(-9999.9, df_sudbury_ont["Spring"].median())
df_sudbury_ont["Summer"] = df_sudbury_ont["Summer"].replace(-9999.9, df_sudbury_ont["Summer"].median())
df_sudbury_ont["Autumn"] = df_sudbury_ont["Autumn"].replace(-9999.9, df_sudbury_ont["Autumn"].median())

#Summerside PEI 

summerside_pei = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/summerside_pei.csv", engine = 'python', sep=r'\s*,\s*',encoding = 'utf-8-sig')
df_summerside_pei = pd.DataFrame(summerside_pei)


df_summerside_pei["Jan"] = df_summerside_pei["Jan"].replace(-9999.9, df_summerside_pei["Jan"].median())
df_summerside_pei["Feb"] = df_summerside_pei["Feb"].replace(-9999.9, df_summerside_pei["Feb"].median())
df_summerside_pei["Mar"] = df_summerside_pei["Mar"].replace(-9999.9, df_summerside_pei["Mar"].median())
df_summerside_pei["Apr"] = df_summerside_pei["Apr"].replace(-9999.9, df_summerside_pei["Apr"].median())
df_summerside_pei["May"] = df_summerside_pei["May"].replace(-9999.9, df_summerside_pei["May"].median())
df_summerside_pei["Jun"] = df_summerside_pei["Jun"].replace(-9999.9, df_summerside_pei["Jun"].median())
df_summerside_pei["Jul"] = df_summerside_pei["Jul"].replace(-9999.9, df_summerside_pei["Jul"].median())
df_summerside_pei["Aug"] = df_summerside_pei["Aug"].replace(-9999.9, df_summerside_pei["Aug"].median())
df_summerside_pei["Sep"] = df_summerside_pei["Sep"].replace(-9999.9, df_summerside_pei["Sep"].median())
df_summerside_pei["Oct"] = df_summerside_pei["Oct"].replace(-9999.9, df_summerside_pei["Oct"].median())
df_summerside_pei["Nov"] = df_summerside_pei["Nov"].replace(-9999.9, df_summerside_pei["Nov"].median())
df_summerside_pei["Dec"] = df_summerside_pei["Dec"].replace(-9999.9, df_summerside_pei["Dec"].median())
df_summerside_pei["Annual"] = df_summerside_pei["Annual"].replace(-9999.9, df_summerside_pei["Annual"].median())
df_summerside_pei["Winter"] = df_summerside_pei["Winter"].replace(-9999.9, df_summerside_pei["Winter"].median())
df_summerside_pei["Spring"] = df_summerside_pei["Spring"].replace(-9999.9, df_summerside_pei["Spring"].median())
df_summerside_pei["Summer"] = df_summerside_pei["Summer"].replace(-9999.9, df_summerside_pei["Summer"].median())
df_summerside_pei["Autumn"] = df_summerside_pei["Autumn"].replace(-9999.9, df_summerside_pei["Autumn"].median())


#Swiftcurrent Saskatchewan 

swiftcurrent_sask = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/swiftcurrent_sask.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_swiftcurrent_sask = pd.DataFrame(swiftcurrent_sask)

df_swiftcurrent_sask["Oct"] = df_swiftcurrent_sask["Oct"].replace(-9999.9, df_swiftcurrent_sask["Oct"].median())

#Sydney Nova Scotia 

sydney_ns = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/syndney_ns.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_sydney_ns = pd.DataFrame(sydney_ns)

df_sydney_ns["Jan"] = df_sydney_ns["Jan"].replace(-9999.9, df_sydney_ns["Jan"].median())
df_sydney_ns["Feb"] = df_sydney_ns["Feb"].replace(-9999.9, df_sydney_ns["Feb"].median())
df_sydney_ns["Mar"] = df_sydney_ns["Mar"].replace(-9999.9, df_sydney_ns["Mar"].median())
df_sydney_ns["Apr"] = df_sydney_ns["Apr"].replace(-9999.9, df_sydney_ns["Apr"].median())
df_sydney_ns["May"] = df_sydney_ns["May"].replace(-9999.9, df_sydney_ns["May"].median())
df_sydney_ns["Jun"] = df_sydney_ns["Jun"].replace(-9999.9, df_sydney_ns["Jun"].median())
df_sydney_ns["Jul"] = df_sydney_ns["Jul"].replace(-9999.9, df_sydney_ns["Jul"].median())
df_sydney_ns["Aug"] = df_sydney_ns["Aug"].replace(-9999.9, df_sydney_ns["Aug"].median())
df_sydney_ns["Sep"] = df_sydney_ns["Sep"].replace(-9999.9, df_sydney_ns["Sep"].median())
df_sydney_ns["Oct"] = df_sydney_ns["Oct"].replace(-9999.9, df_sydney_ns["Oct"].median())
df_sydney_ns["Nov"] = df_sydney_ns["Nov"].replace(-9999.9, df_sydney_ns["Nov"].median())
df_sydney_ns["Dec"] = df_sydney_ns["Dec"].replace(-9999.9, df_sydney_ns["Dec"].median())
df_sydney_ns["Annual"] = df_sydney_ns["Annual"].replace(-9999.9, df_sydney_ns["Annual"].median())
df_sydney_ns["Winter"] = df_sydney_ns["Winter"].replace(-9999.9, df_sydney_ns["Winter"].median())
df_sydney_ns["Spring"] = df_sydney_ns["Spring"].replace(-9999.9, df_sydney_ns["Spring"].median())
df_sydney_ns["Summer"] = df_sydney_ns["Summer"].replace(-9999.9, df_sydney_ns["Summer"].median())
df_sydney_ns["Autumn"] = df_sydney_ns["Autumn"].replace(-9999.9, df_sydney_ns["Autumn"].median())

#Terrace British Columbia 

terrace_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/terrace_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_terrace_bc = pd.DataFrame(terrace_bc)

df_terrace_bc["Jan"] = df_terrace_bc["Jan"].replace(-9999.9, df_terrace_bc["Jan"].median())
df_terrace_bc["Feb"] = df_terrace_bc["Feb"].replace(-9999.9, df_terrace_bc["Feb"].median())
df_terrace_bc["Mar"] = df_terrace_bc["Mar"].replace(-9999.9, df_terrace_bc["Mar"].median())
df_terrace_bc["Apr"] = df_terrace_bc["Apr"].replace(-9999.9, df_terrace_bc["Apr"].median())
df_terrace_bc["May"] = df_terrace_bc["May"].replace(-9999.9, df_terrace_bc["May"].median())
df_terrace_bc["Jun"] = df_terrace_bc["Jun"].replace(-9999.9, df_terrace_bc["Jun"].median())
df_terrace_bc["Jul"] = df_terrace_bc["Jul"].replace(-9999.9, df_terrace_bc["Jul"].median())
df_terrace_bc["Aug"] = df_terrace_bc["Aug"].replace(-9999.9, df_terrace_bc["Aug"].median())
df_terrace_bc["Sep"] = df_terrace_bc["Sep"].replace(-9999.9, df_terrace_bc["Sep"].median())
df_terrace_bc["Oct"] = df_terrace_bc["Oct"].replace(-9999.9, df_terrace_bc["Oct"].median())
df_terrace_bc["Nov"] = df_terrace_bc["Nov"].replace(-9999.9, df_terrace_bc["Nov"].median())
df_terrace_bc["Dec"] = df_terrace_bc["Dec"].replace(-9999.9, df_terrace_bc["Dec"].median())
df_terrace_bc["Annual"] = df_terrace_bc["Annual"].replace(-9999.9, df_terrace_bc["Annual"].median())
df_terrace_bc["Winter"] = df_terrace_bc["Winter"].replace(-9999.9, df_terrace_bc["Winter"].median())
df_terrace_bc["Spring"] = df_terrace_bc["Spring"].replace(-9999.9, df_terrace_bc["Spring"].median())
df_terrace_bc["Summer"] = df_terrace_bc["Summer"].replace(-9999.9, df_terrace_bc["Summer"].median())
df_terrace_bc["Autumn"] = df_terrace_bc["Autumn"].replace(-9999.9, df_terrace_bc["Autumn"].median())

#Teslin Yukon Territories 

teslin_yt = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/teslin_yt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_teslin_yt = pd.DataFrame(teslin_yt)

df_teslin_yt["Jan"] = df_teslin_yt["Jan"].replace(-9999.9, df_teslin_yt["Jan"].median())
df_teslin_yt["Feb"] = df_teslin_yt["Feb"].replace(-9999.9, df_teslin_yt["Feb"].median())
df_teslin_yt["Mar"] = df_teslin_yt["Mar"].replace(-9999.9, df_teslin_yt["Mar"].median())
df_teslin_yt["Apr"] = df_teslin_yt["Apr"].replace(-9999.9, df_teslin_yt["Apr"].median())
df_teslin_yt["May"] = df_teslin_yt["May"].replace(-9999.9, df_teslin_yt["May"].median())
df_teslin_yt["Jun"] = df_teslin_yt["Jun"].replace(-9999.9, df_teslin_yt["Jun"].median())
df_teslin_yt["Jul"] = df_teslin_yt["Jul"].replace(-9999.9, df_teslin_yt["Jul"].median())
df_teslin_yt["Aug"] = df_teslin_yt["Aug"].replace(-9999.9, df_teslin_yt["Aug"].median())
df_teslin_yt["Sep"] = df_teslin_yt["Sep"].replace(-9999.9, df_teslin_yt["Sep"].median())
df_teslin_yt["Oct"] = df_teslin_yt["Oct"].replace(-9999.9, df_teslin_yt["Oct"].median())
df_teslin_yt["Nov"] = df_teslin_yt["Nov"].replace(-9999.9, df_teslin_yt["Nov"].median())
df_teslin_yt["Dec"] = df_teslin_yt["Dec"].replace(-9999.9, df_teslin_yt["Dec"].median())
df_teslin_yt["Annual"] = df_teslin_yt["Annual"].replace(-9999.9, df_teslin_yt["Annual"].median())
df_teslin_yt["Winter"] = df_teslin_yt["Winter"].replace(-9999.9, df_teslin_yt["Winter"].median())
df_teslin_yt["Spring"] = df_teslin_yt["Spring"].replace(-9999.9, df_teslin_yt["Spring"].median())
df_teslin_yt["Summer"] = df_teslin_yt["Summer"].replace(-9999.9, df_teslin_yt["Summer"].median())
df_teslin_yt["Autumn"] = df_teslin_yt["Autumn"].replace(-9999.9, df_teslin_yt["Autumn"].median())

#Thepas Manitoba

thepas_man = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/thepas_man.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_thepas_man = pd.DataFrame(thepas_man)

df_thepas_man["Oct"] = df_thepas_man["Oct"].replace(-9999.9, df_thepas_man["Oct"].median())
df_thepas_man["Nov"] = df_thepas_man["Nov"].replace(-9999.9, df_thepas_man["Nov"].median())
df_thepas_man["Autumn"] = df_thepas_man["Autumn"].replace(-9999.9, df_thepas_man["Autumn"].median())
df_thepas_man["Dec"] = df_thepas_man["Dec"].replace(-9999.9, df_thepas_man["Dec"].median())

#Thompson Manitoba 

thompson_man = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/thompson_man.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_thompson_man = pd.DataFrame(thompson_man)

df_thompson_man["Jan"] = df_thompson_man["Jan"].replace(-9999.9, df_thompson_man["Jan"].median())
df_thompson_man["Feb"] = df_thompson_man["Feb"].replace(-9999.9, df_thompson_man["Feb"].median())
df_thompson_man["Mar"] = df_thompson_man["Mar"].replace(-9999.9, df_thompson_man["Mar"].median())
df_thompson_man["Apr"] = df_thompson_man["Apr"].replace(-9999.9, df_thompson_man["Apr"].median())
df_thompson_man["May"] = df_thompson_man["May"].replace(-9999.9, df_thompson_man["May"].median())
df_thompson_man["Jun"] = df_thompson_man["Jun"].replace(-9999.9, df_thompson_man["Jun"].median())
df_thompson_man["Jul"] = df_thompson_man["Jul"].replace(-9999.9, df_thompson_man["Jul"].median())
df_thompson_man["Aug"] = df_thompson_man["Aug"].replace(-9999.9, df_thompson_man["Aug"].median())
df_thompson_man["Sep"] = df_thompson_man["Sep"].replace(-9999.9, df_thompson_man["Sep"].median())
df_thompson_man["Oct"] = df_thompson_man["Oct"].replace(-9999.9, df_thompson_man["Oct"].median())
df_thompson_man["Nov"] = df_thompson_man["Nov"].replace(-9999.9, df_thompson_man["Nov"].median())
df_thompson_man["Dec"] = df_thompson_man["Dec"].replace(-9999.9, df_thompson_man["Dec"].median())
df_thompson_man["Annual"] = df_thompson_man["Annual"].replace(-9999.9, df_thompson_man["Annual"].median())
df_thompson_man["Winter"] = df_thompson_man["Winter"].replace(-9999.9, df_thompson_man["Winter"].median())
df_thompson_man["Spring"] = df_thompson_man["Spring"].replace(-9999.9, df_thompson_man["Spring"].median())
df_thompson_man["Summer"] = df_thompson_man["Summer"].replace(-9999.9, df_thompson_man["Summer"].median())
df_thompson_man["Autumn"] = df_thompson_man["Autumn"].replace(-9999.9, df_thompson_man["Autumn"].median())

#Thunderbay Ontario

thunderbay_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/thunderbay_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_thunderbay_ont = pd.DataFrame(thunderbay_ont)


#Timmins Victor Power 

timminsvictorpower_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/timminsvictorpower_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_timminsvictorpower_ont  = pd.DataFrame(timminsvictorpower_ont )

df_timminsvictorpower_ont["Jan"] = df_timminsvictorpower_ont["Jan"].replace(-9999.9, df_timminsvictorpower_ont["Jan"].median())
df_timminsvictorpower_ont["Feb"] = df_timminsvictorpower_ont["Feb"].replace(-9999.9, df_timminsvictorpower_ont["Feb"].median())
df_timminsvictorpower_ont["Mar"] = df_timminsvictorpower_ont["Mar"].replace(-9999.9, df_timminsvictorpower_ont["Mar"].median())
df_timminsvictorpower_ont["Apr"] = df_timminsvictorpower_ont["Apr"].replace(-9999.9, df_timminsvictorpower_ont["Apr"].median())
df_timminsvictorpower_ont["May"] = df_timminsvictorpower_ont["May"].replace(-9999.9, df_timminsvictorpower_ont["May"].median())
df_timminsvictorpower_ont["Jun"] = df_timminsvictorpower_ont["Jun"].replace(-9999.9, df_timminsvictorpower_ont["Jun"].median())
df_timminsvictorpower_ont["Jul"] = df_timminsvictorpower_ont["Jul"].replace(-9999.9, df_timminsvictorpower_ont["Jul"].median())
df_timminsvictorpower_ont["Aug"] = df_timminsvictorpower_ont["Aug"].replace(-9999.9, df_timminsvictorpower_ont["Aug"].median())
df_timminsvictorpower_ont["Sep"] = df_timminsvictorpower_ont["Sep"].replace(-9999.9, df_timminsvictorpower_ont["Sep"].median())
df_timminsvictorpower_ont["Oct"] = df_timminsvictorpower_ont["Oct"].replace(-9999.9, df_timminsvictorpower_ont["Oct"].median())
df_timminsvictorpower_ont["Nov"] = df_timminsvictorpower_ont["Nov"].replace(-9999.9, df_timminsvictorpower_ont["Nov"].median())
df_timminsvictorpower_ont["Dec"] = df_timminsvictorpower_ont["Dec"].replace(-9999.9, df_timminsvictorpower_ont["Dec"].median())
df_timminsvictorpower_ont["Annual"] = df_timminsvictorpower_ont["Annual"].replace(-9999.9, df_timminsvictorpower_ont["Annual"].median())
df_timminsvictorpower_ont["Winter"] = df_timminsvictorpower_ont["Winter"].replace(-9999.9, df_timminsvictorpower_ont["Winter"].median())
df_timminsvictorpower_ont["Spring"] = df_timminsvictorpower_ont["Spring"].replace(-9999.9, df_timminsvictorpower_ont["Spring"].median())
df_timminsvictorpower_ont["Summer"] = df_timminsvictorpower_ont["Summer"].replace(-9999.9, df_timminsvictorpower_ont["Summer"].median())
df_timminsvictorpower_ont["Autumn"] = df_timminsvictorpower_ont["Autumn"].replace(-9999.9, df_timminsvictorpower_ont["Autumn"].median())

#Tofino British Columbia 

tofino_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/tofino_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_tofino_bc  = pd.DataFrame(tofino_bc )


df_tofino_bc["Jan"] = df_tofino_bc["Jan"].replace(-9999.9, df_tofino_bc["Jan"].median())
df_tofino_bc["Feb"] = df_tofino_bc["Feb"].replace(-9999.9, df_tofino_bc["Feb"].median())
df_tofino_bc["Mar"] = df_tofino_bc["Mar"].replace(-9999.9, df_tofino_bc["Mar"].median())
df_tofino_bc["Apr"] = df_tofino_bc["Apr"].replace(-9999.9, df_tofino_bc["Apr"].median())
df_tofino_bc["May"] = df_tofino_bc["May"].replace(-9999.9, df_tofino_bc["May"].median())
df_tofino_bc["Jun"] = df_tofino_bc["Jun"].replace(-9999.9, df_tofino_bc["Jun"].median())
df_tofino_bc["Jul"] = df_tofino_bc["Jul"].replace(-9999.9, df_tofino_bc["Jul"].median())
df_tofino_bc["Aug"] = df_tofino_bc["Aug"].replace(-9999.9, df_tofino_bc["Aug"].median())
df_tofino_bc["Sep"] = df_tofino_bc["Sep"].replace(-9999.9, df_tofino_bc["Sep"].median())
df_tofino_bc["Oct"] = df_tofino_bc["Oct"].replace(-9999.9, df_tofino_bc["Oct"].median())
df_tofino_bc["Nov"] = df_tofino_bc["Nov"].replace(-9999.9, df_tofino_bc["Nov"].median())
df_tofino_bc["Dec"] = df_tofino_bc["Dec"].replace(-9999.9, df_tofino_bc["Dec"].median())
df_tofino_bc["Annual"] = df_tofino_bc["Annual"].replace(-9999.9, df_tofino_bc["Annual"].median())
df_tofino_bc["Winter"] = df_tofino_bc["Winter"].replace(-9999.9, df_tofino_bc["Winter"].median())
df_tofino_bc["Spring"] = df_tofino_bc["Spring"].replace(-9999.9, df_tofino_bc["Spring"].median())
df_tofino_bc["Summer"] = df_tofino_bc["Summer"].replace(-9999.9, df_tofino_bc["Summer"].median())
df_tofino_bc["Autumn"] = df_tofino_bc["Autumn"].replace(-9999.9, df_tofino_bc["Autumn"].median())


#Toronto Ontario STAND UP!!!!!

toronto_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/toronto_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_toronto_ont  = pd.DataFrame(toronto_ont)


#Torontoisland Ontario

torontoisland_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/torontoisland_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_torontoisland_ont  = pd.DataFrame(torontoisland_ont)


df_torontoisland_ont["Jan"] = df_torontoisland_ont["Jan"].replace(-9999.9, df_torontoisland_ont["Jan"].median())
df_torontoisland_ont["Feb"] = df_torontoisland_ont["Feb"].replace(-9999.9, df_torontoisland_ont["Feb"].median())
df_torontoisland_ont["Mar"] = df_torontoisland_ont["Mar"].replace(-9999.9, df_torontoisland_ont["Mar"].median())
df_torontoisland_ont["Apr"] = df_torontoisland_ont["Apr"].replace(-9999.9, df_torontoisland_ont["Apr"].median())
df_torontoisland_ont["May"] = df_torontoisland_ont["May"].replace(-9999.9, df_torontoisland_ont["May"].median())
df_torontoisland_ont["Jun"] = df_torontoisland_ont["Jun"].replace(-9999.9, df_torontoisland_ont["Jun"].median())
df_torontoisland_ont["Jul"] = df_torontoisland_ont["Jul"].replace(-9999.9, df_torontoisland_ont["Jul"].median())
df_torontoisland_ont["Aug"] = df_torontoisland_ont["Aug"].replace(-9999.9, df_torontoisland_ont["Aug"].median())
df_torontoisland_ont["Sep"] = df_torontoisland_ont["Sep"].replace(-9999.9, df_torontoisland_ont["Sep"].median())
df_torontoisland_ont["Oct"] = df_torontoisland_ont["Oct"].replace(-9999.9, df_torontoisland_ont["Oct"].median())
df_torontoisland_ont["Nov"] = df_torontoisland_ont["Nov"].replace(-9999.9, df_torontoisland_ont["Nov"].median())
df_torontoisland_ont["Dec"] = df_torontoisland_ont["Dec"].replace(-9999.9, df_torontoisland_ont["Dec"].median())
df_torontoisland_ont["Annual"] = df_torontoisland_ont["Annual"].replace(-9999.9, df_torontoisland_ont["Annual"].median())
df_torontoisland_ont["Winter"] = df_torontoisland_ont["Winter"].replace(-9999.9, df_torontoisland_ont["Winter"].median())
df_torontoisland_ont["Spring"] = df_torontoisland_ont["Spring"].replace(-9999.9, df_torontoisland_ont["Spring"].median())
df_torontoisland_ont["Summer"] = df_torontoisland_ont["Summer"].replace(-9999.9, df_torontoisland_ont["Summer"].median())
df_torontoisland_ont["Autumn"] = df_torontoisland_ont["Autumn"].replace(-9999.9, df_torontoisland_ont["Autumn"].median())

#Trenton Ontario

trenton_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/trenton_ont.csv", engine = 'python', sep=r'\s*,\s*',  encoding = 'utf-8-sig')
df_trenton_ont  = pd.DataFrame(trenton_ont)


#Tuktoyaktuk North West Territories

tuktoyaktuk_nwt = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/tuktoyaktuk_nwt.csv", engine = 'python', sep=r'\s*,\s*', encoding ='utf-8-sig')
df_tuktoyaktuk_nwt = pd.DataFrame(tuktoyaktuk_nwt)

df_tuktoyaktuk_nwt["Jan"] = df_tuktoyaktuk_nwt["Jan"].replace(-9999.9, df_tuktoyaktuk_nwt["Jan"].median())
df_tuktoyaktuk_nwt["Feb"] = df_tuktoyaktuk_nwt["Feb"].replace(-9999.9, df_tuktoyaktuk_nwt["Feb"].median())
df_tuktoyaktuk_nwt["Mar"] = df_tuktoyaktuk_nwt["Mar"].replace(-9999.9, df_tuktoyaktuk_nwt["Mar"].median())
df_tuktoyaktuk_nwt["Apr"] = df_tuktoyaktuk_nwt["Apr"].replace(-9999.9, df_tuktoyaktuk_nwt["Apr"].median())
df_tuktoyaktuk_nwt["May"] = df_tuktoyaktuk_nwt["May"].replace(-9999.9, df_tuktoyaktuk_nwt["May"].median())
df_tuktoyaktuk_nwt["Jun"] = df_tuktoyaktuk_nwt["Jun"].replace(-9999.9, df_tuktoyaktuk_nwt["Jun"].median())
df_tuktoyaktuk_nwt["Jul"] = df_tuktoyaktuk_nwt["Jul"].replace(-9999.9, df_tuktoyaktuk_nwt["Jul"].median())
df_tuktoyaktuk_nwt["Aug"] = df_tuktoyaktuk_nwt["Aug"].replace(-9999.9, df_tuktoyaktuk_nwt["Aug"].median())
df_tuktoyaktuk_nwt["Sep"] = df_tuktoyaktuk_nwt["Sep"].replace(-9999.9, df_tuktoyaktuk_nwt["Sep"].median())
df_tuktoyaktuk_nwt["Oct"] = df_tuktoyaktuk_nwt["Oct"].replace(-9999.9, df_tuktoyaktuk_nwt["Oct"].median())
df_tuktoyaktuk_nwt["Nov"] = df_tuktoyaktuk_nwt["Nov"].replace(-9999.9, df_tuktoyaktuk_nwt["Nov"].median())
df_tuktoyaktuk_nwt["Dec"] = df_tuktoyaktuk_nwt["Dec"].replace(-9999.9, df_tuktoyaktuk_nwt["Dec"].median())
df_tuktoyaktuk_nwt["Annual"] = df_tuktoyaktuk_nwt["Annual"].replace(-9999.9, df_tuktoyaktuk_nwt["Annual"].median())
df_tuktoyaktuk_nwt["Winter"] = df_tuktoyaktuk_nwt["Winter"].replace(-9999.9, df_tuktoyaktuk_nwt["Winter"].median())
df_tuktoyaktuk_nwt["Spring"] = df_tuktoyaktuk_nwt["Spring"].replace(-9999.9, df_tuktoyaktuk_nwt["Spring"].median())
df_tuktoyaktuk_nwt["Summer"] = df_tuktoyaktuk_nwt["Summer"].replace(-9999.9, df_tuktoyaktuk_nwt["Summer"].median())
df_tuktoyaktuk_nwt["Autumn"] = df_tuktoyaktuk_nwt["Autumn"].replace(-9999.9, df_tuktoyaktuk_nwt["Autumn"].median())


#Valdor Quebec 

valdor_queb = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/valdor_queb.csv", engine = 'python', sep=r'\s*,\s*', encoding ='utf-8-sig')
df_valdor_queb = pd.DataFrame(valdor_queb)

df_valdor_queb["Jan"] = df_valdor_queb["Jan"].replace(-9999.9, df_valdor_queb["Jan"].median())
df_valdor_queb["Feb"] = df_valdor_queb["Feb"].replace(-9999.9, df_valdor_queb["Feb"].median())
df_valdor_queb["Mar"] = df_valdor_queb["Mar"].replace(-9999.9, df_valdor_queb["Mar"].median())
df_valdor_queb["Apr"] = df_valdor_queb["Apr"].replace(-9999.9, df_valdor_queb["Apr"].median())
df_valdor_queb["May"] = df_valdor_queb["May"].replace(-9999.9, df_valdor_queb["May"].median())
df_valdor_queb["Jun"] = df_valdor_queb["Jun"].replace(-9999.9, df_valdor_queb["Jun"].median())
df_valdor_queb["Jul"] = df_valdor_queb["Jul"].replace(-9999.9, df_valdor_queb["Jul"].median())
df_valdor_queb["Aug"] = df_valdor_queb["Aug"].replace(-9999.9, df_valdor_queb["Aug"].median())
df_valdor_queb["Sep"] = df_valdor_queb["Sep"].replace(-9999.9, df_valdor_queb["Sep"].median())
df_valdor_queb["Oct"] = df_valdor_queb["Oct"].replace(-9999.9, df_valdor_queb["Oct"].median())
df_valdor_queb["Nov"] = df_valdor_queb["Nov"].replace(-9999.9, df_valdor_queb["Nov"].median())
df_valdor_queb["Dec"] = df_valdor_queb["Dec"].replace(-9999.9, df_valdor_queb["Dec"].median())
df_valdor_queb["Annual"] = df_valdor_queb["Annual"].replace(-9999.9, df_valdor_queb["Annual"].median())
df_valdor_queb["Winter"] = df_valdor_queb["Winter"].replace(-9999.9, df_valdor_queb["Winter"].median())
df_valdor_queb["Spring"] = df_valdor_queb["Spring"].replace(-9999.9, df_valdor_queb["Spring"].median())
df_valdor_queb["Summer"] = df_valdor_queb["Summer"].replace(-9999.9, df_valdor_queb["Summer"].median())
df_valdor_queb["Autumn"] = df_valdor_queb["Autumn"].replace(-9999.9, df_valdor_queb["Autumn"].median())


#Vancouver British Columbia 

vancouver_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/vancouver_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding ='utf-8-sig')
df_vancouver_bc = pd.DataFrame(vancouver_bc)

df_vancouver_bc["Jan"] = df_vancouver_bc["Jan"].replace(-9999.9, df_vancouver_bc["Jan"].median())
df_vancouver_bc["Feb"] = df_vancouver_bc["Feb"].replace(-9999.9, df_vancouver_bc["Feb"].median())
df_vancouver_bc["Mar"] = df_vancouver_bc["Mar"].replace(-9999.9, df_vancouver_bc["Mar"].median())
df_vancouver_bc["Apr"] = df_vancouver_bc["Apr"].replace(-9999.9, df_vancouver_bc["Apr"].median())
df_vancouver_bc["May"] = df_vancouver_bc["May"].replace(-9999.9, df_vancouver_bc["May"].median())
df_vancouver_bc["Jun"] = df_vancouver_bc["Jun"].replace(-9999.9, df_vancouver_bc["Jun"].median())
df_vancouver_bc["Jul"] = df_vancouver_bc["Jul"].replace(-9999.9, df_vancouver_bc["Jul"].median())
df_vancouver_bc["Aug"] = df_vancouver_bc["Aug"].replace(-9999.9, df_vancouver_bc["Aug"].median())
df_vancouver_bc["Sep"] = df_vancouver_bc["Sep"].replace(-9999.9, df_vancouver_bc["Sep"].median())
df_vancouver_bc["Oct"] = df_vancouver_bc["Oct"].replace(-9999.9, df_vancouver_bc["Oct"].median())
df_vancouver_bc["Nov"] = df_vancouver_bc["Nov"].replace(-9999.9, df_vancouver_bc["Nov"].median())
df_vancouver_bc["Dec"] = df_vancouver_bc["Dec"].replace(-9999.9, df_vancouver_bc["Dec"].median())
df_vancouver_bc["Annual"] = df_vancouver_bc["Annual"].replace(-9999.9, df_vancouver_bc["Annual"].median())
df_vancouver_bc["Winter"] = df_vancouver_bc["Winter"].replace(-9999.9, df_vancouver_bc["Winter"].median())
df_vancouver_bc["Spring"] = df_vancouver_bc["Spring"].replace(-9999.9, df_vancouver_bc["Spring"].median())
df_vancouver_bc["Summer"] = df_vancouver_bc["Summer"].replace(-9999.9, df_vancouver_bc["Summer"].median())
df_vancouver_bc["Autumn"] = df_vancouver_bc["Autumn"].replace(-9999.9, df_vancouver_bc["Autumn"].median())


#Victoria British Columbia 

victoria_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/victoria_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding ='utf-8-sig')
df_victoria_bc = pd.DataFrame(victoria_bc)

df_victoria_bc["Feb"] = df_victoria_bc["Feb"].replace(-9999.9, df_victoria_bc["Feb"].median())

#Wabushlake NewFoundland 

wabushlake_nfld = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/wabushlake_nfld.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_wabushlake_nfld  = pd.DataFrame(wabushlake_nfld)

df_wabushlake_nfld["Jan"] = df_wabushlake_nfld["Jan"].replace(-9999.9, df_wabushlake_nfld["Jan"].median())
df_wabushlake_nfld["Feb"] = df_wabushlake_nfld["Feb"].replace(-9999.9, df_wabushlake_nfld["Feb"].median())
df_wabushlake_nfld["Mar"] = df_wabushlake_nfld["Mar"].replace(-9999.9, df_wabushlake_nfld["Mar"].median())
df_wabushlake_nfld["Apr"] = df_wabushlake_nfld["Apr"].replace(-9999.9, df_wabushlake_nfld["Apr"].median())
df_wabushlake_nfld["May"] = df_wabushlake_nfld["May"].replace(-9999.9, df_wabushlake_nfld["May"].median())
df_wabushlake_nfld["Jun"] = df_wabushlake_nfld["Jun"].replace(-9999.9, df_wabushlake_nfld["Jun"].median())
df_wabushlake_nfld["Jul"] = df_wabushlake_nfld["Jul"].replace(-9999.9, df_wabushlake_nfld["Jul"].median())
df_wabushlake_nfld["Aug"] = df_wabushlake_nfld["Aug"].replace(-9999.9, df_wabushlake_nfld["Aug"].median())
df_wabushlake_nfld["Sep"] = df_wabushlake_nfld["Sep"].replace(-9999.9, df_wabushlake_nfld["Sep"].median())
df_wabushlake_nfld["Oct"] = df_wabushlake_nfld["Oct"].replace(-9999.9, df_wabushlake_nfld["Oct"].median())
df_wabushlake_nfld["Nov"] = df_wabushlake_nfld["Nov"].replace(-9999.9, df_wabushlake_nfld["Nov"].median())
df_wabushlake_nfld["Dec"] = df_wabushlake_nfld["Dec"].replace(-9999.9, df_wabushlake_nfld["Dec"].median())
df_wabushlake_nfld["Annual"] = df_wabushlake_nfld["Annual"].replace(-9999.9, df_wabushlake_nfld["Annual"].median())
df_wabushlake_nfld["Winter"] = df_wabushlake_nfld["Winter"].replace(-9999.9, df_wabushlake_nfld["Winter"].median())
df_wabushlake_nfld["Spring"] = df_wabushlake_nfld["Spring"].replace(-9999.9, df_wabushlake_nfld["Spring"].median())
df_wabushlake_nfld["Summer"] = df_wabushlake_nfld["Summer"].replace(-9999.9, df_wabushlake_nfld["Summer"].median())
df_wabushlake_nfld["Autumn"] = df_wabushlake_nfld["Autumn"].replace(-9999.9, df_wabushlake_nfld["Autumn"].median())


#Watsonlake Yukon Territories 

watsonlake_yt = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/watsonlake_yt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_watsonlake_yt = pd.DataFrame(watsonlake_yt)

df_watsonlake_yt["Jan"] = df_watsonlake_yt["Jan"].replace(-9999.9, df_watsonlake_yt["Jan"].median())
df_watsonlake_yt["Feb"] = df_watsonlake_yt["Feb"].replace(-9999.9, df_watsonlake_yt["Feb"].median())
df_watsonlake_yt["Oct"] = df_watsonlake_yt["Oct"].replace(-9999.9, df_watsonlake_yt["Oct"].median())
df_watsonlake_yt["Nov"] = df_watsonlake_yt["Nov"].replace(-9999.9, df_watsonlake_yt["Nov"].median())
df_watsonlake_yt["Dec"] = df_watsonlake_yt["Dec"].replace(-9999.9, df_watsonlake_yt["Dec"].median())
df_watsonlake_yt["Winter"] = df_watsonlake_yt["Winter"].replace(-9999.9, df_watsonlake_yt["Winter"].median())

#Westernhead Nova Scotia

westernhead_ns = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/westernhead_ns.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_westernhead_ns = pd.DataFrame(westernhead_ns)

df_westernhead_ns["Jan"] = df_westernhead_ns["Jan"].replace(-9999.9, df_westernhead_ns["Jan"].median())
df_westernhead_ns["Feb"] = df_westernhead_ns["Feb"].replace(-9999.9, df_westernhead_ns["Feb"].median())
df_westernhead_ns["Mar"] = df_westernhead_ns["Mar"].replace(-9999.9, df_westernhead_ns["Mar"].median())
df_westernhead_ns["Apr"] = df_westernhead_ns["Apr"].replace(-9999.9, df_westernhead_ns["Apr"].median())
df_westernhead_ns["May"] = df_westernhead_ns["May"].replace(-9999.9, df_westernhead_ns["May"].median())
df_westernhead_ns["Jun"] = df_westernhead_ns["Jun"].replace(-9999.9, df_westernhead_ns["Jun"].median())
df_westernhead_ns["Jul"] = df_westernhead_ns["Jul"].replace(-9999.9, df_westernhead_ns["Jul"].median())
df_westernhead_ns["Aug"] = df_westernhead_ns["Aug"].replace(-9999.9, df_westernhead_ns["Aug"].median())
df_westernhead_ns["Sep"] = df_westernhead_ns["Sep"].replace(-9999.9, df_westernhead_ns["Sep"].median())
df_westernhead_ns["Oct"] = df_westernhead_ns["Oct"].replace(-9999.9, df_westernhead_ns["Oct"].median())
df_westernhead_ns["Nov"] = df_westernhead_ns["Nov"].replace(-9999.9, df_westernhead_ns["Nov"].median())
df_westernhead_ns["Dec"] = df_westernhead_ns["Dec"].replace(-9999.9, df_westernhead_ns["Dec"].median())
df_westernhead_ns["Annual"] = df_westernhead_ns["Annual"].replace(-9999.9, df_westernhead_ns["Annual"].median())
df_westernhead_ns["Winter"] = df_westernhead_ns["Winter"].replace(-9999.9, df_westernhead_ns["Winter"].median())
df_westernhead_ns["Spring"] = df_westernhead_ns["Spring"].replace(-9999.9, df_westernhead_ns["Spring"].median())
df_westernhead_ns["Summer"] = df_westernhead_ns["Summer"].replace(-9999.9, df_westernhead_ns["Summer"].median())
df_westernhead_ns["Autumn"] = df_westernhead_ns["Autumn"].replace(-9999.9, df_westernhead_ns["Autumn"].median())


#Whitehourse Yukon Territories 

whitehorse_yt = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/whitehorse_yt.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_whitehorse_yt = pd.DataFrame(whitehorse_yt)


#Wiarton Ontario

wiarton_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/wiarton_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_wiarton_ont = pd.DataFrame(wiarton_ont)

df_wiarton_ont["Oct"] = df_wiarton_ont["Oct"].replace(-9999.9, df_wiarton_ont["Oct"].median())
df_wiarton_ont["Nov"] = df_wiarton_ont["Nov"].replace(-9999.9, df_wiarton_ont["Nov"].median())
df_wiarton_ont["Dec"] = df_wiarton_ont["Dec"].replace(-9999.9, df_wiarton_ont["Dec"].median())
df_wiarton_ont["Autumn"] = df_wiarton_ont["Autumn"].replace(-9999.9, df_wiarton_ont["Autumn"].median())


#Williamslake British Columbia 

williamslake_bc = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/williamslake_bc.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_williamslake_bc = pd.DataFrame(williamslake_bc)

df_williamslake_bc["Jan"] = df_williamslake_bc["Jan"].replace(-9999.9, df_williamslake_bc["Jan"].median())
df_williamslake_bc["Feb"] = df_williamslake_bc["Feb"].replace(-9999.9, df_williamslake_bc["Feb"].median())
df_williamslake_bc["Mar"] = df_williamslake_bc["Mar"].replace(-9999.9, df_williamslake_bc["Mar"].median())
df_williamslake_bc["Apr"] = df_williamslake_bc["Apr"].replace(-9999.9, df_williamslake_bc["Apr"].median())
df_williamslake_bc["May"] = df_williamslake_bc["May"].replace(-9999.9, df_williamslake_bc["May"].median())
df_williamslake_bc["Jun"] = df_williamslake_bc["Jun"].replace(-9999.9, df_williamslake_bc["Jun"].median())
df_williamslake_bc["Jul"] = df_williamslake_bc["Jul"].replace(-9999.9, df_williamslake_bc["Jul"].median())
df_williamslake_bc["Aug"] = df_williamslake_bc["Aug"].replace(-9999.9, df_williamslake_bc["Aug"].median())
df_williamslake_bc["Sep"] = df_williamslake_bc["Sep"].replace(-9999.9, df_williamslake_bc["Sep"].median())
df_williamslake_bc["Oct"] = df_williamslake_bc["Oct"].replace(-9999.9, df_williamslake_bc["Oct"].median())
df_williamslake_bc["Nov"] = df_williamslake_bc["Nov"].replace(-9999.9, df_williamslake_bc["Nov"].median())
df_williamslake_bc["Dec"] = df_williamslake_bc["Dec"].replace(-9999.9, df_williamslake_bc["Dec"].median())
df_williamslake_bc["Annual"] = df_williamslake_bc["Annual"].replace(-9999.9, df_williamslake_bc["Annual"].median())
df_williamslake_bc["Winter"] = df_williamslake_bc["Winter"].replace(-9999.9, df_williamslake_bc["Winter"].median())
df_williamslake_bc["Spring"] = df_williamslake_bc["Spring"].replace(-9999.9, df_williamslake_bc["Spring"].median())
df_williamslake_bc["Summer"] = df_williamslake_bc["Summer"].replace(-9999.9, df_williamslake_bc["Summer"].median())
df_williamslake_bc["Autumn"] = df_williamslake_bc["Autumn"].replace(-9999.9, df_williamslake_bc["Autumn"].median())


#Windsor Ontario

windsor_ont = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/windsor_ont.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_windsor_ont = pd.DataFrame(windsor_ont)


df_windsor_ont["Oct"] = df_windsor_ont["Oct"].replace(-9999.9, df_windsor_ont["Oct"].median())
df_windsor_ont["Nov"] = df_windsor_ont["Nov"].replace(-9999.9, df_windsor_ont["Nov"].median())
df_windsor_ont["Dec"] = df_windsor_ont["Dec"].replace(-9999.9, df_windsor_ont["Dec"].median())
df_windsor_ont["Autumn"] = df_windsor_ont["Autumn"].replace(-9999.9, df_windsor_ont["Autumn"].median())


#Winnipeg Manitoba

winnipeg_man = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/winnipeg_man_cleaned.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_winnipeg_man = pd.DataFrame(winnipeg_man)

df_winnipeg_man["Jan"] = df_winnipeg_man["Jan"].replace(-9999.9, df_winnipeg_man["Jan"].median())
df_winnipeg_man["Feb"] = df_winnipeg_man["Feb"].replace(-9999.9, df_winnipeg_man["Feb"].median())
df_winnipeg_man["Mar"] = df_winnipeg_man["Mar"].replace(-9999.9, df_winnipeg_man["Mar"].median())
df_winnipeg_man["Apr"] = df_winnipeg_man["Apr"].replace(-9999.9, df_winnipeg_man["Apr"].median())
df_winnipeg_man["May"] = df_winnipeg_man["May"].replace(-9999.9, df_winnipeg_man["May"].median())
df_winnipeg_man["Jun"] = df_winnipeg_man["Jun"].replace(-9999.9, df_winnipeg_man["Jun"].median())
df_winnipeg_man["Jul"] = df_winnipeg_man["Jul"].replace(-9999.9, df_winnipeg_man["Jul"].median())
df_winnipeg_man["Aug"] = df_winnipeg_man["Aug"].replace(-9999.9, df_winnipeg_man["Aug"].median())
df_winnipeg_man["Sep"] = df_winnipeg_man["Sep"].replace(-9999.9, df_winnipeg_man["Sep"].median())
df_winnipeg_man["Oct"] = df_winnipeg_man["Oct"].replace(-9999.9, df_winnipeg_man["Oct"].median())
df_winnipeg_man["Nov"] = df_winnipeg_man["Nov"].replace(-9999.9, df_winnipeg_man["Nov"].median())
df_winnipeg_man["Dec"] = df_winnipeg_man["Dec"].replace(-9999.9, df_winnipeg_man["Dec"].median())
df_winnipeg_man["Annual"] = df_winnipeg_man["Annual"].replace(-9999.9, df_winnipeg_man["Annual"].median())
df_winnipeg_man["Winter"] = df_winnipeg_man["Winter"].replace(-9999.9, df_winnipeg_man["Winter"].median())
df_winnipeg_man["Spring"] = df_winnipeg_man["Spring"].replace(-9999.9, df_winnipeg_man["Spring"].median())
df_winnipeg_man["Summer"] = df_winnipeg_man["Summer"].replace(-9999.9, df_winnipeg_man["Summer"].median())
df_winnipeg_man["Autumn"] = df_winnipeg_man["Autumn"].replace(-9999.9, df_winnipeg_man["Autumn"].median())


#Yarmouth Novascotia 

yarmouth_ns = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/yarmouth_ns_cleaned.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig' )
df_yarmouth_ns = pd.DataFrame(yarmouth_ns)

df_yarmouth_ns["Jan"] = df_yarmouth_ns["Jan"].replace(-9999.9, df_yarmouth_ns["Jan"].median())
df_yarmouth_ns["Feb"] = df_yarmouth_ns["Feb"].replace(-9999.9, df_yarmouth_ns["Feb"].median())
df_yarmouth_ns["Mar"] = df_yarmouth_ns["Mar"].replace(-9999.9, df_yarmouth_ns["Mar"].median())
df_yarmouth_ns["Apr"] = df_yarmouth_ns["Apr"].replace(-9999.9, df_yarmouth_ns["Apr"].median())
df_yarmouth_ns["May"] = df_yarmouth_ns["May"].replace(-9999.9, df_yarmouth_ns["May"].median())
df_yarmouth_ns["Jun"] = df_yarmouth_ns["Jun"].replace(-9999.9, df_yarmouth_ns["Jun"].median())
df_yarmouth_ns["Jul"] = df_yarmouth_ns["Jul"].replace(-9999.9, df_yarmouth_ns["Jul"].median())
df_yarmouth_ns["Aug"] = df_yarmouth_ns["Aug"].replace(-9999.9, df_yarmouth_ns["Aug"].median())
df_yarmouth_ns["Sep"] = df_yarmouth_ns["Sep"].replace(-9999.9, df_yarmouth_ns["Sep"].median())
df_yarmouth_ns["Oct"] = df_yarmouth_ns["Oct"].replace(-9999.9, df_yarmouth_ns["Oct"].median())
df_yarmouth_ns["Nov"] = df_yarmouth_ns["Nov"].replace(-9999.9, df_yarmouth_ns["Nov"].median())
df_yarmouth_ns["Dec"] = df_yarmouth_ns["Dec"].replace(-9999.9, df_yarmouth_ns["Dec"].median())
df_yarmouth_ns["Annual"] = df_yarmouth_ns["Annual"].replace(-9999.9, df_yarmouth_ns["Annual"].median())
df_yarmouth_ns["Winter"] = df_yarmouth_ns["Winter"].replace(-9999.9, df_yarmouth_ns["Winter"].median())
df_yarmouth_ns["Spring"] = df_yarmouth_ns["Spring"].replace(-9999.9, df_yarmouth_ns["Spring"].median())
df_yarmouth_ns["Summer"] = df_yarmouth_ns["Summer"].replace(-9999.9, df_yarmouth_ns["Summer"].median())
df_yarmouth_ns["Autumn"] = df_yarmouth_ns["Autumn"].replace(-9999.9, df_yarmouth_ns["Autumn"].median())


#Yellowknife North West Territories

yellowknife_nwt = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/yellowknife_nwt_cleaned.csv", engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_yellowknife_nwt = pd.DataFrame(yellowknife_nwt)

#Yorkton Saskatchewan 

yorkton_sask = pd.read_csv("/Users/bryanekeh/Desktop/data_sets/canadian_wsdata_kmh/yorkton_sask_cleaned.csv",engine = 'python', sep=r'\s*,\s*', encoding = 'utf-8-sig')
df_yorkton_sask = pd.DataFrame(yorkton_sask)

df_yorkton_sask["Jan"] = df_yorkton_sask["Jan"].replace(-9999.9, df_yorkton_sask["Jan"].median())
df_yorkton_sask["Feb"] = df_yorkton_sask["Feb"].replace(-9999.9, df_yorkton_sask["Feb"].median())
df_yorkton_sask["Mar"] = df_yorkton_sask["Mar"].replace(-9999.9, df_yorkton_sask["Mar"].median())
df_yorkton_sask["Apr"] = df_yorkton_sask["Apr"].replace(-9999.9, df_yorkton_sask["Apr"].median())
df_yorkton_sask["May"] = df_yorkton_sask["May"].replace(-9999.9, df_yorkton_sask["May"].median())
df_yorkton_sask["Jun"] = df_yorkton_sask["Jun"].replace(-9999.9, df_yorkton_sask["Jun"].median())
df_yorkton_sask["Jul"] = df_yorkton_sask["Jul"].replace(-9999.9, df_yorkton_sask["Jul"].median())
df_yorkton_sask["Aug"] = df_yorkton_sask["Aug"].replace(-9999.9, df_yorkton_sask["Aug"].median())
df_yorkton_sask["Sep"] = df_yorkton_sask["Sep"].replace(-9999.9, df_yorkton_sask["Sep"].median())
df_yorkton_sask["Oct"] = df_yorkton_sask["Oct"].replace(-9999.9, df_yorkton_sask["Oct"].median())
df_yorkton_sask["Nov"] = df_yorkton_sask["Nov"].replace(-9999.9, df_yorkton_sask["Nov"].median())
df_yorkton_sask["Dec"] = df_yorkton_sask["Dec"].replace(-9999.9, df_yorkton_sask["Dec"].median())
df_yorkton_sask["Annual"] = df_yorkton_sask["Annual"].replace(-9999.9, df_yorkton_sask["Annual"].median())
df_yorkton_sask["Winter"] = df_yorkton_sask["Winter"].replace(-9999.9, df_yorkton_sask["Winter"].median())
df_yorkton_sask["Spring"] = df_yorkton_sask["Spring"].replace(-9999.9, df_yorkton_sask["Spring"].median())
df_yorkton_sask["Summer"] = df_yorkton_sask["Summer"].replace(-9999.9, df_yorkton_sask["Summer"].median())
df_yorkton_sask["Autumn"] = df_yorkton_sask["Autumn"].replace(-9999.9, df_yorkton_sask["Autumn"].median())


df_concatenated_windspeeds = pd.concat([df_abottsfordbc,
df_alert_nu,
df_armstrong_ont,
df_bagotville_queb,
df_baiecomeau_queb,
df_bakerlake_nu,
df_blueriver_bc,
df_bonavista_nfld,
df_brandon_man,
df_broadview_sask,
df_burwash_yt,
df_calgary_alber,
df_cambridgebay_nu,
df_capehooper_nu,
df_capeparry_nwt,
df_caperace_nfld,
df_cartwright_nfld,
df_castlegar_bc,
df_charlotte_town_pei,
df_churchill_man,
df_clyde_nu,
df_coldlake_alber,
df_comox_bc,
df_coralharbour_nu,
df_coronation_alber,
df_cranbrook_bc,
df_danielsharbour_nfld,
df_dauphin_man,
df_dawsoncreek_bc,
df_deaselake_bc,
df_deerlake_nfld,
df_dewarlakes_nu,
df_earlton_ont,
df_edmonton_alber,
df_edmontoncitycentre_alber,
df_edmontonnamao_alber,
df_estevan_sask,
df_estevan_sask,
df_flinflon_man,
df_fortmcmurray_alber,
df_fortnelson_bc,
df_fortsimpson_nwt,
df_fortsmith_nwt,
df_fortstjohn_bc,
df_foxfive_nu,
df_fredericton_nb,
df_ganderinternationalairport_nfld,
df_gaspe_que,
df_gillam_man,
df_goose_nfld,
df_gorebay_ont,
df_grandprairie_alber,
df_greenwood_ns,
df_halifax_ns,
df_hallbeach_nu,
df_hamilton_ont,
df_hayriver_nwt,
df_highlevel_alber,
df_hopea_bc,
df_hopedale_nfld,
df_inukjuak_queb,
df_inuvik_nwt,
df_iqualuit_nu,
df_islandlake_man,
df_jaspar_alber,
df_jeanlesageairport_queb,
df_kamloops_bc,
df_kapuskaking_ont,
df_kelowna_bc,
df_kenora_ont,
df_kingston_ont,
df_kujjuuarapik_queb,
df_langara_bc,
df_laronge_sask,
df_lethbridge_alber,
df_london_ont,
df_longstaffbluff_nu,
df_mayo_yt,
df_mcinessisland_bc,
df_medicinehat_alber,
df_miramichi_nb,
df_miscouisland_nb,
df_moncton_nb,
df_montjoli_queb,
df_montrealpet_queb,
df_moosejaw_sask,
df_mossonee_ont,
df_mouldbay_nwt,
df_muskoka_ont,
df_nanaimo_bc,
df_natashquan_queb,
df_normalwells_nwt,
df_northbattleford_sask,
df_northbay_ont,
df_ottawa_ont,
df_peaceriver_alber,
df_penticton_bc,
df_pilotmound_man,
df_portauxbasque_nfld,
df_porthardy_bc,
df_princealbert_sask,
df_princegeorge_bc,
df_princerupert_bc,
df_princeton_bc,
df_quesnel_bc,
df_reddeer_alber,
df_redlake_ont,
df_regina_sask,
df_resolutecars_nu,
df_rouyn_queb,
df_roverbal_queb,
df_sableisland_ns,
df_sachsharbour_nwt,
df_saintjohn_nb,
df_sandspit_bc,
df_saskatoondiefenbaker_sask,
df_saulstemarie_ont,
df_schefferville_queb,
df_septiles_queb,
df_shearwater_ns,
df_sherbrooke_queb,
df_siouxlookout_ont,
df_smithers_bc,
df_stephenville_nfld,
df_stjohns_nfld,
df_sudbury_ont,
df_summerside_pei,
df_swiftcurrent_sask,
df_sydney_ns,
df_terrace_bc,
df_teslin_yt,
df_thepas_man,
df_thompson_man,
df_thunderbay_ont,
df_timminsvictorpower_ont,
df_tofino_bc,
df_toronto_ont,
df_torontoisland_ont,
df_trenton_ont,
df_tuktoyaktuk_nwt,
df_valdor_queb,
df_vancouver_bc,
df_victoria_bc,
df_wabushlake_nfld,
df_watsonlake_yt,
df_westernhead_ns,
df_whitehorse_yt,
df_wiarton_ont,
df_williamslake_bc,
df_windsor_ont,
df_winnipeg_man,
df_yarmouth_ns,
df_yellowknife_nwt,
df_yorkton_sask],ignore_index=True)

print(df_concatenated_windspeeds) 

#Split the DataFrame into a Training Set and a Test Set
#Training Set has 80% of the size of the DataFrame 
#Test Set has 20% of the size of the DataFrame

train = df_concatenated_windspeeds.sample(frac=0.80, random_state = 200) #shuffle data 
test = df_concatenated_windspeeds.drop(train.index)


#Normalize Values by Calculating the Z-scores of each column in the training set

train_set_mean = train.mean()
train_set_std = train.std()
train_normalization = (train - train_set_mean)/train_set_std

test_set_mean = test.mean()
test_set_std = test.std()
test_normalization = (test - test_set_mean)/test_set_std


#Represent the data 

#Because we scalled all columns into Z scores we should change the variable names
#A resolution in Z's and 1 Z correspomds to a full standard deviation 

resolution_in_Zs = 0.3 #3/10 of a standard deviation 

#Create a bucket feature for each Season
#Create an empty list to append the bucket features to
feature_columns = []

autumn_as_a_numeric_column = tf.feature_column.numeric_column("Autumn")
autumn_boundaries = list(np.arange(int(min(train_normalization['Autumn'])),
                                    int(max(train_normalization['Autumn'])),
                                    resolution_in_Zs))
Autumn = tf.feature_column.bucketized_column(autumn_as_a_numeric_column, autumn_boundaries)

spring_as_a_numeric_column = tf.feature_column.numeric_column("Spring")
spring_boundaries = list(np.arange(int(min(train_normalization["Spring"])),
                                    int(max(train_normalization["Spring"])),
                                    resolution_in_Zs))
Spring = tf.feature_column.bucketized_column(spring_as_a_numeric_column, spring_boundaries)

winter_as_a_numeric_column = tf.feature_column.numeric_column("Winter")
winter_boundaries = list(np.arange(int(min(train_normalization["Winter"])),
                                    int(max(train_normalization["Winter"])),
                                    resolution_in_Zs))
Winter = tf.feature_column.bucketized_column(winter_as_a_numeric_column, winter_boundaries)

summer_as_a_numeric_column = tf.feature_column.numeric_column("Summer")
summer_boundaries = list(np.arange(int(min(train_normalization["Summer"])),
                                    int(max(train_normalization["Summer"])),
                                    resolution_in_Zs))
Summer = tf.feature_column.bucketized_column(summer_as_a_numeric_column, summer_boundaries)

#Create a Feature Cross for Summer, Spring, Autumn, and Winter

seasons = tf.feature_column.crossed_column([Summer,Spring,Autumn], hash_bucket_size=100)
crossed_features = tf.feature_column.indicator_column(seasons)
feature_columns.append(crossed_features)

#Convert list of feature columns into a layer that will later be fed to the model
my_feature_layer =  tf.keras.layers.DenseFeatures(feature_columns)


#Build a linear regression model as baseline 
#This is to create a deep neural network, and find a baseline loss by running 
#a simple linear regression model that uses the feature layer just created
def plot_the_loss_curve(epochs, mse):
    """ Plot a curve of loss vs. epoch."""
    
    plt.figure()
    plt.xlabel("Epoch")
    plt.ylabel("Mean Squared Error")
    
    plt.plot(epochs, mse, label ="Loss")
    plt.legend()
    plt.ylim([mse.min()*0.95, mse.max() * 1.03])
    plt.show()
    
print("Defined the plot_the_loss_curve function.")

#Define fucntions to create and train a linear regression model 

def create_model(my_learning_rate, feature_layer):
    """ Create and compile a simple linear regression model. """
    #Most simple tf.keras models are sequential()
    model = tf.keras.models.Sequential()
    
    #Add the layer containing the feature columns to the model.
    model.add(my_feature_layer)
    
    #Add one linear layer to the model to yield a simple linear regressor
    model.add(tf.keras.layers.Dense(units=1, input_shape=(1,)))
    
    #Construct the layers into a model that Tensorflow can execute
    model.compile(optimizer=tf.keras.optimizers.RMSprop(lr= my_learning_rate),
                  loss="mean_squared_error",
                  metrics=[tf.keras.metrics.MeanSquaredError()])
    return model 

def train_model(model, dataset, epochs, batch_size, label_name):
    """Feed a dataset into the model in order to train it.""" 
    #Split the dataset into features and label. 
    features = {name:np.array(value) for name, value in dataset.items()}
    label = np.array(features.pop(label_name))
    history = model.fit(x=features, y=label, batch_size=batch_size,
                        epochs=epochs, shuffle=True)
    
    #Get details that will be useful for plotting the loss curve.
    epochs = history.epoch 
    hist = pd.DataFrame(history.history)
    rmse = hist["mean_squared_error"]
    
    return epochs, rmse

print("Defined the create_model and train_model functions")


# The following variables are the hyperparameters.

learning_rate = 0.01
epochs = 20
batch_size = 100
label_name = "Winter"

#Establish the model's topography

my_model = create_model(learning_rate, my_feature_layer)

#Train the model on normalized training set.

epochs, mse = train_model(my_model, train_normalization, epochs, batch_size, label_name)
plot_the_loss_curve(epochs, mse)

test_features = {name:np.array(value) for name, value in test_normalization.items()}
test_label = np.array(test_features.pop(label_name)) #isolate the label
print("\n Evaluate the linear regression model against the test set:")
my_model.evaluate(x = test_features, y = test_label, batch_size = batch_size)

# Define a deep neural net model 

def create_model(my_learning_rate, my_feature_layer):
    """Create and compile a simple linear regression model"""
    # Most simple tf.keras models are sequential
    model = tf.keras.models.Sequential()
    
    #Add the layer containing the feature columns to the model.
    model.add(my_feature_layer)
    
    #Describe the topography of the model by calling the tf.keras.layers.Dense
    #method once for each layer. We have specified the following arguments:
    # units specifies the number of nodes in this layer
    # activation specifies the activation function (Rectified Linear Unit)
    # name is just a string that can be usedul when debugging 
    
    #Define the first hidden layer with 20 nodes
    
    model.add(tf.keras.layers.Dense(units = 20,
                                    activation = 'relu',
                                    name = "Hidden1"))
    
    #Implement Dropout Regularization between middle layers
    model.add(tf.keras.layers.Dense(units = 20,
                                activation='relu',
                                kernel_regularizer=tf.keras.regularizers.l2(l=0.08)))  
    

    model.add(tf.keras.layers.Dropout(rate=0.25))


    
    #Define the second hidden layer with 12 nodes
    
    model.add(tf.keras.layers.Dense(units = 12,
                                    activation ='relu',
                                    name = "Hidden2"))
    
    #Define the output layer
    
    model.add(tf.keras.layers.Dense(units=1,
                                    name="Output"))
    model.compile(optimizer=tf.keras.optimizers.Adam(lr=my_learning_rate),
                   loss="mean_squared_error",
                   metrics=[tf.keras.metrics.MeanSquaredError()])
    



    return model 


#Define a training function 

def train_model(model, dataset, epochs, label_name, batch_size=None):
    """Train the model by feeding it data """
    
    #Split the dataset into features and labels.
    features = {name:np.array(value) for name, value in dataset.items()}
    label = np.array(features.pop(label_name))
    history = model.fit(x=features,y=label,batch_size=batch_size,
                        epochs=epochs, shuffle=True)
    
    #The list of epochs is stored separately from the rest of history 
    epochs = history.epoch 
    
    #To track the progression of training, gather a snapshot
    #of the model's mean squared error at each epoch
    
    hist = pd.DataFrame(history.history)
    mse = hist["mean_squared_error"]
    
    return epochs, mse

# Call the functions to build and traina deep neural net

# The following variables are the hyperparameters

learning_rate = 0.01
epochs = 20
batch_size = 1000

# Specify the label

label_name = "Winter"

#Establish the model's topography

my_model = create_model(learning_rate, my_feature_layer)

# Train the model on the normalized training set. We're passing the entire
# normalized training set, but the model wull only use the features 
# defined by the feature_layer

epochs, mse = train_model(my_model, train_normalization, epochs, label_name, batch_size)

plot_the_loss_curve(epochs, mse)

# After building a model against the training set, test that model
# against the test set 

test_features = {name:np.array(value) for name, value in test_normalization.items()}
test_label = np.array(test_features.pop(label_name)) # isolate the label
print("\n Evaluate the new model against the test set:")
my_model.evaluate(x = test_features, y = test_label, batch_size=batch_size)




























































   














  















