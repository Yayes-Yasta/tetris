const height = 750;
const squareSize = height / 22;
let time = new Date();
let nextDrop = time.getTime() / 1000 + 1;
let timeDifference = 1;
let game;
let colors;
let currentTime;

function preload() {
  colors = [
    loadImage("images/purple.png"),
    loadImage("images/light_blue.png"),
    loadImage("images/yellow.png"),
    loadImage("images/orange.png"),
    loadImage("images/dark_blue.png"),
    loadImage("images/red.png"),
    loadImage("images/green.png"),
  ];
}

function setup() {
  createCanvas(height, height);
  game = new Game(height);
  textSize(16);
}

function keyPressed() {
  if (key === " ") game.dropping.rotate(game.setup);
  else if (key === "ArrowUp") game.up();
  else if (key === "ArrowRight") game.right();
  else if (key === "ArrowDown") {
    game.down();
    time = new Date();
    nextDrop = time.getTime() / 1000 + timeDifference;
  } else if (key === "ArrowLeft") game.left();
  else if (key === "c") game.switch();
}

function draw() {
  game.draw(height, squareSize);
  time = new Date();
  currentTime = time.getTime() / 1000;
  if (currentTime >= nextDrop) {
    nextDrop += timeDifference;
    timeDifference -= 0.000001;
    game.dropping ? game.drop() : game.startDrop();
  }
}
