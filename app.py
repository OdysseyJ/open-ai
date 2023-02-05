import os

from chalice import Chalice
import openai

openai.api_key = ""
app = Chalice(app_name='open-ai')


@app.route('/question', methods=['GET'])
def index():
    query_params = app.current_request.to_dict().get("query_params", {})
    question = ""
    if query_params:
        question = query_params.get("q", "")
    res = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""
        Q:{question}\n
        A: \n
        """,
        temperature=0,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )

    return res['choices'][0]["text"] if res['choices'] else "답변을 찾지 못했습니다."
