import os, sys

os.system('make html')
os.system('cp -rf output/* ..//KentWebIO')

os.system('cd ..//KentWebIO')

os.system('git add .')
os.system('git commit -m"update post"')
os.system('git push')


