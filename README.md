![Rakound](https://user-images.githubusercontent.com/50743705/131849955-2bb55d07-5a48-45ac-ab06-a1c45db58819.png)
# Rakound

Rakound is a tool written in Python. Its main goal is to simplify vizualisation of Bloodhound data. It allows to access insignificant data, such as passwords, stored in Active Directory. The tool is provided with various queries in order to retrieve valuable data.

Moreover, cracked passwords (via JohnTheRipper) and hashes (via Impacket Secretsdump) can be imported to modify abuse paths and perform statistics.

Rakound needs Bloodhound data to perform queries. **It is not packaged to collect data by itself.**

## Requirements

Rakound needs the following requirements to work:

* Neo4j database
* Python3
* Bloodhound data

## Quick setup

From terminal, create python environment and install dependencies :

```bash
$ virtualenv -p python3 rakound_env
$ source rakound_env/bin/activate
$ pip3 install -r requirements.txt
```

Run Rakound :

```bash
$ python3 rakound.py
```

## Full documentation

Full documentation is avalaible here : https://rakound.readthedocs.io/en/latest/