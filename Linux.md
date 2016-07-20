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
