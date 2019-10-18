from __future__ import typing
import numpy as np


def save_fcs_kristine(
        filename: str,
        correlation_amplitude: np.ndarray,
        correlation_time: np.ndarray,
        mean_countrate: float,
        acquisition_time: float,
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
    col_1 = np.array(correlation_time)
    col_2 = np.array(correlation_amplitude)
    col_3 = np.zeros_like(correlation_amplitude)
    col_3[0] = mean_countrate
    col_3[1] = acquisition_time
    if isinstance(
            correlation_amplitude_uncertainty,
            np.ndarray
    ):
        data = np.vstack(
            [
                col_1,
                col_2,
                col_3,
                correlation_amplitude_uncertainty
            ]
        ).T
    else:
        data = np.vstack(
            [
                col_1,
                col_2,
                col_3
            ]
        ).T
    np.savetxt(
        filename,
        data,
    )

