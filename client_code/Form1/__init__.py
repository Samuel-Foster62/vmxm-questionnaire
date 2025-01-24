from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  ##below not needed in final implementation but uswd for debugging
  def radERAYes_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    print(self.radERAYes.get_group_value())
    pass

  def radERANo_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    print(self.radERANo.get_group_value())    
    pass