
import sys
import os
import argparse
from argparse import RawTextHelpFormatter

try:
    import fontforge
except ImportError:
    sys.exit(
        "FontForge module could not be loaded. Try installing fontforge python bindings "
        "[e.g. on Linux Debian or Ubuntu: `sudo apt install fontforge python-fontforge`]"
    )

class Renamer:
    def __init__(self):
        self.args = None  # class 'argparse.Namespace'
        self.sourceFont = None  # class 'fontforge.font'
        self.replacements = {}
        self.license = ''
        
        self.setup_arguments()

        self.sourceFont = fontforge.open(self.args.font)

        replacements = self.args.replacements.split(',')

        for replacement in replacements:
            key, value = replacement.split('/')

            self.replacements[key] = value

        self.copyright = self.args.copyright
        
        if self.args.license:
            self.license = open(self.args.license, 'r').read()

        self.setup_font_names()


    def rename(self):
        self.sourceFont.generate(self.args.output, flags=(str('opentype')))
        
        print("\nRenamed: {}".format(self.sourceFont.fontname))

    def setup_arguments(self):
        parser = argparse.ArgumentParser(
            description="Font renamer",
            formatter_class=RawTextHelpFormatter
        )

        parser.add_argument('font', help='The path to the font to rename (e.g., Inconsolata.otf)')
        parser.add_argument('-r', '--replace', dest='replacements', default='', type=str, nargs='?', help='Format: replacement/pattern,replacement/pattern,...')
        parser.add_argument('-license', dest='license', default=False, type=str, nargs='?', help='The path to the license file')
        parser.add_argument('-copyright', dest='copyright', default='', type=str, nargs='?', help='The copyright thing')
        parser.add_argument('-out', '--output', dest='output', default=".", type=str, nargs='?', help='The output font file')

        self.args = parser.parse_args()


    def setup_font_names(self):

        self.sourceFont.familyname = replace_font_name(
            self.sourceFont.familyname,
            self.replacements
        )
        self.sourceFont.fullname = replace_font_name(
            self.sourceFont.fullname,
            self.replacements
        )
        self.sourceFont.fontname = replace_font_name(
            self.sourceFont.fontname,
            self.replacements
        )

        trademark_index = -1

        for i, sfnt_name in enumerate(self.sourceFont.sfnt_names):
            lang, strid, string = sfnt_name

            if strid == "Trademark":
                trademark_index = i

                continue

            self.sourceFont.appendSFNTName(
                lang,
                strid,
                replace_font_name(
                    string,
                    self.replacements
                )
            )

        if trademark_index >= 0:
            sfnt_names = self.sourceFont.sfnt_names

            self.sourceFont.sfnt_names = sfnt_names[:trademark_index] + sfnt_names[trademark_index + 1:]

        self.sourceFont.appendSFNTName(
            "English (US)",
            "License",
            self.license
        )

        self.sourceFont.appendSFNTName(
            "English (US)",
            "Copyright",
            self.copyright
        )

        self.sourceFont.copyright = self.copyright


def replace_font_name(font_name, replacement_dict):
    for key, val in replacement_dict.items():
        font_name = font_name.replace(key, val)
    
    return font_name


def main():
    renamer = Renamer()
    renamer.rename()


if __name__ == "__main__":
    main()
