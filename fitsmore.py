#!/usr/bin/env python
"""
Browse contents of FITS table
"""

__author__ = 'Leo Huckvale <leohuckvale@gmail.com>'

from astropy.table import Table

def main(path, ext):
    """
    Main routine
    """
    table = Table.read(path, hdu=ext)
    table.more(max_width=-1)

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', type=str,
                        help='FITS file to inspect')
    parser.add_argument('-x', '--ext', type=int, default=1,
                        help='Extension for multi-extension FITS')
    args = parser.parse_args()
    
    main(args.file, args.ext)

