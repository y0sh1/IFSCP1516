import argparse


parser = argparse.ArgumentParser(description='Dit is Opdracht 5, IFSCP 1516')
parser.add_argument('-v', action="store_true", dest="verbose", help="Turn on verbosity")
parser.add_argument('-p', action="store", dest="PathToScan", help="Path to the to scan directory", required=True)
parser.add_argument('-d', action="store", dest="DestinationPath", help="Set path to make export to", required=True)
parser.parse_args()

args = parser.parse_args()