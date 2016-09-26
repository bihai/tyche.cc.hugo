#!/usr/bin/env python
# coding:utf-8

import os
import sys
import glob
import locale
import shutil
import argparse
import subprocess

__author__ = 'bihai'

GIT_REPO = [
    ['origin',  'gh-pages', 'git@github.com:bihai/tyche.cc.git'],
    # ['gitcafe', 'gh-pages', 'git@gitcafe.com:coderzh/coderzh-hugo-blog.git'],
    #['coding',  'gh-pages', 'git@git.coding.net:coderzh/hugo-blog-deployed.git'],
]

DEPLOY_DIR = 'tyche.cc'


class ChDir:
    """Context manager for changing the current working directory"""
    def __init__(self, new_path):
        self.newPath = os.path.expanduser(new_path)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, exception_type, exception_value, traceback):
        os.chdir(self.savedPath)


def deploy(args):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
    #parent_dir = './'
    #print parent_dir
    public_dir = os.path.join(current_dir, 'public')
    #public_dir = ('public')
    commit_msg = 'blog'

    with ChDir(current_dir):
        # step1 clean
        if os.path.exists(public_dir):
            shutil.rmtree(public_dir)
            subprocess.call('git add --all', shell=True)
            subprocess.call('git commit -a -m "{0}"'.format(commit_msg), shell=True)
            subprocess.call('git push', shell=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='deploy hugo')
    parser.add_argument('type', help='auto or manual')
    parser.add_argument('-t', dest='test', action='store_true', help='for test')
    args = parser.parse_args()

    if args.type in ['auto', 'manual', 'first']:
        deploy(args)
    else:
        deploy(args)

