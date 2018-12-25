sudo apt-get install -y erlang
sudo apt-get install rabbitmq-server
sudo systemctl enable rabbitmq-server
sudo systemctl start rabbitmq-server
####sudo systemctl status rabbitmq-server


sudo rabbitmqctl add_user root lusine_admin
sudo rabbitmqctl set_user_tags root administrator
sudo rabbitmqctl set_permissions -p / root ".*" ".*" ".*"


sudo rabbitmqctl add_vhost test
sudo rabbitmqctl set_permissions -p task root ".*" ".*" ".*"


## docker compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose