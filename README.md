# Smart Theme Generator

A design-focused mini project that generates color palettes and UI themes from either a HEX input or an uploaded image.
It combines color theory, image processing, and interactive UI elements to help designers quickly create aesthetic themes.  

## Features  
* Generate theme from HEX color  
* Extract dominant color from uploaded image  
* Auto-generate:  
   -Background  
   -Primary  
   -Secondary  
   -Accent  
* Text color (auto contrast)  
* Clickable Color Wheel (pick colors interactively)  
* Color theory suggestions:  
   -Complementary  
   -Analogous  
   -Triadic  
* Live HTML preview  
* Export theme as:  
   -HTML preview  
   -CSS variables  
## Tech Stack  
### Python  
   -Pillow (image processing)  
   -tkinter (file picker)
   -colorsys (color conversions)    
### Frontend (auto-generated)  
   -HTML  
   -CSS    
   -JavaScript (Canvas API)    

## How to Run  

    python main.py  

## Usage  
Option 1: HEX Input  
Enter a HEX color (e.g. #3498db)  
Theme is generated instantly
Option 2: Image Input    
Choose an image from your system  
Dominant color is extracted  
Theme is generated automatically  

## Output  
Opens a browser preview (preview.html)  
Shows:
Image preview    
Theme colors  
Color combinations  
Interactive color wheel  
- Color Wheel  
Click anywhere on the wheel  
Instantly get the selected color  
Visual marker shows selected position    
  
## Color Theory Implementation  

The system generates:  
- Complementary → opposite colors (180°)  
- Analogous → nearby colors (±30°)  
- Triadic → evenly spaced (120°)  

## How It Works  

Convert HEX → RGB → HSL    
Apply transformations:
Lightness adjustment → background  
Hue shifts → secondary & accent  
Generate contrast-aware text color    
Render everything in a dynamic HTML UI  

## Example Output

1. Enter HEX color  
2. Use image  
Choose option: 1  
Enter HEX color: #3498db   

Generated Theme:  
background : #103d5c  
primary : #3498db  
secondary : #3344db  
accent : #db7633  
text : #ffffff  

1. Enter HEX color  
2. Use image  
Choose option: 2  
D:\USER FILES\Desktop\tinkerhub useless project\smart palatte\palatte.py:44: DeprecationWarning: Image.Image.getdata is deprecated and will be removed in Pillow 14 (2027-10-15). Use get_flattened_data instead.  
  pixels = list(img.getdata())  
Extracted: #5e8e77  

Generated Theme:  
background : #25382f  
primary : #5e8e77  
secondary : #5e8d8e  
accent : #8e5e74  
text : #ffffff        


    
<img width="1894" height="900" alt="Screenshot 2026-05-03 161018" src="https://github.com/user-attachments/assets/c67e6f2d-a4ca-4ba0-b91e-6cb5c36c7671" />  
  
<img width="1815" height="603" alt="Screenshot 2026-05-03 161025" src="https://github.com/user-attachments/assets/d69fa9cc-0b9c-48cf-a121-d79300eb4e8d" />  
<img width="1920" height="907" alt="Screenshot 2026-05-03 160155" src="https://github.com/user-attachments/assets/c1668347-1f32-4931-9f3a-9f2f49159ffb" />

<img width="1898" height="924" alt="Screenshot 2026-05-03 160244" src="https://github.com/user-attachments/assets/7847edd5-de47-45e7-9f7b-232884d12909" />

