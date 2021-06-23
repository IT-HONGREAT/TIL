import pandas as pd
with open('html_source.txt','r', encoding='utf-8') as f:
    temp = f.read()
splited = temp.split('<div class="inner_number">')
splited.pop(0)
arr = []
for split in splited:
    arr.append(split.split('</div>')[0])
pd_arr = pd.Series(arr)
print(pd_arr)