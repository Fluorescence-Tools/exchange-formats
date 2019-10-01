# TCSPC file format

## Requirements

### Minimal data

* Photon counts per microtime bin

### Required metadata

* Time bin resolution
* Polarization (VV, VM, VH, angle, or unspecified)
* Instrument response function
  
### Optional data

* Reference measurements (background and instrument response function)
* Multiple measurements per file (i.e. parallel and perpendicular channel for anisotropy or DA and D0 for FRET)
* TAC linearization (reference to linearization measurement)

### Optional metadata

* Maximum number of microtime bins
* For FRET: donor-only lifetime or reference to donor-only measurement
* Raw data file name
* Dead time
* Total measurement time (count rate -> pile up correction)
