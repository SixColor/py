import  requests,json
from pyquery import PyQuery as pq
import  urllib.request

def rq():
    url="https://www.zhihu.com/question/21766551"
    text =requests.get(url,headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0' }).text
    print(text)
    pyquery =pq(text)
    imgs =pyquery.find("img")
    print(imgs.length)

    for index in range(imgs.length):
        io(imgs.eq(index).attr("src"), "text")


def io(content, type):
    if type == "img":
        f = open("zhihu_photoes.txt", 'a', encoding='utf-8')
        content += '\n'
        data = f.write(content)
        print(content)
    else:
        f = open("zhihu_photoes_1.txt", 'a', encoding='utf-8')
        print(content)
        downLoadPic(content)
        content += '\n--------------------------------------------------\n\n'
        data = f.write(content)


count =1;
def downLoadPic(picUrl):
    global count
    if picUrl.startswith('http'):
        response = urllib.request.urlopen(picUrl)
        cat_img = response.read()
        with open('LittleSister\pic'+str(count)+'.jpg', 'wb') as f:
            f.write(cat_img)
        count +=1
    else:
        return
rq()