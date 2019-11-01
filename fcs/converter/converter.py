#!/usr/bin/env python
import argparse
import os

import yaml_fcs
import mat_china
import cor_kristine
import asc_alv


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Convert FCS to yaml-fcs'
    )

    parser.add_argument(
        '-i',
        '--input_type',
        type=str,
        help='Either '
             'asc (ALV Correlator), '
             'cor (Kristine file format), '
             'china-mat (Chinese FCS), '
             'fcs (Zeiss Confocor)'
    )

    parser.add_argument(
        '-t',
        '--output_type',
        type=str,
        default='yaml',
        help='Either cor for Kristine yaml for yaml-FCS'
    )

    parser.add_argument(
        dest='input_filename',
        type=str,
        help='The input filename'
    )

    parser.add_argument(
        dest='output_filename',
        type=str,
        help='The output filename'
    )

    args = parser.parse_args()
    print(args)

    print("Convert FCS curves")
    print("==================")
    print("\tInput filename: %s" % args.input_filename)
    print("\tInput type: %s" % args.input_type)
    print("\tOutput filename: %s" % args.output_filename)
    print("\tOutput type: %s" % args.output_type)

    input_filename = args.input_filename
    input_type = args.input_type
    if input_type.lower() == 'alv':
        d = asc_alv.fcs_read_asc(input_filename)
    elif input_type.lower() == 'cor':
        d = cor_kristine.fcs_read_kristine(
            input_filename
        )
    elif input_type.lower() == 'china-mat':
        d = mat_china.fcs_read_china_mat(input_filename)
    else: #elif args.input_type.lower() == 'yaml':
        d = yaml_fcs.fcs_read_yaml(
            input_filename
        )

    output_filename = args.output_filename
    output_type = args.output_type
    if output_type.lower() == 'cor':
        cor_kristine.fcs_write_dict_to_kristine(
            ds=d,
            filename=output_filename
        )
    else: #elif args.input_type.lower() == 'yaml':
        yaml_fcs.fcs_write_yaml(
            filename=output_filename,
            d=d
        )



