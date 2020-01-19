
async function getData(inputs){
  const response = await fetch("https://g-w1.github.io/first-ML/weights_biases.json");
  const data = await response.json();
  const ans = await JSON.parse(data);
  const mydata = await ans;
  var {weights,biases} = mydata;
  var weights = mydata.weights;
  var biases = mydata.biases;
  inputs = sigmoid(math.add(math.multiply(weights[0],inputs),biases[0]));
  output = sigmoid(math.add(math.multiply(weights[1],inputs),biases[1]));
  if (output[1]<output[0]){
  document.getElementById("header").innerHTML = "Smiley Face";
  return "smiely";

      }else{
           document.getElementById("header").innerHTML = "Frowney Face";
           return "frowney";
      }
  return {weights,biases};
}
getData();
function setup() {
  
  var canv = createCanvas(500, 500);
  canv.parent("canvas");
  background(0);
  let guessButton = select('#guess');
  guessButton.mousePressed(function() {
    let inputs = []
    let img = get();
    img.resize(25, 25);
    img.loadPixels();
    for (let i = 0; i <625; i++) {
      let bright = img.pixels[i * 4];
      inputs.push([bright/255.0]);

    }
console.log(predict(inputs))
})
  let clearButton = select("#clear");
  clearButton.mousePressed(function(){
      background(0);
      document.getElementById("header").innerHTML = "Draw a Smiley face or a Frowney face and hit guess to make the computer classify it";
  })
}
function draw() {
  strokeWeight(60);
  stroke(255);
  if (mouseIsPressed) {
    line(pmouseX, pmouseY, mouseX, mouseY);
}
}
function predict(inputs){
  getData(inputs);
      
}
function sigmoid(z){

        return math.map(z,function(value){
            return 1/(1+math.exp(value*-1))
        })
}
