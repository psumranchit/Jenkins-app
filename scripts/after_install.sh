#!/bin/bash
EC2_INSTANCE_ID=$(curl -s http://169.254.169.254/latest/meta-data/instance-id)
EC2_AZ=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone)
sed -i "s/was deployed/was deployed on $EC2_INSTANCE_ID in $EC2_AZ/g" /flask-web/templates/Jenkins-page.html
chmod 664 /flask-web/templates/Jenkins-page.html
