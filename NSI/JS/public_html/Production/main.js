document.getElementById("red").oninput = function() {
  document.getElementById("red").style.background = "#" + convert(document.getElementById("red").value) + "00" + "00";
  update();
};
document.getElementById("green").oninput = function() {
  document.getElementById("green").style.background = "#00" + convert(document.getElementById("green").value) + "00";
  update();
};
document.getElementById("blue").oninput = function() {
  document.getElementById("blue").style.background = "#0000" + convert(document.getElementById("blue").value);
  update();
};
document.getElementById("submit").onclick = function() {
	update();
}

function convert(n) {
	if(isNaN(n)){
		console.log("Valeur Non entière")
		return;
	}
	if(n > 255 || n < 0){
		console.log("Valeur trop grande ou trop petite (0 < n < 255)")
		return;
	}
	final = ""
	codes = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
	final += codes[Math.floor(n / 16)]
	final += codes[Math.floor(n % 16)]
	return final
}
function update() {
	red = document.getElementById("red").value
	green = document.getElementById("green").value
	blue = document.getElementById("blue").value

	color = "#" + convert(red) + convert(green) + convert(blue)
	document.getElementById("result").style.backgroundColor = color;
	document.getElementById("code").innerHTML = "Code HEX : " + convert(red) + convert(green) + convert(blue);
}