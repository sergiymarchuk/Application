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

Ansible module to download file.

Development environment:
Ansible versions: 2.1
OS: CentOS 7

Update Ansible configuration file: /etc/ansible/ansible.cfg 
```
library        = /root/my-ansible-modules/
```
Create directory /root/my-ansible-modules/
Create module file /root/my-ansible-modules/download_file.py

```
#!/usr/bin/python
# Date: 2016-08-05

DOCUMENTATION = '''
---
module: download_file
short_description: Downloads file via URL
description:
  - This module downloads file via url to local destination.
  - It also checks if file already exists and can overwrite file or skip.
options:
  url:
    description:
      - URL to download file.
    required: true
  dest:
    description:
      - Local file destination
    required: true
  overwrite:
    description:
      - Should module overwrite existing file or not.
    required: true
'''

EXAMPLES = '''
- name: Download file
  download_file: url='https://www.kernel.org/doc/linux/README' dest='/tmp/README' overwrite=yes
'''

from ansible.module_utils.basic import *
import urllib
import os

def main():

    module = AnsibleModule(
        argument_spec = dict(
            url       = dict(required=True),
            dest      = dict(required=True),
            overwrite = dict(default='yes', choices=['yes', 'no']),
        )
    )

    url = module.params.get('url')
    dest = module.params.get('dest')
    overwrite = module.params.get('overwrite')

    try:
        if not os.path.isfile(dest):
            urllib.urlretrieve(url, dest)
            res_txt = "Downloaded"
            change_status = True
        else:
            if overwrite == "yes":
                urllib.urlretrieve(url, dest)
                res_txt = "Overwritten"
                change_status = True
            else:
                res_txt = "File exists"
                change_status = False
    except:
        module.fail_json(msg="Downloading failed. URL or DEST is wrong.")

    response = {"Message": res_txt }
    module.exit_json(changed=change_status, meta=response)

if __name__ == '__main__':  
    main()

```

Make file executable:
```
chmod +x /root/my-ansible-modules/download_file.py
```

Create playbook file /root/play.yml

```
---
- hosts: app-servers
  tasks:
    - name: Download file
      download_file: url='https://www.kernel.org/doc/linux/README' dest='/tmp/README' overwrite=yes
      register: result
    - debug: var=result
```

Create inventory file /root/my-inventory:
```
[app-servers]
192.168.1.111
```

Run playbook:
```
ansible-playbook -i my-inventory play.yml
```

Output example:
```
PLAY [app-servers] *************************************************************

TASK [setup] *******************************************************************
ok: [192.168.1.111]

TASK [Download file] ***********************************************************
changed: [192.168.1.111]

TASK [debug] *******************************************************************
ok: [192.168.1.111] => {
    "result": {
        "changed": true, 
        "meta": {
            "Message": "Downloaded"
        }
    }
}

PLAY RECAP *********************************************************************
192.168.1.111              : ok=3    changed=1    unreachable=0    failed=0   
```

"download-file" module documentation:

```
[ansible-server]# ansible-doc download_file
> DOWNLOAD_FILE

  This module downloads file via url to local destination. It also checks if file
  already exists and can overwrite file or skip.

Options (= is mandatory):

= dest
        Local file destination

= overwrite
        Should module overwrite existing file or not.

= url
        URL to download file.

EXAMPLES:
- name: Download file
  download_file: url='https://www.kernel.org/doc/linux/README' dest='/tmp/README' overwrite=yes
```
