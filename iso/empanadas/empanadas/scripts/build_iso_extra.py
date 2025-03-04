# builds ISO's

import argparse

import empanadas.common
from empanadas.util import IsoBuild


def parse_args():
    parser = argparse.ArgumentParser(description="ISO Compose")

    parser.add_argument('--release', type=str, help="Major Release Version or major-type (eg 9-beta)", required=True)
    parser.add_argument('--arch', type=str, dest='build_arch', help="Architecture")
    parser.add_argument('--isolation', type=str, choices=['auto', 'simple'], dest='mock_isolation', help="Mock Isolation")
    parser.add_argument('--local-compose', action='store_true', help="Compose Directory is Here")
    parser.add_argument('--logger', type=str)
    parser.add_argument('--extra-iso', type=str, help="Granular choice in which iso is built")
    parser.add_argument('--extra-iso-mode', type=str, choices=['podman', 'local'], default='local')
    parser.add_argument('--hashed', action='store_true')
    parser.add_argument('--updated-image', action='store_true')
    parser.add_argument('--image-increment', type=str, default='0')
    return parser.parse_args()


def run():
    args = parse_args()
    cfg = empanadas.common.collect_config(args)
    IsoBuild(cfg).run_build_extra_iso()
