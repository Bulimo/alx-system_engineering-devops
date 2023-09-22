# Install flask using pip3

exec { 'install_flask':
    command  => '/usr/bin/pip3 install flask==2.1.0'
}

package { 'flask':
    ensure   => '2.1.0',  # Specify the desired version here
    provider => 'pip3',  # Use the pip3 provider for managing Python packages
    require  => Exec['install_flask']
}
