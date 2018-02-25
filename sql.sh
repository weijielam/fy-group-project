sudo mysql -u root -p <<EOF
CREATE USER 'dt_admin'@'localhost' IDENTIFIED BY 'dt2016';
CREATE DATABASE dreamteam_db;
GRANT ALL PRIVILEGES ON dreamteam_db . * TO 'dt_admin'@'localhost'
EOF

