const keyInputEncrypt = document.getElementById("keyInputEncrypt");
const messageInput = document.getElementById("messageInput");
const submitEncryptButton = document.getElementById("submitEncryptButton");
const binaryResultText = document.getElementById("binaryResultText");
const base64ResultText = document.getElementById("base64ResultText");

submitEncryptButton.addEventListener("click", function () {
    const key = keyInputEncrypt.value;
    const message = messageInput.value;

    const data = {
        key: key,
        message: message
    };

    fetch("http://localhost:8000/encrypt", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            base64ResultText.textContent = "Base64 Encrypted Result:";
            base64ResultText.appendChild(document.createTextNode(data.base64_encrypted));
        })
        .catch((error) => {
            console.error("Error:", error);
            binaryResultText.textContent = "";
            base64ResultText.textContent = "An error occurred while processing the request.";
        });
})