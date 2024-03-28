import requests
import sqlite3
import pandas  as pd
from bs4 import BeautifulSoup

# Initialization of known entities
url='https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name="movies.db"
table_name ="/Webscraping/top_movies"
df=pd.DataFrame(columns=["Average rank","Film","Year"])
count =0
html_page = requests.get(url).text
data =BeautifulSoup(html_page,"html.parser")

tables=data.find_all('tbody')
rows=tables[0].find_all("tr")

for row in rows:
    if count <50:
        col=row.find_all("td")
        if len(col)!=0:
            data_dict ={"average Rank":col[0].contents[0],
                        "film":col[1].contents[0],
                        "Year":col[1].contents[0] }
            df1 =pd.DataFrame(data_dict,index=[0])
            df =pd.DataFrame([df,df1],ignore_index=True)
            count+=1
    else:
        break

print(df)

df.to_csv(csv_path)
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()