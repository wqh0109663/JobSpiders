import pymysql
import jieba
import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='Wuqihuan19950903', db='jobspider',
                     charset='utf8')
cursor = db.cursor()
cursor.execute("select * from job_ai limit 10000")
results = cursor.fetchall()
f = open("job_ai.txt", "a+")
for item in results:
    f.writelines(item[10])

# 将指针移到开头
f.seek(0)
seg_list = jieba.cut(f.read(), cut_all=False)
counter = dict()
for seg in seg_list:
    counter[seg] = counter.get(seg, 1) + 1
counter_sort = sorted(counter.items(), key=lambda value: value[1], reverse=True)
c = open("jobai.csv", "w+")
writer = csv.writer(c)
writer.writerows(counter_sort)
c.seek(0)
reader_csv = csv.reader(c)
counter1 = {}
for row in reader_csv:
    counter1[row[0]] = counter1.get(row[0], int(row[1]))
wc = WordCloud(font_path="msyh.ttf", max_words=100, height=600, width=1200).generate_from_frequencies(counter1)
plt.axis("off")
plt.imshow(wc)
wc.to_file("image.png")
c.close()
f.close()
cursor.close()
db.close()
