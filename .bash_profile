#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

if [ "$(tty)" = "/dev/tty1" ]
then
    Hyprland
    exit
fi
