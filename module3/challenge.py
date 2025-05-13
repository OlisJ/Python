olti=[
    gpa:=3.5,
    ts:=70
]
usame=[
    gpa:=3.5,
    ts:=55
]
leart=[
    gpa:=3.5,
    ts:=40
]
olis=[
    gpa:=2.5,
    ts:=40
]


if usame[gpa>3.5 and ts>65]:
    print("full")
elif usame[gpa>3.5 and ts>50<65]:
    print('partial')
elif usame[gpa>3.5 and ts<50]:
    print('not')
elif usame[gpa<3.5 ]:
    print('not')
else:
    print('not complete')

