import requests
import streamlit as st
from streamlit_pills import pills

def main():
    st.title("AI Resume")
    st.write("프로젝트명 또는 당신의 경험을 적어주세요. 이력서 맞춤 문장으로 업그레이드 해드릴게요!")

    strength = pills("특성", ["꼼꼼함", "실행력이 좋음", "팀 분위기를 화기애애하게 만듦"], ["🍀", "🎈", "🌈"])
    position = pills("직군", ["프론트엔드개발자", "데이터엔지니어", "프로덕트 매니저"])
    # st.write(selected)

     # 텍스트 입력 상자 추가
    user_input = st.text_input("텍스트 입력", "")

    # 사용자가 입력한 값으로 백엔드 API 호출
    if st.button("API 호출"):
        response = call_backend_api(f"# 경험:{user_input} # 강점 :{strength} # 직군:{position}")
        st.write("백엔드 API 응답:", response)


def call_backend_api(input_text):
    # 백엔드 API 호출
    url = 'http://127.0.0.1:8000/chat'  # 백엔드 서버 주소
    data = {'text': input_text}
    print(data)
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return "백엔드 API 호출 실패"

if __name__ == "__main__":
    main()
