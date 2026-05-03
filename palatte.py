import colorsys
from PIL import Image
from tkinter import Tk, filedialog
import webbrowser

#HELPERS

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16)/255 for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return '#' + ''.join(f'{int(c*255):02x}' for c in rgb)

def rgb_to_hsl(rgb):
    return colorsys.rgb_to_hls(*rgb)

def hsl_to_rgb(hsl):
    return colorsys.hls_to_rgb(*hsl)

#COLOR LOGIC

def adjust_lightness(hsl, factor):
    h, l, s = hsl
    l = max(0, min(1, l * factor))
    return (h, l, s)

def shift_hue(hsl, degree):
    h, l, s = hsl
    h = (h + degree/360) % 1
    return (h, l, s)

#CONTRAST 
def get_text_color(bg_rgb):
    r, g, b = bg_rgb
    luminance = 0.299*r + 0.587*g + 0.114*b
    return '#000000' if luminance > 0.5 else '#ffffff'

#IMAGE COLOR

def get_dominant_color(image_path):
    img = Image.open(image_path)
    img = img.resize((100, 100))
    pixels = list(img.getdata())

    avg = tuple(sum(c)/len(c)/255 for c in zip(*pixels))
    return rgb_to_hex(avg)

#THEME GENERATOR

def generate_theme(base_hex):
    base_hex = base_hex[:7]  # remove alpha if exists

    rgb = hex_to_rgb(base_hex)
    hsl = rgb_to_hsl(rgb)

    bg = rgb_to_hex(hsl_to_rgb(adjust_lightness(hsl, 0.4)))
    primary = base_hex
    secondary = rgb_to_hex(hsl_to_rgb(shift_hue(hsl, 30)))
    accent = rgb_to_hex(hsl_to_rgb(shift_hue(hsl, 180)))
    text = get_text_color(hex_to_rgb(bg))

    return {
        "background": bg,
        "primary": primary,
        "secondary": secondary,
        "accent": accent,
        "text": text
    }

#COLOR THEORY

def get_color_theory(hex_color):
    rgb = hex_to_rgb(hex_color)
    h, l, s = rgb_to_hsl(rgb)

    def make(deg):
        return rgb_to_hex(hsl_to_rgb(((h + deg/360) % 1, l, s)))

    return {
        "Complementary": [hex_color, make(180)],
        "Analogous": [make(-30), hex_color, make(30)],
        "Triadic": [hex_color, make(120), make(240)]
    }

#HTML PREVIEW

def export_html(theme, base_color, image_path=None):
    combos = get_color_theory(base_color)

    img_tag = ""
    if image_path:
        img_tag = f'<img src="file:///{image_path.replace("\\\\","/")}" class="preview-img"/>'

    def render_combo(name, colors):
        blocks = "".join([f'<div class="swatch" style="background:{c}">{c}</div>' for c in colors])
        return f"<h4>{name}</h4><div class='row'>{blocks}</div>"

    combos_html = "".join([render_combo(k, v) for k, v in combos.items()])

    html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Smart Theme</title>

<style>
body {{
  font-family: 'Comfortaa', cursive;
  background: {theme['background']};
  color: {theme['text']};
  padding: 20px;
}}

.container {{
  display: flex;
  gap: 20px;
}}

.card {{
  background: {theme['primary']};
  padding: 20px;
  border-radius: 12px;
  flex: 1;

}}

.preview-img {{
  width: 100%;
  border-radius: 18px;
}}

.row {{
  display: flex;
  gap: 10px;
  margin-bottom: 15px;
}}

.swatch {{
  padding: 20px;
  border-radius: 8px;
  color: white;
  font-size: 12px;
  text-align: center;
  font-weight: bold;
}}

.wheel-container {{
  text-align: center;
  margin-top: 20px;
}}

canvas {{
  border-radius: 50%;
  cursor: crosshair;
}}
</style>

</head>

<body>

<h1>Smart Theme Generator</h1>

<div class="container">

  <div class="card">
    <h3>Image Preview</h3>
    {img_tag if img_tag else "<p>No image</p>"}
  </div>

  <div class="card">
    <h3>Theme Colors</h3>

    <div class="row">
      <div class="swatch" style="background:{theme['primary']}">
        Primary<br>{theme['primary']}
      </div>

      <div class="swatch" style="background:{theme['secondary']}">
        Secondary<br>{theme['secondary']}
      </div>

      <div class="swatch" style="background:{theme['accent']}">
        Accent<br>{theme['accent']}
      </div>
    </div>

    <button style="background:{theme['accent']};padding:10px;border:none;border-radius:6px;color:white;">
      Sample Button
    </button>
  </div>

</div>

<h2>Clickable Color Wheel</h2>

<div class="wheel-container">
  <canvas id="colorWheel" width="250" height="250"></canvas>
  <p>Selected Color: <span id="selectedColor">#000000</span></p>
</div>

<h2>Color Combinations</h2>
{combos_html}

<script>
const canvas = document.getElementById("colorWheel");
const ctx = canvas.getContext("2d");

const radius = canvas.width / 2;

// Draw wheel
function drawWheel() {{
  for (let angle = 0; angle < 360; angle++) {{
    const start = (angle - 1) * Math.PI / 180;
    const end = angle * Math.PI / 180;

    ctx.beginPath();
    ctx.moveTo(radius, radius);
    ctx.arc(radius, radius, radius, start, end);
    ctx.closePath();

    ctx.fillStyle = "hsl(" + angle + ", 100%, 50%)";
    ctx.fill();
  }}
}}

drawWheel();

// Marker
function drawMarker(x, y) {{
  drawWheel();

  ctx.beginPath();
  ctx.arc(x, y, 6, 0, 2 * Math.PI);
  ctx.fillStyle = "#ffffff";
  ctx.fill();

  ctx.strokeStyle = "#000000";
  ctx.lineWidth = 2;
  ctx.stroke();
}}

// Click
canvas.addEventListener("click", function(e) {{
  const rect = canvas.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;

  const pixel = ctx.getImageData(x, y, 1, 1).data;
  const hex = rgbToHex(pixel[0], pixel[1], pixel[2]);

  document.getElementById("selectedColor").innerText = hex;

  drawMarker(x, y);
}});

// HEX
function rgbToHex(r, g, b) {{
  return "#" + [r,g,b].map(x =>
    x.toString(16).padStart(2, "0")
  ).join("");
}}
</script>
</body>
</html>
"""

    with open("preview.html", "w", encoding="utf-8") as f:
        f.write(html)

    webbrowser.open("preview.html")

# ---------- MAIN ----------

print("1. Enter HEX color")
print("2. Use image")

choice = input("Choose option: ")

if choice == "1":
    base = input("Enter HEX color: ")
    path = None

elif choice == "2":
    Tk().withdraw()
    path = filedialog.askopenfilename()

    if not path:
        print("No file selected")
        exit()

    base = get_dominant_color(path)
    print("Extracted:", base)

else:
    print("Invalid")
    exit()

theme = generate_theme(base)

print("\nGenerated Theme:")
for k, v in theme.items():
    print(k, ":", v)

export_html(theme, base, path)