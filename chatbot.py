import streamlit as st
import os
import requests
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from datetime import datetime


load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)


st.sidebar.title('메뉴')
page = st.sidebar.selectbox('페이지를 선택하세요', ['챗봇', '순위'])

if page == '챗봇':
    st.title('ChatGPT 국산')
    #세션 관리 객체. 세션에 키-값 형식으로 데이터를 저장하는 변수
    #openai_model 저장 --> str, message(사용자가 요청한 메시지)--> []
    if 'openai_model' not in st.session_state :
        #openai_model키 없으면 추가
        st.session_state.openai_model = 'gpt-4.1'

    if 'messages' not in st.session_state:
        #message 키 없으면 추가 및 초기화
        st.session_state.messages = []

    #기존의 메시지가 있다면 출력
    for msg in st.session_state.messages:
        with st.chat_message(msg['role']):
            st.markdown(msg['content'])

    #prompt --> 사용자 입력 창
    if prompt := st.chat_input('메시지를 입력하세요'):
        #message --> [], 대화 내용 추가
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })
        
        with st.chat_message('user'):
            st.markdown(prompt)
        
        with st.chat_message('assiatant'):
            stream = client.chat.completions.create(
                model=st.session_state.openai_model,
                #맥락을 유지하면서 텍스트 출력하기
                messages=[
                    {"role": m['role'], "content": m['content']}
                    for m in st.session_state.messages   
                ],
                stream=True #gpt 응답을 스트리밍 방식으로 받기
            )
            response = st.write_stream(stream)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })



elif page == '순위':
    st.title('KBO 순위')
    st.markdown(
        """
        ## KBO 팀 순위 및 경기 일정 확인 사이트
        - [순위 보기](https://www.koreabaseball.com/record/teamrank/teamrankdaily.aspx)
        - [경기 일정 보기](https://www.koreabaseball.com/Schedule/Schedule.aspx)
        """
    )
    #야구 순위 사이트 정보 가져오기
    url = "https://www.koreabaseball.com/Record/TeamRank/TeamRankDaily.aspx"
    headers = {"User-Agent": "Mozilla/5.0"}  # 차단 방지용 헤더
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')#원본 데이터

    # summary 속성을 기준으로 테이블 찾기
    record_table = soup.find("table", summary="순위, 팀명,승,패,무,승률,승차,최근10경기,연속,홈,방문")
    rows = record_table.find_all("tr")

    #순위를 기록할 리스트 생성
    ranking=[]
    #데이터 추출하기
    for tr in record_table.find_all("tr")[1:]:  # 첫 번째 tr은 헤더
        columns = [td.get_text(strip=True) for td in tr.find_all("td")]
        if columns:
            ranking.append(columns)

    #열 이름 정의하기
    data_columns = ['순위', '팀명', '경기','승', '패', '무', '승률', '게임차', '최근10경기', '연속', '홈', '방문']

    #데이터 프레임 정의하기
    df = pd.DataFrame(ranking, columns=data_columns)
    df = df.drop('방문', axis=1)
    # Streamlit에 표 출력
    st.subheader('-----------------------------최신 순위------------------------------')
    st.dataframe(df)

















