#!/usr/bin/env python
# for gunicorn
import sys
sys.path.insert(0, '/code/')

from redFile import app

if __name__ == "__main__":
    app.run()
