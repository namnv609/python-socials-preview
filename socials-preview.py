from bottle import route, run, template, request
import requests as Request
from bs4 import BeautifulSoup
from socials import Facebook
import pdb

@route('/')
def index():
    return template('index.tpl', title='Welcome')

@route('/preview', method='POST')
def preview():
    webUrl = request.forms.get('url')
    response = Request.get(webUrl)
    viewData = {
        'fb': []
    }

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html5lib')
        viewData['fb'] = Facebook.getDetail(soup)
        # pdb.set_trace()

    return template('preview.tpl', viewData)

run(host='localhost', port=8088, debug=True)
