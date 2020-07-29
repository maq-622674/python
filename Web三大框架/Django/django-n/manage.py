#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
###################################################################################################################################################
########################################django项目管理文件 与项目进行交互的命令行工具集的入口##########################################################
###################################################################################################################################################
import os
import sys


def main():
    
    '''
    这段代码是设置环境变量用的，
    使用Linux,我们可能经常去配置~/.bashrc 
    然后写上  export JAVA_HOME=/usr/local/java/jdk1.8.0_231

    环境变量可以理解为一个大字典，如下
    {....,
    'JAVA_HOME': '/usr/local/java/jdk1.8.0_231'，
    'DJANGO_SETTINGS_MODULE': 'XXXX.settings'
    }

    如果环境变量中没有DJANGO_SETTINGS_MODULE，则设置为XXXX.settings
    如果环境变量已经配置了 DJANGO_SETTINGS_MODULE，则不进行更新，函数返回原有值
    而且 os.environ 配置的环境变量是临时的，运行结束后就会消失
    '''
    ######################################################################
    # #设置环境变量DJANGO_SETTINGS_MODULE，值为Social_networking_sites.settings，即django项目的settings.py所在路径
    #manage.py 主要找到默认配置文件setting.py所在位置,与执行命令
    ######################################################################
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    '''
    2.execute_from_command_line
        里面调用了ManagementUtility类中的execute方法
        def execute_from_command_line(argv=None):
            """
            A simple method that runs a ManagementUtility.
            """
            utility = ManagementUtility(argv)
            utility.execute()
        在execute中主要是解析了传入的参数sys.argv，并且调用了get_command()
    3.get_command

    def get_commands():
        """
        Returns a dictionary mapping command names to their callback applications.

        This works by looking for a management.commands package in django.core, and
        in each installed application -- if a commands package exists, all commands
        in that package are registered.

        Core commands are always included. If a settings module has been
        specified, user-defined commands will also be included.

        The dictionary is in the format {command_name: app_name}. Key-value
        pairs from this dictionary can then be used in calls to
        load_command_class(app_name, command_name)

        If a specific version of a command must be loaded (e.g., with the
        startapp command), the instantiated module can be placed in the
        dictionary in place of the application name.

        The dictionary is cached on the first call and reused on subsequent
        calls.
        """
        commands = {name: 'django.core' for name in find_commands(upath(__path__[0]))}
        if not settings.configured:
            return commands
        for app_config in reversed(list(apps.get_app_configs())):
            path = os.path.join(app_config.path, 'management')
            commands.update({name: app_config.name for name in find_commands(path)})
        return commands


    get_command里遍历所有注册的INSTALLED_APPS路径下的management寻找(find_commands)用户自定义的命令。


    def find_commands(management_dir):
        """
        Given a path to a management directory, returns a list of all the command
        names that are available.

        Returns an empty list if no commands are defined.
        """
        command_dir = os.path.join(management_dir, 'commands')
        # Workaround for a Python 3.2 bug with pkgutil.iter_modules
        sys.path_importer_cache.pop(command_dir, None)
        return [name for _, name, is_pkg in pkgutil.iter_modules([npath(command_dir)])
                if not is_pkg and not name.startswith('_')]
   
    可以发现并注册的命令是commands目录下不以"_"开头的文件名。

    4.load_command_class
    将命令文件***.py中的Command类加载进去。
    def load_command_class(app_name, name):
        """
        Given a command name and an application name, returns the Command
        class instance. All errors raised by the import process
        (ImportError, AttributeError) are allowed to propagate.
        """
        module = import_module('%s.management.commands.%s' % (app_name, name))
        return module.Command()
    
    
    5.Command类
    Command类要继承BaseCommand类，其中很多方法，一定要实现的是handle方法，handle方法是命令实际执行的代码

    '''
    ####################################################################
    ##执行命令  sys.argv值为 ['D:/Social_networking_sites/manage.py', 'runserver', '8000']
    ####################################################################
    execute_from_command_line(sys.argv)

##https://www.jianshu.com/p/39c30bbc1ad5
if __name__ == '__main__':
    main()
