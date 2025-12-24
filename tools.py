import hashlib
from langchain.tools import Tool

# MILESTONE 1
# TOOL 1: GREETING
def greet(name: str):
    return f"Hello {name}, I am your Security Advisor Agent!"

greet_tool = Tool(
    name="GreetingTool",
    func=greet,
    description="Use this to greet a person by name. Input should be the name."
)

# MILESTONE 2
# TOOL 2: PASSWORD CHECKER
def check_password_strength(password: str):
    if len(password) < 8:
        return "Weak: Password is too short."
    else:
        has_digit = any(char.isdigit() for char in password)
        has_uppercase = any(char.isupper() for char in password)
        has_lowercase = any(char.islower() for char in password)
        has_specialchar = any(not char.isalnum() for char in password)
        
        if has_digit and has_uppercase and has_lowercase and has_specialchar:
            return "Strong: Password meets all criteria."
        else:
            return "Weak: Missing required character types."

password_tool = Tool(
    name="PasswordStrengthChecker",
    func=check_password_strength,
    description="Use this tool to check if a password is strong or weak. Input should be the password string you want to test."
)

# TOOL 3: HASHER
def generate_hash(text: str):
    try:
        hash_object = hashlib.sha256(text.encode())   # .encode() turns text into bytes
        hash_string = hash_object.hexdigest()         # .hexdigest() turns it back to a readable string
        return f"The SHA-256 hash for '{text}' is: {hash_string}"
    except Exception as e:
        return f"Error generating hash: {str(e)}"

hasher_tool = Tool(
    name="IntegrityHasher",
    func=generate_hash,
    description="Use this to verify the integrity of a message or file name. Input should be the text you want to hash."
)

security_tools = [greet_tool, password_tool, hasher_tool]