import re
import urllib.request


def craw(url, page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pat1 = '<div id="plist".+? <div class="page clearfix">'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]
    pat2 = '<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
    # 前10个物品的源代码为 <img width="220" height="220" data-img="1" src="//img10.360buyimg.com/n7/jfs/t4366/71/2045605853/291379/56c87b03/58ca4dc5N1c303706.jpg">
    # 若用此代码只能爬取前10图片
    # 后 <img width="220" height="220" data-img="1" data-lazy-img="//img12.360buyimg.com/n7/jfs/t5701/106/4395600572/382203/446c260f/594cc3f6Nacc00c48.jpg">
    imagelist = re.compile(pat2).findall(result1)
    x = 1
    for imageurl in imagelist:
        imagename = "F:/CrawlerData/JD/" + str(page) + '-' + str(x) + ".jpg"
        imageurl = "http://" + imageurl
        try:
            urllib.request.urlretrieve(imageurl, filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                x += 1
            if hasattr(e, "reason"):
                x += 1
        x += 1


for i in range(1, 2):
    url = "http://list.jd.com/list.html?cat=9987,653,655&page=" + str(i) + "&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main"
    craw(url, i)
