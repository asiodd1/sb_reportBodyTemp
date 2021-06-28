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
import tkinter as tk

#venlst = {'信本':{},'模板':{},'芳達':{},'鋼筋':{},'正鋼':{},'旺宏':{}}

venlstemp={'張佑宇':[],'鍾欣原':[]}

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


def addingmode():
    global vencomp
    vencomp = venlstemp[entry_emplo.get()]
    
btn_entryemplo = tk.Button(frame_2,text = '確認',command=addingmode)
btn_entryemplo.pack(side=tk.LEFT)

frame_3=tk.Frame(window)
frame_3.pack()
label_entry_2 = tk.Label(frame_3, text = '輸入廠商ID')
label_entry_2.pack(side=tk.LEFT)
entry_venID = tk.Entry(frame_3, show=None)
entry_venID.pack(side=tk.LEFT)


def addingven():
    venlstemp[entry_emplo.get()]=vencomp.append(entry_venID.get())
    
    
btn_entryID = tk.Button(frame_3, text= '加入',command=addingven)
btn_entryID.pack(side=tk.LEFT)

#window.mainloop()
