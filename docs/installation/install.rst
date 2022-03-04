Installation
============

Rakound
-------

Rakound must be downloaded from Digitemis' Github page:

.. code-block:: bash
    
    $ git clone https://github.com/Digitemis/Rakound.git

The directory is structured as follow:

.. code-block:: bash

    $ tree -L1 Rakound
    Rakound
    ├── config/
    ├── database/
    ├── docs/
    ├── exports/
    ├── modules/
    ├── queries/
    ├── rakound.py
    ├── README.md
    └── requirements.txt

At this point, you will have the tool locally. You need to 
follow the next step before using it.

Python
------

Python3 environment must be initialized.

You can create a dedicated environment to prevent conflicts 
with other installed tools. The following command can be used:

.. code-block:: bash

    $ virtualenv -p python3 rakound_env

Then, you need to enter in that environment:

.. code-block:: bash

    $ source rakound_env/bin/activate

Next, all requirements must be installed:

.. code-block:: bash

    $ pip3 install -r requirements.txt

That's all, Rakound can now be runned.