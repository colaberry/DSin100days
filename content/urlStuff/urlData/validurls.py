from selenium import webdriver
# driver = webdriver.Chrome()
import xlrd
print('Idhar')
filename = xlrd.open_workbook('urls.xlsx')
worksheet = filename.sheet_by_name('urls')
print('Idhar1')
print(worksheet.cell( 1, 2).value)
count = 0
while (worksheet.cell( count, 2).value is not ''):
    a=worksheet.cell( count, 2).value
    print(a)
    count += 1

# driver.get('https://www.google.com/')

