from random import randint
from threading import Thread
from time import time, sleep

def download(filename):
    print('開始下載 %s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s 下載完成! 耗費了 %d 秒' % (filename, time_to_download))
    
def main():
    start = time()
    # 使用 threading 模組的 Thread 類別來創建線程 (thread) 
    t1 = Thread (target = download, args =('Python.pdf',))
    t1.start()
    t2 = Thread (target = download, args =('Hot.avi',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('總共耗費了 %.3f 秒.' % (end - start))

if __name__ == '__main__':
    main()
    
