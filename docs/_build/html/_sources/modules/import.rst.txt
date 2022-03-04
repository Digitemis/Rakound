.. _Import module:

Module: import
==============
This module is used to import password files.

General usage:

.. code-block:: none

    🦝 > import <submodule> </path/to/file>

import ntlm
-----------
This submodule imports NTLM hashes.

.. code-block:: none

    🦝 > import ntlm </path/to/file>

Imported file must be formated as follow:

::

    DOMAIN.local\Administrateur:500:aad3b435b51404eeaad3b435b51404ee:e19ccf75ee54e06b06a5907af13cef42:::
    DOMAIN.local\Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
    DOMAIN.local\krbtgt:502:aad3b435b51404eeaad3b435b51404ee:e19ccf75ee54e06b06a5907af13cef42:::
    DOMAIN.local\user1:1001:aad3b435b51404eeaad3b435b51404ee:e19ccf75ee54e06b06a5907af13cef42:::
    DOMAIN.local\user2:1002:921988ba001dc8e14a3b108f3fa6cb6d:e19ccf75ee54e06b06a5907af13cef42:::
    DOMAIN.local\user3:1003:aad3b435b51404eeaad3b435b51404ee:e19ccf75ee54e06b06a5907af13cef42:::
    DOMAIN.local\user4:1004:921988ba001dc8e14a3b108f3fa6cb6d:e19ccf75ee54e06b06a5907af13cef42:::

.. note::

    Using Impacket Secretsdump to dump "NTDS.dit" will provide the attended format.

This submodule adds two property keys to users and/or computers:

* **ntlm**: contains the given NTLM hash
* **lm**: set to true if LM is used in NTLM hash, false if not used

import cracked
--------------
This submodule imports cracked passwords.

.. code-block:: none

    🦝 > import cracked </path/to/file>

Imported file must be formated as follow:

::

    DOMAIN.local\Administrateur:P@ssw0rd:500:aad3b435b51404eeaad3b435b51404ee:e19ccf75ee54e06b06a5907af13cef42:::
    DOMAIN.local\Guest::501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
    DOMAIN.local\krbtgt:P@ssw0rd:502:aad3b435b51404eeaad3b435b51404ee:e19ccf75ee54e06b06a5907af13cef42:::
    DOMAIN.local\user1:P@ssw0rd:1001:aad3b435b51404eeaad3b435b51404ee:e19ccf75ee54e06b06a5907af13cef42:::
    DOMAIN.local\user2:P@ssw0rd:1002:921988ba001dc8e14a3b108f3fa6cb6d:e19ccf75ee54e06b06a5907af13cef42:::
    DOMAIN.local\user3:P@ssw0rd:1003:aad3b435b51404eeaad3b435b51404ee:e19ccf75ee54e06b06a5907af13cef42:::
    DOMAIN.local\user4:P@ssw0rd:1004:921988ba001dc8e14a3b108f3fa6cb6d:e19ccf75ee54e06b06a5907af13cef42:::

.. note::

    JohnTheRipper output (*john --show --format=NT NTDS.dit*) will provide the attended format.

This submodule adds a property key to users and/or computers:

* **cracked_password**: contains the cleartext of cracked password

For all cracked passwords, the corresponding object is set as owned (owned = True). 
This allows to use the following pre-built queries in Bloodhound:

* "Shortest Path from Owned Principals"
* "Shortest Paths to Domain Admins from Owned Principals"
