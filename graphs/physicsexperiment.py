import matplotlib.pyplot as plt
import numpy as np
raedings_of_voltmeter=[0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1,1.05,1.1,1.15,1.2,1.25,1.3,1.35,1.4,1.45,1.5,1.55]
reading_of_ammeter=[0,0,0,0,0.05,0.2,0.4,0.6,0.9,1.2,1.6,1.9,2.3,2.6,3,3.4,3.7,4.1,4.5,4.9,5.3,5.7,6.2,6.5,7,7.4,7.8,8,8.5,8.8,9.4,9.8]
plt.plot(raedings_of_voltmeter,reading_of_ammeter)
plt.title("Experiment")
plt.xlabel("<------ raedings of voltmeter ------>")
plt.ylabel("<------ reading of ammeter ------>")
plt.show()
