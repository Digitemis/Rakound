Configuration
=============

In order to connect Rakound to the neo4j database, 
parameters need to be specify in the file *config/config.ini*.

.. code-block:: none

    $ cat config/config.ini
    [Database]
    uri = bolt://localhost:7687/
    user = neo4j
    password = neo4j

* **uri**: bolt URI formated as "bolt://IP:Port/" (*Default: bolt://localhost:7687/*)
* **user**: neo4j user (*Default: neo4j*)
* **password**: neo4j password (*Default: neo4j*)

If parameters are not specified in the configuration file, Rakound will 
ask you to specify them on startup.

