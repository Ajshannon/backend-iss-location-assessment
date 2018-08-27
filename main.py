import argparse
from modules import astro
from modules import iss


def create_parser():
    """Create an argument parser object"""
    parser = argparse.ArgumentParser()

    return parser


def main():

    astro.astro()
    iss.iss()


if __name__ == '__main__':
    main()
