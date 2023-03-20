<template>
  <div id="app">
    <!-- <h1>Chat with ChatGPT</h1> -->
    <div class="chat-container">
      <div v-for="(message, index) in messages" :key="index" class="message">
        <span :class="message.role">{{ message.content }}</span>
      </div>
    </div>
    <div class="input-container">
      <input v-model="userInput" @keyup.enter="submit" type="text" placeholder="Type your message here..." />
      <button @click="submit">Send</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import '@/assets/chat.css';

export default {
  data() {
    return {
      userInput: "",
      messages: [],
    };
  },
  methods: {
    async submit() {
      if (this.userInput.trim() !== "") {
        const input = this.userInput.trim();
        console.log("Input: " + input);
        this.messages.push({ role: "user", content: input });
        this.userInput = "";

        try {
          const response = await axios.post("http://127.0.0.1:5000/generate", {
            prompt: this.messages[this.messages.length - 1].content,
          });
          console.log("Get resoponse: " + response.status);

          // Split the response into paragraphs
          const paragraphs = response.data.response.split('\n');
          // Push each paragraph as a separate message
          paragraphs.forEach(paragraph => {
            if (paragraph.trim() !== '') {
              this.messages.push({ role: "assistant", content: paragraph });
            }
          });
        } catch (error) {
          console.error("Error:", error);
        }
      }
    }

  },
};
</script>

