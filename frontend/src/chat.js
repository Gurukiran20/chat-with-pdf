console.log("chat.js initialized");

const chatWindow = document.getElementById("chatWindow");
const chatForm = document.getElementById("chatForm");
const userInput = document.getElementById("userInput");

function addMessage(role, text) {
  const msg = document.createElement("div");
  msg.className = `message ${role}`;
  msg.textContent = text;
  chatWindow.appendChild(msg);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

if (chatForm) {
  chatForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const text = userInput.value.trim();
    if (!text) return;

    // show user message
    addMessage("user", text);
    userInput.value = "";

    // show temporary "Thinking..." message from assistant
    const thinkingMsg = document.createElement("div");
    thinkingMsg.className = "message assistant";
    thinkingMsg.textContent = "Thinking...";
    chatWindow.appendChild(thinkingMsg);
    chatWindow.scrollTop = chatWindow.scrollHeight;

    try {
      const result = await sendChatMessage(text);
      thinkingMsg.textContent = result.answer;
    } catch (err) {
      console.error(err);
      thinkingMsg.textContent =
        "Error talking to the backend. Check console & backend logs.";
    }
  });
}
