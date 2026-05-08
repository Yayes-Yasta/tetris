class Tetromino {
  constructor(color, size, xOffset = 0) {
    this.color = color;
    this.rotatingState = 0;
    this.xOffset = xOffset;
  }

  rotate(setup) {}

  draw(size, state = 0) {
    // state 0: on board
    // state 1: holding
    // state 2: next
    for (let block of this.squares) block.draw(size, state, this.xOffset);
  }

  drop() {
    for (let block of this.squares) block.y++;
  }

  checkLost(setup) {
    for (let block of this.squares) {
      if (setup[block.y][block.x]) {
        Game.lose();
        return;
      }
    }
  }
}

class Square extends Tetromino {
  constructor(color, size, board) {
    super(color, size, 0.5);
    this.squares = [
      new Block(color, 4, 0),
      new Block(color, 5, 0),
      new Block(color, 4, 1),
      new Block(color, 5, 1),
    ];
    this.checkLost(board);
  }

  reset() {
    console.log(this.color);
    this.squares = [
      new Block(this.color, 3, 0),
      new Block(this.color, 4, 0),
      new Block(this.color, 3, 1),
      new Block(this.color, 4, 1),
    ];
    this.rotatingState = 0;
  }
}

class Straight extends Tetromino {
  constructor(color, size, board) {
    super(color, size, -0.5);
    this.squares = [
      new Block(color, 3, 0),
      new Block(color, 4, 0),
      new Block(color, 5, 0),
      new Block(color, 6, 0),
    ];
    this.checkLost(board);
  }

  reset() {
    this.squares = [
      new Block(this.color, 3, 0),
      new Block(this.color, 4, 0),
      new Block(this.color, 5, 0),
      new Block(this.color, 6, 0),
    ];
    this.rotatingState = 0;
  }

  rotate(setup) {
    if (this.rotatingState === 0) {
      if (
        this.squares[0].x + 2 <= 9 &&
        this.squares[1].x + 1 <= 9 &&
        0 <= this.squares[3].x - 1 &&
        0 <= this.squares[0].y - 1 &&
        this.squares[2].y + 1 < 22 &&
        this.squares[3].y + 2 < 22
      ) {
        if (
          !setup[this.squares[0].y - 1][this.squares[0].x + 2] &&
          !setup[this.squares[2].y + 1][this.squares[2].x] &&
          !setup[this.squares[1].y][this.squares[1].x + 1] &&
          !setup[this.squares[3].y + 2][this.squares[3].x - 1]
        )
          this.rotatingState = 1;
        this.squares[0].x += 2;
        this.squares[0].y -= 1;
        this.squares[1].x += 1;
        this.squares[2].y += 1;
        this.squares[3].x -= 1;
        this.squares[3].y += 2;
      }
    } else if (this.rotatingState === 1) {
      if (
        0 <= this.squares[0].x - 2 &&
        0 <= this.squares[1].x - 1 &&
        this.squares[3].x + 1 <= 9 &&
        this.squares[0].y + 2 < 22 &&
        this.squares[1].y + 1 < 22 &&
        0 <= this.squares[3].y - 1
      ) {
        if (
          !setup[this.squares[0].y + 2][this.squares[0].x - 2] &&
          !setup[this.squares[1].y + 1][this.squares[1].x - 1] &&
          !setup[this.squares[3].y - 1][this.squares[3].x + 1]
        ) {
          this.rotatingState = 2;
          this.squares[0].x -= 2;
          this.squares[0].y += 2;
          this.squares[1].x -= 1;
          this.squares[1].y += 1;
          this.squares[3].x += 1;
          this.squares[3].y -= 1;
        }
      }
    } else if (this.rotatingState === 2) {
      if (
        this.squares[0].x + 1 <= 9 &&
        0 <= this.squares[2].x - 1 &&
        0 <= this.squares[3].x - 2 &&
        this.squares[0].y + 1 < 22 &&
        0 <= this.squares[2].y - 1 &&
        0 <= this.squares[3].y - 2
      )
        if (
          !setup[this.squares[0].y + 1][this.squares[0].x + 1] &&
          !setup[this.squares[2].y - 1][this.squares[2].x - 1] &&
          !setup[this.squares[3].y - 2][this.squares[3].x - 2]
        ) {
          this.rotatingState = 3;
          this.squares[0].x += 1;
          this.squares[0].y += 1;
          this.squares[2].x -= 1;
          this.squares[2].y -= 1;
          this.squares[3].x -= 2;
          this.squares[3].y -= 2;
        }
    } else if (
      0 <= this.squares[0].x - 1 &&
      this.squares[2].x + 1 <= 9 &&
      this.squares[3].x + 2 <= 9 &&
      0 <= this.squares[0].y - 2 &&
      0 <= this.squares[1].y - 1 &&
      this.squares[3].y + 1 < 22
    ) {
      if (
        !setup[this.squares[0].y - 2][this.squares[0].x - 1] &&
        !setup[this.squares[1].y - 1][this.squares[1].x] &&
        !setup[this.squares[2].y][this.squares[2].x + 1] &&
        !setup[this.squares[3].y + 1][this.squares[3].x + 2]
      )
        this.rotatingState = 0;
      this.squares[0].x -= 1;
      this.squares[0].y -= 2;
      this.squares[1].y -= 1;
      this.squares[2].x += 1;
      this.squares[3].x += 2;
      this.squares[3].y += 1;
    }
  }
}

class T extends Tetromino {
  constructor(color, size, board) {
    super(color, size);
    this.squares = [
      new Block(color, 4, 0),
      new Block(color, 3, 1),
      new Block(color, 4, 1),
      new Block(color, 5, 1),
    ];
    this.checkLost(board);
  }

  rotate(setup) {
    if (this.rotatingState === 0) {
      if (this.squares[1].x + 1 <= 9 && this.squares[1].y + 1 < 22)
        if (!setup[this.squares[1].y + 1][this.squares[1].x + 1]) {
          this.rotatingState = 1;
          this.squares[1].x += 1;
          this.squares[1].y += 1;
        }
    } else if (this.rotatingState === 1) {
      if (this.squares[0].x - 1 >= 0 && this.squares[0].y + 1 < 22) {
        if (!setup[this.squares[0].y + 1][this.squares[0].x - 1]) {
          this.rotatingState = 2;
          this.squares[0].x -= 1;
          this.squares[0].y += 1;
        }
      }
    } else if (this.rotatingState === 2) {
      if (this.squares[3].x - 1 >= 0 && this.squares[3].y - 1 >= 0)
        if (!setup[this.squares[3].y - 1][this.squares[3].x - 1]) {
          this.rotatingState = 3;
          this.squares[3].x -= 1;
          this.squares[3].y -= 1;
        }
    } else if (
      this.squares[0].x + 1 <= 9 &&
      this.squares[1].x - 1 >= 0 &&
      this.squares[3].x + 1 <= 9 &&
      this.squares[0].y - 1 < 22 &&
      this.squares[1].y - 1 < 22 &&
      this.squares[3].y + 1 > 0
    ) {
      if (
        !setup[this.squares[0].y - 1][this.squares[0].x + 1] &&
        !setup[this.squares[1].y - 1][this.squares[1].x - 1] &&
        !setup[this.squares[3].y + 1][this.squares[3].x + 1]
      ) {
        this.rotatingState = 0;
        this.squares[0].x += 1;
        this.squares[0].y -= 1;
        this.squares[1].x -= 1;
        this.squares[1].y -= 1;
        this.squares[3].x += 1;
        this.squares[3].y += 1;
      }
    }
  }

  reset() {
    this.squares = [
      new Block(this.color, 4, 0),
      new Block(this.color, 3, 1),
      new Block(this.color, 4, 1),
      new Block(this.color, 5, 1),
    ];
    this.rotatingState = 0;
  }
}

class J extends Tetromino {
  constructor(color, size, board) {
    super(color, size);
    this.squares = [
      new Block(color, 3, 0),
      new Block(color, 3, 1),
      new Block(color, 4, 1),
      new Block(color, 5, 1),
    ];
    this.checkLost(board);
  }

  rotate(setup) {
    if (this.rotatingState === 0) {
      if (
        this.squares[0].x + 2 < 10 &&
        this.squares[1].x + 1 < 10 &&
        this.squares[3].x - 1 < 10 &&
        this.squares[1].y - 1 >= 0 &&
        this.squares[3].y + 1 < 22
      ) {
        if (
          !setup[this.squares[0].y][this.squares[0].x + 2] &&
          !setup[this.squares[1].y - 1][this.squares[1].x + 1] &&
          !setup[this.squares[3].y + 1][this.squares[3].x - 1]
        ) {
          this.rotatingState = 1;
          this.squares[0].x += 2;
          this.squares[1].x += 1;
          this.squares[1].y -= 1;
          this.squares[3].x -= 1;
          this.squares[3].y += 1;
        }
      }
    } else if (this.rotatingState === 1) {
      if (
        this.squares[1].x + 1 < 10 &&
        this.squares[3].x - 1 >= 0 &&
        this.squares[0].y + 2 < 22 &&
        this.squares[1].y + 1 < 22 &&
        this.squares[3].y - 1 >= 0
      ) {
        if (
          !setup[this.squares[0].y + 2][this.squares[0].x] &&
          !setup[this.squares[1].y + 1][this.squares[1].x + 1] &&
          !setup[this.squares[3].y + 1][this.squares[3].x - 1]
        ) {
          this.rotatingState = 2;
          this.squares[0].y += 2;
          this.squares[1].x += 1;
          this.squares[1].y += 1;
          this.squares[3].x -= 1;
          this.squares[3].y -= 1;
        }
      }
    } else if (this.rotatingState === 2) {
      if (
        this.squares[0].x - 2 >= 0 &&
        this.squares[1].x - 1 >= 0 &&
        this.squares[3].x + 1 < 10 &&
        this.squares[1].y + 1 < 22 &&
        this.squares[3].y - 1 >= 0
      ) {
        if (
          !setup[this.squares[0].y][this.squares[0].x - 2] &&
          !setup[this.squares[1].y + 1][this.squares[1].x - 1] &&
          !setup[this.squares[3].y - 1][this.squares[3].x + 1]
        ) {
          this.rotatingState = 3;
          this.squares[0].x -= 2;
          this.squares[1].x -= 1;
          this.squares[1].y += 1;
          this.squares[3].x += 1;
          this.squares[3].y -= 1;
        }
      }
    } else if (
      this.squares[1].x - 1 >= 0 &&
      this.squares[3].x + 1 < 10 &&
      this.squares[0].y - 2 >= 0 &&
      this.squares[1].y - 1 >= 0 &&
      this.squares[3].y + 1 < 22
    ) {
      if (
        !setup[this.squares[0].y - 2][this.squares[0].x] &&
        !setup[this.squares[1].y - 1][this.squares[1].x - 1] &&
        !setup[this.squares[3].y + 1][this.squares[3].x + 1]
      ) {
        this.rotatingState = 0;
        this.squares[0].y -= 2;
        this.squares[1].x -= 1;
        this.squares[1].y -= 1;
        this.squares[3].x += 1;
        this.squares[3].y += 1;
      }
    }
  }

  reset() {
    this.squares = [
      new Block(this.color, 3, 0),
      new Block(this.color, 3, 1),
      new Block(this.color, 4, 1),
      new Block(this.color, 5, 1),
    ];
    this.rotatingState = 0;
  }
}

class L extends Tetromino {
  constructor(color, size, board) {
    super(color, size);
    this.squares = [
      new Block(color, 5, 0),
      new Block(color, 5, 1),
      new Block(color, 4, 1),
      new Block(color, 3, 1),
    ];
    this.checkLost(board);
  }

  reset() {
    this.squares = [
      new Block(this.color, 5, 0),
      new Block(this.color, 5, 1),
      new Block(this.color, 4, 1),
      new Block(this.color, 3, 1),
    ];
    this.rotatingState = 0;
  }

  rotate(setup) {
    if (this.rotatingState === 0) {
      if (
        this.squares[1].x - 1 >= 0 &&
        this.squares[3].x + 1 < 10 &&
        this.squares[0].y + 2 < 22 &&
        this.squares[1].y + 1 < 22 &&
        this.squares[3].y - 1 >= 0
      ) {
        if (
          !setup[this.squares[0].y + 2][this.squares[0].x] &&
          !setup[this.squares[1].y + 1][this.squares[1].x - 1] &&
          !setup[this.squares[3].y - 1][this.squares[3].x + 1]
        ) {
          this.rotatingState = 1;
          this.squares[0].y += 2;
          this.squares[1].x -= 1;
          this.squares[1].y += 1;
          this.squares[3].x += 1;
          this.squares[3].y -= 1;
        }
      }
    } else if (this.rotatingState === 1) {
      if (
        this.squares[0].x - 2 >= 0 &&
        this.squares[1].x - 1 >= 0 &&
        this.squares[3].x + 1 < 10 &&
        this.squares[1].y - 1 >= 0 &&
        this.squares[3].y + 1 < 22
      ) {
        if (
          !setup[this.squares[0].y][this.squares[0].x - 2] &&
          !setup[this.squares[1].y - 1][this.squares[1].x - 1] &&
          !setup[this.squares[3].y + 1][this.squares[3].x + 1]
        ) {
          this.rotatingState = 2;
          this.squares[0].x -= 2;
          this.squares[1].x -= 1;
          this.squares[1].y -= 1;
          this.squares[3].x += 1;
          this.squares[3].y += 1;
        }
      }
    } else if (this.rotatingState === 2) {
      if (
        this.squares[1].x + 1 < 10 &&
        this.squares[3].x - 1 >= 0 &&
        this.squares[0].y - 2 >= 0 &&
        this.squares[1].y - 1 >= 0 &&
        this.squares[3].y + 1 < 22
      ) {
        if (
          !setup[this.squares[0].y - 2][this.squares[0].x] &&
          !setup[this.squares[1].y - 1][this.squares[1].x + 1] &&
          !setup[this.squares[3].y + 1][this.squares[3].x - 1]
        ) {
          this.rotatingState = 3;
          this.squares[0].y -= 2;
          this.squares[1].x += 1;
          this.squares[1].y -= 1;
          this.squares[3].x -= 1;
          this.squares[3].y += 1;
        }
      }
    } else if (
      this.squares[0].x + 2 < 10 &&
      this.squares[1].x + 1 < 10 &&
      this.squares[3].x - 1 >= 0 &&
      this.squares[1].y + 1 < 22 &&
      this.squares[3].y - 1 >= 0
    ) {
      if (
        !setup[this.squares[0].y][this.squares[0].x + 2] &&
        !setup[this.squares[1].y + 1][this.squares[1].x + 1] &&
        !setup[this.squares[3].y - 1][this.squares[3].x - 1]
      ) {
        this.rotatingState = 0;
        this.squares[0].x += 2;
        this.squares[1].x += 1;
        this.squares[1].y += 1;
        this.squares[3].x -= 1;
        this.squares[3].y -= 1;
      }
    }
  }
}

class S extends Tetromino {
  constructor(color, size, board) {
    super(color, size);
    this.squares = [
      new Block(color, 5, 0),
      new Block(color, 4, 0),
      new Block(color, 4, 1),
      new Block(color, 3, 1),
    ];
    this.checkLost(board);
  }

  reset() {
    this.squares = [
      new Block(this.color, 5, 0),
      new Block(this.color, 4, 0),
      new Block(this.color, 4, 1),
      new Block(this.color, 3, 1),
    ];
    this.rotatingState = 0;
  }

  rotate(setup) {
    if (this.rotatingState === 0) {
      if (
        this.squares[1].x + 1 < 10 &&
        this.squares[3].x + 1 < 10 &&
        this.squares[0].y + 2 < 22 &&
        this.squares[1].y + 1 < 22 &&
        this.squares[3].y - 1 >= 0
      ) {
        if (
          !setup[this.squares[0].y + 2][this.squares[0].x] &&
          !setup[this.squares[1].y + 1][this.squares[1].x + 1] &&
          !setup[this.squares[3].y - 1][this.squares[3].x + 1]
        ) {
          this.rotatingState = 1;
          this.squares[0].y += 2;
          this.squares[1].x += 1;
          this.squares[1].y += 1;
          this.squares[3].x += 1;
          this.squares[3].y -= 1;
        }
      }
    } else if (this.rotatingState === 1) {
      if (
        this.squares[0].x - 2 >= 0 &&
        this.squares[1].x - 1 >= 0 &&
        this.squares[3].x + 1 < 10 &&
        this.squares[1].y + 1 < 22 &&
        this.squares[3].y + 1 < 22
      ) {
        if (
          !setup[this.squares[0].y][this.squares[0].x - 2] &&
          !setup[this.squares[1].y + 1][this.squares[1].x - 1] &&
          !setup[this.squares[3].y + 1][this.squares[3].x + 1]
        ) {
          this.rotatingState = 2;
          this.squares[0].x -= 2;
          this.squares[1].x -= 1;
          this.squares[1].y += 1;
          this.squares[3].x += 1;
          this.squares[3].y += 1;
        }
      }
    } else if (this.rotatingState === 2) {
      if (
        this.squares[1].x - 1 >= 0 &&
        this.squares[3].x - 1 >= 0 &&
        this.squares[0].y - 2 >= 0 &&
        this.squares[1].y - 1 >= 0 &&
        this.squares[3].y + 1 >= 0
      ) {
        if (
          !setup[this.squares[0].y - 2][this.squares[0].x] &&
          !setup[this.squares[1].y - 1][this.squares[1].x - 1] &&
          !setup[this.squares[3].y + 1][this.squares[3].x - 1]
        ) {
          this.rotatingState = 3;
          this.squares[0].y -= 2;
          this.squares[1].x -= 1;
          this.squares[1].y -= 1;
          this.squares[3].x -= 1;
          this.squares[3].y += 1;
        }
      }
    } else if (
      this.squares[0].x + 2 < 10 &&
      this.squares[1].x + 1 < 10 &&
      this.squares[3].x - 1 >= 0 &&
      this.squares[1].y - 1 >= 0 &&
      this.squares[3].y - 1 >= 0
    ) {
      if (
        !setup[this.squares[0].y][this.squares[0].x + 2] &&
        !setup[this.squares[1].y - 1][this.squares[1].x + 1] &&
        !setup[this.squares[3].y - 1][this.squares[3].x - 1]
      ) {
        this.rotatingState = 0;
        this.squares[0].x += 2;
        this.squares[1].x += 1;
        this.squares[1].y -= 1;
        this.squares[3].x -= 1;
        this.squares[3].y -= 1;
      }
    }
  }
}

class Z extends Tetromino {
  constructor(color, size, board) {
    super(color, size);
    this.squares = [
      new Block(color, 3, 0),
      new Block(color, 4, 0),
      new Block(color, 4, 1),
      new Block(color, 5, 1),
    ];
    this.checkLost(board);
  }

  reset() {
    this.squares = [
      new Block(this.color, 3, 0),
      new Block(this.color, 4, 0),
      new Block(this.color, 4, 1),
      new Block(this.color, 5, 1),
    ];
    this.rotatingState = 0;
  }

  rotate(setup) {
    if (this.rotatingState === 0) {
      if (
        this.squares[0].x + 2 < 10 &&
        this.squares[1].x + 1 < 10 &&
        this.squares[3].x - 1 >= 0 &&
        this.squares[1].y + 1 < 22 &&
        this.squares[3].y + 1 < 22
      ) {
        if (
          !setup[this.squares[0].y][this.squares[0].x + 2] &&
          !setup[this.squares[1].y + 1][this.squares[1].x + 1] &&
          !setup[this.squares[3].y + 1][this.squares[3].x - 1]
        ) {
          this.rotatingState = 1;
          this.squares[0].x += 2;
          this.squares[1].x += 1;
          this.squares[1].y += 1;
          this.squares[3].x -= 1;
          this.squares[3].y += 1;
        }
      }
    } else if (this.rotatingState === 1) {
      if (
        this.squares[1].x - 1 >= 0 &&
        this.squares[3].x - 1 >= 0 &&
        this.squares[0].y + 2 < 22 &&
        this.squares[1].y + 1 < 22 &&
        this.squares[3].y - 1 >= 0
      ) {
        if (
          !setup[this.squares[0].y + 2][this.squares[0].x] &&
          !setup[this.squares[1].y + 1][this.squares[1].x - 1] &&
          !setup[this.squares[3].y - 1][this.squares[3].x - 1]
        ) {
          this.rotatingState = 2;
          this.squares[0].y += 2;
          this.squares[1].x -= 1;
          this.squares[1].y += 1;
          this.squares[3].x -= 1;
          this.squares[3].y -= 1;
        }
      }
    } else if (this.rotatingState === 2) {
      if (
        this.squares[0].x - 2 >= 0 &&
        this.squares[1].x - 1 >= 0 &&
        this.squares[3].x + 1 < 10 &&
        this.squares[1].y - 1 >= 0 &&
        this.squares[3].y - 1 >= 0
      ) {
        if (
          !setup[this.squares[0].y][this.squares[0].x - 2] &&
          !setup[this.squares[1].y - 1][this.squares[1].x - 1] &&
          !setup[this.squares[3].y - 1][this.squares[3].x + 1]
        ) {
          this.rotatingState = 3;
          this.squares[0].x -= 2;
          this.squares[1].x -= 1;
          this.squares[1].y -= 1;
          this.squares[3].x += 1;
          this.squares[3].y -= 1;
        }
      }
    } else if (
      this.squares[1].x + 1 < 10 &&
      this.squares[3].x + 1 < 10 &&
      this.squares[0].y - 2 >= 0 &&
      this.squares[1].y - 1 >= 0 &&
      this.squares[3].y + 1 < 22
    ) {
      if (
        !setup[this.squares[0].y - 2][this.squares[0].x] &&
        !setup[this.squares[1].y - 1][this.squares[1].x + 1] &&
        !setup[this.squares[3].y + 1][this.squares[3].x + 1]
      ) {
        this.rotatingState = 0;
        this.squares[0].y -= 2;
        this.squares[1].x += 1;
        this.squares[1].y -= 1;
        this.squares[3].x += 1;
        this.squares[3].y += 1;
      }
    }
  }
}
