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
soup = soup.find('div',{"class":"internalMarks"})
arr = soup.find_all('div',{'class':'panel'})
for i in arr:
    sub = str(i)[str(i).find('/b>')+12:str(i).find('</a>')].strip()
    print(sub+':\n')
    vals = i.find_all('td')
    for a in range(0,len(vals),3):
        assign = str(vals[a])[str(vals[a]).find('>')+1:str(vals[a]).find('</td>')]
        if assign == '':
            assign = 'Unnamed'
        max = str(vals[a+1])[str(vals[a+1]).find('>')+1:str(vals[a+1]).find('</td>')]
        score = str(vals[a+2])[str(vals[a+2]).find('>')+1:str(vals[a+2]).find('</td>')]
        print(assign+'- '+score+'/'+max)
    print('\n---\n')
