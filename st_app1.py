import streamlit as st

st.set_page_config(
    page_title='Hello'
    #page_icon='icon'
)

st.write('# 안녕하세요 반갑습니다!')

st.sidebar.success('데모 선택') #success: 초록색

st.markdown(
    """
    Streamlit은 머신 러닝 및 데이터 과학 프로젝트를 위해 특별히 제작된 오픈 소스 앱 프레임워크입니다..
    ### 자세히 알아보고 싶으신가요?
    - [streamlit.io](https://streamlit.io)
    - [설명서](https://docs.streamlit.io)
    - [커뮤니티 포럼](https://discuss.streamlit.io)에서 질문하기
    """
)
st.title("앱 제목")

st.header("헤더입니다")
st.subheader("서브헤더입니다")

st.caption("작은 설명 텍스트입니다")

st.title("앱 제목")

st.code("a = 1234")
with st.echo(): #실행
    st.write('이 코드는 출력됩니다.')

#LaTeX 형식으로 수학 표현식을 표시
st.caption("LaTeX 형식으로 수학 표현식을 표시")
st.latex("\int a x^2 \,dx")

#이름 입력받기
name = st.text_input("이름")
#콘솔에서 출력
print(name)
#브라우저에서 출력
st.write(name)