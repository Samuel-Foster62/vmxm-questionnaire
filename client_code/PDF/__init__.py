from ._anvil_designer import PDFTemplate
from anvil import *
import anvil.server


class PDF(PDFTemplate):
  def __init__(self, name, email, affil, bag, contact, prot, crystCond, 
               crystMethod, cryo, morph, size, number, sizing, sg, cell,
               molASU, exptPrior, exptAim, priorStruc, priorMR, pdbcode, pdbfile, images, **properties):
    # Set Form properties and Data Bindings.
      self.init_components(**properties)
      self.txtName.text = name
      self.txtEmail.text =email
      self.txtAffil.text =affil
      self.txtBAG.text = bag
      self.dropContact.selected_value = contact
      self.txtProtName.text = prot
      self.txtCrystCond.text = crystCond
      self.txtCrystalisationMethod.text = crystMethod
      self.txtCryoBuff.text = cryo
      self.dropMorphology.selected_value =morph
      self.txtCrystSize.text = size
      self.txtCrystQuant.text = number
      self.txtSizing.text = sizing
      self.txtSpaceGroup.text = sg
      self.txtUnitCell.text = cell
      self.txtMolperASU.text =molASU
      self.taPrior.text = exptPrior
      self.taAim.text = exptAim
      self.chkPriorStruct.checked = priorStruc
      self.chkMR.checked = priorMR
      self.txtPDB.text = pdbcode
      self.txtPDBFile.text = pdbfile
      self.repeating_panel_1.items = images

    # Any code you write here will run before the form opens.
