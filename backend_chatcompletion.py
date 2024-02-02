# 아래 명령어로 로컬에서 api 띄울 수 있음
# uvicorn backend_chatcompletion:app --reload
# 띄운 api는 swagger로 확인 가능 (http://localhost:8000/docs)
# http://127.0.0.1:8000/chat 엔드포인트로 POST 요청을 보내 사용자의 입력(text)을 전달하면, 챗봇의 응답을 받을 수 있음

import os
import openai
from fastapi import FastAPI
from pydantic import BaseModel

# OpenAI API 키 설정
openai.api_key = os.getenv('OPENAI_API_KEY')

app = FastAPI()

class ChatInput(BaseModel):
    text: str

def chat_with_openai(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "챗봇은 친절하고 유익한 대화를 제공한다."},
                {"role": "user", "content": text},
            ]
        )

        result = response['choices'][0]['message']['content']
        return result
    except Exception as e:
        print(f"Error: {e}")
        return "죄송합니다, 답변을 생성하는데 문제가 발생했습니다."

@app.post("/chat")
def chat(input_text: ChatInput):
    response_text = chat_with_openai(input_text.text)
    return {"response": response_text}
