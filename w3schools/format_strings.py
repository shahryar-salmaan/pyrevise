# Format Strings

color: str = "Blue"

msg: str = f"My fav color is {color}." # F-Strings

print(msg)

tax: int = 15

txt: str = f"The tax is {tax:.2f}" # F-String with a Modifier
print(txt)

txt: str = f"The double tax is {tax * 2}" # F-String with an expression
print(txt)
