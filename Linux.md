1. <p> Add new application as new servise into system. </p>

<pre>
cp /opt/app/current/init.d/AppName.init.d /etc/init.d/AppName
systemctl enable AppName.serv
chkconfig --list AppName
service AppName status
</pre>

2. <p> Bash. For.</p>

<pre>
 ssh host-02 'mkdir /home/UserName/link-nfs'
 rsync -ar -e ssh /home/UserName/link-nfs/ host-02:/home/UserName/link-nfs/

for i in $(cat inventory); do echo $i; ssh -q $i mkdir /home/UserName/link-nfs; done
for i in $(cat inventory); do echo $i; ssh -q $i mkdir ls -ld /home/UserName/link-nfs; done

for i in $(cat inventory); do echo $i; rsync -ar -e ssh /home/UserName/link-nfs/ $i:/home/UserName/link-nfs/; done

for i in $(cat inventory); do echo $i; ssh -q $i rm -rf /home/UserName/link-nfs/RPM-Packege-xxx.i386.rpm /home/UserName/link-nfs/RPM-Packege-yyy.rpm; done
<pre>
