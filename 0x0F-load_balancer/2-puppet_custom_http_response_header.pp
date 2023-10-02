# Install Nginx and configure custom header

# Install Nginx
exec { 'install_nginx':
    command => '/usr/bin/apt-get update && /usr/bin/apt-get -y install nginx',
    creates => '/usr/sbin/nginx',
}

package { 'nginx':
    require  => Exec['install_nginx'],
}

# Ensure the 'nginx' service is enabled and running
service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => Exec['install_nginx'],
}

# root message hello world
file { '/var/www/html/index.html' :
    ensure  => 'file',
    content => 'Hello World!',
    require => Package['nginx'],
}

# Configure custom header in Nginx site configuration
file_line { 'custom_header':
    ensure  => present,
    path    => '/etc/nginx/sites-available/default',
    line    => "        add_header X-Served-By ${hostname};",
    after   => 'server_name _;',
    require => Package['nginx'],
}

# Restart Nginx after updating the site configuration
exec { 'restart_nginx':
    command => '/usr/sbin/service nginx restart',
    require => File_line['custom_header'],
}
