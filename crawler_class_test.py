from crawler_class import CafeCrawler

crawler = CafeCrawler(file='html_source.txt')
print(crawler.generate_dataframe())