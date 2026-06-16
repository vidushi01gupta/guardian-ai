console.log("SCRIPT LOADED");
function send() {
    console.log("SEND CLICKED");

    let message = document.getElementById("msg").value

    let chat = document.getElementById("chatbox")

    chat.innerHTML += `<div class="user">${message}</div>`

    if (navigator.geolocation) {

        navigator.geolocation.getCurrentPosition(function(position) {

            let latitude = position.coords.latitude
            let longitude = position.coords.longitude

            let location = latitude + "," + longitude
            console.log("ABOUT TO SEND FETCH");

            fetch("/chat", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({
                    message: message,
                    location: location
                })
            })
            .then(res => {
    console.log("FETCH RESPONSE:", res.status);
    return res.json();
})
.then(data => {
    console.log("DATA RECEIVED:", data);

    chat.innerHTML += `<div class="bot">${data.reply}</div>`;
    chat.scrollTop = chat.scrollHeight

                
                 
})
.catch(err => {
    console.error("FETCH ERROR:", err);
});
            
            

        })

    }

    document.getElementById("msg").value = ""
}

function voice() {

    const micBtn = document.getElementById("micBtn");
    const listeningStatus = document.getElementById("listeningStatus");
    const statusText = document.getElementById("statusText");

    micBtn.classList.add("mic-listening");
    listeningStatus.style.display = "block";
    statusText.innerText = "Listening... speak now";

    function callVoice(location) {
        fetch("/voice?location=" + encodeURIComponent(location))
        .then(res => res.json())
        .then(data => {
            const chat = document.getElementById("chatbox");

            if (data.user) {
                chat.innerHTML += `<div class="user">🎤 ${data.user}</div>`;
            }

            statusText.innerText = "Processing...";

            chat.innerHTML += `<div class="bot">${data.reply}</div>`;
            chat.scrollTop = chat.scrollHeight;

       
        })
        .catch(err => {
            console.log("Error:", err);
            statusText.innerText = "Something went wrong";
        })
        .finally(() => {
            micBtn.classList.remove("mic-listening");

            setTimeout(() => {
                listeningStatus.style.display = "none";
                statusText.innerText = "Click mic to speak";
            }, 1000);
        });
    }

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function(position) {
                let location =
                    position.coords.latitude + "," + position.coords.longitude;

                callVoice(location);
            },
            function(error) {
                callVoice("LOCATION_NOT_AVAILABLE");
            },
            {
                enableHighAccuracy: true,
                timeout: 5000,
                maximumAge: 0
            }
        );
    } else {
        callVoice("LOCATION_NOT_SUPPORTED");
    }
}

function speak(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "en-US";
    speechSynthesis.speak(utterance);
}