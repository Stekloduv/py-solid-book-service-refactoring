def display(self, display_type: str) -> None:
    if display_type == "console":
        print(self.content)
    elif display_type == "reverse":
        print(self.content[::-1])
    else:
        raise ValueError(f"Unknown display type: {display_type}")