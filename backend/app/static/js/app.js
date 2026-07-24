const messageInput = document.getElementById("message");
const sendBtn = document.getElementById("sendBtn");
const fileInput = document.getElementById("fileInput");
const chatWindow = document.getElementById("chatWindow");
const history = document.getElementById("history");
const newChatBtn = document.getElementById("newChatBtn");

let userId = localStorage.getItem("userId");

if (!userId) {
    userId = crypto.randomUUID();
    localStorage.setItem("userId", userId);
}

newChatBtn.onclick = () => {

    chatWindow.innerHTML = `
        <div class="welcome">
            <h1>DocChat AI</h1>
            <p>Upload a PDF and ask questions.</p>
        </div>
    `;

};

sendBtn.onclick = sendMessage;

messageInput.addEventListener("keydown", function (e) {

    if (e.key === "Enter" && !e.shiftKey) {

        e.preventDefault();

        sendMessage();

    }

});

fileInput.addEventListener("change", uploadFile);

function addMessage(text, isUser) {

    const msg = document.createElement("div");

    msg.className = isUser ? "message user-message" : "message bot-message";

    msg.innerHTML = `
        <div class="bubble">
            ${text}
        </div>
    `;

    chatWindow.appendChild(msg);

    chatWindow.scrollTop = chatWindow.scrollHeight;

}
async function sendMessage() {

    const question = messageInput.value.trim();

    if (question === "")
        return;

    if (document.querySelector(".welcome"))
        document.querySelector(".welcome").remove();

    addMessage(question, true);

    messageInput.value = "";

    const loading = document.createElement("div");

    loading.className = "message bot-message";

    loading.id = "loading";

    loading.innerHTML = `
        <div class="bubble">
            Thinking...
        </div>
    `;

    chatWindow.appendChild(loading);

    chatWindow.scrollTop = chatWindow.scrollHeight;

    try {

        const response = await fetch("/api/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                question: question,

                userId: userId

            })

        });

        const data = await response.json();

        loading.remove();

        addMessage(data.answer, false);

    }

    catch (e) {

        loading.remove();

        addMessage("Server Error", false);

    }

}
async function uploadFile() {

    const file = fileInput.files[0];

    if (!file)
        return;

    const formData = new FormData();

    formData.append("file", file);

    addMessage("Uploading " + file.name + "...", false);

    try {

        const response = await fetch("/api/upload", {

            method: "POST",

            body: formData

        });

        const data = await response.json();

        addMessage("✅ " + data.message, false);

    }

    catch {

        addMessage("Upload Failed", false);

    }

}