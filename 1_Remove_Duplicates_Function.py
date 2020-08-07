"""
Automation is a huuuuge part of Python’s playbook and an equally big part of why programmers love the language so much. When it comes to programming and web development (or data science or machine learning or any of the other fields Python is used for), being able to automate processes that would otherwise take forever to complete by hand is CRUCIAL.
"""

"""
 for removing duplicates from lists, is a low-key-yet-totally-on-point Python script example of how powerful Python’s automating functions can be.
 """

#Try to remove the duplicates elements in the list

def remove_duplicates(list):
    result = []
    if list:
        for i in  list:
            if i not in result:
                result.append(i)
    return result

if __name__ == '__main__':
    list = [1,2,3,3,'apple','huawei','fortinet','fortinet']
    new_list = remove_duplicates(list)
    print(new_list)