from newspaper import Article
url = 'https://freemeteo.vn/thoi-tiet/ho-chi-minh-city/history/daily-history/?gid=1566083&station=11437&date=2021-03-15&language=vietnamese&country=vietnam&fbclid=IwAR2XzksNDNghsZmI76WV74PfD1Xa3perS3I3SsCexqMX7vkRYqWtLVbPRYM'
article = Article(url)
article.download()
article.parse()
# Xong rồi đấy, giờ lấy data thôi
print(article.title)