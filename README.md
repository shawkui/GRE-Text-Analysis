# Simple Text Analysis on GRE Text

此项目是我在准备GRE的时候打发时间搞的，数据是网上的一些备考资料上整理来的。

环境：Python 3.6， nltk，wordcloud，matplotlib

基本功能：

* 数据处理：对GRE题目文本去除标点符号，去除题号，选项符号，下划线等无关文本；

* 单词b变体还原，把一些单词的变形还原回动词形式（可选）；

* 词汇表收集：生产文本中的单词表；

* 单词计数和排序，简单的统计单词出现的频率并生产词频图（如下）；

  ![freqcurve](https://github.com/shawkui/GRE-Text-Analysis/blob/master/data/freqcurve.png)

* 生成常出现的词语搭配（如下）；

* 数据对象保存（json格式和txt格式）；

* 根据词频生成词云。![wordcloud](https://github.com/shawkui/GRE-Text-Analysis/blob/master/data/wordcloud.png)

数据：[阅读](https://drive.google.com/open?id=1qss2obMc-EK9uAi2xb0sULgLBJi6_HHk),[填空](https://drive.google.com/open?id=1yW1iOvbEWsi0QXEMLvm9LXZsxOmpqwDK)
