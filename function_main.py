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

input_messages = [{"role": "user", "content":'내 생일은 2001-04-06이고, 100달러를 원화로 환전해주고, 키는 190에 모무게는 80이야. BMI를 계산해줘'}]


response = client.responses.create(
    model='gpt-4.1',
    input=input_messages,
    tools=tools,
)

#dict(response.output[0])
#call에 대한 응답 데이터
# tool_call = response.output[0]
# #json형태로 변환
# args = json.loads(tool_call.arguments)

# tool_name = tool_call.name

# #나이 계산일 때
# if tool_name == 'calculate_age':
#     result = calculate_age(args['birthday'])
#     print(f'현재 나이는 {result}세 입니다.')
# #환율 계산일 때
# elif tool_name == 'convert_currency':
#     result = convert_currency(args['amount'])
#     print(f'원화로는 {result}원 입니다.')
# #BMI계산일 때
# elif tool_name == 'calculate_bmi':
#     result = calculate_bmi(args['height'],args['weight'])
#     print(f'BMI 점수는 {result}입니다.')
# #그 외(에러)
# else:
#     result = {'ERROR': f'예정에 없는 함수 호출입니다: {tool_name}.'}

#한 번에 출력하기!
if response.output:
    for tool_call in response.output:
        if tool_call.type == 'function_call':   #타입이 함수호출일 때만
            if tool_call.name == 'calculate_age':
                print(f'호출 도구: {tool_call.name}')
                print(f'매개변수: {tool_call.arguments}')
                #매개변수 추출
                args = json.loads(tool_call.arguments)
                #함수 실행 결과
                result = calculate_age(args['birthday'])
                input_messages.append(tool_call)
                input_messages.append({
                    "type" : "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": str(result)   

                })
            
            if tool_call.name == 'convert_currency':
                print(f'호출 도구: {tool_call.name}')
                print(f'매개변수: {tool_call.arguments}')
                #매개변수 추출
                args = json.loads(tool_call.arguments)
                #함수 실행 결과
                result = convert_currency(args['amount'])
                input_messages.append(tool_call)
                input_messages.append({
                    "type" : "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": str(result)   
                })
            
            if tool_call.name == 'calculate_bmi':
                print(f'호출 도구: {tool_call.name}')
                print(f'매개변수: {tool_call.arguments}')
                #매개변수 추출
                args = json.loads(tool_call.arguments)
                #함수 실행 결과
                result = calculate_bmi(args['height'], args['weight'])
                input_messages.append(tool_call)
                input_messages.append({
                    "type" : "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": str(result)   
                })
                

#print(input_messages)


response_msg = client.responses.create(
    model='gpt-4.1',
    input=input_messages,
    tools=tools,
)
print(response_msg.output_text)









