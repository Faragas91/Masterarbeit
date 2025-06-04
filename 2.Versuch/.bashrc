
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/c2210542009/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/c2210542009/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/c2210542009/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/c2210542009/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

export PATH=$PATH:/home/c2210542009/Masterarbeit/tools/ncbi-blast-2.16.0+/bin
export PATH=$PATH:/home/c2210542009/Masterarbeit/ViennaRNA/bin