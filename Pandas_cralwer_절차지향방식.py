import pandas as pd

with open('html_source.txt',encoding='utf-8') as f:
    temp = f.read()

#게시글 번호
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

#작성자

splitted_4 = temp.split('<div class="pers_nick_area">')

splitted_4.pop(0)
nickname_list = []
for i in splitted_4:
    nickname_list.append(i.split(',')[3])
nickname_list.pop(0)

#조회수

splitted_5 = temp.split('<td class="td_view">')
splitted_5.pop(0)
view_list = []

for i in splitted_5:
    view_list.append(i.split('</td')[0])
view_list.pop(0)

#좋아요

splitted_6 = temp.split('<td class="td_likes">')
splitted_6.pop(0)
like_list = []

for i in splitted_6:
    like_list.append(i.split('</td>')[0])
like_list.pop(0)

#_set_index()
dict_data = {'글번호': number_list,
             '제목': title_list,
             '날짜':date_list,
             "작성자":nickname_list,
             '조회수': view_list,
             '좋아요': like_list}

data = pd.DataFrame(dict_data)
num_df = data.set_index('글번호')


print(data)