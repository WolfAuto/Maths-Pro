import subprocess
import sys

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", "--user", package])
install("bcrypt")
install("yagmail")
install("validate_email")
install("pandas")
install("sqlalchemy")
