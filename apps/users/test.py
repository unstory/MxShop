def test():
    try:
        return 1
    finally:
        return 2
result = test()
print(result)
