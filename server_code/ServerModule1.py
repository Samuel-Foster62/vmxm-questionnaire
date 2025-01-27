import anvil.email
import anvil.server
import anvil.pdf
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
    
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
def send_feedback(name, email, feedback):
  # Send yourself an email each time feedback is submitted
  anvil.email.send(#to="vmxm@diamond.ac.uk", # Change this to your email address and remove the #!
                   subject=f"Feedback from {name}",
                   text=f"""
                   
  A new person has filled out the feedback form!

  Name: {name}
  Email address: {email}
  Feedback:
  {feedback}
  """)

@anvil.server.callable
def create_pdf(name, email, affil, bag, contact, prot, seq, era, crystCond, 
               lcp, crystMethod, cryo, morph, size, density, number, sizing, sg, cell,
               molASU, exptPrior, exptAim, priorStruc, priorMR, pdbcode):
  pdf = anvil.pdf.render_form('PDF', name, email, affil, bag, contact, prot, seq, era, crystCond, 
               lcp, crystMethod, cryo, morph, size, density, number, sizing, sg, cell,
               molASU, exptPrior, exptAim, priorStruc, priorMR, pdbcode)
  return pdf