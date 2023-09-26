# install nginix

exec { 'install_nginx':
    command => '/usr/bin/apt-get update && /usr/bin/apt-get -y install nginx',
    creates => '/usr/sbin/nginx',
    # ensure   => 'installed',
}
# Ensure the 'nginx' service is enabled and running
service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => Exec['install_nginx'],
}

package { 'nginx':
    require  => Exec['install_nginx'],
}


file { '/var/www/html/index.html' :
    ensure  => 'file',
    content => 'Hello World!',
    require => Package['nginx'],
}

file { 'error_404':
    ensure  => 'file',
    content => "Ceci n'est pas une page",
    path    => '/var/www/html/404.html',
    require => Package['nginx'],
}

file_line { 'redirect_me' :
    ensure  => present,
    path    => '/etc/nginx/sites-enabled/default',
    line    => '        location /redirect_me {',
    replace => false,
    match   => 'server_name _;',
    require => Package['nginx'],
}

file_line { 'redirect_me_redirect':
    ensure  => present,
    path    => '/etc/nginx/sites-available/default',
    line    => '                 return 301 https://www.youtube.com;',
    replace => false,
    match   => 'location /redirect_me {',
    require => File_line['redirect_me'],
}

file_line { 'error_page' :
    ensure  => present,
    path    => '/etc/nginx/sites-enabled/default',
    line    => '       error_page 404 /404.html;',
    replace => false,
    match   => '^\s*location / \{',
    require => Package['nginx'],
}
