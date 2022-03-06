#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

if [[ "$(tty)" = "/dev/tty1" ]]; then
	pgrep qtile || startx
fi
alias an='ani-cli'
alias sp='ncspot'
alias ..='cd ..'
alias ls='ls --color=auto'
alias pm='pulsemixer'
alias rn='ranger'
alias qtile='vim .dotfiles/.config/qtile/config.py'
alias airpods='bluetoothctl connect 74:9E:AF:E7:E1:00'
alias o='xdg-open'
alias yt='ytfzf'
alias subs='ytfzf -cSI --sort'
S1='[\u@\h \W]\$ '


### PATH

if [ -d "$HOME/.local/bin" ] ;
	  then PATH="$HOME/.local/bin:$PATH"
fi


