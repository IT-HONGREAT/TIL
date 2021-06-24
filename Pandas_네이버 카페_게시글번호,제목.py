import pandas as pd

with open('html_source.txt',encoding='utf-8') as f:
    temp = f.read()
# 게시글 번호
splitted = temp.split('<div class="inner_number">')
splitted.pop(0)

number_list=[]

for i in splitted:
    number_list.append(i.split('</div>')[0])

pd_arr = pd.Series(number_list)


#게시글 제목
splitted_2 = temp.split('<a class="article"')

splitted_2.pop(0)
title_list = []

for i in splitted_2:
    title_list.append(i.split('</a>')[0].split('>')[-1]
               .replace("\t","")
               .replace("\n","")
               .strip())

pd_arr2 = pd.Series(title_list)

#날짜

splitted_3 = temp.split('<td class="td_date">')

splitted_3.pop(0)
date_list = []

for i in splitted_3:
    date_list.append(i.split('</td')[0])

pd_arr3 = pd.Series(date_list)

date_list.pop(0)  #날짜를 모은 리스트를 pop시킴



# 글번호를 리스트로 그냥 받고, 인덱스로 지정해서 데이터프레임화시킴.
dict_data = {'제목': title_list,'날짜':date_list}

data = pd.DataFrame(dict_data, index=number_list)


print(data)