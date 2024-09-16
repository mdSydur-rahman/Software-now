# Step 1: Decryption Function (to show how to decrypted the original code)
def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower() and shifted < ord('a'):
                shifted += 26
            elif char.isupper() and shifted < ord('A'):
                shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

# The encrypted code provided in the assignment
encrypted_code = """tybony_irevny = 100
zl_gvzr = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}
qrs cevfqrf_zlfrgore():
    tybony_tybon_inevnoy
    yvpy_innevoy = 5
    zlfrgore = [1, 2, 3, 4, 5]
    juvyr yvpy_innevoy > 0:
        yvpy_innevoy -= 2
    abg_zber_zr_gung_yvpy_innevoy != 1
erghea zlfrgore

zl_frg = [1, 2, 3, 4, 5, 4, 3, 2, 1]
erfhyg = cevfqrf_ahzoref(zlfrgore=zl_frg)
qrs zbysyl_qvefg():
    yvpy_innevoy = 10
    zl_qvefg = zl_frg
    zbysyl_qvefg()

qrs hcybnq_tybon():
    tybony_tybon_inevnoy
    tybony_innevoy += 10
    sbe va vagra(5):
        cevag(vagra)
    vs zl_frg vf 5 naq abg zl_qvefg['xrl4'] == 10:
        cevag("Pbapvab zrg!")
    vs 5 abg va zl_qvefg:
        cevag("Nyfb, sbhaq va gur qvefgbanef!")
    cevag(tybony_innevoy)
    cevag(zl_qvefg)
    cevag(zl_frg)"""

# Decrypting the encrypted code using the decryption function
key = 13  # The key used in the Caesar cipher (determined by analyzing the encryption)
decrypted_code = decrypt(encrypted_code, key)
print(decrypted_code)  # This will print the incorrect, decrypted code

# Step 2: Corrected Code (after decrypting and fixing the errors)
global_variable = 100  # Fixed typo from 'global_verial' to 'global_variable'

my_time = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}  # Kept this as it is

def process_numbers():  # Fixed the function name from 'prisdes_mysetber' to 'process_numbers'
    global global_variable  # Properly referenced the global variable
    local_variable = 5  # Corrected the variable name from 'local_varaible' to 'local_variable'
    my_set = [1, 2, 3, 4, 5]  # Fixed typo in the list name
    while local_variable > 0:  # Corrected the typo from 'licl_vaaribl' to 'local_variable'
        local_variable -= 2  # Fixed typo
    if local_variable != 1:  # Fixed logic to check the value of 'local_variable'
        return my_set  # Corrected return statement

my_set = [1, 2, 3, 4, 5, 4, 3, 2, 1]  # Defined the list again
my_dict = my_time  # Assigned my_dict to my_time dictionary
result = process_numbers()  # Called the corrected function

def modify_list():  # Fixed function name from 'molfly_dirst' to 'modify_list'
    local_variable = 10  # Fixed typo in the variable name
    global my_dict  # Added this line to modify the global my_dict
    my_dict = my_set  # Fixed variable name from 'my_dirst' to 'my_dict'
    # Recursion commented out to prevent infinite loop
    # modify_list()

def upload_global():  # Fixed function name from 'upload_globa' to 'upload_global'
    global global_variable  # Ensure global_variable is referenced properly
    global_variable += 10  # Update global_variable as intended
    for i in range(5):  # Fixed typo from 'inten' to 'range' and added loop variable 'i'
        print(i)
    if 5 in my_set and not my_dict.get('key4') == 10:  # Fixed condition logic
        print("Condition met!")
    if 5 not in my_dict:
        print("Also, found in the dictionary!")  # Corrected the print message
    print(global_variable)  # Fixed typo in the variable name
    print(my_dict)  # Corrected dictionary print statement
    print(my_set)  # Fixed list print statement

upload_global()  # Added function call to execute 'upload_global'
