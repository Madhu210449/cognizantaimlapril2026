import sys
import os

#add project root to python path

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..','..')
)
sys.path.insert(0, project_root)

from conf.logger_conf import setup_logger
"""
entry point for healthcare application . this module will initialize the application and start the main loop
"""

logger = setup_logger()

def run():
    """
    test logger
    """
    logger.info("Starting healthcare application")
    
""" handle entry point for healthcare application """

if __name__ == "__main__":
    run()