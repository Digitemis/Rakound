Rakound
=======

.. meta::
   :description lang=en: Explore Bloodhound data

.. image:: images/Rakound_logo.png
   :align: center
   :width: 300px
   :alt: Rakound logo
 
|

Rakound is a tool written in Python. Its main goal is to simplify vizualisation of 
Bloodhound data. It allows to access insignificant data, such as passwords, stored 
in Active Directory. The tool is provided with various queries in order to retrieve 
valuable data.

Moreover, cracked passwords (via JohnTheRipper) and hashes (via Impacket Secretsdump)
can be imported to modify abuse paths and perform statistics.

Rakound needs Bloodhound data to perform queries. **It is not packaged to collect data 
by itself.**

Requirements
------------

Rakound needs the following requirements to work:

* Neo4j database
* Python3
* Bloodhound data

Tool
----

Rakound is available on Digitemis' Github: https://github.com/Digitemis/Rakound

Improvements & Bugs
-------------------

If you discover some bugs or want some new features, please submit them directly on
the Github page.

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Installation & Configuration

   installation/install
   installation/config
   installation/run

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Usage

   modules/all
   modules/db
   modules/config
   modules/admin
   modules/user
   modules/computer
   modules/password
   modules/import
   modules/search
   modules/stats