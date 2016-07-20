<pre>
# -*- mode: ruby -*-
# vi: set ft=ruby :
##Vagrant.configure(2) do |config|
Vagrant.configure(2) do |config|
  config.ssh.insert_key = false
  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--memory", "1024"]
  end
# Application server 1.
  config.vm.define "app1" do |app|
    app.vm.hostname = "app1-ser.ora"
    app.vm.box = "geerlingguy/centos7"
    app.vm.network :private_network, ip: "192.168.55.101"
  end
# Application server 2.
  config.vm.define "app2" do |app|
    app.vm.hostname = "app2-ser.ora"
    app.vm.box = "geerlingguy/centos7"
  app.vm.network :private_network, ip: "192.168.55.102"
  end
# Database server.
  config.vm.define "db" do |db|
    db.vm.hostname = "db-ser.ora"
    db.vm.box = "geerlingguy/centos7"
    db.vm.network :private_network, ip: "192.168.55.103"
  end
end
</pre>
