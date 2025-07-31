const submitbutton = document.getElementById("Submit");
const promptarea   = document.getElementById("Prompt");
const chatop       = document.getElementById("Chatoutput");

submitbutton.addEventListener("click", async function () {
  const textinput = promptarea.value.trim();

  if (!textinput) {
    chatop.innerHTML = "Please enter something...";
    return;
  }

  chatop.innerHTML = "Thinking...";

  try {
    const response = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: textinput })
    });
    

    const data = await response.json();
    console.log(data);
    if (data.response) {
      chatop.innerHTML = data.response;   // <── bold rendered
    } else {
      chatop.innerHTML = "Sorry, I couldn't understand that.";
    }
  } catch (err) {
    chatop.innerHTML = "Error connecting to the server.";
  }

  promptarea.value = "";
});

