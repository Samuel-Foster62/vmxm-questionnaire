from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server


class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.lblImgName.text = self.item['filename']
    self.imgArea.source = self.item['img']
    # Any code you write here will run before the form opens.
