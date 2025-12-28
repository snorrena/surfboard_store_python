class Surfboard:
	"""Simple Surfboard data class."""

	def __init__(self, brand: str, model: str, length: float, width: float):
		self.brand = brand
		self.model = model
		self.length = float(length)
		self.width = float(width)

	def print_info(self) -> None:
		"""Prints surfboard information to the terminal."""
		print(f"Brand: {self.brand}")
		print(f"Model: {self.model}")
		print(f"Length: {self.length}")
		print(f"Width: {self.width}")


if __name__ == "__main__":
	# Example usage
	sb = Surfboard("WaveCo", "Falcon", 6.5, 21.0)
	sb.print_info()
