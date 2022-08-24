Vagrant.configure("2") do |config|
  config.vm.box = "gusztavvargadr/ubuntu-desktop"
  config.vm.synced_folder ".", "/home/vagrant/Desktop/oyk-python"
  config.vm.provider "virtualbox" do |v|
    v.name = "OYK-Python-2022"
    v.memory = 2048
    v.gui = true
    config.vm.network "public_network"
    v.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
  end

  config.vm.provision "shell", inline: <<-SHELL

    export DEBIAN_FRONTEND=noninteractive
    # Add Python PPA
    add-apt-repository ppa:deadsnakes/ppa -y

    # VsCode
    wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | apt-key add -
    add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"

    # Install Python 3.9
    apt-get install -y python3.9 python3.9-distutils code libxcb-xinerama0 qttools5-dev-tools

    # Install Pipenv
    wget -q https://raw.githubusercontent.com/pypa/pipenv/master/get-pipenv.py -O- | python3.9

    # Installation finihed
    echo "####################################################"
    echo "##             Installation finished             ###"
    echo "####################################################"
  
  SHELL
end
