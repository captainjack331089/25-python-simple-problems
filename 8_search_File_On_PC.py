"""
If you’re looking for a particular file or type of file on a computer, the last thing you want to do is hunt and peck your way there. And that means—if you find yourself working on an application or software program that needs to be able to find files—you’ll need a way to automate the process.
"""
# Create a function to search a file on PC

import fnmatch
import os

def get_Search_File_Location(search_location, search_type):
    matches = []
    for root, dirnames, filenames in os.walk(search_location):
        for extensions in search_type:
            for filename in fnmatch.filter(filenames, extensions):
                matches.append(os.path.join(root, filename))

    return matches

if __name__ == '__main__':

    images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
    md = ['Into_HTML.md']
    search_location = '/Users/captainjack33/'

    matches = get_Search_File_Location(search_location, md)
    print(matches)