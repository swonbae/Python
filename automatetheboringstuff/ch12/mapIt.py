#! python3
# mapIt.py - Launches a map in the browser using an address from the command line or clipboard.
# Derived from 'https://automatetheboringstuff.com/2e/chapter12/' by Al Sweigart

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+address)
