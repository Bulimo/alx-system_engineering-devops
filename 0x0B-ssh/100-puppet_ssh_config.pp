# Puppet manifest to make changes to our configuration file.

file_line { 'pass_auth':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
    match  => '^PasswordAuthentication',  # Specify a regular expression to match the line
}

file_line { 'id_file':
    ensure => present,
    path   => '/etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/school',
    match  => '^IdentityFile',  # Specify a regular expression to match the line
}

file { '/etc/ssh/ssh_config':
    ensure => present,
}
