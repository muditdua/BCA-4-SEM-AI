"""
Q9(b): First Order Predicate Logic - FORWARD CHAINING
======================================================
Forward chaining is DATA-DRIVEN: start with the known facts, repeatedly fire
every rule whose premises are all satisfied (using unification to bind
variables) and add the new conclusions to the fact base, until either the
query is derived or no new facts can be inferred (a "fixed point").

Knowledge base (classic "Colonel West" problem):
  1. American(x) ^ Weapon(y) ^ Sells(x,y,z) ^ Hostile(z)  =>  Criminal(x)
  2. Owns(Nono,x) ^ Missile(x)                            =>  Sells(West,x,Nono)
  3. Missile(x)                                           =>  Weapon(x)
  4. Enemy(x,America)                                     =>  Hostile(x)
Facts: Owns(Nono,M1), Missile(M1), American(West), Enemy(Nono,America)

Representation:
  - Literal : tuple ("Predicate", arg1, ...)
  - Variable: string starting with '?'
  - Rule    : (list_of_premises, conclusion)
"""

FACTS = {
    ("Owns", "Nono", "M1"),
    ("Missile", "M1"),
    ("American", "West"),
    ("Enemy", "Nono", "America"),
}

RULES = [
    ("R1", [("American", "?x"), ("Weapon", "?y"), ("Sells", "?x", "?y", "?z"), ("Hostile", "?z")],
     ("Criminal", "?x")),
    ("R2", [("Owns", "Nono", "?x"), ("Missile", "?x")],
     ("Sells", "West", "?x", "Nono")),
    ("R3", [("Missile", "?x")],
     ("Weapon", "?x")),
    ("R4", [("Enemy", "?x", "America")],
     ("Hostile", "?x")),
]


def is_var(t):
    return isinstance(t, str) and t.startswith("?")


def walk(t, s):
    while is_var(t) and t in s:
        t = s[t]
    return t


def unify(x, y, s):
    """Unify x and y under substitution s; return new substitution or None."""
    if s is None:
        return None
    x, y = walk(x, s), walk(y, s)
    if x == y:
        return s
    if is_var(x):
        return {**s, x: y}
    if is_var(y):
        return {**s, y: x}
    if isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):
        for a, b in zip(x, y):
            s = unify(a, b, s)
            if s is None:
                return None
        return s
    return None


def substitute(t, s):
    t = walk(t, s)
    if isinstance(t, tuple):
        return tuple(substitute(a, s) for a in t)
    return t


def fmt(lit):
    return f"{lit[0]}({', '.join(lit[1:])})"


def match_premises(premises, facts, s):
    """Yield every substitution that makes ALL premises match some fact."""
    if not premises:
        yield s
        return
    first, rest = premises[0], premises[1:]
    for fact in facts:
        s2 = unify(first, fact, s)
        if s2 is not None:
            yield from match_premises(rest, facts, s2)


def forward_chain(facts, rules, query=None):
    """Run forward chaining. Returns (final_facts, True/False for the query)."""
    facts = set(facts)
    iteration = 0
    while True:
        iteration += 1
        new_facts = set()
        print(f"\n--- Iteration {iteration} ---")
        for name, premises, conclusion in rules:
            for s in match_premises(premises, facts, {}):
                inferred = substitute(conclusion, s)
                if inferred not in facts and inferred not in new_facts:
                    new_facts.add(inferred)
                    used = [fmt(substitute(p, s)) for p in premises]
                    print(f"  {name}: {' ^ '.join(used)}  =>  {fmt(inferred)}")
        if not new_facts:
            print("  (no new facts - fixed point reached)")
            break
        facts |= new_facts
        if query is not None and query in facts:
            print(f"\n  Query {fmt(query)} has been derived!")
            return facts, True
    return facts, (query in facts if query is not None else None)


if __name__ == "__main__":
    print("=== Forward Chaining in First Order Logic ===")
    print("Initial facts:")
    for f in sorted(FACTS):
        print("  ", fmt(f))

    query = ("Criminal", "West")
    final_facts, proved = forward_chain(FACTS, RULES, query)

    print("\nAll facts in the knowledge base after inference:")
    for f in sorted(final_facts):
        print("  ", fmt(f))
    print(f"\nIs {fmt(query)} entailed by the KB?  {proved}")
