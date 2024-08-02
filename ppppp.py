from datetime import timedelta,datetime
import pyautogui as pg
import time as t

start_date_str = input('Enter the start date in the format YYYY-DD-MM: ')
start_date = datetime.strptime(start_date_str, "%Y-%d-%m")
today = datetime.today()
date_list = []
count = 0
while start_date <= today:
    date_list.append(start_date.strftime("%Y-%m-%d"))
    count += 1
    filename = f"{count}.py"
    with open(filename, "w") as f:
        f.close()
    pg.click(863, 590)
    t.sleep(1)
    # pg.typewrite("git init")
    pg.typewrite ('git add' f' "{count}.py"') 
    pg.press('enter')
    t.sleep(1) 
    pg.typewrite ('git commit --date ' f'"{start_date}" -m " ir" ')
    pg.press('enter')
    t.sleep(6)
    pg.typewrite ('git push')
    pg.press('enter')
    t.sleep(10)
    start_date += timedelta(days=1)
