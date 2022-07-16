# import PyPDF2

# pdf = open('031002100211_95367889.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdf)
# page_one = pdfReader.getPage(0)
# txt = page_one.extractText()

# print(txt)

import os
import re
import pdfplumber
# with pdfplumber.open("031002100211_95367889.pdf") as pdf:
#     page01 = pdf.pages[0] #指定页码
#     text = page01.extract_text()#提取文本
#     print(text)

def get_money_from_pdf(filename):
    with pdfplumber.open(filename) as pdf:
        print('file name: ' + filename)
        page01 = pdf.pages[0] #指定页码
        table1 = page01.extract_table()#提取单个表格
        table2 = page01.extract_tables()#提取多个表格
        buyer_str = table1[0][1]
        print('buyer: ' + str(buyer_str))
        sell_str = table1[3][1]
        if(sell_str == ""):
            sell_str = table1[10][3]
        money_str = table1[2][2]
        if(money_str == "" or money_str == None):
            money_str = table1[8][5]
        print('seller: ' + sell_str + "\n" + money_str)
        pattern = re.compile(r'.+(\b\d+\.\d+)', re.IGNORECASE)
        res = re.match(pattern, money_str)
        # print(len(res.groups())) # len = 4  
        result = res.group(1)
        # print (result)
        
        return float(result)

# get_money_from_pdf("050002000211-45771476.pdf")

root_curdir = os.path.curdir
invoices_dir = os.path.join(root_curdir, "not-sent")
print(invoices_dir)

def read_files(curdir):
    filenames= os.listdir (curdir)
    sum = 0.0
    for index, filename in enumerate(filenames):
        print("No: {}".format(index + 1))
        full = os.path.join(os.path.abspath(curdir), filename)
        money = get_money_from_pdf(full)
        sum += money
    
    print('SUM: {}'.format(sum))

if __name__ == '__main__':
    try:
        print('start to read files')
        read_files(invoices_dir)
        print('stop to read files')
    except Exception as ex:
        print(ex)