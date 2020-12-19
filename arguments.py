def is_cli_only(options):
    for option in options:
        if '--cli=' in option or '-c=' in option:
            optArr = option.split('=')
            value = optArr[1]
            if isinstance(value, int):
                return int(value)

    return 1


def rotate_image(options):
    for option in options:
        if '--rotate=' in option or '-r=' in option:
            optArr = option.split('=')
            value = optArr[1]
            if isinstance(value, int):
                return int(value)

    return 1
