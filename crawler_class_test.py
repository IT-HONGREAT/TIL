from crawler_class import CafeCrawler

crawler = CafeCrawler(file='html_source.txt')
print(crawler.generate_dataframe())

print(crawler.filter_view(30, high = 40))

print(crawler.filter_date(20210614, high=20210617))