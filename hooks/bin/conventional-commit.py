import re, sys

conventions = """
- chore: Changes updating grunt tasks (build system, external dependencies, external tools, ci, etc)
- docs: Documentation only changes
- feat: A new feature
- fix: A bug fix
- perf: A code change that improves performance
- refactor: A code change that neither fixes a bug nor adds a feature
- revert: One or several commits revert using the command revert
- style: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- test: Adding missing tests or correcting existing tests
- <type>!: Breaking change
"""

exemples = """
+ 479c48b test: prepared test cases for user authentication
+ a992020 chore: moved to semantic versioning
+ b818120 fix: #13
+ c6e9a97 fix: 5476
+ dfdc715 feat: 9512
+ a234556 feat!: 6729
"""

def main():
    pattern = r'(chore|docs|feat|fix|perf|refactor|revert|style|test)!?:\s.*'
    filename = sys.argv[1]
    message = open(filename, 'r').read()
    match = re.match(pattern, message)
    if match == None:
        print("\nCOMMIT FAILED!")
        print("\nPlease enter commit message in the conventional format and try to commit again.")
        print("\nConventions:")
        print(conventions)
        print("\nExamples:")
        print(exemples)
        sys.exit(1)

if __name__ == "__main__":
    main()