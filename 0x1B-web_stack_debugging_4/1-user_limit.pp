# Change the OS configuration so that it is possible to login with the holberton user and open a file.
exec {'set hard nofile':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 1000/" /etc/security/limits.conf',
}

exec {'set soft nofile':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 1000/" /etc/security/limits.conf',
}
