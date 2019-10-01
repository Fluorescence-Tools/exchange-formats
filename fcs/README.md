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
  