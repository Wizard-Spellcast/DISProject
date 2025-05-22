# Contributing to the project

## Setup development enviorement
Download and setup postgresql 17, leave all settings as defaults except the password which can be changed as you wish but remeber to set the password inside password.txt to corrispond to the password you have chosen.

## Build web-app and deply image
Execute "podman build -f Podfile -t web-app"
Then execute "podman play kube kube.yaml", which will run both the web-app and the postgresql server that the web-app uses to store data.