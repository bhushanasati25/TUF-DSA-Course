# Check if Two Strings are Isomorphic

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    s_map, t_map = {}, {}
    for cs, ct in zip(s, t):
        if cs in s_map and s_map[cs] != ct:
            return False
        if ct in t_map and t_map[ct] != cs:
            return False
        s_map[cs] = ct
        t_map[ct] = cs
    return True


if __name__ == "__main__":
    print(is_isomorphic("egg", "add"))    # True
    print(is_isomorphic("foo", "bar"))    # False
