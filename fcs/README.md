# FCS file format

## Requirements

### Minimal data

* Time axis
* Correlation data
* Noise/correlation channel weights or measurement time and average count rate

### Required metadata

* Normalization of correlation function (fluctation or signal?)
* Unit of time axis
  
### Optional data

* Error bars
  
### Optional metadata

* Auto- or cross-correlation function? (Mention correlation channels)
* Type of time axis: linear, logarithmic, multiple-tau, ...
* Channel count rate (for brightness calculation) (Should be mandatory, otherwise error weighting hard)
* Determination of error bars (If the weights were calculate provide the function)
* Channel description
* Raw data file name
* Correlation algorithm used
* If filtered-FCS: Filters, microtime patterns, pure species data

## Parameter table

| Name | Examples | Mandatory | Description | Recommended abbreviation | Abbreviations | Type |
|---------------------------------------------------|----------------------------------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|---------------|-------------------------------|
| Correlation time axis | [1, 2, 4, 8, ...] | yes | The correlation time axis is  | tc | tc, tau | array/list of floating points |
| Type of time axis | linear, logarithmic, multiple-tau, ... | no |  |  |  | string |
| Unit of correlation time axis | ms  (default) | no | If the unit of the correlation time axis is not provided, it is implicitly assumed that the correlation times are provided in milliseconds. |  |  | string |
| Correlation amplitude | [2, 1.2, 1.1, 1.0, ...]  | yes | The correlation amplitude is the  | G | G, Corr | array/list of floating points |
| Uncertainty estimate of the correlation amplitude | [0.2, 0.2, 0.1, 0.1, ...] | no (see description) | The uncertainty estimate of the correlation amplitude can be either estimated using single photon counting data by splitting the registered photon stream into several chunks, or by using analytical approximations (add references). If no such estimates are provided, the mean count rate and the measurement time need to be provided (see below)  | ? |  | array/list of floating points |
| Aquisition time of the experiment | 16.s | yes | The aquisition time of the experiment is provided in seconds. |  |  |  |
| Mean count rate of the correlation channels | 20.2 | yes | The mean count rates are given in MHz. |  |  | float |
| Type of normalization | - | yes |  |  |  | string |
| Original data |  | yes | This field refers to the original data file(s). The original data file is either the output of the correlator hardware or a ordered set of TTTR files. |  |  | string |
  
  