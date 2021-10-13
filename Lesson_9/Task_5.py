class Stationary:
    def __init__(self, title="Something that an draw"):
        self.title = title

    def draw(self):
        print(f"Just start drawing! {self.title}")


class Pen(Stationary):
    def draw(self):
        print(f"Start drawing with {self.title} pen!")


class Pencil(Stationary):
    def draw(self):
        print(f"Start drawing with {self.title} pencil!")


class Marker(Stationary):
    def draw(self):
        print(f"Start drawing with {self.title} marker!")


stat = Stationary()
pen = Pen("Parker")
pencil = Pencil("Faber-Castell")
marker = Marker("COPIC")

office_suplies = [stat, pen, pencil, marker]

for i in office_suplies:
    i.draw()