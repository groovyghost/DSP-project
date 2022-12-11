# -*- mode: ruby -*-
# vi: set ft=ruby :
VAGRANTFILE_API_VERISON = "2"

Vagrant.configure(VAGRANTFILE_API_VERISON) do |config|
  config.vm.box = "ubuntu/focal64"
  config.ssh.insert_key = false
  config.vm.synced_folder ".", "/vagrant", disabled: true
  config.vm.provider :virtualbox do |v|
    v.memory = 1024
    v.linked_clone = true
  end
  # Database server.
  config.vm.define "mongo.db" do |mongo|
    mongo.vm.hostname = "mongo.db"
    mongo.vm.network "forwarded_port", guest: 27017, host: 27017
    mongo.vm.network :private_network, ip: "192.168.56.6"
    mongo.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/mongodb.yml"
      ansible.inventory_path = "ansible/hosts.ini"
      ansible.limit = "all"
    end
  end

  # Database server.
  config.vm.define "mysql.db" do |mysql|
    mysql.vm.hostname = "mysql.db"
    mysql.vm.network "forwarded_port", guest: 3306, host: 3306
    mysql.vm.network :private_network, ip: "192.168.56.7"
    mysql.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/mysql.yml"
      ansible.inventory_path = "ansible/hosts.ini"
      ansible.limit = "all"
    end
  end
end
