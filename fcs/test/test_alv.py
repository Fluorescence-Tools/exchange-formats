import utils
import os
import unittest
import glob

TOPDIR = os.path.abspath('..')
utils.set_search_paths(TOPDIR)

import io_routines.fcs_read_asc_alv


class Tests(unittest.TestCase):

    def test_read_asc_alv(self):
        for f in glob.glob(
                '../asc/*.ASV'
        ):
            d = io_routines.fcs_read_asc_alv.openASC(
                path=f,
            )
        f = '../asc/ALV-7004USB_ac01_cc01_10.ASC'
        d = io_routines.fcs_read_asc_alv.openASC(
            path=f,
        )


if __name__ == '__main__':
    unittest.main()
