# TCPSC file formats in PAM

The situation is a bit unstructured at the moment, as there exist three separate text-based file formats to store microtime histograms.

## Data for fitting in the module *TauFit* (.dec)

```
TAC range [ns]:		 80.00
Microtime Bins:		 8192
Resolution [ps]:	 9.77

BB1			BG1			
Decay	IRF	Scatter	Decay	IRF	Scatter	
9	4	57	4	4	16
10	3	68	4	4	10
6	9	58	8	5	15
7	15	63	15	12	14
10	20	79	11	14	17
```

The metadata is specified in the header as the total channel range (TAC range) in nanoseconds, the number of bins in the microtime histogram (Microtime Bins) and the resolution of a single bin. This informatino is redundant as the three parameters are related, but this it is easier for a human to have all relevant parameters available.

Next, the channel name is given (`BB1`). In PAM, channels are always PIE channels and the name is taken as the name chosen by the user in the PAM program. Multiple channels are appended horizontally, separated by *three* tab stops.

To fit a decay, we require information about the instrument response function and the background (scatter). This information is always stored in the PAM software, so it is added to the file as well.

Multiple channels can be saved in on *.dec* file by appending the channels in the same pattern in the horizontal direction using tab separators.

## Export of fit results

This file format is solely used to make the data available for plotting in other software. It stores just the decay, fit result and the weighted residuals in a csv file. The time is given in nanoseconds.

```
time_ns,intensity,fit,wres
0.00977,18,NaN,NaN
0.01954,225,NaN,NaN
0.02931,1686,NaN,NaN
0.03908,5472,NaN,NaN
0.04885,9270,NaN,NaN
0.05862,10428,NaN,NaN
```

## Microtime patterns

This file format is used to store microtime patterns for the use in filtered-FCS. It is independent of PIE channel boundaries and stores the total microtime histogram of the detector. As such, it contains information about the detector number and routing channel. No time information is saved, as everything is handled in units of microtime bins. In PAM, for fFCS it is generally assumed that polarized detection is used, which is why by default two channels are expeected.

The header contains the name of the raw data file, without extension, and the detector and routing channel numbers of the two channels. The microtime histograms are appended in csv format.

```
Microtime patterns of measurement: 2species_different_gamma_gr-br_1
Channel 1: Detector 1 and Routing 1
Channel 2: Detector 2 and Routing 1
0,0
0,0
0,0
0,0
0,0
0,0
0,0
```