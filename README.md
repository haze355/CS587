# CS587 DATABASE IMPLEMENTATION

Author: Yiming Zhang

## Wisconsin Benchmark Project
## Part One

https://docs.google.com/document/d/1Y-IaA0u18_pY6Z6-gTqP0pJ_Ean5tONhxcf9gzUtK_8/edit?usp=sharing

Here is the schema used in table onekup in database:

```SQL
CREATE TABLE ONEKUP
(
  unique1         integer NOT NULL,             # unique, random order
  unique2         integer NOT NULL PRIMARY KEY, # unique, sequential
  two             integer NOT NULL,             # unique1 mod 2
  four            integer NOT NULL,             # unique1 mod 4
  ten             integer NOT NULL,             # Cunique1 mod 10
  twenty          integer NOT NULL,             # unique1 mod 20
  onePercent      integer NOT NULL,             # unique1 mod 100
  tenPercent      integer NOT NULL,             # unique1 mod 10
  twentyPercent   integer NOT NULL,             # unique1 mod 5
  fiftyPercent    integer NOT NULL,             # unique1 mod 2
  unique3         integer NOT NULL,             # unique1 mod unique
  evenOnePercent  integer NOT NULL,             # onePercent * 2
  oddOnePercent   integer NOT NULL,             # onePercent * 2 + 1
  stringu1        char(52) NOT NULL,            # candidate key
  stringu2        char(52) NOT NULL,            # candidate key
  string4         char(52) NOT NULL,            # cyclic
)
```

## Part Two

https://docs.google.com/document/d/1YivibuX53ho1tcY-2r9xcyhjEjU5wIRdrySL9f9xVdI/edit?usp=sharing

```SQL
50% selectivity:
UPDATE onehundredkup1
SET two = 1
WHERE four = 0 or four = 1

75% selectivity:
UPDATE onehundredkup1
SET two=1
WHERE four <= 2

100% selectivity:
UPDATE onehundredkup1
SET two=1
WHERE four >= 0

Bulk update using index
UPDATE onehundredkup1
SET unique1 = unique2

```

