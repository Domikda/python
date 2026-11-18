# Print obrazku z 1 a 0

picture = [
    "00111100",
    "01100110",
    "11000011",
    "11000011",
    "11000011",
    "01100110",
    "00111100",
    "00000000",
]

# AI pomoc
for row in picture:
    print("".join("██" if pixel == "1" else "  " for pixel in row))     
