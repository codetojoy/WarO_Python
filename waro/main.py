
"""
The entry point for the War-O game
"""

import sys
import traceback

import config
import tourney

def main():
    """
    entry point for the War-O game
    """
    try:
        json_file = sys.argv[1]
        configuration = config.build_config_from_json_file(json_file)
        tourney.play_tourney(configuration)
        print("Ready.")
    except:
        e = sys.exc_info()[0]
        print("major error: " + str(e))
        traceback.print_exc()
        sys.exit(-1)

if __name__ == "__main__":
    main()
