## Como replicarlo

## First steps to replicate the proyect
 
1. Install [Git](https://git-scm.com/download/linux).
    * [How to Get and Configure Your Git and GitHub SSH Keys](https://www.freecodecamp.org/news/git-ssh-how-to/).
2. Install Git LFS.
    * Install [Git LFS](https://git-lfs.github.com/) `sudo apt install git-lfs` for Linux Ubuntu (To get the LFS up and working in your machine).
3. Install [Docker](https://docs.docker.com/engine/install/) y [Docker-compose](https://docs.docker.com/compose/install/).
4. Install [python3](https://www.python.org/downloads/).
5. Fork or clone the [repository](https://github.com/jorgeav527/life-expectancy).
5. Create a virtual enviroment.
    * Create a env using [conda](https://docs.conda.io/en/latest/).
    * Create a env using [venv](https://www.geeksforgeeks.org/create-virtual-environment-using-venv-python/).
    * Install packages from the requirements.txt (only for vscode to dont complain).
6. Reproduce the development enviroment with.
    * Follow the commands
>```bash
>docker build . --tag extending_airflow:latest
>docker compose up airflow-init
>docker compose up -d
>```
    * To down the contairners and the volumns
>```bash
>docker compose down --volumes --remove-orphans
>```
