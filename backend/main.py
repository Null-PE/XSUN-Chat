import openai
from flask import Flask, request, jsonify
from flask_cors import CORS
import yaml

app = Flask(__name__)
CORS(app)


# 从 settings.yml 文件中读取 API 密钥
with open("settings.yml", "r") as ymlfile:
    config = yaml.safe_load(ymlfile)
openai.api_key = config["api_key"]


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": prompt
        }],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )

    if response is not None:
        return response.choices[0].message.content.strip()
    else:
        raise Exception("API request failed")

@app.route('/generate', methods=['POST', 'GET'])  # 更改路由
def generate():
    data = request.get_json()
    prompt = data['prompt']
    print(f'Q: {prompt}')
    response_text = chat_with_gpt(prompt)
    print(f'A: {response_text}')
    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(debug=True)
