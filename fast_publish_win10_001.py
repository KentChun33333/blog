import os, sys

cmd = os.system

cmd('make html')
cmd('cp -r output/* ../KentWebIO')
#cmd('cd ../KentWebIO')
cmd('git -C ../KentWebIO add .')
cmd('git -C ../KentWebIO commit -m"update post"')
cmd('git -C ../KentWebIO push')

cmd('git add .')
cmd('git commit -m"update post"')
cmd('git push')

