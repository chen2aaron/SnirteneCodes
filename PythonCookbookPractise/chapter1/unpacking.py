
# 1.1 Unpacking a Sequence into Separate Variables

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_, shares, price, _ = data

print(shares, price)


# 1.2 Unpacking Elements from Iterables of Arbitrary Length
def drop_first_last(grade):
    first, *middle, last = grade
    return sum(middle) / len(middle)

grade = (20, 30, 40, 50, 60)
print(drop_first_last(grade))


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname, fields, homedir, sh)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name, year)