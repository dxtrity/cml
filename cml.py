

# Init Constants
body = False
header = False
div = False

# Find the content
def find_this(file):
    with open(file, "r") as f:
        global body
        global header
        global div

        found_body = f.read().find("body")
        found_header = f.read().find("header")
        found_div = f.read().find("div")

        if found_body != -1:
            body = True

        if found_header != -1:
            header = True

        if found_div != -1:
            div = True

# Find new lines
def test_for_space(file_path):
    with open(file_path, "w") as f:
        file = f.read()
        if "\n" in file:
            find_space = f.read().find("\n")
            return find_space
        else:
            return "Invalid Operation"

# Make the file
def make(file):
    pass

# Adding content
def add_body(file_path):
    with open(file_path, "w") as f:
        f.write("<body>\n\n</body>")

def add_header(file_path):
    pass
    
def add_div(file_path):
    with open(file_path, "w") as f:
        var = f.read()

test = add_header("test.cml")
print(test)