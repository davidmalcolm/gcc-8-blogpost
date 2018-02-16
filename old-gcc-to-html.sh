echo '<pre class="f9 b9">'
(echo $ gcc $@ ; /usr/bin/gcc $@ -fdiagnostics-color=always 2>&1) \
    | ~/coding-3/gcc-git-bugfixing/src/ansi2html.sh \
        --bg=dark --palette=solarized --body-only \
    | sed 's|[ \t]*$||'
echo '</pre>'
