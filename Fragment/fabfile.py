from __future__ import with_statement
from fabric.api import *
import ConfigParser

env.colorize_errors = True
env.use_ssh_config = True
env.roledefs = {
    'www': ['tiger', 'dragon'],
    'op': ['tiger', 'dragon'],
    'consumer_cron': ['worker'],
    'consumer_pay': ['worker'],
    'consumer_msg': ['worker'],
}


@hosts('localhost')
def deploy(*programs):
    def usage(all_programs):
        print '''
Usage:
fab deploy:<program>

All available programs:\n%s
''' % '\n'.join(all_programs)
        exit()

    def get_all_programs():
        config = ConfigParser.ConfigParser()
        config.read('supervisord.conf')
        all_programs = [p[8:] for p in config.sections() if p.startswith('program:')]
        return config, all_programs

    def deploy_by_git(program, config):
        section = 'program:' + program
        try:
            num = config.getint(section, 'numprocs')
        except:
            num = 1

        try:
            name_fmt = config.get(section, 'process_name', raw=True)
        except:
            name_fmt = ''

        directory = '/'.join(config.get(section, 'command', raw=True).split(' ')[1].split('/')[:5])

        if num > 1:
            names = [program + ':' + name_fmt % {'process_num': i} for i in range(0, num)]
        else:
            if name_fmt:
                names = [program + ':' + name_fmt % {'process_num': 1}]
            else:
                names = [program]

        with cd(directory):
            sudo('pwd', user='deploy')
            cmd = (
                'git checkout . '
                # 'git checkout . && '
                # 'git fetch origin && '
                # 'git rebase origin/develop '
            )
            sudo(cmd, user='deploy')

        with cd('/home/deploy'):
            cmd = ' && '.join(['supervisorctl restart ' + name for name in names])
            run(cmd)
            cmd = 'supervisorctl status %s' % ' '.join(names)
            run(cmd)

    # main program goes here
    config, all_programs = get_all_programs()
    if not programs:
        usage(_all_programs)

    if programs[0] == 'all':
        programs = all_programs

    invalid_programs = set(programs) - set(all_programs)

    if invalid_programs:
        print 'Invalid program%s: %s \n' % ('s' if len(invalid_programs) > 1 else '', ', '.join(invalid_programs))
        usage(all_programs)

    for program in programs:
        with settings(roles=[program]):
            execute(deploy_by_git, program, config)
