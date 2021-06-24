import pandas as pd


class CafeCrawler:

    def __init__(self, file):
        f = open(file, 'r', encoding='UTF-8')
        self.source = f.read()
        self.df = pd.DataFrame()

    def generate_dataframe(self):

        self._split_number()
        self._split_title()
        self._split_date()
        self._split_nickname()
        self._split_view()
        self._split_like()

        self.df.set_index('글번호', inplace=True)

        return self.df

    def _split_number(self):
        # open => read 한 temp를 함수처리.....

        splitted = self.source.split('<div class="inner_number">')
        splitted.pop(0)

        number_list = []

        for i in splitted:
            number_list.append(i.split('</div>')[0])

        self.df['글번호'] = number_list

    def _split_title(self):

        splitted_2 = self.source.split('<a class="article"')

        splitted_2.pop(0)
        title_list = []

        for i in splitted_2:
            title_list.append(i.split('</a>')[0].split('>')[-1]
                              .replace("\t", "")
                              .replace("\n", "")
                              .strip())

        self.df['제목'] = title_list

    def _split_date(self):

        splitted_3 = self.source.split('<td class="td_date">')

        splitted_3.pop(0)
        date_list = []

        for i in splitted_3:
            date_list.append(i.split('</td')[0])

        date_list.pop(0)  # 날짜를 모은 리스트를 pop시킴

        self.df['날짜'] = date_list

    def _split_nickname(self):

        splitted_4 = self.source.split('<div class="pers_nick_area">')

        splitted_4.pop(0)
        nickname_list = []
        for i in splitted_4:
            nickname_list.append(i.split(',')[3])
        nickname_list.pop(0)

        self.df['작성자'] = nickname_list

    def _split_view(self):

        splitted_5 = self.source.split('<td class="td_view">')
        # splitted_5 = splitted_5[2:]
        splitted_5.pop(0)
        splitted_5.pop(0)

        view_list = []

        for i in splitted_5:
            # print(type(i.split('</td')[0]))
            # print(i.split('</td')[0])
            view_list.append(int(i.split('</td')[0]))

        self.df['조회수'] = view_list

    def _split_like(self):

        splitted_6 = self.source.split('<td class="td_likes">')
        splitted_6.pop(0)
        like_list = []

        for i in splitted_6:
            like_list.append(i.split('</td>')[0])
        like_list.pop(0)

        self.df['좋아요'] = like_list

    def filter_view(self, low, **kwargs):

        if not kwargs.get('high'):
            return self.df[self.df['조회수'] >= low]

        else:
            return self.df[(self.df['조회수'] < kwargs['high']) & (self.df['조회수'] >= low)]




