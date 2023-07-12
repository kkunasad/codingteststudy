from ipywidgets import *
import ipywidgets as widgets
import os, sys
import matplotlib.pyplot as plt
import json
import base64
from IPython.display import display, Image

#smile_button = widgets.Button(description="smiley?")
#normal_button = widgets.Button(description="not smiley")
#next_button = widgets.Button(description="next",icon='arrow-right')
#output = widgets.Output()

#display(smile_button,normal_button, next_button, output)



from ipywidgets import *

t1 = Text("text input", layout=Layout(
    width="80px", border="1px dashed red"
))
b1 = Button(description="button")
HBox((t1,b1))
