#!/usr/bin/python3
import argparse
import logging
import sys


import Pret


def main():
    # parse arguments
    parser = argparse.ArgumentParser(description='Main script argument parser.')
    parser.add_argument('--log',
                        help='Log level',
                        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
                        default="INFO")
    parser.add_argument('--capital',
                        help='capital',
                        default=360000,
                        type=float)
    parser.add_argument('--ti',
                        help='taux intérêts',
                        default=0.04,
                        type=float)
    parser.add_argument('--ta',
                        help='taux assurance',
                        default=0.005,
                        type=float)
    parser.add_argument('--duration',
                        help='durée du prêt en années',
                        default=25,
                        type=int)
    args = parser.parse_args()

    # Create root logger. In modules: logger=logging.getLogger(__name__) will inherit this root logger.
    logger = logging.getLogger()
    logger.setLevel(args.log)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)

    testPret = Pret.Pret(args.capital, args.ti, args.duration, args.ta)

    testPret.build()
    print(testPret)
    testPret.graph2()


if __name__ == '__main__':
    main()
