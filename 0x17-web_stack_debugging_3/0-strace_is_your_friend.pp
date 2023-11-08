# Change the extension error in wp_locale_require setting in wp-settings.php file
exec { 'fix config typo':
  command => "sed -i.bak 's/.phpp/.php/' /var/www/html/wp-settings.php",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  creates => '/var/www/html/wp-settings.php.bak',
  onlyif  => "grep -q '.phpp' /var/www/html/wp-settings.php",
}
