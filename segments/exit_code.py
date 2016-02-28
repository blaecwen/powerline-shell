
error_symbol = u"\u2718"

def add_exit_code_segment(powerline):
    if powerline.args.prev_error == 0:
        return
    fg = Color.CMD_FAILED_FG
    bg = Color.CMD_FAILED_BG
    powerline.append(' %s %s ' % (error_symbol, str(powerline.args.prev_error)), fg, bg)
