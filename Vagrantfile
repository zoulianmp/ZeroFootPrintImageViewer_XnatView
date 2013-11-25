VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define :xnatview do |xnatview_config|
    xnatview_config.vm.box = "precise64_base"
    xnatview_config.vm.box_url = "http://files.vagrantup.com/precise64.box"
    xnatview_config.vm.network :private_network, ip: "192.168.100.15"
    xnatview_config.vm.provider :virtualbox do |vb|
      vb.customize ["modifyvm", :id, "--memory", "2048"]
      vb.customize ["modifyvm", :id, "--cpus", "2"]
    end

#    xnatview_config.vm.provision "shell", path: "fabric_wrapper.sh"
  end

end
