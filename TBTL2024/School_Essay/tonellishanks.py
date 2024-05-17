import random


def power_modulo(a: int, b: int, n: int) -> int:
    """ Computes a ^ b mod n """
    result = 1
    while b != 0:
        if b % 2 == 1:
            # b odd
            result = (result * a) % n
        a = (a * a) % n
        b >>= 1
    return result


def extended_gcd(a: int, b: int) -> (int, int, int):
    # optional check
    if a == 0:
        return b, 0, 1

    # without this check the first iteration will divide by zero
    if b == 0:
        return a, 1, 0

    un_prev = 1
    vn_prev = 0
    un_cur = 0
    vn_cur = 1

    while True:
        qn = a // b
        new_r = a % b
        a = b
        b = new_r

        if b == 0:
            return a, un_cur, vn_cur

        # Update coefficients
        un_new = un_prev - qn * un_cur
        vn_new = vn_prev - qn * vn_cur

        # Shift coefficients
        un_prev = un_cur
        vn_prev = vn_cur
        un_cur = un_new
        vn_cur = vn_new


def inverse_modulo(a: int, n: int) -> int:
    _, b, _ = extended_gcd(a, n)
    return b % n


def legendre_symbol(a: int, p: int, /) -> int:
    return power_modulo(a, (p - 1) >> 1, p)


def _choose_b(p: int, /) -> int:
    b = 2
    while legendre_symbol(b, p) == 1:
        b = random.randrange(2, p)
    return b


def _tonelli_shanks_recursive(a: int, k: int, p: int, b: int, b_inverse: int, /):
    """
    Computes a square root of a modulo prime p
    :param a: the number to take the square root of
    :param k: positive integer, such that a^m = 1 (mod p) where m = (p-1)/(2^k)
    :param p: odd prime p modulo which we are working
    :param b: an arbitrary non-square modulo p
    :param b_inverse: the inverse of b modulo p, i.e., b * b_inverse = 1 (mod p)
    :return: one of the square roots of a modulo p (the other can be obtained via negation modulo p)
    """

    m = (p - 1) >> k
    a_m = 1

    while m % 2 == 0 and a_m == 1:
        m >>= 1
        k += 1
        a_m = power_modulo(a, m, p)

    if a_m == p - 1:
        # a^m = -1 (mod p)
        b_power = 1 << (k - 1)
        b_power_half = 1 << (k - 2)
        a_next = (a * power_modulo(b, b_power, p)) % p
        a_next_root = _tonelli_shanks_recursive(a_next, k, p, b, b_inverse)
        a_root = a_next_root * power_modulo(b_inverse, b_power_half, p)
        return a_root % p

    # we now handle the case when m is odd
    # this case is easy, a^((m+1)/2) is a square root of a
    return power_modulo(a, (m + 1) >> 1, p)


def tonelli_shanks(a: int, p: int, /) -> int | None:
    """
    Computes a square root of a modulo prime p
    :param a: the number to take the square root of
    :param p: odd prime p modulo which we are working
    :return: one of the square roots of a modulo p (the other can be obtained via negation modulo p)
    """

    if legendre_symbol(a, p) != 1:
        # a is not not a square modulo p
        return None

    b = _choose_b(p)
    b_inverse = inverse_modulo(b, p)
    return _tonelli_shanks_recursive(a, 1, p, b, b_inverse)
