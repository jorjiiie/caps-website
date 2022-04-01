var predictions = [];
var predictions2 = [];
var last = 0;
webgazer.setGazeListener((data, elapsedTime) => {
    if (data == null) {
        return;
    }
    var xprediction = data.x; //these x coordinates are relative to the viewport
    var yprediction = data.y; //these y coordinates are relative to the viewport
	//console.log(elapsedTime/1000, last);
	if ((elapsedTime/1000) > last) {
		last+=0.2;
		console.log(elapsedTime/1000.0,last,xprediction, yprediction);
	
//predictions.push(([xprediction, yprediction, elapsedTime/1000.0]));
		predictions2.push({"xprediction":xprediction, "yprediction": yprediction, "time" : elapsedTime/1000.0});
		predictions.push({"xprediction":xprediction, "yprediction": yprediction, "time" : elapsedTime/1000.0});
	
	}
	//:w
	//console.log(predictions);
}).begin();

function download(text, name, type) {
  var a = document.getElementById("a");
  var file = new Blob([text], {type: type});
  a.href = URL.createObjectURL(file);
  a.download = name;
}

var paused = false;
function pause() {
	var butt = document.getElementById("pause_button");

	if (paused) {
		butt.innerHTML = "Click to pause";
		webgazer.resume();
	} else {
		butt.innerHTML = "Click to resume";
		webgazer.pause();
	}
	paused = !paused;
}


function reset() {
	predictions = [];
}
webgazer.pause();
