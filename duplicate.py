
from pathlib import Path
import sys

folder = Path("b")
source = folder / "source.svg"

amount = int(sys.argv[1])

if amount < 1 or amount > 5000:
    raise ValueError("Choose between 1 and 5000 copies.")

if not source.exists():
    raise FileNotFoundError("b/source.svg is missing!")

original = source.read_bytes()
links = []

for i in range(1, amount + 1):
    filename = f"copy-{i}.svg"
    (folder / filename).write_bytes(original)

    url = (
        f"https://cdn.jsdelivr.net/gh/"
        f"bananas1234567/svg@main/b/{filename}"
    )
    links.append(url)

Path("links.txt").write_text("\n".join(links) + "\n")

print(f"Created {amount} SVG copies!")
print("Links saved in links.txt")
