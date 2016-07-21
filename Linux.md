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



groupadd test

#Создать группу testgroup2 с ID 506
groupadd -g 506 testgroup2

#Создать группу testgroup3 с системным ID по умолчанию
groupadd -r testgroup3


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
du -h --max-depth=1 -B M |sort -rn
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

# dmesg |grep DMI
DMI 2.5 present.
DMI: innotek GmbH VirtualBox/VirtualBox, BIOS VirtualBox 12/01/2006

# dmesg |grep DMI
DMI 2.5 present.
DMI: HP ProLiant DL380 Gen BIOS P40 10/25/2012

# dmidecode -s system-product-name
VirtualBox

# dmidecode -s system-product-name
...
ProLiant DL380 p Gen8

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

<p>14. Forward X over SSH. </p>
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

<p>16. Apt. Ununtu.<p>
<pre>
apt-cache search git
</pre>

<p>17. </p>
<pre>
Comment. --Ping on ethernet level.
arping 192.168.16.254
</pre>

<p>18. at </p>
<pre>


at hh:mm dd.mm.yy

echo "shutdown -h +0 "  |  at now +20min

#atq
3   Thu Oct 18 10:25:00 2012 a linuxaria
4   Thu Oct 18 20:00:00 2012 a linuxaria
6   Fri Oct 19 00:00:00 2012 a linuxaria

If you have to check task from at just run this: at -c #task
Example:
at -c identifier_task

So you can see task 
</pre>

<p>18. Bash</p>
<pre>
@linux:~/tmp$ true; echo $?
0
@linux:~/tmp$ false; echo $?
1
</pre>

<p>19. Process bg fg </p>
<pre>


#on running process CTRL+Z
#fg
#jobs посик заданий
#bg №jobs вернуть из бекраунда в интерактивный режим процесс
#fg %1

kill %n


</pre>

<p>20. Block device.</p>
<pre>
blkid
lsblk
lsscsi
</pre>

<p>21. Cron check. </p>
<pre>
#!/bin/bash
#List all cron jobs for all users
for user in `cat /etc/passwd | cut -d":" -f1`;
do 
crontab -l -u $user;
done
</pre>

<p>22. Crul. </p>
<pre> 
Curl

curl -LO http://c.speedtest.net/mini/mini.zip ; rm -f mini.zip

wget -O /tmp/login.tmp --keep-session-cookies --save-cookies=/tmp/cookies.txt --post-data 'login=USERRRR&pwd=PASSSSS' http://url.domain.local/webacula/auth/login wget -O /var/www/html/status_o.html --load-cookies=/tmp/cookies.txt http://url.domain.local/webacula/job/terminated
</pre>

<p>23. Cut</p>
<pre>

# ifconfig eth0 192.168.50.254 netmask 255.255.255.0 # Первый IP адрес
# ifconfig eth0:0 192.168.51.254 netmask 255.255.255.0 # Второй IP адрес
# ip addr add 192.168.50.254/24 dev eth0 # Эквивалентные команды для ip
# ip addr add 192.168.51.254/24 dev eth0 label eth0:1


 ifconfig | cut -d " " -f 1 | sed -e /^$/d
 ifconfig | cut -d " " -f 1 | grep -v '^$\|^#'

 cat /etc/passwd | cut -d ':' -f 1,2
 cat /etc/passwd | cut -c 7-10
</pre>

<p>24. dd </p>
<pre>
dd if=/dev/zero of=/root/xxx1 bs = 1M count = 100    -CREATE FILE SIZE 100MB 
dd if=/root/xxx1 of=/dev/null bs=1M        -READ FILE  block size = 1М and !!! remeber about cache 

</pre>

<p>25. df</p>
<pre>
# df -hP | awk '{print $5, $6}' |  awk 'NR > 1'
71% /
1% /dev/shm
7% /boot
</pre>


<p>27. dig host</p>
<pre>
# dig MX google.com
# dig @127.0.0.1 NS sun.com # check local server
# dig @204.97.212.10 NS MX sun.com # request to external server
# dig AXFR @ns1.xname.org sun.com # get all zone (forwarding zone)
# dig -x 78.31.70.238 #backresolve

# host -t MX sun.com # Получить записть типа MX(Mail Exchange)
# host -t NS -T sun.com # Получить NS запись через TCP соединение
# host -a sun.com # Получить все
# host 78.31.70.238 бекрезолв
# nslookup 78.31.70.238 бекрезолв
</pre>

<p> 28. dhclient </p>
<pre>
dhclient -r eth0 //renew ip address
</pre>

<p>29. drop_caches </p>
<pre>
echo 1 > /proc/sys/vm/drop_caches
Comment. --After this command system will be caches again and we can get slowdown
Comment. -- Virt память что используется многими процессами если однажны какйото процес загрузил либо или можуль то из памяти другой вызывает это а не запускается все заново 
Comment. --RES сколько использует процесс vmstat inact vmstat active

</pre>

<p>30. file</p>
<pre>
file -s /dev/sda2 
</pre>

<p>31. find</p>
<pre>


find * -mtime +30 | xargs rm
find * -mtime +30 | xargs rm -rf
find /path/to/files* -mtime +5 -exec rm {} \;

find /jira -type f -mtime +365 -exec mv "{}" /tmp/temporary-folder/ \;
find /exports -type f -mtime +365 -exec mv "{}" /tmp/temporary-folder/exports \;

в системе файлов с разрешениями suid и sgid. Для вывода на экран списка всех таких файлов можно использовать команду find:
# find / -type f -perm +6000 -exec Is -I {} \;

find . -name '*.xml' -type f -print | xargs du -ch  get disk usage sum for files of type

find . -type f | awk -F'.' '{print $NF}' | sort| uniq -c | sort -g   look how many files in system for type

find / -mount -size +5000000c -exec ls -l {} \;

find /etc /home –name filename

mtime число — в качестве числа можно указать количество дней, прошедших со дня последнего редактирования файла. Например, если вы вчера редактировали файл с именем note, но не помните, куда его сохранили, то выполните следующую команду:
find / –name note –mtime 1

-type тип — ключ позволяет указать тип файла. В качестве типа можно указывать:
• d — каталог;
• f — обычный файл;
• p — именованный канал;
• l — символическая ссылка.
С помощью find можно искать не только имена файлов или директорий, но и искать по содержимому файлов. Вот вам интересная команда, которую можно запомнить или записать:
find . –type f –name "*" –print | xargs grep "текст, который ищем"
</pre>

<p>33. ftp</p>
<pre>
login:password@ip
</pre>

<p>34. fuser</p>
<pre>
fuser -v -n tcp 5666
fuser -v /

fuser -v -k -i ./
                     USER        PID ACCESS COMMAND
./:                  root      23870 ..c.. bash
                     root      23941 ..c.. bash
                     root      25849 ..c.. python
Kill process 23870 ? (y/N) n
Kill process 23941 ? (y/N) n
Kill process 25849 ? (y/N) n

Comment. --But we can type "y" :) 
</pre>

<p>35. pandoc. Git convert file to pdf format. </p>
<pre>
pandoc 01_vagrant.md -f markdown -t docx -o test.docx
pandoc 01_vagrant.md -f markdown -t pdf -o test.pdf
</pre>

<p>36.git </p>
<pre>
mkdir myProj && cd myProj/ && git init && git pull https://github.com/sergiimarchuk/qalPY
rm -f mountVSfstab.pyc networkCheck.pyc partiotionCheck.pyc statInfo.pyc usersCheck.pyc
git commit -a
git remote add origin https://github.com/sergiimarchuk/qalPY.git
git add *
git commit -m " Comments "
git status
git commit -a
git status
git push origin +master

git config --global user.email "you@example.com"

git remote -v
</pre>

<p>38. html </p>
<pre>
<html><body><h1><a href="load/name_file_2010.rar">Please clik here for starting download</h1></body></html> --> (делаем ссылку на веб)
</pre>

<p>39. iptables </p>
<pre>
iptables -t nat -A POSTROUTING -o eth0 (external) -j MASQUERADE
echo "1" > /proc/sys/net/ipv4/ip_forward

-A RH-Firewall-1-INPUT -i eth0 -j ACCEPT
#Forward port 
-A PREROUTING -d IP-SERVER-EXTERNAL -p tcp -m tcp --dport 3391 -j DNAT --to-destination 192.168.0.56:3389

iptables -A INPUT -s 55.225.yyy.xxx -j REJECT
</pre>

<p>40. limits.conf </p>
<pre>
Under /etc/security/limits.conf:
oracle       soft    nofile          4096
oracle        hard    nofile          131072
oracle        soft    nproc           2047
oracle        hard    nproc           32768

check
..>ulimit -n 
</pre>

<p>41. logger</p>
<pre>
$ logger TEST 111111 222222 33333

You can see message in /var/log/message file
tail -f /var/log/message

</pre>

<p>42. ls </p>
<pre>
ls -l --time-style=+"%Y-%m-%d %H:%M:%S" #date and time when file was created
</pre>

<p>43. lsof. restore file from pid etc.</p>
<pre>
# lsof | grep 26294 смотрим например куда писался ПИД файла как пример
crond     26294                 root    3uW     REG               0,18         6     103393 /run/crond.pid
если кто то удалил /run/crond.pid как пример мы можем
# ls -l /proc/26294/fd
lrwx------. 1 root root 64 Jul 25 02:32 3 -> /run/crond.pid
все содержимое все еще хранится в 3 соответсвенно нужно прочитать например
cat /proc/26294/fd/3 > /run/crond.pid в наш искомый файл или любой другой 

#lsof -i :22
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
sshd     1658 root    3u  IPv4  10246      0t0  TCP *:ssh (LISTEN)
sshd     1658 root    4u  IPv6  10248      0t0  TCP *:ssh (LISTEN)
sshd    23868 root    3u  IPv4 260664      0t0  TCP 10.0.2.15:ssh->10.0.2.2:49600 (ESTABLISHED)
sshd    23939 root    3u  IPv4 261039      0t0  TCP 10.0.2.15:ssh->10.0.2.2:51066 (ESTABLISHED)
sshd    23983 root    3u  IPv4 261310      0t0  TCP 10.0.2.15:ssh->10.0.2.2:51175 (ESTABLISHED)


lsof | grep /mnt/addtional-disk
lsof: WARNING: can't stat() reiserfs file system /dev/.static/dev
Output information may be incomplete.
mc 14134 beast cwd DIR 8,1 4096 1 /mnt/addtional-disk

</pre>

<p>44. mail</p>
<pre>
#mail -s logs email@mx-servername.com < server.log отправить лог 
</pre>
