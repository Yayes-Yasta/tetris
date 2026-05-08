const tetrominoes = [T, Straight, Square, J, L, Z, S];

class Game {
  constructor(height) {
    let board = [];
    for (let i = 0; i < 22; i++) {
      board.push([]);
      for (let j = 0; j < 10; j++) {
        board[i].push(null);
      }
    }
    this.setup = board;
    this.height = height;
    let rows = [];
    rows.length = 22;
    rows.fill(0);
    this.rows = rows;
    this.dropping = this.getRandomTetromino();
    this.next = this.getRandomTetromino();
    this.holding = null;
    this.switchAllowed = true;
  }

  getRandomTetromino() {
    let index = floor(random(7));
    return new tetrominoes[index](colors[index], this.height / 22, this.setup);
  }

  up() {
    while (true) {
      if (this.drop() === 0) break;
    }
  }

  right() {
    for (let square of this.dropping.squares) {
      if (square.x + 1 > 9 || this.setup[square.y][square.x + 1]) return;
    }
    for (let square of this.dropping.squares) square.x += 1;
  }

  down() {
    this.drop();
  }

  left() {
    for (let square of this.dropping.squares) {
      if (square.x - 1 < 0 || this.setup[square.y][square.x - 1]) return;
    }
    for (let square of this.dropping.squares) square.x -= 1;
  }

  switch() {
    if (this.switchAllowed) {
      this.switchAllowed = false;
      console.log(this.dropping.squares[0].img);
      console.log(this.dropping.reset);
      this.dropping.reset();
      if (this.holding) {
        let temp = this.holding;
        this.holding = this.dropping;
        this.dropping = temp;
        return;
      }
      console.log(this.dropping.squares[0].img);
      this.holding = this.dropping;
      console.log(this.holding.squares[0].img);
      this.dropping = this.getRandomTetromino();
      console.log("a");
    }
  }

  draw(height, squareSize) {
    background(BACKGROUND);
    for (let row of this.setup) {
      for (let square of row) {
        if (square) square.draw(squareSize, 0, undefined);
      }
    }

    this.dropping.draw(squareSize);
    let x = squareSize * 6;
    // left line of the board
    stroke(LINES);
    line(x, 0, x, height);
    // HOLD section
    fill(BACKGROUND);
    rect(0, 1, x, x);
    noStroke();
    fill(LINES);
    text("HOLD:", 1, 14);
    if (this.holding) this.holding.draw(squareSize, 1);

    stroke(LINES);
    line(x, height, x + squareSize * 10, height);
    // right line of the board
    x = squareSize * 16;
    line(x, 1, x, height);
    // NEXT section
    noFill();
    rect(x, 0, height - x, height - x);
    noStroke();
    fill(LINES);
    text("NEXT:", x + 1, 14);
    this.next.draw(squareSize, 2);
  }

  drop() {
    for (let block of this.dropping.squares) {
      if (block.y >= 21 || this.setup[block.y + 1][block.x]) {
        this.startDrop();
        return 0;
      }
    }
    this.dropping.drop();
  }

  startDrop() {
    this.addToRows();
    for (let block of this.dropping.squares)
      this.setup[block.y][block.x] = block;
    this.dropping = this.next;
    this.next = this.getRandomTetromino();
    this.fullRow();
    this.switchAllowed = true;
  }

  addToRows() {
    for (let square of this.dropping.squares) this.rows[square.y]++;
  }

  fullRow() {
    for (let row = 0; row < 22; row++) {
      if (this.rows[row] === 10) {
        this.rows[row] = 0;
        this.setup.splice(row, 1);
        let insert = [];
        insert.length = 10;
        insert.fill(null);
        this.setup.unshift(insert);
        this.rows.splice(row, 1);
        this.rows.unshift(0);
        for (let i = 0; i <= row; i++) {
          for (let j = 0; j < 10; j++) {
            if (this.setup[i][j]) this.setup[i][j].y++;
          }
        }
      }
    }
  }
  static lose() {
    console.log("you lost");
  }
}
