# builds ISO's

import argparse

import empanadas.common
from empanadas.util import IsoBuild


def parse_args():
    parser = argparse.ArgumentParser(description="ISO Artifact Builder")

    parser.add_argument('--release', type=str, help="Major Release Version", required=True)
    parser.add_argument('--s3', action='store_true', help="S3")
    parser.add_argument('--rc', action='store_true', help="Release Candidate")
    parser.add_argument('--arch', type=str, dest='build_arch', help="Architecture")
    parser.add_argument('--local-compose', action='store_true', help="Compose Directory is Here")
    parser.add_argument('--force-unpack', action='store_true', help="Force an unpack")
    parser.add_argument('--force-download', action='store_true', help="Force a download")
    parser.add_argument('--s3-region', type=str, help="S3 region (overrides defaults)")
    parser.add_argument('--s3-bucket', type=str, help="S3 bucket name (overrides defaults)")
    parser.add_argument('--s3-bucket-url', type=str, help="S3 bucket url (overrides defaults)")
    parser.add_argument('--logger', type=str)
    return parser.parse_args()


def run():
    args = parse_args()
    cfg = empanadas.common.collect_config(args)
    IsoBuild(cfg).run_pull_lorax_artifacts()
