.. _Admin module:

Module: admin
=============
This module is used to query data about privileged accounts.

General usage:

.. code-block:: none

    🦝 > admin <submodule>[=enabled]

Results can be exported to a csv file using the keyword "**export**" 
at the end of the command:

.. code-block:: none

    🦝 > admin <submodule> export

A csv file will be generated in "**exports**" directory.

admin domain
------------
This submodule finds all members of "domain admins" group.

.. code-block:: none

    🦝 > admin domain

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > admin domain=enabled

admin enterprise
----------------
This submodule finds all members of "enterprise admins" group.

.. code-block:: none

    🦝 > admin enterprise

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > admin enterprise=enabled

admin schema
------------
This submodule finds all members of "schema admins" group.

.. code-block:: none

    🦝 > admin schema

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > admin schema=enabled

admin accountOperators
----------------------
This submodule finds all members of "account operators" group.

.. code-block:: none

    🦝 > admin accountOperators

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > admin accountOperators=enabled

admin administrators
--------------------
This submodule finds all members of "administrators" group.

.. code-block:: none

    🦝 > admin administrators

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > admin administrators=enabled

admin backupOperators
---------------------
This submodule finds all members of "backup operators" group.

.. code-block:: none

    🦝 > admin backupOperators

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > admin backupOperators=enabled

admin printOperators
--------------------
This submodule finds all members of "print operators" group.

.. code-block:: none

    🦝 > admin printOperators

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > admin printOperators=enabled

admin replicators
-----------------
This submodule finds all members of "replicators" group.

.. code-block:: none

    🦝 > admin replicators

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > admin replicators=enabled

admin serverOperators
---------------------
This submodule finds all members of "server operators" group.

.. code-block:: none

    🦝 > admin serverOperators

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > admin serverOperators=enabled

admin adminSDHolder
-------------------
This submodule lists membership of all previous groups.

.. code-block:: none

    🦝 > admin adminSDHolder

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > admin adminSDHolder=enabled

admin passwordneverexpires
--------------------------
This submodule finds all privileged users with a password 
that never expires.

.. code-block:: none

    🦝 > admin passwordneverexpires

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > admin passwordneverexpires=enabled
