function setup() {

  createCanvas(280, 280);
  background(0);
  let guessButton = select('#guess');
  guessButton.mousePressed(function() {
    let inputs = []
    let img = get();
    img.resize(25, 25);
    img.loadPixels();
    console.log(img.length)
    for (let i = 0; i <625; i++) {
      let bright = img.pixels[i * 4];
      inputs.push(bright/255.0);
    }
predict(inputs)
})
}
function draw() {
  strokeWeight(10);
  stroke(255);
  if (mouseIsPressed) {
    line(pmouseX, pmouseY, mouseX, mouseY);
}
}
function predict(inputs){
console.log(inputs)
}
