"""Every tetromino consists of 4 squares"""


class Block:
    """Every square is stored in an array inside the board-object"""

    def __init__(self, img, x, y):
        self.img = img
        self.x = x
        self.y = y

    def draw(self, window, size, state, x_offset=0):
        """A single square is drawn here"""
        y_offset = 0.5 if x_offset == -0.5 else 0
        if state == 0:
            window.blit(self.img, (self.x * size + size * 6, self.y * size + 1))
            return
        if state == 1:
            window.blit(self.img, (size * (self.x - 1.5 + x_offset), self.y * size + size * 2 + 1 + y_offset * size))
            return
        window.blit(self.img, (size * (self.x + 14.5 + x_offset), size * (self.y + 2 + y_offset) + 1))
