import os
import tests
from pathlib import Path

import tests


#def resource_path(file_name):
#    os.path.abspath(os.path.join(os.path.dirname(__file__), '../resources'))


def path(file_name):
    return str(
        Path(tests.__file__).parent.joinpath(f'resources/{file_name}').absolute()
    )
