# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Theme
ZSH_THEME="powerlevel10k/powerlevel10k"
plugins=(git zsh-autosuggestions sudo web-search copypath copyfile zsh-syntax-highlighting extract jsontools asdf auto-notify)
export PATH=$HOME/.local/bin:$HOME/.cargo/bin:$PATH

source $ZSH/oh-my-zsh.sh

# User configuration
export EDITOR='lvim'
# Keybidings
bindkey '^H' backward-kill-word
# My aliases
alias zconfig="lvim ~/.zshrc"
alias cdfiis='cd $HOME/suno/fiis-front/'
alias cdfunds='cd $HOME/suno/funds-explorer/'
alias cdint='cd $HOME/suno/integracao-apis'
alias cdtemp='cd /mnt/c/Users/julio/Desktop/temp/'
alias convertwebpall="mogrify -format webp"
alias convertjpgall="mogrify -format jpg"
alias convertpngall="mogrify -format png"
alias minifyjpg="jpegoptim"
alias minifypng="optipng"
alias startdocker="sudo service docker start"
alias stopdocker="sudo service docker stop"
alias wsl='wsl.exe'
alias explorer='explorer.exe'
alias functions='echo "searchtagactivefunds notifyme mailme mailmyipv6 s3upload"'
alias l='exa -la --icons'
alias cdut='cd /mnt/c/Users/julio/OneDrive/Documents/UTFPR'
alias unroll="PIPENV_PIPFILE=~/Tools/Unrolled/Pipfile pipenv run python ~/Tools/Unrolled/main.py"
notifyme(){
  curl -s -o /dev/null  "https://maker.ifttt.com/trigger/notifyme/with/key/dllPS2ycSCnelY2cMhI7b0?value1=$1"
}
mailme(){
  curl -s -o /dev/null  "https://maker.ifttt.com/trigger/mailme/with/key/dllPS2ycSCnelY2cMhI7b0?value1=$1"
}
mailmyipv6(){
  ipv6=$(ip -6 addr show enp4s0 | grep -m1 -oP '(?<=inet6\s)[\da-f:]+')
  mailme $ipv6
}
source ~/.fundszshrc.sh
source ~/.fiiszshrc.sh

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# export display for x server on wsl
# if grep -qi microsoft /proc/version; then
#   export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2; exit;}'):0.0
#   export LIBGL_ALWAYS_INDIRECT=1
# fi

# Start Docker daemon automatically when logging in if not running.
DOCKERISRUNNING=`ps aux | grep dockerd | grep -v grep`
if [ -z "$DOCKERISRUNNING" ]; then
    sudo dockerd > /dev/null 2>&1 &
    disown
fi

export PATH=/home/$USER/Tools/FakeStreamDeck/gcc-arm-none-eabi-10-2020-q4-major/bin:$PATH
export PICO_SDK_PATH=/home/juliohmb/Tools/rp2040_sdk/pico-sdk