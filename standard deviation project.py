from collections import Counter
import pandas as pd
import plotly.express as px
import csv
import math

with open ("data.csv",newline="")as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
data=[]

for i in range(len(filedata)):
    num=filedata[i][1]
    data.append(float(num))

n=len(data)


   
total=0

for i in data:
    total=total+i

mean=total/n
print(mean)


df=pd.read_csv("data.csv")
print(df)
fig=px.scatter(df,x="Index", y="Height", title="Height Data")
fig.update_layout(shapes=[dict(type="line",y0=mean,y1=mean,x0=0,x1=n)])
fig.show()

SDlist=[]

for i in data:
    i=i-mean
    SDlist.append(i)


squarelist=[]

for i in SDlist:
    i=i**2
    squarelist.append(i)


sum=0
for i in squarelist:
    sum=sum+i

print(sum)

result=sum/len(data)-1

print(result)

sd=math.sqrt(result)
print(sd)

