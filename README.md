======
Acadia
======

CMS framework built on the Django platform.

TO INSTALL
----------

To install under a virtualenv:

    # Step 0. Create your virtualenv. (virtualenvwrapper highly recommended)
    mkvirtualenv acadia
    cdvirtualenv
    easy_install -a --prefix . pip
    pip install -r /path/to/acadia/requirements.txt

The pip line can be run again if you change anything in the requirements file.

Then, while still "in" the virtualenv, run Acadia with the built-in Django web server:

    # both "acadia"s are necessary to get into the python module dir
    cd /path/to/acadia/acadia
    python manage.py runserver


LICENSE
-------

Copyright 2009 Pat Collins <pat@burned.com>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
