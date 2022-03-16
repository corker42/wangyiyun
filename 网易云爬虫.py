# 接口： http://music.163.com/api/v1/resource/comments/R_SO_4_{歌曲id}?limit=100&offset={页码}

import requests
import jieba
from wordcloud import WordCloud

def getHTML(url):
    headers = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    }
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    # print(r.json(),type(r.json()))
    return r.json()['comments']

if __name__ == '__main__':
    urls = [f'http://music.163.com/api/v1/resource/comments/R_SO_4_1358935915?limit=100&offset={i}' for i in range(1, 104)]
    for url in urls:
        comments = getHTML(url)
        for i in comments:
            content = i['content'] + '\n'
            # print(content)
            with open('contents1.txt', 'a+', encoding='utf8') as file:
                file.write(content)
    txt = ''
    with open('contents1.txt', 'r', encoding='utf8') as file:
        for f in file:
            f.replace('\n', '')
            txt = txt + f
    print(txt)
    words = jieba.lcut(txt)  # 精确分词
    newtxt = ''.join(words)  # 空格拼接
    wordcloud = WordCloud(
        scale=4,
        font_path="C:\Windows\Fonts\STXINGKA.TTF",
        background_color='black'
    ).generate(newtxt)
    wordcloud.to_file('春风十里 (Live).jpg')

