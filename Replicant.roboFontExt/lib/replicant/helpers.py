from vanilla.dialogs import askYesNo

def createArchiveYesNo():
    return askYesNo("No archive folder exists", "A new folder named _archive will be created for the saved file. Continue?")