import argparse
from getpass import getpass
import os.path
import praw
import requests


parser = argparse.ArgumentParser()
parser.add_argument("-U","--username", help="Reddit Username")