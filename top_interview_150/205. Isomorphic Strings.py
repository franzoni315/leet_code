def isIsomorphic(s: str, t: str) -> bool:
    print(s, t)

    d = {}
    d_inv = {}

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if s[i] not in d:
            if t[i] in d_inv:
                if d_inv[t[i]] != s[i]:
                    return False
            else:
                d_inv[t[i]] = s[i]
            d[s[i]] = t[i]
        else:
            if d[s[i]] != t[i]:
                return False

    # print()

    return True


if __name__ == '__main__':
    print(isIsomorphic('egg', 'add'))
    print(isIsomorphic('foo', 'bar'))
    print(isIsomorphic('paper', 'title'))
    print(isIsomorphic('badc', 'baba'))
