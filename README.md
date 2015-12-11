[![Build Status](https://travis-ci.org/gauntlt/gauntlt-demo.svg?branch=master)](https://travis-ci.org/gauntlt/gauntlt-demo)

# Gauntlt Demo
This is a demo set of attacks that can be used to demo gauntlt and learn how to implement it. Each directory in `./examples` contains a specific type of attack that you might want to run.  Inside each example you will find a README.md which will have a challenge and some hints on how to solve it.  We recommend reading that first and then try to create an attack to solve the challenge.

## Installation
```
$ git clone https://github.com/secure-pipeline/gauntlt-demo
$ cd ./gauntlt-demo
$ git submodule update --init --recursive
$ bundle
```

## Start targets
This includes gruyere and railsgoat as a target to pratice against and in the future we will bundle other services.  To start the default targets run the following.
```
$ bundle exec start_services

# For some reason railsgoat doesnt exit cleanly from a Ctl-C with service manager so you 
# will have to stop it manually
# ps -ef | grep rails
# kill -9 <PID>
# Please send a pull request if you know how to fix this
```

You can also run the following to start individual targets which include: railsgoat and gruyere
```
$ bundle exec start_services config/railsgoat.rb
$ bundle exec start_services config/gruyere.rb
```
After you stop the service, you may have to kill the process manually.  

For railsgoat, you can also just do the following:
```
$ cd vendor/railsgoat
$ bundle install --binstubs
$ rake db:setup
$ rake server:start
```

## Run a Gauntlt attack
Once you have a target ready, you can start customizing attacks and testing them against the target.
```
$ cd ./examples
$ bundle exec gauntlt hello_world/hello_world.attack
```

## Work through the examples
You might find it helpful to head over to `./examples` and work through the examples.  After running `hello_world` it might be good to start with `port_check` 

