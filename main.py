import sys
import signal

opts = [opt for opt in sys.argv[1:] if opt.startswith("")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

def signal_handler(sig, frame):
    print("Keyboard interrupt detected, exiting...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    print("the mean is", sum((int(opts) for opts in opts)) / len(opts))
    print("the sum is", sum(int(opts) for opts in opts))
    print("the max is", max(int(opts) for opts in opts))
    print("the min is", min(int(opts) for opts in opts))
    sys.exit(0)
except ValueError:
    print("For the program to work, you must enter a number like this: python main.py -5")
    sys.exit(1)
except ZeroDivisionError:
    print("For the program to work, you must enter a number like this: python main.py -5")
    sys.exit(1)
except KeyboardInterrupt:
    print("For the program to work, you must enter a number like this: python main.py -5")
    sys.exit(1)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')

while True:
    pass
