#!/usr/bin/env python

from PIL import Image
import os, os.path
import glob
import random
from vhs import vhs

from gimpfu import *

gettext.install("gimp20-python", gimp.locale_directory, unicode=True)

PAL_WIDTH = 720 
PAL_HEIGHT = 576
path = 'dataset/ImagesDatasetHD/*'

def run():
    readFolderVhs()

def readFolderVhs():
    image_list = []
    opacity = 100.0
    for file in glob.glob(path + '.jpg'):
        filename_w_ext = os.path.basename(file)
        filename, file_extension = os.path.splitext(filename_w_ext)

        # Generate random num fro glitch
        glitch = random.randint(0, 545)
        
        img = pdb.file_jpeg_load(file, file)
        layer = pdb.gimp_image_get_active_layer(img)
        
        vhs(img, layer, False, True, True, glitch, 2, 3, filename)
        
        image_list.append(img)
    return image_list

register(
    "python-fu-vhs",
    N_("Makes image look like it came from a PAL VHS tape."),
    "Makes image look like it came from a PAL VHS tape.",
    "Dave Jeffery",
    "Dave Jeffery",
    "2009",
    N_("V_HS..."),
    "RGB*, GRAY*",
    [
        (PF_IMAGE, "image", _("Input image"), None),
        (PF_DRAWABLE, "drawable", _("Input drawable"), None),
        (PF_TOGGLE, "add_border", _("Add VHS border?"), True),
        (PF_TOGGLE, "add_messy", _("Add messy head change?"), True),
        (PF_TOGGLE, "add_glitch", _("Add glitch?"), True),
    (PF_SLIDER, "glitch_y", _("Glitch y-position (pixels)"), 146, (0, 545, 1)),
        (PF_RADIO, "down_interpol", _("Down-scaling interpolation method"), 2,
         ((_("None"), INTERPOLATION_NONE),
          (_("Linear"), INTERPOLATION_LINEAR),
          (_("Cubic"), INTERPOLATION_CUBIC),
          (_("Sinc Lanczos"), INTERPOLATION_LANCZOS))),
        (PF_RADIO, "up_interpol", _("Up-scaling interpolation method"), 3,
         ((_("None"), INTERPOLATION_NONE),
          (_("Linear"), INTERPOLATION_LINEAR),
          (_("Cubic"), INTERPOLATION_CUBIC),
          (_("Sinc Lanczos"), INTERPOLATION_LANCZOS)))        
    ],
    [],
    vhs,
    menu="<Image>/Filters/Artistic",
    domain=("gimp20-python", gimp.locale_directory)
    )

if __name__ == "__main__":
    run()