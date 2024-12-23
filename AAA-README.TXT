March 22, 2022

Notes on the uploaded NOW data:

Two of the NOW data files exceeded the Cornell Box 15GB single-file upload limit:
   
   now-db.tar
   now-wlp.tar
   
These .tar files were split into 10GB pieces with these Linux commands:

        split  -d -a 3 -b 10G --verbose now-db.tar now-db.tar.
		
		split  -d -a 3 -b 10G --verbose now-wlp.tar now-wlp.tar.

Use the following commands to combine the pieces into single .tar files

        cat now-db.tar.???  > now-db.tar

        cat now-wlp.tar.??? > now-wlp.tar
		
		