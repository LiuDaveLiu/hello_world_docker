#!/usr/bin/env python3
import pydicom
import matplotlib.pyplot as plt
import os

base_dir='C:/Users/lliu10/OneDrive - Inside MD Anderson/Documents/Brain-Tumor-Progression'

#ds1 = pydicom.dcmread(base_dir+'/PGBM-001/04-02-1992-FH-HEADBrain Protocols-79896/11.000000-T1post-80644/1-13.dcm')

ds1 = pydicom.dcmread('/input/DICOM/1-13.dcm')
ax = plt.hist(ds1.pixel_array.ravel(), bins = 256)

plt.savefig('/output/first_plot1.png', transparent = True)

print("Docker is magic!")