from tabula import read_pdf
import pandas as pd
import numpy

df = read_pdf("input.pdf", pages='all')
df = numpy.array(df)
for i in range(len(df)):
    df[i] = numpy.array(df[i])

arr = []
ans = []
c = 0

for i in range(474):
    if(len(df[i][0]) != 11 and len(df[i][0]) != 1):
        arr.append(df[i])

for i in range(len(arr)):
    if(arr[i][0][2][3:7] == '2080'):
        ans.append(arr[i])
        c = c + 1

f = 'output.csv'

for i in range(len(ans)):
        d = pd.DataFrame(ans[i])
        d.to_csv(f,mode='a',index=False)  
