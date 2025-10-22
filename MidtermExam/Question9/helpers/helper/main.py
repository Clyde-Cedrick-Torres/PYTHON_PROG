from helpers import string_utils as su          # alias avoids long dotted paths
from helpers.math_utils import area            # import a single function

def main() -> None:
    print(su.shout("hello"))
    print(area(3, 4))

if __name__ == "__main__":
    main()