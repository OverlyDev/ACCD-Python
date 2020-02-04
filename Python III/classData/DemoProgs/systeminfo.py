"""System-Level Information

This program covers some system-level information we did not cover in
class. specifically, you can access the account name under which the
program is running, the number of cores on the hardware, the version
of Python you are running and OS/Chip information.  The latter two
categories of information are made available as named tuples.  We didn't
cover these in class, so this is an example of how they can be used.
"""

import os, sys, platform, getpass

print('Account name:', getpass.getuser())

print()
cur_sys = platform.system()
print('OS:', cur_sys)

print('\nNumber of cores:', os.cpu_count())  # New in 3.4
if cur_sys == 'Windows':
    pass
else:
    print('Available cores -', len(os.sched_getaffinity(0)))
                                        # number of cores available to
                                        # this program. Not usable 
                                        # in Windows
print('\nPython version -', sys.version_info)  # produces a named tuple
# The following usage ignores the names.  Note the use of the * operator
# to parse the tuple into individual arguments
print('Current Python is {0}.{1}.{2}'.format(*sys.version_info))

env = platform.uname()  # produces a named tuple
print('\nPlatform', env)
# Avoid using the names in this tuple
print('{0} {2} {5}'.format(*env))
# This usage employs the names
print(env.system, env.release, env.processor)
