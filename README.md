# KapostTechnicalInterview
Repo for Kapost technical interview.

To use first build the project using this command in the root directory:

> docker build ".\" -t IMAGE_TAG

Next use this command to run the image itself replacing $dest, $src, $minsize ($minsize should be in MB):

> docker run IMAGE_TAG $dest $src $minsize

NOTE: currently only works with a single account but enviroment variables can be adjusted manually in Dockerfile or during the Docker build command
