import sys
from fontTools.ttLib import TTFont
from fontTools.varLib.mutator import instantiateVariableFont

font_path = "media/fonts/SF-Pro (1).ttf"
font = TTFont(font_path)

if "fvar" in font:
    fvar = font["fvar"]
    print("Variable axes found:")
    for axis in fvar.axes:
        print(f" - {axis.axisTag}: min={axis.minValue}, default={axis.defaultValue}, max={axis.maxValue}")
    
    # SF Pro usually uses 'wght' for Weight (Heavy = 800/900)
    # and 'wdth' for Width (Compressed = 50 to 75)
    # Let's instantiate it with Heavy Compressed parameters:
    # Usually Heavy is wght=900, Compressed is wdth=50.
    
    axes = {}
    for axis in fvar.axes:
        if axis.axisTag == "wght":
            axes["wght"] = 900
        elif axis.axisTag == "wdth":
            axes["wdth"] = 50
        else:
            axes[axis.axisTag] = axis.defaultValue
    
    print("Instantiating with axes:", axes)
    static_font = instantiateVariableFont(font, axes)
    static_font.save("media/fonts/SF-Pro-Compressed-Heavy.ttf")
    print("Successfully created static font: media/fonts/SF-Pro-Compressed-Heavy.ttf")
else:
    print("Not a variable font! Cannot instantiate.")
