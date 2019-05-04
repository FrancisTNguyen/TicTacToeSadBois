class Scene:
    def __init__(self, director, background=(0, 0, 0)):
        self.director = director
        self.background = background

    def keydown(self, key):
        pass

    def keyup(self, key):
        pass

    def mousebuttondown(self, button, position):
        pass

    def reset(self):
        pass

    def update(self):
        pass

    def render(self):
        self.director.screen.fill(self.background)

    def exit(self):
        pass
