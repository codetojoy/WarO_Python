
"""
The entry point for the War-O game
"""

import sys
import traceback

from config import build_config_from_json_file
from tourney import play_tourney

def main():
    """
    entry point for the War-O game
    """
    try:
        json_file = sys.argv[1]
        config = build_config_from_json_file(json_file)
        play_tourney(config)
        print("Ready.")
    except:
        e = sys.exc_info()[0]
        print("major error: " + str(e))
        traceback.print_exc()
        sys.exit(-1)

if __name__ == "__main__":
    main()
