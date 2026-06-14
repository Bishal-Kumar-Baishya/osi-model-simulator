const progressionContainer = document.getElementById("progressionContainer");
const receivedMessage = document.getElementById("receivedMessage");

document.getElementById("sendForm").addEventListener("submit", function(e){
    e.preventDefault();
    const message = document.querySelector("input[name='message']").value;

    const formData = new FormData();
    formData.append("message", message)

    fetch("/send", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        for (let layername in data){
            let html = `<h3>${layername}</h3>`;
            html += `<pre>${JSON.stringify(data[layername])}</pre>`;

            progressionContainer.innerHTML += html;
        }
        const finalMessage = data["ApplicationLayer"]["data"];
        receivedMessage.innerHTML = `<p>${finalMessage}</p>`;
    })
    .catch(error => console.log("Error:", error))
})