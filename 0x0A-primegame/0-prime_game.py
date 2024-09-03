#!/usr/bin/python3


def isWinner(x, nums):
    """
    Determines the winner of multiple rounds of a game played by Maria and Ben.

    Parameters:
    x (int): The number of rounds.
    nums (list): An array of integers where each integer represents the
    upper limit of the set of consecutive integers for that round.
    Returns:
    str: The name of the player who won the most rounds ("Maria" or "Ben").
         If the winner cannot be determined, returns None.
    """
    if x <= 0 or not nums:
        return None

    def sieve_of_eratosthenes(n):
        """
        Generates a list of prime counts up to each number from 0 to n
        using the Sieve of Eratosthenes algorithm.
        Parameters:
        n (int): The upper limit for generating primes.
        Returns:
        list: A list where the index represents the number and the value at
        index represents the count of prime numbers from 2 to that number.
        """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        prime_count = [0] * (n + 1)
        for p in range(2, n + 1):
            prime_count[p] = prime_count[p-1] + (1 if is_prime[p] else 0)
        return prime_count
    max_n = max(nums)
    prime_count = sieve_of_eratosthenes(max_n)
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
