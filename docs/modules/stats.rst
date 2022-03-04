.. _Stats module:

Module: stats
=============
.. warning::

    This module can only be used after successfull NTLM and cracked 
    passwords imports.

This module is used to generate statistics on imported passwords.

General usage:

.. code-block:: none

    🦝 > stats password[=enabled] <filter>

stats password admin
--------------------
This submodule evaluates the robustness of cracked password for 
privileged users.

.. code-block:: none

    🦝 > stats password admin

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > stats password=enabled admin

stats password user
-------------------
This submodule evaluates the robustness of cracked password for 
unprivileged users.

.. code-block:: none

    🦝 > stats password user

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > stats password=enabled user

stats password all
------------------
This submodule evaluates the robustness of cracked password for 
all users.

.. code-block:: none

    🦝 > stats password all

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > stats password=enabled all