# Increases the amount of traffic an Nginx server can handle

# Increase the ULIMIT of the file
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
} ->

# Restart Nginx
service { 'nginx-restart':
  name    => 'nginx',
  ensure  => 'running',
  enable  => true,
  require => Exec['fix--for-nginx'],
}
