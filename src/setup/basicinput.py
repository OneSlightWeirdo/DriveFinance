RESERVED_CHARACTERS = [
    ':','"','%','*',
    '(',')','{','}',
    '[',']','@','\'',
    '#','\\','|','.','/']

YES_ALTERNATIVES = ["yes"]
NO_ALTERNATIVES = ["no"]

def yes_no_input():
    """ Prompts the user for a yes/no response

    :returns: whether the user responded yes
    :rtype: bool
    """
    code = raw_input().strip().lower()
    while (
        code != 'y' and
        code != 'n' and
        code not in YES_ALTERNATIVES + NO_ALTERNATIVES):
        print("Unrecognised input!"
            + " Please type 'y' or 'Y' for yes, 'n' or 'N' for no")
        code = raw_input().strip().lower()
    return (code == 'y' or code in YES_ALTERNATIVES)

def text_input():
    """ Prompts the user to input text excluding reserved characters

    :returns: the user's valid input
    :rtype: str
    """
    code = raw_input().strip()
    while any([character in RESERVED_CHARACTERS for character in code]):
        print("Please refrain from using any of the"
            + " following reserved characters:")
        print(RESERVED_CHARACTERS)
        code = raw_input().strip()
    return code