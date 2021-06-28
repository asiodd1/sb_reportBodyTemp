vendorList={'信本':{'H0289550':'江鎮廷','U9168010':'張佑宇'},
            '模板':{'T8616750':'徐格隆'}}


while True:

    company = int(input('進入信本請按1,模板請按2'))    

    if company == 1 :
        print()
        print('信本')
        for key in vendorList['信本']:
            print(key+':'+vendorList['信本'][key])
        print()
        continue
    elif company == 2:
        print()
        print('模板')
        for key in vendorList['模板']:
            print(key+':'+vendorList['模板'][key])
        print()
        continue
    else:
        print('\n請重新輸入:\n')
        continue
