Dict = {'氫': 'hydrogen', '氦': 'helium', '鋰': 'lithium', '鈹': 'beryllium', 
        '硼': 'boron', '碳': 'carbon', '氮': 'nitrogen', '氧': 'oxygen', 
        '氟': 'fluorine', '氖': 'neon', '鈉': 'sodium'}

#print(Dict.keys())

#print(Dict)

Chinese = (input("請輸入一個中文單字: "))

print(Dict.get(Chinese, "字典中找不到這個單字!"))