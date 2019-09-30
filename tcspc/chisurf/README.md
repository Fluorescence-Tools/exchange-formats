# TCSPC formats in Chisurf

There are two major formats currently supported

1. Standard CSV files
    1. without time axis
    2. with time axis
    3. with channel axis
2. Jordi files
3. Fixed width column files

Standard csv files contain the fluorescence decay histogram 
of a single channel and typically a time or channel number
axis.

Jordi files contain the fluorescence decays of the parallel
and perpendicular axis saved subsequently in a single file.

# FCS formats
Currently the old Kristine format and the new Kristine format
are supported for text based FCS curves.

In the "old Kristine" format the time axis is the first column,
the correlation amplitudes are in the second column. The third
column contains the mean count rate of the detectors and the 
measurement time (to calculate the weights).

The "new" Kristine format extends the old Kristine format by
adding an additional column, that contains the weights, as 
determined during the correlation calculation. 

# ChiSurf data formats

For saving fluorescence decays, Chisurf uses separate CSV files of
the fluorescence decay, the model function, and the weighted residuals
(see example). I programmed the saving this way, so that plots can be 
easier generated e.g. with Excel or Origin. Additionally, Chisurf saves
upon saving the fluorescence decays as a JSON file (see example.)

The meta data of an analysis are outputed as an analysis report 
to a Word document including screenshots (Suren wanted that), 
to a text file, and to a JSON file that can be opened again in the software.

In the Word document, the parameters are saved in an table that can be
copied for instance to Excel.

Beyond generating and opening analysis results (saved in separate JSON files)
the JSON files containing the curves are not used (to my (Thomas) knowledge).

