#!./pash.py

# Regular python
print("Python")
numbers = {1: 'one', 2: 'two'}

# Regular shell commands
!echo "Shell"
# Capture the output
now = ! date +%s
# Command in brackets. Print result
print(! date +%s)

multiline = (!
    echo A B
    -a (parentheses)
    -o ! is ignored
)

# Interpolation of commands
for key, value in numbers.items():
    !echo {key}={value}

!echo {"Any python expression, ignore in quotes".upper()}

# Environment variable in shell. Raises an error if missing.
! echo $HOME/somewhere
# Environment variable in Python. Returns None if missing.
$missing_variable is None
! echo a_{$variable or "default value"} b_c
! find . -exec cat {} +

# Same applies to program arguments
if $1:
    !echo "First argument: $1"
    for arg in $*:
        print(arg)


# Output conversion
file_list = l! ls -1

simple_string = 'Output: ' + ! echo some output
from_json = j! echo [1, 2]
to_integer = 2 + (i! echo 2) + 2
list_of_lines = l! ls
rows_then_columns = c! ls -l
fields_then_rows = r! ls -l

# Print stdout and stderr
! cmd
# Capture stdout, print stderr
out = ! cmd
# Capture stderr, print stdout
err = e! cmd
# Capture both
out, err = oe! cmd
# Include the return code
out, err, ret = oer! cmd