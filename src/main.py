import pydicom
import matplotlib.pyplot as plt
import os

for root,_,files in os.walk('/input'):
  file = [f for f in files if f.endswith('.dcm')]
  for i in file:
    ds1 = pydicom.dcmread(os.path.join(root,i))
    ax = plt.hist(ds1.pixel_array.ravel(), bins = 256)

    plt.savefig('/output/first_plot1.png', transparent = True)
    break

print("Docker is magic!")