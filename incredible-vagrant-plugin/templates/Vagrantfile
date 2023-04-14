Vagrant.configure("2") do |config|
  config.vm.box = "debian/buster64"
  config.vm.hostname = "app"
  config.vm.define "app"
  config.vm.provision "docker"

  config.vagrant.plugins = ['vagrant-vbguest']

  config.vm.network "private_network", ip: "192.168.56.10"

  config.vm.synced_folder "./", "/home/vagrant/project"

  config.vm.provider "virtualbox" do |vb|
    vb.cpus = 4
    vb.memory = "2048"
  end


  config.vm.provision "shell", path: 'provision/provision.sh'
  config.vm.provision "shell", path: 'provision/build.sh'

end