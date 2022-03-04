.. _Config module:

Module: config
==============
This module is used to manage database configuration.

General usage:

.. code-block:: none

    🦝 > config <submodule>

config create
-------------
This submodule creates a new configuration file. The current 
configuration will be erased.

.. code-block:: none

    🦝 > config create

config update
-------------
This submodule updates the current configuration file.

To only update **bolt URI**:

.. code-block:: none

    🦝 > config update uri

To only update **neo4j user**:

.. code-block:: none

    🦝 > config update user

To only update **neo4j password**:

.. code-block:: none

    🦝 > config update password

To update **all configuration file**:

.. code-block:: none

    🦝 > config update all

config delete
-------------
This submodule resets configuration file to default.

.. code-block:: none

    🦝 > config delete

config verify
-------------   
This submodule prints current configuration and database 
connection status.

.. code-block:: none

    🦝 > config verify
