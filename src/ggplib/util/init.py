import ggplib.util.log

_setup_once = False

def setup_once(log_name_base="test"):
    from ggplib import interface

    global _setup_once
    if not _setup_once:
        interface.initialise_k273(1, log_name_base=log_name_base)
        ggplib.util.log.initialise()
