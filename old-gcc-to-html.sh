echo '<pre style="background-color: #073642; color: #EEE8D5">'
(echo $ gcc $@ ; /usr/bin/gcc $@ -fdiagnostics-color=always 2>&1) \
    | ~/coding-3/gcc-git-bugfixing/src/ansi2html.sh \
        --bg=dark --palette=solarized --body-only \
    | sed 's|<span class="bold">|<span style="color: #FDF6E3">|g' \
    | sed 's|<span class="f1">|<span style="color: #D30102">|g' \
    | sed 's|<span class="f2">|<span style="color: #859900">|g' \
    | sed 's|<span class="f4">|<span style="color: #268BD2">|g' \
    | sed 's|<span class="f5">|<span style="color: #D33682">|g' \
    | sed 's|<span class="f6">|<span style="color: #2AA198">|g' \
    | sed 's|[ \t]*$||'
echo '</pre>'
