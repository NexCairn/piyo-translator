import sys
import argparse
from piyo.core import PiyoTranslator

def main():
    parser = argparse.ArgumentParser(description="Piyo Translator CLI")
    parser.add_argument("text", nargs="?", help="Text to translate (or read from stdin)")
    parser.add_argument("-d", "--decode", action="store_true", help="Decode Piyo to text")
    
    args = parser.parse_args()
    
    # Read input
    if args.text:
        input_text = args.text
    else:
        # Read from stdin if no argument provided
        if sys.stdin.isatty():
            # If no input and tty, show help
            parser.print_help()
            return
        input_text = sys.stdin.read().strip()

    try:
        if args.decode:
            result = PiyoTranslator.decode(input_text)
        else:
            result = PiyoTranslator.encode(input_text)
        
        print(result)
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
