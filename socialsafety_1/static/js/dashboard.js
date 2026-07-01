function activateSOS(){

let count = 3;

const status =
document.getElementById("sosStatus");

status.innerHTML =
"SOS activating in 3 seconds";

let timer = setInterval(()=>{

count--;

status.innerHTML =
"SOS activating in "
+ count +
" seconds";

if(count<=0){

clearInterval(timer);

status.innerHTML =
"🚨 SOS ACTIVATED";

alert(
"Emergency Alert Activated!"
);

}

},1000);

}

function getLocation(){

if(navigator.geolocation){

navigator.geolocation.getCurrentPosition(

function(position){

document.getElementById(
"locationText"
).innerHTML =

"Latitude: "
+ position.coords.latitude +

"<br>Longitude: "
+ position.coords.longitude;

}

);

}

}

function voiceSOS(){

const SpeechRecognition =
window.SpeechRecognition ||
window.webkitSpeechRecognition;

if(!SpeechRecognition){

alert(
"Voice recognition not supported."
);

return;
}

const recognition =
new SpeechRecognition();

recognition.start();

recognition.onresult =
function(event){

const speech =
event.results[0][0].transcript
.toLowerCase();

if(
speech.includes("i need help") ||
speech.includes("sos")
){

activateSOS();

}

};

}
