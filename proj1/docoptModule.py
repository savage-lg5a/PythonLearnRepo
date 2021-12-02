"""UserManage
Usage:
  user_manage user (add|delete) (<name>) [<password>  --authority=<authority>]
  user_manage change_name <name>
  user_manage change_pwd <password>
  user_manage add_description <description>...
  user_manage -h | --help
  user_manage --version

Options:
    -h --help                     帮助.
    -v --version                  查看版本号.
    --authority=<authority>       权限设置 [default: user].
    --group=<group>               分组
"""
from docopt import docopt

arguments = docopt(__doc__, version='UserManage 2.0')

if arguments.get('add'):
    print(arguments)

elif arguments.get('delete'):
    print(arguments)

elif arguments.get('change_name'):
    print(arguments)


