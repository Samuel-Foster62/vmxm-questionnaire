from ._anvil_designer import PDFTemplate
from anvil import *
import anvil.server


class PDF(PDFTemplate):
  def __init__(self, name, email, affil, bag, contact, prot, seq, era, crystCond, 
               lcp, crystMethod, cryo, morph, size, density, number, sizing, sg, cell,
               molASU, exptPrior, exptAim, priorStruc, priorMR, pdbcode, **properties):
    # Set Form properties and Data Bindings.
      self.init_components(**properties)
      self.txtName.text = name
      self.txtEmail.text =email
      self.txtAffil.text =affil
      self.txtBAG.text = bag
      self.dropContact.selected_value = contact
      self.txtProtName.text = prot
      self.txtSeq.text = seq
      if era:
        self.radERAYes.selected = True
      else:
        self.radERANo.selected = True
      self.txtCrystCond.text = crystCond
      self.chkLCP.checked = lcp
      self.txtCrystalisationMethod.text = crystMethod
      self.txtCryoBuff.text = cryo
      self.dropMorphology.selected_value =morph
      self.txtCrystSize.text = size
      self.txtCrystQuant.text = number
      self.txtCrystDensity.text = density
      self.txtSizing.text = sizing
      self.dropSpaceGroup.selected_value = sg
      self.txtUnitCell.text = cell
      self.txtMolperASU.text =molASU
      self.taPrior.text = exptPrior
      self.taAim.text = exptAim
      self.chkPriorStruct.checked = priorStruc
      self.chkMR.checked = priorMR
      self.txtPDB.text = pdbcode

    # Any code you write here will run before the form opens.
