import sys
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# dates = pd.date_range('20130101', periods=6)
# print(dates)

# df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
# print(df)  11.26-12.27-details'
# def filter(x):
#     return True if x['Check In'] > datetime.time(9, 5, 0) or x['Check Out'] < datetime.time(18, 0, 0) else False

# 11.26-12.27-details
file_name = sys.argv[1]
print('file name: ' + file_name)

def filter(x):
    time_format = '%H:%M'
    if str(x['签到时间']) == 'nan' or str(x['签退时间']) == 'nan':
        return True
    if str(x['上班时间']) == 'nan' or str(x['下班时间']) == 'nan':
        return False
    if datetime.strptime(str(x['上班时间']), time_format) + timedelta(minutes = 5) < datetime.strptime(str(x['签到时间']), time_format):
        return True
    if datetime.strptime(str(x['下班时间']), time_format) > datetime.strptime(str(x['签退时间']), time_format):
        return True
    return False

try:
    with pd.ExcelFile(file_name + '.xlsx') as xlsx:
        df = pd.read_excel(xlsx, file_name)
        df_filtered = df[df.apply(filter, axis=1)]
        print(df_filtered)
        df_filtered.to_excel(file_name + '_filtered.xlsx', sheet_name=file_name, index=False)
except Exception as ex:
    print('数据导出异常') 
    print(ex)