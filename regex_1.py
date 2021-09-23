import re
email_pattern = r'\w+.\w+@\w+[.]\w+'
phone_pattern = r'\d{10}'
text = 'priyanshu shukla priyanshu.shukla@gmail.com 8004954515'
email_pattern_compile = re.compile(email_pattern)
phone_pattern_compile = re.compile(phone_pattern)
email_result  = email_pattern_compile.search(text).group()
phone_result = phone_pattern_compile.search(text).group()
def get_result():
    return {
        'email':email_result,
        'contact_number':phone_result
    }


if __name__ == '__main__':
    print(get_result())
    