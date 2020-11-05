import time

for i in range(0, 101, 2):
  time.sleep(0.1)
  num = i // 2
  if i == 100:
    # 字符串格式化
    # %3s——右对齐，占位符3位  %有特殊含义：想要打印%，使用%%表示
    # %-50s——左对齐，占位符50位
    # \r 回车  \n 换行
    process = "\r[%3s%%]: |%-50s|\n" % (i, '|' * num)
  else:
    process = "\r[%3s%%]: |%-50s|" % (i, '|' * num)
  print(process, end='', flush=True)