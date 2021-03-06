from __future__ import annotations
from typing import Dict, List
import numpy as np
import os
import re
import scipy

from . import weights


def fcs_write_PAM_text(
        filename: str,
        correlation_amplitude: np.ndarray,
        correlation_time: np.ndarray,
        mean_countrate: float,
        acquisition_time: float = None,
        correlation_amplitude_uncertainty: np.ndarray = None,
        verbose: bool = True
) -> None:
    """

    :param filename: the filename
    :param correlation_amplitude: an array containing the amplitude of the
    correlation function
    :param correlation_amplitude_uncertainty: an estimate for the
    uncertainty of the correlation amplitude
    :param correlation_time: an array containing the correlation times
    :param mean_countrate: the mean countrate of the experiment in kHz
    :param acquisition_time: the acquisition of the FCS experiment in
    seconds
    :return:
    """
    if verbose:
        print("Saving correlation: %s" % filename)
    data = np.vstack(
        [
            np.array(correlation_time),
            np.array(correlation_amplitude),
            np.array(correlation_amplitude_uncertainty),
            np.array(correlation_amplitude)  # normally, the sub-measurements are stored here. 
        ]
    ).T
    # define the header
    header = ('Correlation file for %s of Channels A cross B\n'
              'Count rate channel 1 [kHz]: %.2f\n'
              'Count rate channel 2 [kHz]: %.2f\n'
              'Valid bins: 1\nData starts here:') % (filename, mean_countrate,
                                                     mean_countrate)
    np.savetxt(
        filename,
        data,
        header=header,
        comments=''
    )


def fcs_write_PAM_mat(
        filename: str,
        correlation_amplitude: np.ndarray,
        correlation_time: np.ndarray,
        mean_countrate: float,
        acquisition_time: float = None,
        correlation_amplitude_uncertainty: np.ndarray = None,
        verbose: bool = True
) -> None:
    """

    :param filename: the filename
    :param correlation_amplitude: an array containing the amplitude of the
    correlation function
    :param correlation_amplitude_uncertainty: an estimate for the
    uncertainty of the correlation amplitude
    :param correlation_time: an array containing the correlation times
    :param mean_countrate: the mean countrate of the experiment in kHz
    :param acquisition_time: the acquisition of the FCS experiment in
    seconds
    :return:
    """
    if verbose:
        print("Saving correlation: %s" % filename)

    header = ('Correlation file for %s of Channels A cross B') % (filename)

    data_dictionary = {
        'Cor_Times': correlation_time,
        'Cor_Average': correlation_amplitude,
        'Cor_SEM': correlation_amplitude_uncertainty,
        'Cor_Array': correlation_amplitude,
        'Valid': 1,
        'Counts': np.array([mean_countrate/2, mean_countrate/2]),
        'Header': header
    }

    scipy.io.savemat(
        filename,
        data_dictionary
    )


def fcs_write_dict_to_PAM(
        filename: str,
        ds: List[Dict],
        verbose: bool = True,
        Type: str = 'mat'
) -> None:
    for i, d in enumerate(ds):
        root, ext = os.path.splitext(
            filename
        )
        fn = root + ("_%02d_" % i) + ext
        if Type is 'text':
            fcs_write_PAM_text(
                filename=fn,
                verbose=verbose,
                correlation_time=d['correlation_time'],
                correlation_amplitude=d['correlation_amplitude'],
                correlation_amplitude_uncertainty=1. / np.array(d['weights']),
                acquisition_time=d['acquisition_time'],
                mean_countrate=d['mean_count_rate']/2
            )
        elif Type is 'mat':
            fcs_write_PAM_mat(
                filename=fn,
                verbose=verbose,
                correlation_time=d['correlation_time'],
                correlation_amplitude=d['correlation_amplitude'],
                correlation_amplitude_uncertainty=1. / np.array(d['weights']),
                acquisition_time=d['acquisition_time'],
                mean_countrate=d['mean_count_rate']/2
            )


def fcs_read_PAM_text(
        filename: str,
        verbose: bool = False
) -> List[Dict]:
    """
    :param filename:
    :param verbose:
    :return:
    """
    # read the meta data
    rx_dict = {
        'line0': re.compile(r'Correlation file for: (?P<orig_filename>.*) of Channels (?P<chan1>.*) cross (?P<chan2>.*)\n'),
        'line1': re.compile(r'Count rate channel 1 \[kHz\]: (?P<countrate1>.*)\n'),
        'line2': re.compile(r'Count rate channel 2 \[kHz\]: (?P<countrate2>.*)\n'),
        'line3': re.compile(r'Valid bins: (?P<valid_bins>.*)\n')
    }
    with open(filename) as f:
        lines = f.readlines()
        lines = lines[0:4]
        orig_filename = rx_dict['line0'].match(lines[0]).group('orig_filename')
        chan1 = rx_dict['line0'].match(lines[0]).group('chan1')
        chan2 = rx_dict['line0'].match(lines[0]).group('chan2')
        countrate1 = np.float(rx_dict['line1'].search(lines[1]).group('countrate1'))
        countrate2 = np.float(rx_dict['line2'].search(lines[2]).group('countrate2'))
        valid_bins = rx_dict['line3'].match(lines[3]).group('valid_bins')

    valid_bins = np.array([np.float(i) for i in valid_bins.split('  ')])
    # the correlation data
    data = np.loadtxt(filename, skiprows=5).T

    # First try to use experimental errors
    try:
        w = 1. / data[2]
    except IndexError:
        # In case everything fails
        # Use no errors at all but uniform weighting
        w = np.ones_like(data[1])
    return [
        {
            'filename': filename,
            'correlation_time': data[0].tolist(),
            'correlation_amplitude': data[1].tolist(),
            'weights': w.tolist(),
            'acquisition_time': None,
            'mean_count_rate': countrate1+countrate2,
            'intensity_trace': None
        }
    ]


def fcs_read_PAM_mat(
        filename: str,
        verbose: bool = False
) -> List[Dict]:
    d = scipy.io.loadmat(filename)
    # save intensity traces
    if verbose:
        print("Reading from file: %s" % filename)

    # read the data
    t = d['Cor_Times']
    c = d['Cor_Average']
    w = d['Cor_SEM']
    valid_bins = d['Valid']
    header = d['Header'][0]
    rx = re.compile(r'Correlation file for: (?P<orig_filename>.*) of Channels (?P<chan1>.*) cross (?P<chan2>.*)')
    orig_filename = rx.match(header).group('orig_filename')
    chan1 = rx.match(header).group('chan1')
    chan2 = rx.match(header).group('chan2')

    countrate = np.mean(d['Counts'])
    return [
        {
            'filename': filename,
            'correlation_time': t.tolist(),
            'correlation_amplitude': c.tolist(),
            'weights': w.tolist(),
            'acquisition_time': None,
            'mean_count_rate': countrate,
            'intensity_trace': None
        }
    ]
