# 基于Scrapy框架的Python3就业信息Jobspiders爬虫
* Items.py : 定义爬取的数据
* pipelines.py : 管道文件，异步存储爬取的数据
* spiders文件夹 : 爬虫程序
* settings.py : Srapy设定，请参考 [官方文档](https://scrapy-chs.readthedocs.io/zh_CN/latest/topics/settings.html#topics-settings-ref)
* scrapy spider
* 爬取三大知名网站,使用三种技术手段
* 第一种直接从网页中获取数据，采用的是scrapy的基础爬虫模块，爬的是**51job**
* 第二种采用扒接口,从接口中获取数据，爬的是**智联招聘**
* 第三种采用的是整站的爬取,爬的是**拉钩网**
* 获取想要的数据并将数据存入mysql数据库中，方便以后的就业趋势分析
## 实现功能：
* 从三大知名网站上爬取就业信息，爬取**发布工作的日期**，**薪资**，**城市**，**岗位有那些福利**，**要求**，**分类**等等，并将爬到的数据存到**mysql数据库中**
##  使用教程：
####  运行前需要安装的环境
* Python3
* mysql
* 安装好scrapy框架
* (安装虚拟环境和虚拟环境的wrapper)
* 其次就是安装一些模块,如果没有安装虚拟环境可以在pycharm中进行安装，alt+enter选择，如果没有正确的模块，就在setting中的project中的解释器Interpreter，再点击+号在里面搜索
####  运行项目
* git clone https://github.com/wqh0109663/JobSpiders.git
* 把下好的项目在pycharm中打开
* 运行main文件，打开注释内容，运行需要的spider即可
* 或者直接在命令行中运行scrapy runspider XX某某spider

##  下面是一条爬到的数据

![](https://github.com/wqh0109663/JobSpiders/raw/master/JobSpiders/images/java.png)   

##  下面是博客地址
* 里面包含一些简要的说明
* [博客戳这里](https://blog.csdn.net/qq_36992605/article/details/81382110)


* 分析未完待续...  
