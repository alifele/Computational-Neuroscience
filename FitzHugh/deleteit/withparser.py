import argparse

des= '''
This file will Generate the animations of the neural dynamics for you.
by passing the tau_I as the first argument of this function, then the
simulation gif will be generated for you.
$ python3 animations.py -tau_I 12

'''

def get_args():
    parser = argparse.ArgumentParser(description=des)
    parser.add_argument('-tau_I', help = 'Enter the value of tau', dest='tau_I',type=float, required=True)
    args = parser.parse_args()

    return args.tau_I


tau_I = get_args()

print(tau_I)
