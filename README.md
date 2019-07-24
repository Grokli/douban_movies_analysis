# 豆瓣电影可视化分析
## 项目简介
通过scrapy爬虫爬取豆瓣电影限定在2019年的电影，根据爬取的数据进行可视化数据分析。
## 代码执行顺序
1.`main.py`运行爬虫程序，爬取的数据存放在`movies.csv`  
2.`analyse_movies.ipython`运行可视化分析程序，主要是通过matplotlib库进行绘图，得到的图片存放在`pictures`文件夹中。
## 分析思路
爬虫部分就不做介绍了，主要分析一下绘图的过程。 
首先看一下`movies.csv`文件中的数据格式：  

| comments | during_time | language | location | rate | star | title | types |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |  
| 4497 | 117 | 日语 | 日本 | 7.8 | 40 | 命运之夜——天之杯II ：迷失之蝶 | "剧情,动画,奇幻" |

1.首先我想先看评论数排名前30的是哪些电影，所以我通过柱状图来描绘这一事实：  
![评论数前30的电影](https://github.com/Grokli/douban_movies_analysis/blob/master/pictures/comments.png)  
令我没有想到的是《流浪地球》排名第一远远超过第二名《复仇者联盟4：终局之战》......看来大家还是很支持国产电影的哈。  

2.我还想看看所有这些电影的时长分布是怎样的，得到的直方图如下所示：  
![电影时长分布](https://github.com/Grokli/douban_movies_analysis/blob/master/pictures/during_time.png)  
大部分电影都在100分钟左右，和我所料不差。  

3.再来看一看这些电影的星级分布，用小提琴图比较适合分析这种情况，小提琴图跟箱线图差不多，只不过小提琴图在箱线图的基础上增加了每个值的分布情况，可以直观的看到哪个值比较多，哪个值比较少。  
![电影星级指数分布](https://github.com/Grokli/douban_movies_analysis/blob/master/pictures/star.png)  
可以看到，3星和3.5星的电影占了绝大多数，果然正态分布在哪都适用，极好和极差的电影都占少数，绝大多数都是比较一般的电影。  

4.最后看一看各国电影的平均评价指数排名，还是用直方图来分析：  
![各国电影的平均评价指数排名](https://github.com/Grokli/douban_movies_analysis/blob/master/pictures/location_VS_rate.png)  
排名第一的是哥伦比亚的电影，平均评价指数是8点多，当然这和参与平均的电影数量有关，不一定准确。中国的电影排在了倒数第六位......平均评价指数是5.6左右。参与排名的还有台湾，香港，没有把它们合并到中国是因为我偷懒没多做处理，这可不是因为我政治不正确啊，我可是爱党爱国的好青年。  
***
关于这些图的绘图过程都在`analyse_movies.ipython`这个文件里了，略显青涩的画图手法，但是这算是我个人一次不错的尝试了。