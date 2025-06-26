import json
import os
from function_module import tools, calculate_age, calculate_bmi, convert_currency
from openai import OpenAI
from dotenv import load_dotenv

#키 가져오기
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

#OpenAI 객체 생성
client = OpenAI(api_key=OPENAI_API_KEY)

input_messages = input('입력하세요: ')


response = client.responses.create(
    model='gpt-4.1',
    input=input_messages,
    tools=tools,
)

#dict(response.output[0])
#call에 대한 응답 데이터
tool_call = response.output[0]
#json형태로 변환
args = json.loads(tool_call.arguments)

#함수가 3개이기 때문에 name에 따라 다른 결과 반환하기
tool_name = tool_call.name

#나이 계산일 때
if tool_name == 'calculate_age':
    result = calculate_age(args['birthday'])
#환율 계산일 때
elif tool_name == 'convert_currency':
    result = convert_currency(args['amount'])
#BMI계산일 때
elif tool_name == 'calculate_bmi':
    result = calculate_bmi(args['height'],args['weight'])
#그 외(에러)
else:
    result = {'ERROR': f'예정에 없는 함수 호출입니다: {tool_name}.'}
print(f'결과는 {result} 입니다.')














