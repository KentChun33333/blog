import os

cmd = os.system
github_io_dir = '../KentWebIO'

cmd('make html')
cmd(f'cp -r output/* {github_io_dir}')
cmd(f'git -C {github_io_dir} add .')
cmd(f'git -C {github_io_dir} commit -m"update post"')
cmd(f'git -C {github_io_dir} push')

cmd('git add .')
cmd('git commit -m"update post"')
cmd('git push')

