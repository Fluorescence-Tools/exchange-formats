# File formats for photon distribution analysis (PDA)

## Three-color PDA file format

```
# place for comments
timebin = 1; # timebin in ms
NBB, NBG, NBR, NGG, NGR
46,54,16,95,28
35,60,17,113,46
38,58,14,82,33
67,51,10,94,23
20,32,6,36,13
32,35,9,46,23
7,37,20,50,14
.....
```

The first lines until the keyword `timebin = ` may be used for comments for the dataset.

The timebin specifies the binning used for processing the burst-wise dataset for PDA, given in milliseconds. If the whole burst is used, timebin can be set to Inf.

The next line specifies the channel names. `NXY` denotes the number of photon in spectral channel Y after excitation by laser X.

The experimental data is listed as columns, separated by commas.

See also: https://pam.readthedocs.io/en/latest/tcPDA.html#from-text-file.
