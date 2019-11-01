from __future__ import annotations
from typing import Dict, List

import yaml


def numpy_to_list(d):
    for k, v in d.items():
        if isinstance(v, dict):
            numpy_to_list(v)
        else:

            print("{0} : {1}".format(k, v))


def fcs_write_yaml(
        filename: str,
        d: List[Dict],
        verbose: bool = False
) -> None:
    """

    :param filename:
    :param verbose:
    :return:
    """
    with open(filename, 'w') as fp:
        yaml.dump(
            data=d,
            stream=fp,
            default_flow_style=False
        )


def fcs_read_yaml(
        filename: str,
        verbose: bool = False
) -> List[Dict]:
    """

    :param filename:
    :param verbose:
    :return:
    """
    d = [{}]
    with open(filename, 'r') as fp:
        d = yaml.safe_load(
            fp
        )
    return d
