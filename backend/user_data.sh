#!/bin/bash
sudo yum update -y
sudo yum install git -y
sudo amazon-linux-extras install docker
sudo service docker start
sudo usermod -a -G docker ec2-user
sudo chkconfig docker on
sudo curl -L https://github.com/docker/compose/releases/download/1.29.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
ssh-keygen -t ed25519 -C "arpitkjain@deloitte.com"
sudo reboot