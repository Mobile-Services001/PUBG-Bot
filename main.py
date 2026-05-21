import subprocess
import threading
import time

def run_bot1():
    subprocess.run(["python", "bottt.py"])

def run_bot2():
    subprocess.run(["python", "my_bot.py"])

# Bot နှစ်ခုလုံးကို အပြိုင် Run မယ်
t1 = threading.Thread(target=run_bot1)
t2 = threading.Thread(target=run_bot2)

t1.start()
t2.start()

# Main process မပိတ်သွားအောင် စောင့်ပေးထားမယ်
t1.join()
t2.join()
