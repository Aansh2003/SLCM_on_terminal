import mechanize
from bs4 import BeautifulSoup
import os
import cv2
import pytesseract
import webbrowser
import sys
import parameters
pytesseract.pytesseract.tesseract_cmd = parameters.path_for_tesseract

url = 'https://slcm.manipal.edu/'

br = mechanize.Browser()
html = br.open(url)

soup = BeautifulSoup(html,features='lxml')
image = soup.findAll('img')[1]

src = url+image['src']

data = br.open(src).read()
br.back()
save = open(str(os.path.expanduser("~"))+parameters.path_from_home+'/captcha.jpeg', 'wb')
save.write(data)
save.close()

im = cv2.imread(str(os.path.expanduser("~"))+parameters.path_from_home+'/captcha.jpeg')
img_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
txt = pytesseract.image_to_string(img_rgb)

txt = txt.strip()

br.select_form(nr=0)
br.form['txtUserid'] = parameters.username
br.form['txtpassword'] = parameters.password
br.form['txtCaptcha'] = txt

req = br.submit()

if str(br.geturl()) == url:
    print("Incorrect details")
    sys.exit()

req = br.open(url+'Academics.aspx')
soup = BeautifulSoup(req,features='lxml')
soup = soup.find('table',{"id":"tblAttendancePercentage"})
arr = soup.find_all('td')
for i in range(len(arr)):
    if i%8==2:
        print(str(arr[i])[str(arr[i]).find('>')+1:str(arr[i]).find('/')-1]+':')
        print('Total classes:'+str(arr[i+2])[str(arr[i+2]).find('>')+1:str(arr[i+2]).find('/')-1])
        print('Days present:'+str(arr[i+3])[str(arr[i+3]).find('>')+1:str(arr[i+3]).find('/')-1])
        print('Days absent:'+str(arr[i+4])[str(arr[i+4]).find('>')+1:str(arr[i+4]).find('/')-1])
        print('Percentage:'+str(arr[i+5])[str(arr[i+5]).find(';">')+3:str(arr[i+5]).find('</span>')-1])
        print('---')
