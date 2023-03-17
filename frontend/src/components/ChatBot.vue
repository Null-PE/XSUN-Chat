<template>
  <div class="chat-container">
    <div class="chat-header">GPT</div>
    <div class="chat-body">
      <div v-for="(message, index) in messages" :key="index" class="message">
        <div v-if="message.role === 'user'" class="user-message">
          <div class="message-content">{{ message.content }}</div>
        </div>
        <div v-else class="bot-message">
          <div class="message-content">{{ message.content }}</div>
        </div>
      </div>
      <div class="input-box">
        <textarea v-model="prompt" placeholder="请输入您的问题" @keydown.enter="handleKeyDown" />
        <button ref="sendButton" class="send-button" @click="generateResponse">发送</button>
      </div>
    </div>
  </div>
</template>

<script>
import api from '@/js/api';
import '@/assets/chat.css'; 

export default {
  data() {
    return {
      prompt: '',
      messages: []
    };
  },
  methods: {
    async generateResponse() {
      console.log(`Q: ${this.prompt}`);

      // 向后端发送请求并获取响应
      const response = await api.generateResponse(this.prompt);
      const message = response.data.response;
      console.log(`A: ${message}`);

      // 添加用户输入和机器人响应到对话记录中
      this.messages.push({ role: 'user', content: this.prompt });
      this.messages.push({ role: 'bot', content: message });

      // 清空输入框
      this.prompt = '';

      // 滚动到底部
      const chatBody = document.querySelector('.chat-body');
      chatBody.scrollTop = chatBody.scrollHeight;
    },
    handleKeyDown(event) {
      if (event.keyCode === 13 && event.metaKey) {
        event.preventDefault();
        this.$refs.sendButton.click();
      } else if(event.keyCode === 13){
        // 换行
        this.prompt += "\n";
      }
    }
  }
};
</script>