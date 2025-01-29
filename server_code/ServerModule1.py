import anvil.server
from anvil.pdf import PDFRenderer
import gemmi
import re

@anvil.server.callable
def get_spacegroups():
  spacegroups = [gemmi.SpaceGroup(i).hm for i in range(1, 231) if gemmi.SpaceGroup(i).is_sohncke()]
  return spacegroups

@anvil.server.callable
def check_email(email):
  pattern = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$" 
  if re.fullmatch(pattern, email):
    return True
  else:
    return False
    
@anvil.server.callable
def create_pdf(name, email, affil, bag, contact, prot, seq, era, crystCond, 
               lcp, crystMethod, cryo, morph, size, density, number, sizing, sg, cell,
               molASU, exptPrior, exptAim, priorStruc, priorMR, pdbcode, images):
  pdf = anvil.pdf.render_form('PDF', name, email, affil, bag, contact, prot, seq, era, crystCond, 
               lcp, crystMethod, cryo, morph, size, density, number, sizing, sg, cell,
               molASU, exptPrior, exptAim, priorStruc, priorMR, pdbcode, images)
  return pdf