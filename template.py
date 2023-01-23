import argparse

# Instantiate parser
parser = argparse.ArgumentParser(description='Description')

# Add options
parser.add_argument('required_positional', help="required positional", type=str)
parser.add_argument('required_with_choices', help="required positional", choices=['generate', 'reconstruct'])
parser.add_argument('--long','-l', help="option with shortcut and default", type=int, default=1)
parser.add_argument('--flag', help='boolen flag, default false', action='store_true')

# Make dict with options
args = vars(parser.parse_args())
