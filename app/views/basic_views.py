from flask import Blueprint, render_template
from app.models import Question
from app.models import Answer

fisa = Blueprint('basic', __name__, url_prefix='/fisa')
#basic : 우리가 부르는 별명
#__name__ : flask 프레임워크가 찾을 이름
#prefix : 라우팅 주소

@fisa.route('/prac_me')
def about_me():
    return f'저는 {__name__} 입니다'

@fisa.route('/prac_hello')
def prac_hello():
    return f'안녕하세요'

@fisa.route('/prac_bye')
def prac_bye():
    return f'잘 가세요'