import requests

# 定义后端 API 地址
API_URL = "http://127.0.0.1:5000/generate"


# 定义测试函数
def test_generate_response(prompt):
    # 发送 POST 请求到后端
    response = requests.post(API_URL, json={"prompt": prompt})

    print(response)
    # 检查请求是否成功
    assert response.status_code == 200

    # 获取响应数据
    data = response.json()

    # 检查响应数据是否正确
    assert "response" in data
    assert isinstance(data["response"], str)

    # 打印生成的对话回复
    print(data["response"])


# 测试函数
prompt = "Hello, how are you doing today?"
test_generate_response(prompt)
