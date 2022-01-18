# User .bash_profile  Should live at ~/.bash_profile

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi
## Set ENV stuff
# If you ever want to do "admin commands", adding these can be useful
#export PATH=$PATH:/sbin:/usr/sbin
export PAGER=more
export EDITOR=vi
#export EDITOR=emacs
export RSYNC_RSH=rsh
## IceCube specific

## CVMFS setup.
if [ -f /cvmfs/icecube.opensciencegrid.org/py3-v4.1.1/setup.sh ]; then
	echo "Cvmfs setup..."
	eval `/cvmfs/icecube.opensciencegrid.org/py3-v4.1.1/setup.sh`
else
	echo "No cvmfs"
fi

# Lastly, make sure our local shell customizations are set
source ~/.bashrc
