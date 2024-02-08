# Code courtesy of Anyks

def get_settings(settings: dict = {}) -> dict:
    """
    Mutate dict passed in argument (defaults to singleton `{}`) to hold settings defined in `options.txt`.
    A new dict may be given as argument to receive settings unique to a scope, avoiding to modify or to be modified by other part of the program.
    """
    if len(settings) != 0:
        return settings # settings shouldn't be changed from file at runtime
    version = "0.0.0"
    default = f'version:"{version}"\ndefault_max_energy:4\ndefault_energy_per_turn:3\nhand_size:5\ndeck_size:30\nprogressbar_sytle:1\nstrong_percent_increase:20\npassive_heal:10\npassive_commander_heal:20\ndev_mode:true'
    if "options.txt" not in os.listdir(cwd_path):
        with open(os.path.join(cwd_path, "options.txt"), "x") as io:
            # feel free to add new default options if needed
            content = default
            io.write(content)
            io.close()
    else: # no need to read what was just written
        with open(os.path.join(cwd_path, "options.txt"), "r") as io:
            content = io.read()
            io.close()
    for line in content.split("\n"): # possible bugs on windows due to \r\n but should work with str.strip
        line = line.strip()
        # Ideally there shouldn't be empty lines, but it's better to check anyway
        if len(line) == 0:
            continue
        key, value, *_ = line.split(":") # please don't put two semicolons in a line though
        value = value.strip()
        if len(value) == 0:
            # I'd rather not immport the whole conveniance module just for a warn,
            # but anyway I think we can assume nobody will leave a key unasigned in options.txt,
            # you've been warned here so don't complain if you do 👀
            continue
        # would unecessary pollute the namespace if defined outside
        def isfloat(arg: str):
            for c in arg:
                if not (c.isdigit() or c == '.'):
                    return False
            return True
        if value[0] == value[-1] == '"':
            value = value[1:-1] # no strip after as spaces may be intentional
        elif value == "true":
            value = True
        elif value == "false":
            value = False
        elif value.isdigit():
            # Note: doesn't support negative numbers (should be fixed)
            value = int(value)
        elif isfloat(value):
            value = float(value)
        # technically valid string option even without "", they are only needed for numeric values (e.g. "1", "true")
        settings[key.strip()] = value # value is already stripped/parsed
    if "version" not in settings or ltsemver(settings["version"], version):
        # relevant even to non-dev users, so a print is fine.
        print("Detected outdated options, updating to new defaults. \033[1;31mNote\033[0m: this overrides all previous options.")
        with open(os.path.join(cwd_path, "options.txt"), "w") as io:
            io.write(default)
            io.close()
        settings.clear() # I admit this is really spaghetti and another solution should be done.
        # Nonetheless it shouldn't break anything
        return get_settings(settings)
    return settings