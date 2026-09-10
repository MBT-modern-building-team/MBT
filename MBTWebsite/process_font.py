import sys
try:
    from fontTools.ttLib import TTFont
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "fonttools"])
    from fontTools.ttLib import TTFont

font_path = "media/fonts/SF-Pro (1).ttf"
font = TTFont(font_path)
if "fvar" in font:
    fvar = font["fvar"]
    print("Variable axes found:")
    for axis in fvar.axes:
        print(f" - {axis.axisTag}: min={axis.minValue}, default={axis.defaultValue}, max={axis.maxValue}")
else:
    print("Not a variable font!")
