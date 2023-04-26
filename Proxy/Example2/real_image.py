from image import Image

class RealImage(Image):
    def __init__(self, filename: str) -> None:
        self.filename = filename
    
    def real_image(self) -> None:
        self.load_from_disk(self.filename)
    
    def display(self) -> None:
        print(f"Displaying {self.filename}")
    
    def load_from_disk(self) -> None:
        print(f"Loading {self.filename}")

