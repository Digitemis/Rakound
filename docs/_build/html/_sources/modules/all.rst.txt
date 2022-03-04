All modules
===========

In the interactive shell, you must use all provided modules 
to query the neo4j database.

Here is the list of all available modules:

* **config**: manage database configuration (see :ref:`Config module`)
* **db**: manage database connection (see :ref:`Db module`)
* **admin**: query data related to admins (see :ref:`Admin module`)
* **user**: query data related to users (see :ref:`User module`)
* **computer**: query data related to computers (see :ref:`Computer module`)
* **password**: query data related to passwords (see :ref:`Password module`)
* **import**: import cracked passwords and ntlm hashes (see :ref:`Import module`)
* **search**: search information in neo4j database (see :ref:`Search module`)
* **stats**: perform statistics on cracked passwords (see :ref:`Stats module`)
* **help**: print help for a given module

An autocompletion is available in the interactive shell. By pressing <tab> twice, 
available modules are suggested. By doing the same after a module, it will show 
you available submodules.

Help informations for a specific module can be printed with the following command:

.. code-block:: none

    🦝 > help <module_name>

