#tools 함수 모듈 만들기
from datetime import datetime

#나이 계산 함수
def calculate_age(birthday):
    today = datetime.now()
    birthday = datetime.strptime(birthday, "%Y-%m-%d")
    age = today.year - birthday.year
    if(today.month, today.day) < (birthday.month, birthday.day):
        age -=1
    return age

#환율 변환 함수
def convert_currency(amount):
    k_won = amount*1330
    return k_won

#BMI(체질량지수) 계산 함수
def calculate_bmi(height, weight):
    bmi = weight/ ((height/100)**2)
    return round(bmi, 2)    #소수점 2자리까지만 출력


#tools
tools = [{
    #나이 계산
    'type': 'function',
    'name': 'calculate_age',
    'description': '생일(YYYY-MM-DD)을 입력받아 현재 나이를 계산한다.',
    'parameters':{
        'type': 'object',
        'properties': {
            'birthday': {'type': 'string', "description": "생년월일, 형식:YYYY-MM-DD"}
        },
        'required': ['birthday'],
        'additionalProperties': False
    },
    'strict': True
    },
    {
    #환율 변환
    'type': 'function',
    'name': 'convert_currency',
    'description': '달러를 입력받아 원화로 변환한다.',
    'parameters':{
        'type': 'object',
        'properties': {
            'amount': {'type': 'number',"description": "달러(USD) 금액"}
        },
        'required': ['amount'],
        'additionalProperties': False
    },
    'strict': True

    },
    {
    #BMI 계산
    'type': 'function',
    'name': 'calculate_bmi',
    'description': '키와 몸무게를 입력받아 BMI를 계산한다.',
    'parameters':{
        'type': 'object',
        'properties': {
            'height': {'type': 'number',"description": "키(cm)"},
            'weight': {'type': 'number',"description": "몸무게(kg)"}
        },
        'required': ['height','weight'],
        'additionalProperties': False
    },
    'strict': True
    }
]
