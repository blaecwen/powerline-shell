
def add_username_segment(powerline):
    import os
    if powerline.args.shell == 'bash':
        user_prompt = ' \\u '
    elif powerline.args.shell == 'zsh':
        user_prompt = ' %n '
    else:
        user_prompt = ' %s ' % os.getenv('USER')

    if os.getenv('USER') == 'root':
        bgcolor = Color.USERNAME_ROOT_BG
        fgcolor = Color.USERNAME_ROOT_FG
        user_prompt = u' \u26A1' + user_prompt
    else:
        bgcolor = Color.USERNAME_BG
        fgcolor = Color.USERNAME_FG

    powerline.append(user_prompt, fgcolor, bgcolor)
