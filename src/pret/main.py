#!/usr/bin/python3
import argparse
import logging
import sys


import Pret


def get_arguments():
    args = {
        "--log": {
            "help": "Log level",
            "choices": ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
            "default": "INFO",
        },
        "--capital": {
            "help": "Capital",
            "default": 360000,
            "type": float,
        },
        "--ti": {
            "help": "Taux intérêts",
            "default": 4,
            "type": float,
        },
        "--total-assurance": {
            "help": "Coût total assurance",
            "default": 4000,
            "type": float,
        },
        "--duration": {
            "help": "Durée du prêt en années",
            "default": 20,
            "type": int,
        },
    }
    parser = argparse.ArgumentParser(description="Main script argument parser.")
    for key, value in args.items():
        parser.add_argument(key, **value)
    return parser.parse_args()


def main():
    # parse arguments
    args = get_arguments()

    # Create root logger. In modules: logger=logging.getLogger(__name__) will inherit this root logger.
    logger = logging.getLogger()
    logger.setLevel(args.log)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter("%(name)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)

    pret_immo = Pret.Pret(
        args.capital, args.ti / 100, args.duration, args.total_assurance
    )

    pret_immo.build()
    print(pret_immo)
    pret_immo.graph2()


if __name__ == "__main__":
    main()
