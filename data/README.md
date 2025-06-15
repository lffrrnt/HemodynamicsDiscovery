# Data-driven modeling and classification of brain blood-flow pathologies: measurement data

Authors: Irem Topal, Alexander Cherevko, Yuri Bugay, Maxim Shishlenin,
Jean Barbier, Deniz Eroglu, Édgar Roldán,
Roman Belousov (roman.belousov@embl.de)

The clinical data, provided with this directory as supplementary information, were acquired during neurosurgical operations at the Meshalkin Research Institute of Circulation Pathology (Novosibirsk, Russia) between March 2012 and September 2017 (see below). Blood velocity and pressure were recorded using a Doppler sonography from an intravascular guidewire with a diameter 0.34 mm. The signals were processed through an analogue-to-digital converter at a frequency of 200-Hz. A noise filter was applied to eliminate Fourier components, whose frequencies exceed the nominal time resolution of the device. We collected velocity and pressure data before, during, and after surgery from ten patients: five with arterial aneurysms (AA), and five with arteriovenous malformations (AVM), all of whom underwent a successful surgical treatment. Each time series lasted between 3.345–5.375 s, with a time step of ∆t = 5 ms , corresponding to approximately five cardiac cycles per patient. The time-averaged values of pressure and velocity were subtracted from each trajectory before fitting the data to theoretical models.

The measurement data are organized by sub-directories AA and AVM for each malformation class respectively. These subdirectories contain spreadsheet files in Excel XLSX format, one per each patient, with three sheets reporting time series of pressure and velocities before, during, and after the surgery respectively. The names of the files correspond to the patients' anonymization codes.

## Patients' anonymization codes and dates of data acquisition

### AA patients
1. K3: 2017-09-26
2. S2: 2015-04-22
3. K1: 2013-03-15
4. G2: 2012-03-20
5. R1: 2014-11-12 

### AVM patients
1. S3: 2017-04-26
2. K2: 2012-12-06
3. S1: 2013-03-06
4. L1: 2015-08-03
5. G1: 2015-07-14 

