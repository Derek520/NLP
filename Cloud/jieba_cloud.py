import jieba
import jieba.analyse
from matplotlib import pyplot as plt
from scipy.misc import imread
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator

# 1.读取数据
with open("news.txt","r") as f:
    text = f.read()

# 2.基于 TextRank 算法的关键词抽取,top50
keywords = jieba.analyse.textrank(text, topK=50, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
file = ",".join(keywords)

# 指定中文字体，不然中文显示框框
font = r'./font/simhei.ttf'
print(file)
# 指定背景图,随意
image = imread('i.png')

wc = WordCloud(
    font_path=font,
    background_color='white',#背景色
    mask=image,#背景图
    stopwords=STOPWORDS,#设置停用词
    max_words=100,#设置最大文字数
    max_font_size=100,#设置最大字体
    width=800,
    height=1000,

)

#生成词云
image_colors = ImageColorGenerator(image)
wc.generate(file)

# 使用matplotlib,显示词云图
plt.imshow(wc)  #显示词云图
plt.axis('off') #关闭坐标轴
plt.show()

# 保存图片
wc.to_file('news.png')

