from ._anvil_designer import QuestionnaireTemplate
from anvil import *
import anvil.server

class Questionnaire(QuestionnaireTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.selected_file = None
    self.txtName.text = ""
    self.txtEmail.text = ""
    self.txtProtName.text = ""
    
    spacegroups = anvil.server.call('get_spacegroups')
    self.dropSpaceGroup.items = [sg for sg in spacegroups]
    self.email = None
    self.images = []
    # Any code you write here will run before the form opens.

  def chkCryo_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    self.txtCryoBuff.enabled = self.chkCryo.checked

  def btnSubmit_click(self, **event_args):
    """This method is called when the button is clicked"""
    #anvil.server.call("clean up”)
    Essential = [self.txtName, self.txtEmail, self.txtProtName]

    print(f"Essential list: {Essential}")
    res = False
    for ele in Essential:
      if not ele.text:
        ele.role = "input-error"
        res = True
    if res: #any(e == "" for e in Essential):
      alert("Empty Essential fields")
    else: 
     self.UserData()
     if self.selected_file:
        anvil.server.call('uploadPDB', self.selected_file)
     #anvil.server.call("recieveData", self.data)
     pdf = anvil.server.call('create_pdf', **self.data)
     anvil.media.download(pdf)
      ##now want to add images to a container below pdf
      ##and parse pdb/ cif file ready for emailing
     alert("Sent responses to VMXm team! Please check your emails for a copy")
    pass
    
  def UserData(self):
    self.data = {
      'name': self.txtName.text,
      'email': self.txtEmail.text,
      'affil': self.txtAffil.text,
      'bag': self.txtBAG.text,
      'contact': self.dropContact.selected_value,
      'prot': self.txtProtName.text,
      'crystCond': self.txtCrystCond.text,
      'crystMethod': self.txtCrystalisationMethod.text,
      'cryo': self.txtCryoBuff.text,
      'morph': self.dropMorphology.selected_value,
      'size': self.txtCrystSize.text,
      'number': self.txtCrystQuant.text,
      'sizing': self.txtSizing.text,
      'sg': self.dropSpaceGroup.selected_value,
      'cell': self.txtUnitCell.text,
      'molASU': self.txtMolperASU.text,
      'exptPrior': self.taPrior.text,
      'exptAim': self.taAim.text,
      'priorStruc': self.chkPriorStruct.checked,
      'priorMR': self.chkMR.checked,
      'pdbcode': self.txtPDB.text,
      'images': self.images

    }
                  
  def txtEmail_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    if not anvil.server.call('check_email', self.txtEmail.text):
      self.txtEmail.role = "input-error"
    else:
      self.txtEmail.role = "outlined"
    pass

  def txtName_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    if not self.txtName.text:
       self.txtName.role = "input-error"

  def txtProtName_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    if not self.txtProtName.text:
       self.txtProtName.role = "input-error"

  def flPDB_change(self, file, **event_args):
      if file:
        valid_extensions = ['.pdb', '.cif']
        file_name = file.name
        if not any(file_name.endswith(ext) for ext in valid_extensions):
            alert("Invalid file type. Please upload a .pdb or .cif file.")
            self.selected_file = None
            return

        max_size_mb = 5
        file_size_in_bytes = len(file.get_bytes())
        if file_size_in_bytes > max_size_mb * 1024 * 1024:
            alert("File size exceeds the limit of 5 MB. Please upload a smaller file or contact the VMXm team.")
            self.selected_file = None
            return

        self.selected_file = file
        alert("File selected: " + file.name)
      pass

  def file_loader_2_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.images = []
    for fl in self.flImages.files:
      fn = fl.name
      self.images.append({'filename': fn, 'img': fl})
    pass
