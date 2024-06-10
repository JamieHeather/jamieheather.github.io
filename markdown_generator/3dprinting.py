# iterating on the theme, a quick python script to populate a md table from a tsv of 3d printed labware details

import pandas as pd

dat = pd.read_csv('3dprinting.tsv', sep='\t')

out_file = '../_pages/3dprinting.md'

prefix = '\n'.join([
    '---',
    'layout: archive',
    'title: "3d printed labware"',
    'permalink: /3dprinting/',
    'author_profile: true',
    '---',
    '\n',
    '{% include base_path %}',
    "\n\nI've been 3d printing labware since my PhD, as it's a cheap, quick, and convenient way to produce "
    "exactly what's needed at the bench. These are a selection of the 3d printing files I've generated for "
    "use in the lab, made available for others to download, edit, print, and use. "
    "They're designed in TinkerCAD, usually in a modular format that allows quick customisation "
    "for specific lab roles.\n\n",
    '| Print | Details |\n|:-----:|:-----:|\n'
])

file_dir = '../files/3dprinting/'

with open(out_file, 'w') as out_file:
    out_file.write(prefix)
    for row in dat.index:
        row_dat = dat.loc[row]
        out_str = '| <img src="' + file_dir + row_dat['image_file'] + '" width="300"/> | '
        out_str += ' <br> '.join([
            '**' + row_dat['title'] + '**',
            "[![Static Badge](https://img.shields.io/badge/stl-8A2BE2)](" + file_dir + row_dat['stl_file'] + ") \\| "
            "[![Static Badge](https://img.shields.io/badge/thingiverse-blue)](https://www.thingiverse.com/thing:" +
            str(row_dat['thingiverse_id']) + ")"
        ])
        out_str += ' |\n'

        out_file.write(out_str)

    out_text = ("\nAlternatively all of my public designs can be found "
                "[on my Thingiverse page](https://www.thingiverse.com/jamimmunology/designs).\n\n"
                "Note that these are shared here under a CC BY-NC-SA license, "
                "however certain models are available under a less restrictive license from Thingiverse.\n")
    out_file.write(out_text)
