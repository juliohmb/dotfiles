const form = document.getElementById("message-form");
const input = document.getElementById("message-input");
const messages = document.getElementById("messages");

form.addEventListener("submit", async event => {
  event.preventDefault();

  // Get the user's input
  const prompt = input.value;

  // Generate a response
  const response = await fetch("/response", {
    method: "POST",
    body: JSON.stringify({ prompt }),
    headers: {
      "Content-Type": "application/json"
    }
  }).then(res => res.text());

  // Add the user's message and the response to the chatbox
  const message = document.createElement("div");
  message.classList.add("message");

  const promptElement = document.createElement("p");
  promptElement.innerText = prompt;
  message.appendChild(promptElement);

  const responseElement = document.createElement("p");
  responseElement.innerText = response;
  message.appendChild(responseElement);

  messages.appendChild(message);

  // Clear the input field
  input.value = "";
});
