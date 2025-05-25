# Databases and Information Systems Group Project

## Prerequisite
* Podman

## How to run
Run the following to build and run a clean version of the web-app alongside its database

`podman kube down kube.yaml`\
`podman volume rm pgsql-pvc`(If you want to wipe the database)\
`podman build -f Podfile -t web-app`\
`podman play kube kube.yaml`

Then navigate to:
`http://localhost:5000`


The data is inserted by code in the insert tab,
this works for some reason, this adds all test data into
the DB

To thest the app try searching for the artist habe