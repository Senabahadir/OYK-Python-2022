Vagrant.configure("2") do |config|
    config.vm.box = "fasmat/ubuntu2204-desktop"
    compiler.vm.synced_folder ".", "/home/vagrant/app"
    compiler.vm.provider "virtualbox" do |v|
      v.name = "OYK-Python-2022"
      v.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
    end
end