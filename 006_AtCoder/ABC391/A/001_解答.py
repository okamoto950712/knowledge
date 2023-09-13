DATA = """tourist 3858
ksun48 3679
Benq 3658
Um_nik 3648
apiad 3638
Stonefeang 3630
ecnerwala 3613
mnbvmar 3555
newbiedmy 3516
semiexp 3481
"""

username_to_rating = {
    name: rating for name, rating in map(lambda s: s.split(), DATA.splitlines())
}
print(username_to_rating[input()])
