#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

if [[ "$(tty)" = "/dev/tty1" ]]; then
	pgrep qtile || startx
fi
alias anime='cd github/ani-cli/ && ./ani-cli'
alias sp='ncspot'
alias yt='ytfzf -t'
alias ..='cd ..'
alias ls='ls --color=auto'
alias pm='pulsemixer'
alias neofetch='neofetch --source .icons/ascii-art.txtl'
alias rn='ranger'
alias matrix='unimatrix -c blue'
S1='[\u@\h \W]\$ '


### PATH

if [ -d "$HOME/.local/bin" ] ;
	  then PATH="$HOME/.local/bin:$PATH"
fi


