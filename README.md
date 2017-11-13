Udacity Linux Server Configuration Project
==========================================
Private IP Address: 172.26.0.221
Public IP Address/App URL: 50.112.72.208
SSH Port is 2200.

The software that I have downloaded include: flask, packaging, oauth2client, redis, passlib, flask-httpauth, sqlalchemy, psycopg2, bleach, requests.

In order to ssh into the application using a OSx/Linux distro, you would use the command sudo ssh -i theSecretKey.pub grader@50.112.72.208 -p 2200 with the password being blank. 

The application is located in /var/www/html/reality-catalog.
<h3> Grader </h3>
For the Grader user I configured the SSH by using:
  sudo chmod 700 /home/grader/.ssh.
  sudo chmod 644 /home/grader/.ssh/authorized_keys
while placing the public key in the authorized_keys file.
I also changed the owner from root to grader using sudo:
  chown -R grader:grader /home/grader/.ssh

For the SSH Port I changed it from 22 to 2200 in lightsail as well as the file /etc/ssh/sshd_config by using the command:
sudo vim /etc/ssh/sshd_config and changing the port number.

This allows you to ssh using:
  sudo ssh -i privateKey.pub grader@50.112.72.208 -p 2200 

the server was configured so that the root user can only be accessed internally by using the command: 
  sudo vim /etc/ssh/sshd_config. changed PermitRootLogin line "no".

The user grader was created and and an ssh-keygen pairing was given in order to remote as the grader. I changed the apache configurations in order to host our web application with the configurations below:

<VirtualHost *:80>
	DocumentRoot /var/www/html/reality-catalog



	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined

 	WSGIDaemonProcess catalog user=ubuntu group=ubuntu threads=5 python-home=/var/www/html/reality-catalog python-path=/usr/local/lib/python2.7/site-packages
	WSGIScriptAlias / /var/www/html/reality-catalog/catalog.wsgi
	<Directory /var/www/html/reality-catalog>
		AllowOverride none
        	#WSGIProcessGroup catalog
        	WSGIApplicationGroup %{GLOBAL}
        	WSGIScriptReloading On
    		Require all granted
	</Directory>
</VirtualHost>

Here are a list of some of the 3rd party resources used to complete the project:
https://www.jakowicz.com/flask-apache-wsgi/ <br />
https://www.ssh.com/ssh/host-key <br />
https://www.linode.com/docs/security/use-public-key-authentication-with-ssh <br />
https://www.digitalocean.com/community/questions/ubuntu-16-04-creating-new-user-and-adding-ssh-keys <br />
https://support.rackspace.com/how-to/logging-in-with-an-ssh-private-key-on-linuxmac/ <br />
https://www.fullstackpython.com/blog/ssh-keys-ubuntu-linux.html <br />
https://git-scm.com/book/en/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key <br />
https://mediatemple.net/community/products/dv/204403684/connecting-via-ssh-to-your-server <br />
https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh <br />
http://flask.pocoo.org/docs/0.12/deploying/mod_wsgi/ <br />
A lot of stackoverflow links were looked at in the course of the project to configure wsgi correctly.
