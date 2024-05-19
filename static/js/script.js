document.addEventListener('DOMContentLoaded', function () {
    const chatButton = document.getElementById('chat-button');
    const chatWindow = document.getElementById('chat-window');
    const closeChat = document.getElementById('close-chat');
    const sendChat = document.getElementById('send-chat');
    const chatInput = document.getElementById('chat-input');
    const chatBody = document.querySelector('.chat-body');
  
    chatButton.addEventListener('click', () => { // Exibindo o chat
      chatWindow.style.display = 'flex';
    });
  
    closeChat.addEventListener('click', () => { // Fechando o chat
      chatWindow.style.display = 'none';
    });
  
    sendChat.addEventListener('click', () => {
      const msg = chatInput.value.trim();
      if (msg) {
        const msgElement = document.createElement('div');
        msgElement.textContent = `Você: ${msg}`;
        chatBody.appendChild(msgElement);
        chatInput.value = '';
        chatBody.scrollTop = chatBody.scrollHeight;
      }
    });
  
    chatInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        sendChat.click();
      }
    });
  });