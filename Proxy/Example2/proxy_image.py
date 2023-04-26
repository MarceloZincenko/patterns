from image import Image
from real_image import RealImage

class ProxyImage(Image):

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.real_image = RealImage(filename)

    def display(self) -> None:
        self.real_image.display()