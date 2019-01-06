import os
import sys

try:
    templatepath = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "packages", "template")
    if templatepath not in sys.path:
        sys.path.append(templatepath)
    import template
    from template import *
    sys.modules['template'] = template
except ImportError:
    raise RuntimeError(
        "web2py depends on template, which apparently you have not installed.\n" +
        "Probably you cloned the repository using git without '--recursive'" +
        "\nTo fix this, please run (from inside your web2py folder):\n\n" +
        "     git submodule update --init --recursive\n\n" +
        "You can also download a complete copy from http://www.web2py.com."
    )