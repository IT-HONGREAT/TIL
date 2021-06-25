def export_data(self):
    with open('phone_info.txt','w',encoding='utf-8') as f:

        f.write(f'user={self.user}\n')
        f.write(f'number={self.number}\n')
        f.write(f'company={self.company}\n')
        f.write(f'model={self.model}\n')
        f.write(f'os={self.os}\n')

def import_data(self,path):

    data = {}
    with open(path,'r',encoding='utf-8') as f:
        for line in f.readlines():
            key,value = tuple(line.split('='))
            data[key] = value.replace('\n','')


    self.user = data['user']
    self.number = data['number']
    self.company = data['company']
    self.model = data['model']
    self.os = data['model']


