import re
import subprocess
import sys

def invoke_gcc(cmd):
    print(subprocess.check_output(['bash', './gcc-to-html.sh', cmd]))

def invoke_old_gcc(cmd):
    print(subprocess.check_output(['bash', './old-gcc-to-html.sh', cmd]))

def include_source(path):
    # TODO: pygments
    print('<pre>')
    with open(path) as f:
        for line in f:
            sys.stdout.write(line)
    print('</pre>')

def handle_file(path):
    with open(path) as f:
        for line in f:
            m = re.match('INVOKE_GCC (.*)', line)
            if m:
                invoke_gcc(m.group(1))
                continue
            m = re.match('INVOKE_OLD_GCC (.*)', line)
            if m:
                invoke_old_gcc(m.group(1))
                continue
            m = re.match('INCLUDE (.*)', line)
            if m:
                handle_file(m.group(1))
                continue
            m = re.match('INCLUDE_SOURCE (.*)', line)
            if m:
                include_source(m.group(1))
                continue
            sys.stdout.write(line)

handle_file(sys.argv[1])
