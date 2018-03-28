# fyp-group-project
Group 7: Final Year Group Project

## Install and Run Instructions using scripts
1. Install Git and clone the repo
```
sudo apt install git  -y
git clone https://github.com/weijielam/fygroupproject.git
```

2. Run installation scripts

```
cd fygroupproject
sudo bash install.sh
Create an SQL password for root user
Enter SQL root user password when prompted
```
3. Create an admin account 
```
cd dream-team
sudo bash flaskshell.sh
```

```
from app.models import User
from app import db
admin = User(email="admin@admin.com",username="admin",password="admin2018",is_admin=True)
db.session.add(admin)
db.session.commit()
exit()
```

4. Running Flask App: run.sh
```
cd ..
sudo bash run.sh
```
5. Open up browser at localhost:5000

For Feature Documentation go to Documentation/Feature Documentation.md


