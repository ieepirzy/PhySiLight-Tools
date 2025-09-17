
#We calculate the relativistic kinetic energy for a particle using the following equation:
#E_k=\sqrt{(\frac{h}{\lambda}c)^2+(mc^2)^2}\space-(m_0c^2)

import math
#Start by defining variables, based on the exercise (Krane exercises 4.7, §4.2):

# The desired de Broglie' wavelength in m:
lambda_ = 14 #fm

# Masses being examined (MeV/c^2), values found from literature and wikipedia
m_electron = 0.5109989461
m_neutron = 939.5654133
m_alpha = 3727

#speed of light c:
c = 299792458 #m/s
#planck's constant h:
h = 6.626070040e-34 #Js

# To save time and sanity, we use the well known result h*c = 1240 eV nm
hc = 197.3269788 #MeV·fm

#Making use of the matter-energy equivalence, we can now calculate the kinetic energy as such:

#Relativistic kinetic energy in MeV
Ek_electron = math.sqrt((hc/lambda_)**2 + m_electron**2) - m_electron
Ek_neutron = math.sqrt((hc/lambda_)**2 + m_neutron**2) - m_neutron
Ek_alpha = math.sqrt((hc/lambda_)**2 + m_alpha**2) - m_alpha

print(Ek_electron, Ek_neutron, Ek_alpha)
