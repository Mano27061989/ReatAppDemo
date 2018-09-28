How to Run: 

1)./httpry 'dst (10.1.1.2 or 10.1.1.5 or 10.1.1.9 or 10.1.1.7)' -d -o /var/log/httpry/enp0s3.log

2) while [ 1 ] ;do kill -HUP  $HTTPRY_PID  ;sleep 1;done

3) python sendUserStat.py &

4) python sendSysStat.py &

5) cp API.war to /opt/tomcat/webapps/API.war
   mkdir -p /home/Hackathon/acpudb
   mkdir -p /home/Hackathon/userdb

6) systemctl restart tomcat.service

7) in react app folder -> npm install rc-progress --save
   npm run start
7) in browser: http://localhost:3000/ for GUI

