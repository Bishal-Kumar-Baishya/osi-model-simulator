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
        for (let layername in data.encapsulation){
            let html = `<h3>${layername}</h3>`;
            html += `<pre>${JSON.stringify(data.encapsulation[layername])}</pre>`;

            progressionContainer.innerHTML += html;
        }
        const finalMessage = data["encapsulation"]["ApplicationLayer"]["data"];
        receivedMessage.innerHTML = `<p>${finalMessage}</p>`;

        for (let layername in data.decapsulation){
            let html = `<h3>${layername}</h3>`;
            if (typeof data.decapsulation[layername] === "string"){
                html += `<p>${data.decapsulation[layername]}</p>`;
            } else {
                html += `<pre>${JSON.stringify(data.decapsulation[layername], null, 2)}</pre>`;
            }

            progressionContainer.innerHTML += html;
        }
    })
    .catch(error => console.log("Error:", error))
})