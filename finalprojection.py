a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
k=0
count='x'
winner="none"
while k==0:
    if a==b and b==c and c==1:
        k=1
        winner='x'
    if a==b and b==c and c==2:
        k=1
        winner='o'
    if d==e and e==f and f==1:
        k=1
        winner='x'
    if d==e and e==f and f==2:
        k=1
        winner='o'
    if g==h and h==i and f==1:
        k=1
        winner='x'
    if g==h and h==i and f==2:
        k=1
        winner='o'
    if a==d and d==g and g==1:
        k=1
        winner='x'
    if a==d and d==g and g==2:
        k=1
        winner='o'
    if b==e and e==h and h==1:
        k=1
        winner='x'
    if b==e and e==h and h==2:
        k=1
        winner='o'
    if c==f and f==i and i==1:
        k=1
        winner='x'
    if c==f and f==i and i==2:
        k=1
        winner='o'
    if winner=="none":
        if count=='x':
            choice=input("x's turn, where ya choose")
            if choice=='a' and a==0:
                a=1
            if choice=='b' and b==0:
                b=1
            if choice=='c' and c==0:
                c=1
            if choice=='d' and d==0:
                d=1
            if choice=='e' and e==0:
                e=1
            if choice=='f' and f==0:
                f=1
            if choice=='g' and g==0:
                g=1
            if choice=='h' and h==0:
                h=1
            if choice=='i' and i==0:
                i=1
        if count=='o':
            choice=input("o's turn, where ya choose")
            if choice=='a' and a==0:
                a=2
            if choice=='b' and b==0:
                b=2
            if choice=='c' and c==0:
                c=2
            if choice=='d' and d==0:
                d=2
            if choice=='e' and e==0:
                e=2
            if choice=='f' and f==0:
                f=2
            if choice=='g' and g==0:
                g=2
            if choice=='h' and h==0:
                h=2
            if choice=='i' and i==0:
                i=2
    if count=='x':
        count='o'
    if count=='o':
        count='x'
            