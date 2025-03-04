# builds ISO's

import argparse

import empanadas.common
from empanadas.util import IsoBuild


def parse_args():
    parser = argparse.ArgumentParser(description="ISO Compose")

    parser.add_argument('--release', type=str, help="Major Release Version or major-type (eg 9-beta)", required=True)
    parser.add_argument('--isolation', type=str, choices=['auto', 'simple'], dest='mock_isolation', help="mock isolation mode")
    parser.add_argument('--rc', action='store_true', help="Release Candidate, Beta, RLN")
    parser.add_argument('--local-compose', action='store_true', help="Compose Directory is Here")
    parser.add_argument('--logger', type=str)
    parser.add_argument('--hashed', action='store_true')
    return parser.parse_args()


def run():
    args = parse_args()
    cfg = empanadas.common.collect_config(args)
    IsoBuild(cfg).run()
