import csv
import math
#Please download key ratios csv from morningstar.in and give its name below
f = open('HAVELLS Key Ratios.csv')
reader = csv.reader(f)
mylist = list(reader)
f.close()
#print(mylist[5])
#a=1
#b=2
#c=3
#d=4
#mylist[5]=[a,b,c,d]
#x=mylist[5][1]
#mylist[5][1] = 5
#print(mylist[5])
#################################################################################################################################
import urllib.request
from bs4 import BeautifulSoup as BS
#Change this URL for each company
req = urllib.request.Request('https://in.investing.com/equities/havells-india', headers={'User-Agent': 'Mozilla/5.0'}) #VERY IMP
html = urllib.request.urlopen(req).read()
soup = BS(html, "html.parser")


def convfloat(var,dum):
    print(var)
    if(var==dum or var=="-"):
        var=float(0.0)
    else:
        n=len(var)
        rstr=""
        for ctr in range(0,n):
            print(ctr)
            if(var[ctr]!=','):
                rstr=rstr+var[ctr]
        var=float(rstr)
    return(var)


#to get last trade price
ltp1=soup.find(class_="newInput inputTextBox alertValue")
ltp = ltp1['value']
a=''
ltp=convfloat(ltp,a)
print (float(ltp))



#to get name
scrip=soup.find(class_="float_lang_base_1 relativeAttr").get_text()
print (scrip)

financials= soup.find_all(id="pairSublinksLevel1")
req=financials[0]
#print(req)

#to get industry
industry=soup.find(class_="companyProfileHeader").get_text()
print (industry)

#to get market cap
mcap=soup.find_all(class_="float_lang_base_2 bold")
marketcap=(mcap[7]).get_text()
print (marketcap)


urls=[]
for link in req.findAll('a'):
    links=link.get('href')
    links="https://in.investing.com"+links
    urls.append(str(links))

#print(urls[8])

balancesheet=urls[9]
ratios=urls[10]

print(balancesheet)

#Enter balance sheet
req = urllib.request.Request(balancesheet, headers={'User-Agent': 'Mozilla/5.0'}) #VERY IMP
html = urllib.request.urlopen(req).read()
soup = BS(html, "html.parser")

#to parse Total Current assets
balsh= soup.find_all(id="parentTr")
req=balsh[0]
print(balsh[0])
#to parse Total Current assets
ca=[]
for record in req.findAll('td'):
    ca.append(str(record.text))
currentassets=ca[2]
currentassets=convfloat(currentassets,a)/10
print(currentassets)

req=balsh[1]
#to parse Total Total Assets
ta=[]
for record in req.findAll('td'):
    ta.append(str(record.text))
totalassets=ta[2]
totalassets=convfloat(totalassets,a)/10
print(totalassets)

req=balsh[2]
#to parse Current Liabilities
cl=[]
for record in req.findAll('td'):
    cl.append(str(record.text))
currentliabilities=cl[2]
currentliabilities=convfloat(currentliabilities,a)/10
print(currentliabilities)

req=balsh[3]
#to parse Total Liabilities
tl=[]
for record in req.findAll('td'):
    tl.append(str(record.text))
totalliabilities=tl[2]
if totalliabilities== "-":
    totalliabilities="0"
totalliabilities=float(totalliabilities)/10
print(totalliabilities)

req=balsh[4]
#to parse Total Equity
te=[]
for record in req.findAll('td'):
    te.append(str(record.text))
totalequity=te[2]
if totalequity== "-":
    totalequity="0"
totalequity=float(totalequity)/10
print(totalequity)

#to parse goodwill
balsh= soup.find_all(class_="child")
req=balsh[12]
gw=[]
for record in req.findAll('td'):
    gw.append(str(record.text))
goodwill=gw[2]
if goodwill== "-":
    goodwill="0"
goodwill=float(goodwill)/10
print(goodwill)

#to parse intangibles
req=balsh[13]
inta=[]
for record in req.findAll('td'):
    inta.append(str(record.text))
intangibles=inta[2]
if intangibles== "-":
    intangibles="0"
intangibles=float(intangibles)/10
print(intangibles)

#print(balsh[12])
#value1= soup.find_all('span')
#print(value1)
#a=value1[0].index("Total Common Shares Outstanding")
print(mylist)

#a is dummy variable
a=mylist[2][0]

#function to convert variables to float
def convfloat(var,dum):
    print(var)
    if(var==dum or var=="-"):
        var=float(0.0)
    else:
        n=len(var)
        rstr=""
        for ctr in range(0,n):
            print(ctr)
            if(var[ctr]!=','):
                rstr=rstr+var[ctr]
        var=float(rstr)
    return(var)


nshares=(convfloat(mylist[11][10],a))/10
#print(nshares)

eps=float(mylist[8][10])
#print(eps)

pe=ltp/eps
cacl=currentassets/currentliabilities
ca=1.1*currentassets
nta=totalassets-goodwill-intangibles
ntas=nta/nshares
pnta=ltp/ntas


ltde=convfloat(mylist[99][10],a)



roe1=convfloat(mylist[38][6],a)
roe2=convfloat(mylist[38][7],a)
roe3=convfloat(mylist[38][8],a)
roe4=convfloat(mylist[38][9],a)
roe5=convfloat(mylist[38][10],a)
roe5ya=(roe1+roe2+roe3+roe4+roe5)/5
ni5y=convfloat(mylist[56][10],a)
rg10y=convfloat(mylist[47][10],a)
eps10y=convfloat(mylist[62][10],a)
print(mylist[9][0])
print(mylist[12][0])
d8=convfloat(mylist[9][1],a)
d9=convfloat(mylist[9][2],a)
d10=convfloat(mylist[9][3],a)
d11=convfloat(mylist[9][4],a)
d12=convfloat(mylist[9][5],a)
d13=convfloat(mylist[9][6],a)
d14=convfloat(mylist[9][7],a)
d15=convfloat(mylist[9][8],a)
d16=convfloat(mylist[9][9],a)
d17=convfloat(mylist[9][10],a)
b8=convfloat(mylist[12][1],a)
b9=convfloat(mylist[12][2],a)
b10=convfloat(mylist[12][3],a)
b11=convfloat(mylist[12][4],a)
b12=convfloat(mylist[12][5],a)
b13=convfloat(mylist[12][6],a)
b14=convfloat(mylist[12][7],a)
b15=convfloat(mylist[12][8],a)
b16=convfloat(mylist[12][9],a)
b17=convfloat(mylist[12][10],a)
if(b17<1 or b8<1):
    bvchange="NA"
else:
    bvchange=((math.pow((b17/b8),0.1))-1)*100

###########################################################################################################

####################################################################################################################
print(nshares)
nlist=[[scrip,industry,nshares,marketcap,ltp,eps,pe,totalassets,currentassets,currentliabilities,cacl,totalliabilities,ca,goodwill,intangibles,nta,ntas,pnta,ltde,roe1,roe2,roe3,roe4,roe5,roe5ya,ni5y,rg10y,eps10y,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,bvchange]]
print(nlist)
#all data will be put into this csv file. This file is overwritten every time you run the code.
my_new_list = open('stock.csv', 'w', newline = '')
csv_writer = csv.writer(my_new_list)
csv_writer.writerows(nlist)
my_new_list.close()