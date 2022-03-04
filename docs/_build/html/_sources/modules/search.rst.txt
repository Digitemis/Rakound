.. _Search module:

Module: search
==============
This module is used to search information in the neo4j database.

General usage:

.. code-block:: none

    🦝 > search <submodule> <filter> <term>

.. warning::

    The provided search term must be a single word. You can't use 
    this module to search for a complete sentence containing spaces.

Results can be exported to a csv file using the keyword "**export**" 
at the end of the command:

.. code-block:: none

    🦝 > search <submodule> <filter> <term> export

A csv file will be generated in "**exports**" directory.

search password
---------------
This module operates search on passwords.

General usage:

.. code-block:: none

    🦝 > search password <filter> [term]

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > search password=enabled <filter> [term]

is
^^
This directive finds passwords corresponding to the searched term. 
**It is case sensitive**.

.. code-block:: none

    🦝 > search password is P@ssw0rd

like
^^^^
This directive finds passwords containing the searched term. 
**It is not case sensitive**.

.. code-block:: none

    🦝 > search password like QwErTy

lm
^^
This directive finds passwords using LM storage. 

.. code-block:: none

    🦝 > search password lm

user_as_pass
^^^^^^^^^^^^
This directive finds passwords equal to username. 
**It is not case sensitive**.

.. code-block:: none

    🦝 > search password user_as_pass

empty
^^^^^
This directive finds empty passwords.

.. code-block:: none

    🦝 > search password empty

.. note::
    We recommend to use this directive with "**password=enabled**" 
    to see only enabled users with empty password.

search user
---------------
This module operates search on users.

General usage:

.. code-block:: none

    🦝 > search user <filter> [term]

To filter by enabled users, "**=enabled**" must be used:

.. code-block:: none

    🦝 > search user=enabled <filter> [term]

is
^^
This directive finds users corresponding to the searched term. 
**It is case sensitive**.

.. code-block:: none

    🦝 > search user is user1

like
^^^^
This directive finds users containing the searched term. 
**It is not case sensitive**.

.. code-block:: none

    🦝 > search user like adm

search computer
---------------
This module operates search on computers.

General usage:

.. code-block:: none

    🦝 > search computer <filter> <term>

is
^^
This directive finds computers corresponding to the searched term. 
**It is case sensitive**.

.. code-block:: none

    🦝 > search computer is SRV01

like
^^^^
This directive finds computers containing the searched term. 
**It is not case sensitive**.

.. code-block:: none

    🦝 > search computer like SRV

search description
------------------
This module operates search on description field.

General usage:

.. code-block:: none

    🦝 > search description <filter> [term]

is
^^
This directive finds descriptions corresponding to the searched term. 
**It is case sensitive**.

.. code-block:: none

    🦝 > search description is testsecret

like
^^^^
This directive finds descriptions containing the searched term. 
**It is not case sensitive**.

.. code-block:: none

    🦝 > search description like pass

not_empty
^^^^^^^^^
This directive finds all not empty descriptions.

.. code-block:: none

    🦝 > search description not_empty
