.. _User module:

Module: user
=============
This module is used to query data about unprivileged accounts.

General usage:

.. code-block:: none

    🦝 > user <submodule>[=enabled]

Results can be exported to a csv file using the keyword "**export**" 
at the end of the command:

.. code-block:: none

    🦝 > user <submodule> export

A csv file will be generated in "**exports**" directory.

user readlaps
-------------
This submodule finds if any unprivileged user can read LAPS passwords.

.. code-block:: none

    🦝 > user readlaps

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > user readlaps=enabled

user passwordneverexpires
-------------------------
This submodule finds all unprivileged users with a password that 
never expires.

.. code-block:: none

    🦝 > user passwordneverexpires

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > user passwordneverexpires=enabled

user localadmin
---------------
This submodule finds all unprivileged users with local admin 
rights on computers.

.. code-block:: none

    🦝 > user localadmin

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > user localadmin=enabled

user localadminDC
-----------------
This submodule finds all unprivileged users with local admin 
rights on domain controllers.

.. code-block:: none

    🦝 > user localadminDC

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > user localadminDC=enabled