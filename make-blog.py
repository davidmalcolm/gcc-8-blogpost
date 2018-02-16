import re
import subprocess
import sys

from pygments import highlight
from pygments.lexers import guess_lexer_for_filename
from pygments.formatters import HtmlFormatter

class Writer:
    def write(self, text):
        sys.stdout.write(text)

    def invoke_gcc(self, cmd, helper_script):
        out = subprocess.check_output(['bash', helper_script, cmd],
                                      stderr=subprocess.PIPE)
        assert 'class=' not in out
        self.write(out + '\n')

    def include_source(self, path):
        self.write('<pre>\n')
        with open(path) as f:
            code = f.read()
        lexer = guess_lexer_for_filename(path, code)
        self.write(highlight(code, lexer, HtmlFormatter(noclasses=True)))
        self.write('</pre>\n')

    def handle_file(self, path):
        with open(path) as f:
            for line in f:
                m = re.match('INVOKE_GCC (.*)', line)
                if m:
                    self.invoke_gcc(m.group(1), './gcc-to-html.sh')
                    continue
                m = re.match('INVOKE_OLD_GCC (.*)', line)
                if m:
                    self.invoke_gcc(m.group(1), './old-gcc-to-html.sh')
                    continue
                m = re.match('INCLUDE (.*)', line)
                if m:
                    self.handle_file(m.group(1))
                    continue
                m = re.match('INCLUDE_SOURCE (.*)', line)
                if m:
                    self.include_source(m.group(1))
                    continue
                self.write(line)

w = Writer()
w.handle_file(sys.argv[1])
