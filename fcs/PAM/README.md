# PAM FCS file type

Example file:

```
Correlation file for: FILENAME of Channels A cross B
Count rate channel 1 [kHz]: 4.63
Count rate channel 2 [kHz]: 4.63
Valid bins: 1   2   3   4   5   6   7   8   9  10
Data starts here: 
0.000001000000	0.78401964	0.01427645	0.82219936	0.80599370	0.81429455	0.77572412	0.81233506	0.78853782	0.86718409	0.71361022	0.72256694	0.71775051
0.000002000000	0.77602264	0.01178762	0.79130150	0.81075255	0.75638306	0.76802329	0.81233503	0.71904294	0.75785143	0.75404712	0.75665360	0.83383591
0.000003000000	0.78519994	0.00620840	0.77585256	0.77188836	0.81350118	0.78266687	0.78810801	0.82213967	0.78499071	0.76778039	0.76378800	0.78128369
0.000004000000	0.77228518	0.00672627	0.80984014	0.77426777	0.79446177	0.75492106	0.75919190	0.79464717	0.78886772	0.71818790	0.75110455	0.77736186
```

The header contains the filename, specified as the ful path, and the name of the channels. The channel names are given by the names of the PIE channels that are cross-correlated, i.e. they could be named "GG" and "RR" to specify signal in the green channel after green excitation and the red channel after red excitation.

Next, the average count rates of the channels are given in kHz. This information is used to compute the molecular brightness in the fit program.

In PAM, correlation functions for a measurement are calculated by splitting the total measurement into a number of equal time bins (here 10), for which correlation functions are calculated separately. These separate correlation functions are averaged to obtain the total correlation function, and their standard error is used to address the uncertainty of the measurement. Additionally, it is possible to exclude some of these time intervals in PAM, i.e. if an aggreate was present for some of them. The **Valid bins** line in the header specifies which of the individual correlation functions are to be used (in this case, all).

After the line `Data start here:`, the data is given as columns. The individual columns contain, from left to right:

* Correlation time in seconds
* Average correlation functions
* Standard error of the average correlation function
* The individual correlation functions for the different time intervals

In this case, there are thus 13 columns.
