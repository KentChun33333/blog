#! /usr/bin/env python

"""
### Author : Kent Chiu
- Note Identity Encoding Regulation : className-xx-name.ipynb
 - className should be correnspoding to content/folderName/
 - xx and name should be in one-to-one relation
 - name must not contain - symbol
 - xx in [00,99]
 - where we call className-xx-name == NoteID

- Asset Identity Encoding Regulation : className-xx-name-yy == NoetID-yy
 - yy in [00,99]
 - yy is the number on the condition of Asset Type, for example :
   - RL-01-MDP-00.jpg
   - RL-01-MDP-00.avi

- Asset Type
 - img (jpg | png)
 - video (avi with h264 codec) better via youtube or other CDN
 - audio (mp3) better via youtube or other CDN

"""

import argparse, os, re

# get cli-variables as input address
parse = argparse.ArgumentParser()
parse.add_argument('-f', '--file', required=True,
    help='the full address of the notebook file')
arg = parse.parse_args()

# Functions : get corresponding asset (one Note to many Assets)
def get_asset( dirname ,NoteID):
    assert os.path.isdir(dirname+'/image') == True
    assert os.path.isdir('output/image') == True
    file_list = os.listdir(dirname+'/image')
    for item in file_list :
        if str.lower(item.split('.')[-1]) not in ('jpg','png','jepg','bmp','avi'):
            continue
        if re.match(r'{}-*[0-9]'.format(NoteID) ,item.split('.')[0]):
            input_asset  = os.path.join(dirname+'/image',item)
            output_asset = os.path.join('output/image',item)
            yield input_asset, output_asset


if __name__ == '__main__':
    dirname      = os.path.dirname(arg.file) # /xx/xx
    filename     = (arg.file).split('/')[-1] # /xx/xx/yyy.ipynb > yyy.ipynb
    class_name   = filename.split('-')[0]

    assert os.path.isdir('content/{}'.format(class_name))==True
    assert len(filename.split('.'))==2

    NoteID , filetype   = filename.split('.') # NoteID = yyy

    output_file  = 'content/{}/{}'.format(class_name,filename)

    # cp the articles to content
    os.system('cp {} {}'.format(arg.file, output_file))

    # cp the assets
    print (dirname, NoteID)
    for input_asset, output_asset in get_asset(dirname, NoteID):
        os.system('cp {} {}'.format(input_asset, output_asset))
        print ('[*] cp the assces {} to {}'.format(input_asset, output_asset))

    # git auto, use git to rollback
    os.system('../git_auto')
    print ('---------------- [blog] git push already -------------------')
    print ('[*] please adding ipynb-meta file')
    print ('[*] then pelican  content -> output git add . && commit && push')




