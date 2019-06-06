import xlwt

# 新建工作薄
workbook = xlwt.Workbook(encoding='utf-8')

# 新建sheet
sheet1 = workbook.add_sheet("测试表格")

# 写入数据
sheet1.write(0,0,"姓名")          # 第1行第1列数据
sheet1.write(0,1,"学号")          # 第1行第2列数据
sheet1.write(1,0,"张三")          # 第2行第1列数据
sheet1.write(1,1,"036")           # 第2行第2列数据

# 保存
workbook.save(r'D:/test.xls')
