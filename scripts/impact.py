#!/usr/bin/env python
import argparse

from impactlib.refresh import refresh
from impactlib.search import search
from impactlib.install import install

parser = argparse.ArgumentParser(prog='impact')
subparsers = parser.add_subparsers(help='command help')

def call_refresh(args):
    if args.source_list==[] or args.source_list==None:
        source_list = None
    else:
        source_list = args.source_list
    refresh(output=args.output, verbose=args.verbose,
            source_list=source_list, tolerant=args.forgiving,
            ignore_empty=args.ignore)

def call_search(args):
    search(term=args.term[0], description=args.description,
           verbose=args.verbose)

def call_install(args):
    install(pkgname=args.pkgname[0], verbose=args.verbose,
            username=args.username, password=args.password,
            token=args.token, dry_run=args.dry_run)

parser_refresh = subparsers.add_parser('refresh',
                                       help="Used for private package listings")
parser_refresh.add_argument("source_list", nargs="*")
parser_refresh.add_argument("-v", "--verbose", action="store_true",
                            help="Verbose mode", required=False)
parser_refresh.add_argument("-f", "--forgiving", action="store_true",
                            help="Allow non-semver tags", required=False)
parser_refresh.add_argument("-i", "--ignore", action="store_true",
                            help="Ignore packages with no versions",
                            required=False)
parser_refresh.add_argument("-o", "--output", default=None,
                            help="Output file", required=False)
parser_refresh.set_defaults(func=call_refresh)

parser_search = subparsers.add_parser('search',
                                      help="Search for term in package")
parser_search.add_argument("term", nargs=1)
parser_search.add_argument("-v", "--verbose", action="store_true",
                           help="Verbose mode", required=False)
parser_search.add_argument("-d", "--description", action="store_true",
                           help="Include description", required=False)
parser_search.set_defaults(func=call_search)

parser_install = subparsers.add_parser('install',
                                       help="Install a named package")
parser_install.add_argument("pkgname", nargs=1)
parser_install.add_argument("-v", "--verbose", action="store_true",
                            help="Verbose mode", required=False)
parser_install.add_argument("-d", "--dry_run", action="store_true",
                            help="Suppress installation", required=False)
parser_install.add_argument("-u", "--username", default=None,
                            help="GitHub username", required=False)
parser_install.add_argument("-p", "--password", action=None,
                            help="GitHub password", required=False)
parser_install.add_argument("-t", "--token", default=None,
                            help="GitHub OAuth token", required=False)
parser_install.set_defaults(func=call_install)

args = parser.parse_args()

args.func(args)
