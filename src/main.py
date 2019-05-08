from data_process import GREText

# 导入数据
data_path=r'../data/rawdata_reading.txt'
txt=GREText(data_path)

#输出排序后的单词
print(txt.sort_word())
#查找单词出现频率
print(txt.lookup('success'))
#保存数据
txt.save_json('../data/test.json')
txt.save_txt('../data/test.txt')
#常用搭配
print(txt.text.collocations())
#输出单词表
print(txt.get_word())
#词频图
#txt.plot_freq(30)
#词云
txt.word_cloud()
