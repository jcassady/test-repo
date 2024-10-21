class Tire:
    def __init__(self, width, aspect_ratio, diameter):
        self.width = width
        self.aspect_ratio = aspect_ratio
        self.diameter = diameter

    def size(self):
        sidewall_height = (self.aspect_ratio / 100) * self.width
        overall_diameter = (2 * sidewall_height) + self.diameter
        return