# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  #config.vagrant.plugins = "vagrant-disksize"
  config.ssh.insert_key = false

  #config.vm.box = "generic/rhel7"
  #config.vm.box = "generic/rhel8"
  #config.vm.box = "generic/rhel9"
  config.vm.box = "ubuntu/jammy64"
  
  config.vm.synced_folder './parcial', '/home/vagrant/repogit'
  config.vm.hostname = "VMDiscos"
  config.vm.define :VMDiscos do |t|
  end

  

  config.vm.network "private_network", :name => '', ip: "192.168.56.3"

  # Agrego un nuevo disco (Ver Readme.md)
  config.vm.disk :disk, size: "10GB", name: "extra_storage"
  config.vm.disk :disk, size: "2GB", name: "extra_storage2"

  config.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
      vb.name = "VMDiscos"
      vb.cpus = 2
      vb.linked_clone = true
  end

  # Puedo Ejecutar un script que esta en un archivo
  config.vm.provision "shell", path: "script_Enable_ssh_password.sh"

  # Agrega la key Privada de ssh en .vagrant/machines/default/virtualbox/private_key
  config.ssh.insert_key = true

end
