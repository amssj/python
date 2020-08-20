def is_center(x):
    return int(x.lower().find('center') > 1)

list = [1,2,3,4,5]

df[’hood’] = ["center", "west", "center", "east"]
.map(is_center)

["center", "west", "center", "east"]
    ->
[1, 0, 1, 0]
