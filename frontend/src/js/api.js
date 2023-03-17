import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:5000', // 将这里的 URL 替换为你的 Flask 服务器的地址
  headers: {
    'Content-Type': 'application/json'
  }
});

export default {
  generateResponse(prompt) {
    return apiClient.post('/generate', { prompt });
  }
};
