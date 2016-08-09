from array2d import *

from random  import *
from Tkinter import *



# The clamping gui that most layers have. 
class ClampGUI():
  def __init__(self, title="Clamping", min_val=0, max_val=255):
    self.title = title
    
    self.min = min_val
    self.max = max_val
    
    self.top_limit_var = IntVar()
    self.btm_limit_var = IntVar()
    
    self.enabled_var = IntVar()
    
  def layoutGUI(self, parent, heightmap):
    frame = LabelFrame(parent, text="Clamping")
    frame.pack(fill=X, padx=5)
      
    self.enabled_checkbox = Checkbutton(frame, 
        text="enabled", offvalue=0, onvalue=1, variable=self.enabled_var)
    self.enabled_checkbox.pack()
      
    top_slider = Scale(frame, label="Top limit:", 
      orient=HORIZONTAL, variable=self.top_limit_var, from_=self.min, to=self.max
    )
    self.top_slider = top_slider
    top_slider.pack(fill=X)
    
    btm_slider = Scale(frame, label="Bottom limit:", 
      orient=HORIZONTAL, variable=self.btm_limit_var, from_=self.min, to=self.max
    )
    self.btm_slider = btm_slider
    btm_slider.pack(fill=X)
    
    
  def isEnabled(self):
    return self.enabled_var.get()
    
  def getTopValue(self):
    return self.top_limit_var.get()
    
  def getBottomValue(self):
    return self.btm_limit_var.get()
    
  def copy(self):
    gui = ClampGUI()
    top = self.getTopValue()
    btm = self.getBottomValue()
    
    new_top_var = IntVar()
    new_top_var.set(top)
    
    new_btm_var = IntVar()
    new_btm_var.set(btm)

    gui.top_limit_var = new_top_var
    gui.btm_limit_var = new_btm_var
    
    return gui
    