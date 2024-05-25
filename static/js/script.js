document.addEventListener('DOMContentLoaded', function () {
    const chatButton = document.getElementById('chat-button');
    const chatWindow = document.getElementById('chat-window');
    const closeChat = document.getElementById('close-chat');
    const sendChat = document.getElementById('send-chat');
    const chatInput = document.getElementById('chat-input');
    const chatBody = document.querySelector('.chat-body');
    const agendarAgora = document.querySelector('.agendar-agora')
  
    // Duas maneiras de exibir o chat: 

    // 1 - clcar em "Agendar agora", no navbar:
    agendarAgora.addEventListener('click', () => {
      chatWindow.style.display = 'flex';
    })

    // 2 - clicar no botãozinho do chat (funciona como um toggle)
    chatButton.addEventListener('click', () => {
      if(chatWindow.style.display == 'flex') {
        return chatWindow.style.display = 'none'
      }
      return chatWindow.style.display = 'flex';
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
  

    // Permanecer a navbar ao scrollar:
    
  });