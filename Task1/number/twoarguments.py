def format_number(number,format_spec):
    format_spec=format(number,format_spec)
    return format_spec

number=145
format_spec='o'

format_spec=format_number(145,'o')
print(format_spec)