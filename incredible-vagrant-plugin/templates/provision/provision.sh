#!/bin/bash

apt-get update
apt-get install -y curl git cmake tmux vim default-jre default-jdk maven # ...
sudo curl -L https://github.com/docker/compose/releases/download/1.25.3/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
curl -sLS https://get.arkade.dev | sudo sh
curl -L https://github.com/kubernetes/kompose/releases/download/v1.28.0/kompose-linux-amd64 -o kompose
sudo arkade get kubectl
sudo arkade get kind
sudo mv /root/.arkade/bin/kubectl /usr/local/bin/
sudo mv /root/.arkade/bin/kind /usr/local/bin/
sudo chmod +x /usr/local/bin/kubectl
sudo chmod +x /usr/local/bin/kind
chmod +x kompose
sudo mv ./kompose /usr/local/bin/kompose
kind create cluster
arkade install ingress-nginx