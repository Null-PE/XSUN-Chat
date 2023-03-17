# ChatGPT Web Application (项目内容均为ChatGPT生成)

本项目使用Vue.js、Python Flask和OpenAI的ChatGPT API构建了一个简单的Web应用程序，用户可以与ChatGPT进行交互。

## 项目结构

```
.
├── server.py            # Flask后端应用程序
├── settings.yml      # 存储API密钥的配置文件
├── frontend  # Vue.js前端项目文件夹
│   ├── src
│   │   ├── components
│   │   │   └── Chat.vue  # 主要的Vue.js组件
│   │   └── ...
│   └── ...
└── README.md         # 本文件
```

## 安装和运行

1. 克隆此仓库
2. 安装后端所需的Python库
```bash
pip install Flask flask-cors requests openai pyyaml
```
3. 将您的API密钥添加到settings.yml文件中
```yaml
api_key: "your_api_key_here"  # 请用您的API密钥替换此处的字符串
```
4. 安装前端所需的依赖库:
```bash
cd frontend
npm install
```
5. 运行后端服务:
```bash
cd ..
python server.py
```
后端服务将在http://localhost:5000上运行。

6. 在另一个终端窗口中，运行前端服务：
```bash
cd frontend
npm run serve
```
前端服务将在http://localhost:8080上运行。

现在，您可以在浏览器中访问http://localhost:8080，与ChatGPT进行交互。