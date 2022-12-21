
from super_bot import initialize_bot
from build_data.db import db

# bot entry point

if __name__ == '__main__':
  db.create()
  initialize_bot()