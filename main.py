
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import requests
from bs4 import BeautifulSoup as soup
from flask import render_template
app = Flask(__name__)
class karl():
    def __init__(self,s):
        self.name = s
@app.route('/')
def hello_world():
    print("gone teachers:")
    url = "https://wa-bsd405.edupoint.com//Service/SubLogin.asmx/LoadSubs"
    session = requests.Session()
    data = {
      'curSchoolOrgYearGU':'4C5D9CB6-9676-47C8-82EE-48F152FDDF02'
    }
    headers = {
      'contentType': "application/json"
    }
    r = session.post(url,data=data,headers=headers)
    bs=soup(r.text,"html.parser")
    html = bs.findAll("name")
    html.pop(0)
    hi = []
    for name in html:
        print (str(name).split(">")[1].split("<")[0])
        hi.append(karl(str((str(name).split(">")[1].split("<")[0]))))
    return render_template("main.html",data=hi)
if __name__ == '__main__':
    app.run()
