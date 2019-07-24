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

首先我想先看评论数排名前30的是哪些电影，所以我通过柱状图来描绘这一事实：  

![评论数前30的电影](https://github.com/Grokli/douban_movies_analysis/blob/master/pictures/comments.png)