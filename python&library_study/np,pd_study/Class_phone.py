class Phone:   #일반전화기를 표현한 클래스

    def __init__(self,**kwargs):
        self.number = kwargs['number']
        self.user = kwargs['user']
        self.company = kwargs['company']
        self.model = kwargs['model']

    def on(self):
        print(f"안녕하세요{self.user}! 번호는{self.number}이고, 저희는{self.company}입니다")

class Smartphone(Phone):   #스마트폰 클래스

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.os = kwargs['os']
        print(f"we are {self.os}")

    def on(self):     #os와 lte내용 추가
        print("전원을 켭니다!")
        print(f"안녕하세요{self.user}! 번호는{self.number}이고, 저희는{self.company}입니다.\nwelcome {self.os} world!!")
        print("lte 접속합니다")


    def export_data(self):     #위의 클래스들의 주요 정보들을 텍스트파일에 쓰는기능,즉 내보내는 기능
        with open('phone_info.txt','w',encoding='utf-8') as f:

            f.write(f'user={self.user}\n')
            f.write(f'number={self.number}\n')
            f.write(f'company={self.company}\n')
            f.write(f'model={self.model}\n')
            f.write(f'os={self.os}\n')

    def import_data(self,path):    #텍스트 파일을 가져와서 읽는 기능

        data = {}
        with open(path,'r',encoding='utf-8') as f:
            for line in f.readlines():
                key,value = tuple(line.split('='))
                data[key] = value.replace('\n','')


        self.user = data['user']
        self.number = data['number']
        self.company = data['company']
        self.model = data['model']
        self.os = data['os']


a = Smartphone(number='01094802331',user='인영',company='kt',os='Android',model='galaxy8+')

a.export_data()
a.import_data('phone_info.txt')
a.on()