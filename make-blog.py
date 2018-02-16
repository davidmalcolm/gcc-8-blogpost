import re
import subprocess
import sys

from pygments import highlight
from pygments.lexers import guess_lexer_for_filename
from pygments.formatters import HtmlFormatter

def invoke_gcc(cmd, helper_script):
    out = subprocess.check_output(['bash', helper_script, cmd],
                                  stderr=subprocess.PIPE)
    assert 'class=' not in out
    print(out)

def include_source(path):
    print('<pre>')
    with open(path) as f:
        code = f.read()
    lexer = guess_lexer_for_filename(path, code)
    sys.stdout.write(highlight(code, lexer, HtmlFormatter(noclasses=True)))
    print('</pre>')

def handle_file(path):
    with open(path) as f:
        for line in f:
            m = re.match('INVOKE_GCC (.*)', line)
            if m:
                invoke_gcc(m.group(1), './gcc-to-html.sh')
                continue
            m = re.match('INVOKE_OLD_GCC (.*)', line)
            if m:
                invoke_gcc(m.group(1), './old-gcc-to-html.sh')
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
