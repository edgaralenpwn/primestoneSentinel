@@ -0,0 +1,153 @@
# Primestone Sentinel

An all-powerful toolset for Primestone.

Sentinel is an autonomous agent for persisting, processing and automating Primestone V12.1 governance objects and tasks.

Sentinel is implemented as a Python application that binds to a local version 12.1 primestoned instance on each Primestone V12.1 Masternode.

This guide covers installing Sentinel onto an existing 12.1 Masternode in Ubuntu 14.04 / 16.04.

## Installation

### 1. Install Prerequisites

Make sure Python version 2.7.x or above is installed:

    python --version

Update system packages and ensure virtualenv is installed:

    $ sudo apt-get update
    $ sudo apt-get -y install python-virtualenv

Make sure the local Primestone daemon running is at least version 12.1 (120100)

    $ primestone-cli getinfo | grep version

### 2. Install Sentinel

Clone the Sentinel repo and install Python dependencies.

    $ git clone https://github.com/edgaralenpwn/primestoneSentinel.git && cd primestoneSentinel
    $ export LC_ALL=C
    $ virtualenv ./venv
    $ ./venv/bin/pip install -r requirements.txt
    

### 2.a. Check primestone.conf

Change the configuration checking, and appending if missing the following
parameters rpcuser and rpcpassword needs to be replaced

    rpcuser=<ADD A RANDOM STRING HERE>
    rpcpassword=<ADD A RANDOM STRING HERE>
    listen=1
    server=1
    discover=1
    rpcport=19470
    rpcthreads=8
    rpcallowip=127.0.0.1
    daemon=1
    listen=1
    server=1
    staking=0
    discover=1

    addnode=54.36.163.216:8585

                          

Clone the Sentinel repo and install Python dependencies.    


### 2.b. remove old files
Enter the wallet folder and stop the wallet

    ./primestone-cli stop 
    
Enter the primestone config folder mentioned during the installation
    
    rm mncache.dat
    rm mnpayments.dat
    
Enter the wallet folder and restart the wallet 

    ./primestoned -daemon -reindex
    
Check the sync status

    watch ./primestone-cli mnsync status

As soon as you see the following response press CTRL+C

    ./primestone-cli mnsync status
    {
    "AssetID": 999,
    "AssetName": "MASTERNODE_SYNC_FINISHED",
    "Attempt": 0,
    "IsBlockchainSynced": true,
    "IsMasternodeListSynced": true,
    "IsWinnersListSynced": true,
    "IsSynced": true,
    "IsFailed": false
    }

Finally start the masternode

    ./primestone-cli masternode start


