import os
import sys

from invoke import task

try:
    from scss import Scss
except ImportError:
    SCSS_FLAG = False
else:
    SCSS_FLAG = True

try:
    from cssmin import cssmin
except ImportError:
    CSSM_FLAG = False
else:
    CSSM_FLAG = True

try:
    from slimit import minify
except ImportError:
    SLIM_FLAG = False
else:
    SLIM_FLAG = True


class cd(object):
    """
    Context manager for changing the current working directory.
    """
    def __init__(self, new_path):
        self.new_path = new_path

    def __enter__(self):
        self.saved_path = os.getcwd()
        os.chdir(self.new_path)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.saved_path)


@task
def scss(themes=None):
    """
    Convert source/scss files to static/css files

    Requires pyscss."""
    if not SCSS_FLAG:
        print "This task requires pyScss.  (pip install pyscss)"
        sys.exit(0)

    with cd('source/scss'):
        if themes is None:
            themes = (i for i in  os.listdir('themes') if os.path.isfile('themes/' + i))
        else:
            themes = (i.strip() for i in themes.split(','))

        for theme in themes:
            print theme
            compiler = Scss()
            l = "@import 'themes/" + theme[0:-5] + "';\n\n"
            result = compiler.compile(l + open('main.scss').read())
            with open('../../static/css/' + theme[0:-5] + '.css', 'w') as css_file:
                print css_file.name
                css_file.write(result + '\n')


@task
def minify():
    """
    Minifies .css and .js files in static/*, recursively.
    """
    if not (CSSM_FLAG and SLIM_FLAG):
        print "This task requires both slimit and cssmin."
        print "(pip install slimit cssmin)"
        sys.exit(0)

    for root, dirs, files in os.walk('static'):
        for name in files:
            if name.endswith('.min.js') or name.endswith('.min.css'):
                os.remove(os.path.join(root, name))
                files.remove(name)

        for name in files:
            if name.endswith('.js'):
                func = minify
                suff = '.min.js'
            elif name.endswith('.css'):
                func = cssmin
                suff = '.min.css'
            else:
                continue

            with open(os.path.join(root, name), 'r') as f:
                mind = func(f.read())
            fn = os.path.splitext(name)[0] + suff
            with open(os.path.join(root, fn), 'w') as f:
                f.write(mind)



@task('scss', 'minify', default=True)
def build():
    """Build the entire project."""
    pass