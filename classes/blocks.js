class Block {
  constructor(img, x, y) {
    this.img = img;
    this.x = x;
    this.y = y;
  }

  draw(size, state, xOffset = 0) {
    const yOffset = xOffset == -0.5 ? 0.5 : 0;
    if (state === 0) {
      image(this.img, size * (this.x + 6), this.y * size + 1, size, size);
      return;
    }
    if (state === 1) {
      image(
        this.img,
        size * (this.x - 1.5 + xOffset),
        size * (this.y + 2 + yOffset) + 1,
        size,
        size
      );
      return;
    }
    if (xOffset === 0.5) xOffset = -0.5;
    image(
      this.img,
      size * (this.x + 14.5 + xOffset),
      size * (this.y + 2 + yOffset) + 1,
      size,
      size
    );
  }
}
