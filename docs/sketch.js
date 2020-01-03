function setup() {
  createCanvas(280, 280);
  background(200);
  let guessButton = select('#guess');
  guessButton.mousePressed(function() {
    let inputs = [];
    let img = get();
    img.resize(25, 25);
    img.loadPixels();
    for (let i = 0; i < img.length; i++) {
      let bright = img.pixels[i * 4];
      inputs[i] = (255 - bright) / 255.0;
      console.log(inputs)
    }})}
function draw() {
  strokeWeight(10);
  stroke(0);
  if (mouseIsPressed) {
    line(pmouseX, pmouseY, mouseX, mouseY);
}}
