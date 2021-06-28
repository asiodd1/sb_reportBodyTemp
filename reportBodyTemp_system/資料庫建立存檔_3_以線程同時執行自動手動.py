'''
try:
    fh = open("testfile", "w+",encoding='UTF-8')
    venlst={'信本':{'江振廷':'h0289550','張佑宇':'U9168010'}}
    fh.write(str(venlst))
except IOError:
    print ("Error: 没有找到文件或读取文件失败")
else:
    print( "内容写入文件成功")
    fh.close()
'''
import json
import time
import tkinter as tk
from selenium import webdriver
from random import randint
from threading import Thread

#venlst = {'信本':{},'模板':{},'芳達':{},'鋼筋':{},'正鋼':{},'旺宏':{}}

#venlstemp={'張佑宇':[],'鍾欣原':[]}




#label_time= tk.Label(window,textvariable = time.ctime(), bg= 'white',width=30)
#label_time.pack()


def autoreport():
    browser2=webdriver.Chrome(r'C:\chromedriver')
    while True:

        wday=(time.localtime(time.time())).tm_wday
        hr=(time.localtime(time.time())).tm_hour
        mn=(time.localtime(time.time())).tm_min
        wset={0,1,2,3,4}
        
        if wday in wset and hr==7 and mn==30:
            
            fh2 = open('venlstemp', 'r+', encoding='UTF-8')
            data2 = fh2.readlines()
            fh2.close()
            venlst_str2 = data2[0]
            venlst2 = json.loads(venlst_str2)

            emploIDlst=[]
            for i in venlst2:
                for j in venlst2[i]:
                    emploIDlst.append(j)
            
            url='https://zh.surveymonkey.com/r/VendorHealthCheck'
            
            
            
            for i in range(len(emploIDlst)):

                browser2.get(url)

                buttonagree=browser2.find_element_by_xpath('//*[@id="673322538_4424691400_label"]/span[1]')
                emploID=browser2.find_element_by_xpath('//*[@id="673322548"]')
                button2=browser2.find_element_by_xpath('//*[@id="673322540_4424691402_label"]/span[1]')
                bodytemp=browser2.find_element_by_xpath('//*[@id="673322536"]')
                button4=browser2.find_element_by_xpath('//*[@id="673322545_4424691427_label"]/span[1]')
                button5=browser2.find_element_by_xpath('//*[@id="673322546_4424691428_label"]/span[1]')
                button6=browser2.find_element_by_xpath('//*[@id="673322547_4424691430_label"]/span[1]')

                buttonpage=browser2.find_element_by_xpath('//*[@id="patas"]/main/article/section/form/div[2]/button')

                buttonagree.click()
                emploID.send_keys(emploIDlst[i])

                button2.click()

                bodytemp.send_keys(str(35.5+randint(1,12)*0.1))

                button4.click()
                button5.click()
                button6.click()
                buttonpage.click()

                button8=browser2.find_element_by_xpath('/html/body/main/article/section/form/div[1]/div[1]/div/div/fieldset/div/div/div[4]/div/label/span[1]')
                button9=browser2.find_element_by_xpath('//*[@id="673325885_4424715311_label"]/span[1]')
                buttonYes=browser2.find_element_by_xpath('//*[@id="673322537_4424691392_label"]/span[1]')
                buttonDone=browser2.find_element_by_xpath('//*[@id="patas"]/main/article/section/form/div[2]/button[2]')


                button8.click()
                button9.click()
                buttonYes.click()
                buttonDone.click()

            browser2.close()
            time.sleep(55)
            
        else:
            pass


def userreport():
    def addingmode():
        reportthem.delete("1.0","end")
        reportthem.insert('end',venlst[entry_emplo.get()])
        

    def addingvenID():
        venlst[entry_emplo.get()].append(entry_venID.get())
        reportthem.delete("1.0","end")
        reportthem.insert('end',venlst[entry_emplo.get()])


    def exitapp():
        window.destroy()


    def savedata():
        newdata = json.dumps(venlst,ensure_ascii=False)
        fh = open('venlstemp', 'r+', encoding='UTF-8')
        fh.seek(0)
        fh.write(newdata)
        fh.close()


    def reportBodyTemp():
        url='https://zh.surveymonkey.com/r/VendorHealthCheck'
        emploIDlst = venlst[entry_emplo.get()]
        browser2=webdriver.Chrome(r'C:\chromedriver')
        for i in range(len(emploIDlst)):

            browser2.get(url)

            buttonagree=browser2.find_element_by_xpath('//*[@id="673322538_4424691400_label"]/span[1]')
            emploID=browser2.find_element_by_xpath('//*[@id="673322548"]')
            button2=browser2.find_element_by_xpath('//*[@id="673322540_4424691402_label"]/span[1]')
            bodytemp=browser2.find_element_by_xpath('//*[@id="673322536"]')
            button4=browser2.find_element_by_xpath('//*[@id="673322545_4424691427_label"]/span[1]')
            button5=browser2.find_element_by_xpath('//*[@id="673322546_4424691428_label"]/span[1]')
            button6=browser2.find_element_by_xpath('//*[@id="673322547_4424691430_label"]/span[1]')

            buttonpage=browser2.find_element_by_xpath('//*[@id="patas"]/main/article/section/form/div[2]/button')

            buttonagree.click()
            emploID.send_keys(emploIDlst[i])

            button2.click()

            bodytemp.send_keys(str(35.5+randint(1,12)*0.1))

            button4.click()
            button5.click()
            button6.click()
            buttonpage.click()

            button8=browser2.find_element_by_xpath('/html/body/main/article/section/form/div[1]/div[1]/div/div/fieldset/div/div/div[4]/div/label/span[1]')
            button9=browser2.find_element_by_xpath('//*[@id="673325885_4424715311_label"]/span[1]')
            buttonYes=browser2.find_element_by_xpath('//*[@id="673322537_4424691392_label"]/span[1]')
            buttonDone=browser2.find_element_by_xpath('//*[@id="patas"]/main/article/section/form/div[2]/button[2]')


            button8.click()
            button9.click()
            buttonYes.click()
            buttonDone.click()
        
    fh = open('venlstemp', 'r+', encoding='UTF-8')
    data = fh.readlines()
    fh.close()
    venlst_str = data[0]
    venlst = json.loads(venlst_str)

    window = tk.Tk()
    window.geometry('500x300')

    frame_1 = tk.Frame(window)
    frame_1.pack()
    label_title = tk.Label(frame_1,text = '廠商名單')
    label_title.pack()

    frame_2=tk.Frame(window)
    frame_2.pack()
    label_entry_1 = tk.Label(frame_2, text = '輸入你的姓名')
    label_entry_1.pack(side=tk.LEFT)
    entry_emplo = tk.Entry(frame_2, show=None)
    entry_emplo.pack(side=tk.LEFT)

    btn_entryemplo = tk.Button(frame_2, text = '確認',command=addingmode)
    btn_entryemplo.pack(side=tk.LEFT)

    frame_3=tk.Frame(window)
    frame_3.pack()
    label_entry_2 = tk.Label(frame_3, text = '輸入廠商工號')
    label_entry_2.pack(side=tk.LEFT)
    entry_venID = tk.Entry(frame_3, show=None)
    entry_venID.pack(side=tk.LEFT)

    btn_entryID = tk.Button(frame_3, text = '加入',command=addingvenID)
    btn_entryID.pack(side=tk.LEFT)

    reportthem = tk.Text(window, height=10)
    reportthem.pack()

    btn_exit = tk.Button(window, text = '退出',command=exitapp)
    btn_exit.pack(side=tk.RIGHT)

    btn_save = tk.Button(window, text = '存檔',command=savedata)
    btn_save.pack(side=tk.RIGHT)

    btn_report = tk.Button(window, text = '送出',command=reportBodyTemp)
    btn_report.pack(side=tk.RIGHT)

    window.mainloop()


def main():
    t1 = Thread(target = userreport)
    t1.start()
    t2 = Thread(target = autoreport)
    t2.start()
    t1.join()
    t2.join()
    
if __name__ == '__main__':
    main()
