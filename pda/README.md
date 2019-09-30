# Photon distribution analysis (PDA) file format

## Requirements

### Minimal data

* Photon counts in the donor and acceptor (FRET) channels

### Required metadata

* Time bin used to bin the data

### Optional data

* Photon counts in PIE/ALEX channels (acceptor signal after acceptor excitation)
* Reference to Photon IDs (selection) if a selection was used

  
### Optional metadata

* Background counts of the different channels
* Experimental correction factors (crosstalk etc.)
* Raw data file name
* Type of data set: burst-wise or complete measurement
  