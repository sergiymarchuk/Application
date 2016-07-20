<p>1. Add new application as new servise into system. </p>

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
