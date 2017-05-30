import webbrowser as wb
import time
totle_break = 3
break_count = 0
while (break_count < totle_break):
    time.sleep(5)
    wb.open('http://www.baidu.com')
    break_count = break_count + 1