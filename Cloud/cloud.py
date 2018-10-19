import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from scipy.misc import imread



# 词云，会自动统计每个词出现的频次，出现越多，显示越大,以空格和标点符号进行分割统计
with open('zhihu.csv','r') as f:
    string = f.read()

# 指定中文字体，不然中文显示框框
font = r'./font/simhei.ttf'
# backgroud_Image = plt.imread('./i.png')
# 结巴分词
cut_text =' '.join(jieba.lcut(string))
# 加载指定的图片
image = imread('i.png')
# 词云参数设置
wc = WordCloud(font_path=font,  #如果是中文必须要添加这个，否则会显示成框框
               mode='RGBA',  # 设置透明底色
               background_color="white",  #设置背景颜色
               mask=image,  #设置背景图片
               max_words=2000,  #设置最大文字数
               stopwords=STOPWORDS,  #设置停用词
               max_font_size=50,  # 设置字体最大值
               width=800, #图宽
               height=1000,#图高
               )
#生成词云
image_colors = ImageColorGenerator(image)# 基于背景颜色设置字体色彩
wc.generate(cut_text)#根据文本生成词云

#显示
plt.imshow(wc)#显示词云图
plt.axis("off")#关闭坐标轴
plt.show()#显示窗口
wc.to_file('test.png')# 保存图片

