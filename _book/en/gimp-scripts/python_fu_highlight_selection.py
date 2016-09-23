#!/usr/bin/python

from gimpfu import *

def plugin_main(timg, tdrawable):
    
    cl_white = (255,255,255)
    pdb.gimp_context_set_foreground(cl_white)
    
    cl_black = (0,0,0)
    pdb.gimp_context_set_background(cl_black)
    
    # create new layer which will contain "fade out BG"
    layer_fade_out = pdb.gimp_layer_new(timg,
                       timg.width,      # layer width
                       timg.height,     # layer height
                       1,               # layer type - RGBA
                       "fade out BG",   # layer name
                       70,              # layer opacity in %
                       0                # layer mode - NORMAL
                       )
    # insert layer_fade_out to the top of the stack
    pdb.gimp_image_insert_layer(timg, layer_fade_out, None, -1)
    
    # invert selection
    pdb.gimp_selection_invert(timg)
    # fill selection with BG color
    pdb.gimp_edit_fill(layer_fade_out, 1)
    
    # create new layer which will contain "highlight stroke"
    layer_highlight = pdb.gimp_layer_new(timg,
                       timg.width,          # layer width
                       timg.height,         # layer height
                       1,                   # layer type - RGBA
                       "highlight stroke",  # layer name
                       100,                 # layer opacity in %
                       0                    # layer mode - NORMAL
                       )
    # insert layer_highlight to the top of the stack
    pdb.gimp_image_insert_layer(timg, layer_highlight, None, -1)
    
    # invert selection
    pdb.gimp_selection_invert(timg)
    
    highlight_brush_name = "Papaya highlight brush"
    # create highlight brush if not exists
    brushes_list = pdb.gimp_brushes_get_list(highlight_brush_name)
    if brushes_list[0] == 0:
        pdb.gimp_brush_new(highlight_brush_name)
    # select highlight brush
    pdb.gimp_context_set_brush(highlight_brush_name)
     
    # stroke selection with FG color
    pdb.gimp_edit_stroke(layer_highlight)

register(
        "python_fu_highlight_selection",
        "Fades out unselected area and highlight selection with stroke",
        "Fades out unselected area and highlight selection with stroke",
        "qnd s.r.o.",
        "qnd s.r.o.",
        "2014",
        "<Image>/Tools/Highlight selection",
        "RGB*, GRAY*",
        [],
        [],
        plugin_main)

main()