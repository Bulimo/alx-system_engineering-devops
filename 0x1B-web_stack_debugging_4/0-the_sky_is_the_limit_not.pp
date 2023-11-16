# Fix Nginx "accept4() failed (24: Too many open files)" message when simulting user requests

exec {'change max open files limit':
  command => 'sed -i "s/15/10000/" /etc/default/nginx',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}

# Restart nginx service
exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
