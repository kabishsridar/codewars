"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
"""
def validate_pin(pin):
    status = True
    length = True
    if pin.isdigit():
        staus = True
    else:
        status = False

    if len(str(pin)) == 4 or len(str(pin)) == 6:
        length = True
    else:
        length = False
    print(length and status)
validate_pin("1234")
