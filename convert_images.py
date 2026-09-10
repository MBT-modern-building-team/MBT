from PIL import Image

def convert_and_resize(src, dest, max_width):
    try:
        with Image.open(src) as img:
            if img.width > max_width:
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
            img.save(dest, "WEBP", quality=85)
            print(f"Converted {src} -> {dest}")
    except Exception as e:
        print(f"Error processing {src}: {e}")

convert_and_resize('Construz/MBTApp/static/img/mbt/mapa-polska-hq.png', 'Construz/MBTApp/static/img/mbt/mapa-polska-hq.webp', 800)
convert_and_resize('Construz/MBTApp/static/img/mbt/o-nas-zespol.jpg', 'Construz/MBTApp/static/img/mbt/o-nas-zespol.webp', 800)
convert_and_resize('Construz/MBTApp/static/img/mbt/o-nas-2.jpg', 'Construz/MBTApp/static/img/mbt/o-nas-2.webp', 800)
