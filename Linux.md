<p>1. Add new application as new servise into system. Centos 7 / RedHat 7</p>

<pre>
cp /opt/app/current/init.d/AppName.init.d /etc/init.d/AppName
systemctl enable AppName.serv
chkconfig --list AppName
service AppName status
</pre>

<p>2. Bash. For.</p>
<pre>
 ssh host-02 'mkdir /home/UserName/link-nfs'
 rsync -ar -e ssh /home/UserName/link-nfs/ host-02:/home/UserName/link-nfs/

for i in $(cat inventory); do echo $i; ssh -q $i mkdir /home/UserName/link-nfs; done
for i in $(cat inventory); do echo $i; ssh -q $i mkdir ls -ld /home/UserName/link-nfs; done

for i in $(cat inventory); do echo $i; rsync -ar -e ssh /home/UserName/link-nfs/ $i:/home/UserName/link-nfs/; done

for i in $(cat inventory); do echo $i; ssh -q $i rm -rf /home/UserName/link-nfs/RPM-Packege-xxx.i386.rpm /home/UserName/link-nfs/RPM-Packege-yyy.rpm; done
</pre>

<p>3. User Management </p>
<pre>
useradd UserName -d /home/UserName -s /bin/bash -G group1,appgroup -c "User.Name@domain.ext User Name Phone Number etc."

Comment. -- Date of expiration will be set.
useradd -e 2025-12-31 username


usermod -aG new_suplemmenatry_group username

Comment. -- Setup shell sh ksh or nologin etc.
usermod -s /sbin/nologin username

Comment. -- Remove user force or remove home folder username 
userdel -f username
userdel -r username

Comment. --  Change primery group for username.
groupmod -g GID username 

passwd -l username
passwd -u username

Comment. -- Get day after 90 days as example.
date -d +"90 days"

Comment. -- User must change password on next attempting to login.
chage -d 0 USER-NAME 

Comment. -- Get info about userID oracle.
chage -l oracle 
Ref. passwd -S oracle

Comment. -- Change expiration day for ID oracle.
chage -E "2025-07-31" oracle

Comment. -- Change expiration day to 'never'.
chage -I -1 -m 0 -M 99999 -E -1 testuser

• -I -1 : This will set the “Password inactive” to never
• -m 0 : This will set the minimum number of days between password change to 0
• -M 99999 : This will set the maximum number of days between password change to 99999
• -E -1 : This will set “Account expires” to never.
This will disable the password expiry of a user if it is already enabled.

Comment. -- Get info about iserID.
getent passwd UID
getent passwd USERNAME

Additional settings for users
/etc/login.defs
/etc/libuser.conf
/etc/default/useradd
</pre>

<p> 4. Create Random Password </p>
<pre>
dd if=/dev/urandom bs=1 count=20 2>/dev/null | base64
or
date +%s | sha256sum | base64 | head -c 32 ; echo to create a password
</pre>

<p>5. Date </p>
<pre>

date -s "28 OCT 2015 10:38:00"

hwclock --show

date --set="23 June 1988 10:00:00"
date --set="10:00:00"

rm -rf /etc/localtime
ln -s /usr/share/zoneinfo/Europe/Kiev /etc/localtime

date
</pre>

<p>6. Disk usage.</p> 
<pre>
du -h --max-depth=1/usr/mail/domain/ | grep M 

du -sh /usr/spool/mail/
</pre>

<p>7. Gnome.</p>
<pre>
CentOS6
Comment. --desktop install 6.7 centos
yum -y groupinstall "X Window System"
yum install x11 fonts
yum -y groupinstall "Desktop"
yum -y groupinstall "General Purpose Desktop"
</pre>

<p>8. Hardware. Dmidecode. </p>
<pre>
Comment. --Get info about memory slots etc.
dmidecode | grep -A 12 "Memory Device"| grep -e "Memory Device" -e "Size:" -e "Speed: " | grep -ve "Mapped Address" -ve "Range"

dmidecode -t system

dmidecode -t memory

dmidecode -t bios

dmidecode -s system-product-name

dmidecode -t baseboard

  bios
  system
  baseboard
  chassis
  processor
  memory
  cache
  connector
  slot

</pre>

<p>8. Get info about page size  </p>
<pre>
getconf PAGE_SIZE 
</pre>

<p>9. Process memory usage utilization.</p>
<pre>
 ps aux | sort -nk +4 | tail 
 ps axo %mem,pid,euser,cmd | sort -nr | head -n 10 
</pre>

<p>10. MariaDB on Centos6</p>
<pre>
#Install Mariadb on centos 6
#Prepare yum.
#/etc/yum.repos.d/MariaDB.repo
#add next lines

[mariadb]
name = MariaDB-5.5.39
baseurl=https://downloads.mariadb.com/files/MariaDB/mariadb-5.5.39/yum/rhel6-amd64/
# alternative: baseurl=http://archive.mariadb.org/mariadb-5.5.39/yum/rhel6-amd64/
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1

yum install MariaDB-server MariaDB-client

create user 'root'@'10.0.2.2' identified by 'yourpassword';
grant all privileges on *.* to 'root'@'10.0.2.2' with grant option;
flush privileges;

CREATE USER 'serge'@'%' IDENTIFIED BY 'P!S@O#D';
GRANT ALL PRIVILEGES ON *.* TO 'serge'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;

service mysql status
service mysql start

<p> Reset password on MariaDB</p>
Comment. --Reset password root MariaDB
1. sudo mysqld_safe --skip-grant-tables --skip-networking &
2. Let login into another terminal session
3. mysql -u root
4. use mysql;
5. update user set password=PASSWORD("new-password") where User='root';
6. flush privileges;
7. exit
8. Lets go the first teminal 
9. kill jobs
10. #jobs
11. kill %jobs
12. Check new password:
13. mysql -u root -p
</pre>

<p>10. Provide hash</p>
<pre>
Comment. --Create password in hash view.  
@centos6-64-p ~]$ grub-crypt
Password:
Retype password:
$6$YmEr.x8G8GS6AI7t$EefHuvzesJ2uvsrGSx0RWTAUtLDK47fW/gag0TDNpukVdAa0ApkfUxoYcd7Ck0Fp6HnTQRNWLRYREP1eLqZwS1
</pre>

<p> 11. SSH. </p>
<pre>
Comment. --Run ssh agent.
eval `ssh-agent -s` 
Comment. --Use key spec. path.
ssh-add -i /path/id_rsa
</pre>

<p> 12. SSH. Convert key.</p>
<pre>
If client provide public key which was created by Windows puttygen, it has been converted in OpenSSH format before use in unix/linux

$ cat id_rsa.pub
---- BEGIN SSH2 PUBLIC KEY ----
Comment: "rsa-key-20151002"
Asadasd1yc2EAAAABJQfsadshcNNOPNpoRBUsFDSDFSdffp3J6Kn5Ob
8J+8FVr/o1KpvzQQGLrdjwWfczEFdFim5OKQDFSDFSDluD+asdpz2JmASE
nNhwGmCL1sdfsdfw2M5PAXhHgr9tOeag9ad/dWMDSFSDFkYi/20vpI
xdmDSwMJuptv30/sMRvDwPxSYfiasdtXnJp4FUBCSADCDSFDSFxNFwXCQqRs5r
UKjRsacaXg4TQku91gCkhrj9sBlRrTxs9OqaenHASasSWEQWEDREFSDCWEWD
l/kJ/5qwxj+Fez+lurG7GlgsEYDZizTgMkUEB6QuGPNTIbn+pQ==
---- END SSH2 PUBLIC KEY ----

$ ssh-keygen -i -f id_rsa.pub > id_rsa.pub
$cat id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAlhcNNOPNpoRBU8SEW/zn8pdpkcfp3J6Kn5Ob8J+8FVr/o1KpvzQQGLrdjwWfczEFdFim5OKQluD+wZFTP4eG7Y15pz2JmXrF3G3EnNhwGmCL1h56pAsHM5PAXhHgr9tO6Sz42eag9N4qzpEcQZlsrO4/dWMkYi/20vpIxdmDSwMJuptv30/sMRvDwPxSYfiRqi8u5qjtATtlBgtXnJp4FUBCxNFwXCQqRs5rUKjRCBKL2sVuGwFYDIhnyIP3Xg4TQku91gCkhrj9sBlRrTxs9OqaenHE/1BzHnq6l/kJ/5qwxj+Fez+lurG7GlgsEYDZizTgMkUEB6QuGPNTIbn+pQ==
</pre>

<p>13. TSM. </p>
<pre>
*  Some usefully dsmc or dsmc_afs commands follow:                               *
*                                                                                *
*                                                                                *
*        - when was the latest backup?                                           *
*  dsmc>   q fi                                                                  *
*                                                                                *
*        - which files from your home pwd are backed up?                         *
*  dsmc>   q b *                                                                 *
*                                                                                *
*        - which old file versions from your home pwd are backed up?             *
*  dsmc>   q b -ina *                                                            *
*                                                                                *
*        - simple file restore, with replace option:                             *
*  dsmc>   restore -rep=yes /afs/desy.de/user/a/anyuser/show.html                *
*                                                                                *
*        - selection menu of old file versions:                                  *
*  dsmc>   restore -ina -pick /afs/desy.de/user/a/anyuser/exp.cmz                *
*                                                                                *
*        - restore old file version with date limit                              *
*  dsmc>   restore -ina -pitdate=2002.07.18  /afs/desy.de/user/a/anyuser/x.cpp   *
*                                                                                *
*                                                                                *
*        - restore old directory version, with date limit and replace data       *
*  dsmc>   restore -ina -rep=yes -subdir=yes -pitdate=2002.05.12 /afs/desy.de/user/a/anyuser/tesla/     
*                                                                                *
*                                                                                *
*        - online help                                                           *
*  dsmc>   help                                                                  *
*                                                                                *
*        - work done                                                             *
*  dsmc>   quit                                                                  *
*                                                                                *
*                                                                                *
*  Start the TSM/ADSM GUI with:  dsm or dsm_afs                                  * 
</pre>

<p>14. </p>
<pre>
Putty ..> Connection ..> SSS ..> Auth ..> X11 ..> Enabled X11 forwarding  (check box -- status ON)
As example let's connect to internal linux server via ssh 
after login Router Server checking DISPLAY value
echo $DISPLAY
localhost:44.0
let go to target server 
ssh -X target-server-name
echo $DISPLAY
localhost:10.0
rpm -qa | grep x11
...

xorg-x11...

...

xclock

P.S.
on windows statiion was prepared xming packege and run 
</pre>

<p>15. </p>
<pre>

</pre>
