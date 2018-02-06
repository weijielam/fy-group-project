# fyp-group-project
Final Year Group Project


This project shows you how to build a basic web application using popular web technologies 
like NPM, Webpack, React and Python.

Dependencies
- Ubuntu 16.04 LTS
- Node.js v8.9.4
- NPM 5.6.0
- Python
- pip

## Installing and Running from scratch
1. Clone the repo
```git
git clone https://github.com/weijielam/fygroupproject.git
```

2. Install NPM, nodejs and curl
```
sudo apt-get remove nodejs npm ## remove existing nodejs and npm packages
sudo apt-get install curl  
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs  
```
3. Install pip
```
sudo apt-get install python-pip
```
4. cd to fypgroupproject/fullstack_template/static directory, run npm install, npm run watch
```
cd fypgroupproject/fullstack_template/static
npm install
npm run watch
```
5. Open new terminal, create virtualenv, start virtualenv
```
cd
virtualenv venv
source venv/bin/activate
```
6. Install flask
```
cd fygroupproject
pip install flask
```
7. Start server, cd to server directory "python server.py"
```
cd fullstack_template/server
python server.py
```

### A Simple Website
When you click the button, 'Hello' will be displayed in a random European language.

This is what it should look like:
![Simple Website](simple_website.png?raw=true "A Simmple Website")


