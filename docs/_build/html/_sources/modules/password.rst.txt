.. _Password module:

Module: password
================
This module is used to query data about passwords.

General usage:

.. code-block:: none

    🦝 > password <submodule>[=enabled]

Results can be exported to a csv file using the keyword "**export**" 
at the end of the command:

.. code-block:: none

    🦝 > password <submodule> export

A csv file will be generated in "**exports**" directory.

password comment
----------------
This submodule tries to find passwords in "description" field, based on 
the following patterns: "pw", "pass", "mdp" and "code".

.. code-block:: none

    🦝 > password comment

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > password comment=enabled

password userpassword
---------------------
This submodule tries to find if any passwords are stored in "userpassword" 
field.

.. code-block:: none

    🦝 > password userpassword

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > password userpassword=enabled

password changeddate
--------------------
This submodule lists all users whose password has not been changed for a 
given number of days.

By default, it takes 90 days:

.. code-block:: none

    🦝 > password changeddate

To specify custom period, give the number of days (for example, 180 days):

.. code-block:: none

    🦝 > password changeddate 180

This can be useful to check passwords that not meet password age policy.

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > password changeddate=enabled