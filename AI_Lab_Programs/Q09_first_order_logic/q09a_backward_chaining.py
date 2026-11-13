facts = [("Owns","Nono","M1"), ("Missile","M1"), ("American","West"), ("Enemy","Nono","America")]
rules = [([("American","?x"), ("Weapon","?y"), ("Sells","?x","?y","?z"), ("Hostile","?z")], ("Criminal","?x")),
         ([("Owns","Nono","?x"), ("Missile","?x")], ("Sells","West","?x","Nono")),
         ([("Missile","?x")], ("Weapon","?x")),
         ([("Enemy","?x","America")], ("Hostile","?x"))]
show = lambda l: l[0] + "(" + ",".join(l[1:]) + ")"
def w(x, s):
    while x in s: x = s[x]
    return x
def sub(l, s): return tuple(w(x, s) for x in l)
def unify(a, b, s):
    if len(a) != len(b) or a[0] != b[0]: return None
    s = dict(s)
    for x, y in zip(a[1:], b[1:]):
        x, y = w(x, s), w(y, s)
        if x != y:
            if x[0] == "?": s[x] = y
            elif y[0] == "?": s[y] = x
            else: return None
    return s
def match(p, kb, s):
    if not p: yield s
    else:
        for f in kb:
            s2 = unify(p[0], f, s)
            if s2 is not None: yield from match(p[1:], kb, s2)
def forward(q):
    kb = set(facts)
    while q not in kb:
        new = {sub(c, s) for p, c in rules for s in match(p, kb, {})} - kb
        if not new: return False
        for c in new: print("  inferred", show(c))
        kb |= new
    return True
def backward(goals, s, d=0):
    if not goals: yield s; return
    g = sub(goals[0], s)
    print("  goal", show(g))
    r = lambda l: tuple(x + str(d) if x[0] == "?" else x for x in l)
    for f in facts:
        s2 = unify(g, f, s)
        if s2 is not None: yield from backward(goals[1:], s2, d + 1)
    for p, c in rules:
        s2 = unify(g, r(c), s)
        if s2 is not None: yield from backward([r(x) for x in p] + goals[1:], s2, d + 1)
print("Forward Chaining")
print("Criminal(West) proved:", forward(("Criminal", "West")))
print("\nBackward Chaining")
print("Criminal(West) proved:", next(backward([("Criminal", "West")], {}), None) is not None)