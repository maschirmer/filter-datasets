# dataset_gammaweb
deployment of ds creation on gammaweb cluster

datasets:
https://github.com/linanqiu/reddit-dataset

https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment/

https://huggingface.co/datasets/mschi/twitter_stream_pile/resolve/main/twitter_stream_2020_02_01.tar

https://www.kaggle.com/datasets/kaggle/reddit-comments-may-2015

https://www.kaggle.com/datasets/patjob/articlescrape

RUN CONTAINER: srun --mem=5g --container-image=ds_cont_ubuntu.sqsh --container-name="dscont03" --container-writable --pty bash -i

SLURM IP ADRESS = 141.54.132.206

this is repo for deployment of a docker image on the gammaweb cluster.
inside the image i want to do:

- download dataset
- unpack dataset
- unpack bz2 to json

- run python script that builds dataset on the downloaded dataset
- run python script that filters for english language and replaces the first ds
- run python script that uses a filter and creates a dataframe / dataset of future tense classified texts


what i need:

- dockerfile
- github action workflow for building the image and pushing to ghcr.io
  - why that? --> if i change the image, its easy to rebuild and push again to ghcr.io
- the actual python scripts
- a command pipeline on gammaweb to get it all going




docker image:

- base image: maybe just basic python 3.9 image python 3.9-alpine
- pip update and stuff
- install the reqs from requirements.txt
- install curl ? if not preinstalled
- install unzip ? if not preinstalled

docker container:

1st:
- dataset_container.sqsh
- name: dscont01

2nd:
- ds_cont_ubuntu.sqsh
- name: dscont02

3rd:
- ds_cont_ubuntu.sqsh
- name: dscont03

download the dataset (use curl)
- curl url --output filename (that is stored on storage)
- url: https://archive.org/download/archiveteam-twitter-stream-2020-02/twitter_stream_2020_02_01.tar
- use curl -L to enable website redirection

--> nope: upload it via scp
website: https://success.tanaza.com/s/article/How-to-use-SCP-command-on-Windows

unzip dataset
- apt-get install unzip
- cd $HOME
- unzip filename

github:
- create access tokens



github actions workflow:
  - choose the workflow then manually run workflow

ghcr authentication setup

- on betaweb run:
    touch $HOME/.config/enroot/.credentials
    chmod 600 $HOME/.config/enroot/.credentials
- then:
    echo "machine ghcr.io login GITHUB_USERNAME password GITHUB_ACCESS_TOKEN_WITH_PERMISSION_READ_PACKAGES" >> $HOME/.config/enroot/.credentials
    
    if doesnt work, remove .config file with:
      rm $HOME/.config/enroot/.credentials
    
    and run again with correct credentials (password = token, the actual token, not the name of the token)


gammaweb usage:
- command from betaweb entrypoint to gammaweb: srun 
- make srun interactive: srun --pty
- import container from registry:
  - import as sqsh file!
  - instantiate from sqsh file with container-image = ./imagename.sqsh
- execute container:
  - uoload github credentials to server --> see slurm_deployment.md (with enroot, and manage )
  - srun --mem=5g (memory to be applied) --container-image=[imagename] --pty (make interactive) bash -i
  - important: run with --container-name="name" and --container-writable because slurm doesnt clean up after we finished srun --> store the container       instance on the file system --> installing additional software
  - 
  - 
