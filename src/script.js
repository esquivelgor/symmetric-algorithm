const keyInputEncrypt = document.getElementById("keyInputEncrypt");
const messageInput = document.getElementById("messageInput");
const submitEncryptButton = document.getElementById("submitEncryptButton");
const base64ResultText = document.getElementById("base64ResultText");

const keyInputDecrypt = document.getElementById("keyInputDecrypt");
const encryptedInput = document.getElementById("encryptInput");
const submitDecryptButton = document.getElementById("submitDecryptButton");
const ResultDecrypt = document.getElementById("DecryptedPlainText");

submitEncryptButton.addEventListener("click", function () {
    const key = keyInputEncrypt.value;
    const message = messageInput.value;

    const data = {
        message: message,
        key: key
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
            base64ResultText.appendChild(document.createTextNode(data.base64_encrypted));
        })
        .catch((error) => {
            console.error("Error:", error);
            binaryResultText.textContent = "";
            base64ResultText.textContent = "An error occurred while processing the request.";
        });
})

submitDecryptButton.addEventListener("click", function () {
    const key = keyInputDecrypt.value;
    const encryptedMessage = encryptedInput.value; // Change the input variable to match your input element's id

    const data = {
        message: encryptedMessage,
        key: key
    };
    
    fetch("http://localhost:8000/decrypt", { // Assuming you have an endpoint for decryption
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            ResultDecrypt.appendChild(document.createTextNode(data.decrypted_plain_text)); // Display the decrypted message
        })
        .catch((error) => {
            console.error("Error:", error);
            ResultDecrypt.textContent = "An error occurred while processing the request.";
        });
})
