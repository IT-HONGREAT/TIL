from Pandas_crawler_class import CafeCrawler

crawler = CafeCrawler(file='html_source.txt')
print(crawler.generate_dataframe())

print(crawler.filter_view(30, high = 40))

print(crawler.filter_date('2021.06.14', high='2021.06.17'))