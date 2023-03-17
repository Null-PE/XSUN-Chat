<template>
    <div class="message" :class="{ 'user-message': isUserMessage, 'bot-message': !isUserMessage }">
        <div class="message-content" :class="{ 'loading': isLoadingMessage }">
            <div v-if="isLoadingMessage">玩儿命思考中...</div>
            <div v-else>{{ message.content }}</div>
        </div>
    </div>
</template>
  
<script>
export default {
    name: "ChatMessage",
    props: {
        message: {
            type: Object,
            required: true,
        },
        isUserMessage: {
            type: Boolean,
            default: false,
        },
        isLoadingMessage: {
            type: Boolean,
            default: false,
        },
    },
};
</script>
  
<style scoped>