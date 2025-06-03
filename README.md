# Databases and Information Systems Group Project

## Prerequisite

* Podman or docker

## How to run

### Podman 

Run the following to build and run a clean version of the web-app alongside its database

`podman kube down kube.yaml`\
`podman volume rm pgsql-pvc`(If you want to wipe the database)\
`podman build -f Podfile -t web-app`\
`podman play kube kube.yaml`

### Docker

- (possibly start docker socket)
- `docker pull postgres`
- `docker run --name wizard -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres`
- change the host ip in `.env` to the result of `docker inspect wizard | grep -i ipaddr`

---

Then navigate to:
`http://localhost:5000`


The data is inserted by code in the insert tab,
this works for some reason, this adds all test data into
the DB

To thest the app try searching for the artist habe
