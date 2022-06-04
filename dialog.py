#!/usr/bin/env python
from subprocess import Popen, PIPE

proc = Popen(['zenity', '--password'], stdout=PIPE, universal_newlines=True)
sudo_password, errs = proc.communicate(timeout=150)

config_proc = Popen("""zenity --list --title="MiniDspConfig"
  --column=Config --column=#Subs
  Music 1
  Movie 2""".split(), stdout=PIPE, universal_newlines=True)

config, errs = config_proc.communicate(timeout=150)
# print(sudo_password, config)

if config.strip() == 'Music':
    cc = "1"
else:
    cc = "0"

print(cc)

command = '/home/seydanator/Documents/Projects/minidsp-UI/minidsp config'.split()

p = Popen(['sudo', '-S'] + command + [cc], stdin=PIPE, stderr=PIPE, universal_newlines=True)

sudo_prompt = p.communicate(sudo_password.strip() + '\n')[1]
print(sudo_prompt)

