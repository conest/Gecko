class Vec2Int:
    x: int = 0
    y: int = 0

    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.set(x, y)
    
    def set(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y