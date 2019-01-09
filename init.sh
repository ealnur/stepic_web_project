sudo /etc/init.d/mysql start
#mysql -uroot -e "create user 'admin'@'localhost'"
#mysql -uroot -e "set password for 'admin'@'localhost' = password('pass111')"
#mysql -uroot -e "create database mybase"
mysql -uroot -e "create database stepic_web;"
#mysql -uroot -e "grant all on mybase.* to 'admin'@'localhost'"
mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"
sudo ln -sf ~/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf ~/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart

