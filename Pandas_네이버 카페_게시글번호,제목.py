import pandas as pd

with open('html_source.txt',encoding='utf-8') as f:
    temp = f.read()
# 게시글 번호
splitted = temp.split('<div class="inner_number">')
splitted.pop(0)

number=[]

for i in splitted:
    number.append(i.split('</div>')[0])

pd_arr = pd.Series(number)


#게시글 제목
splitted_2 = temp.split('<a class="article"')
splitted_2.pop(0)
title = []

for i in splitted_2:
    title.append(i.split('</a>')[0].split('>')[-1]
               .replace(" ","")
               .replace("\n","")
               .strip())

pd_arr2 = pd.Series(title)

data = pd.DataFrame(number,title)
print(data)

