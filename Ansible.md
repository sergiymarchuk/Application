<pre>
Comment. --Run playbook.yml according to inventory file 
ansible-playbook -i invetory -v playbook.yml

-i invetory Spec. file include info: like list of servers or additional env.
-v output all info on console during running 
</pre>

<pre>
vi /etc/ansible/hosts
[appsrv]
appsrv ansible_ssh_port=3333 ansible_ssh_host=127.0.0.1 ansible_ssh_private_key_file=~/.vagrant.d/id_rsa
[monsrv]
monsrv ansible_ssh_port=4444 ansible_ssh_host=127.0.0.1 ansible_ssh_private_key_file=~/.vagrant.d/id_rsa
</pre>

<pre>
- name: Change time zone
command: sed -i 's/# php_value date.timezone Europe\/Riga/php_value date.timezone Europe\/Kiev/g' /etc/httpd/conf.d/zabbix.conf
command: awk '{print $1,$2,$3}' /path/filename
command: awk  -F':' '{print $1,$2,$3}' /path/filename
</pre>

<pre>
---
- hosts: homework
  sudo: yes
  remote_user: vagrant

  tasks:
  - hostname: name=serverone

  - name: Install wget
    yum: name=wget state=present

  - name: Install wget
    yum: name=strace state=present

  - name: Add EPEL repository
    yum: name=epel-release state=present

  - name: Install Zabbix-Server
    yum: name=zabbix-server-mysql state=present

  - name: Install Zabbix-Web-Mysql
    yum: name=zabbix-web-mysql state=present

  - name: Install Mysql Server
    yum: name=mysql-server state=present
  - service: name=mysqld state=started
  - service: name=mysqld enabled=yes

  - name: Install the latest version of Apache.
    yum: name=httpd state=latest
    yum: name=mod_ssl state=latest

  - service: name=httpd state=restarted

  - name: Install Zabbix-Client
    yum: name=zabbix-agent state=present

  - service: name=zabbix-agent state=started
  - service: name=zabbix-agent enabled=yes


  - name: Install SNMPD
    yum: name=net-snmp-utils state=present
    yum: name=net-snmp state=present

  - service: name=snmpd state=started
  - service: name=snmpd enabled=yes
</pre>


