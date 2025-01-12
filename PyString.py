# used by tkinter
import tkinter as tk
from tkinter import ttk

# used by ps executer
from timeit import default_timer as timer
import random
import math

# importing with tkinter
from pathlib import Path
from tkinter import filedialog

# message
import tkinter.messagebox as tkmb
from tkinter import messagebox

# needed to open directory
import os
from tkinter import filedialog
from tkinter import *
from pathlib import Path

# scrollbar
from tkinter import filedialog, Scrollbar

# identifying file extension
import imghdr

# image size
# from PIL import Image

# font sizes for buttons
from tkinter import font

#text width --> entrx pixel width
from PIL import ImageFont


filename = ""
# importing text from files
def import_():
    # file browsser window
    filename = filedialog.askopenfilename(
        title="Open file", filetypes=[("Text file", ".txt")]
    )
    if filename:
        # clearing input field
        input_field.delete("1.0", "end")
        # Read the content and import it into the input text box field
        with open(filename, "r", encoding="utf-8") as f:
            for line in f.readlines():
                input_field.insert("end", line)


# saving file
def save_():

    # file browser window(dor saving)
    file = filedialog.asksaveasfilename(
        title="Save File", filetypes=[("Text file", ".txt")], defaultextension=".txt"
    )
    # read the text in the import field and put it in a text file

    text = input_field.get("1.0", "end-1c")
    with open(file, "w") as f:
        f.write(str(text))

    # messsage
    tkmb.showinfo("Message", "Success")


def save_ctr_s():
    print("coming soon.")


def run():

    # opening terminal window
    terminal = tk.Tk()
    terminal.geometry("500x500")
    terminal.config(background="#DCDCDC")
    terminal.title("PyString OutPut")

    # output
    output = ttk.Frame(master=terminal)
    output_text = tk.Text(master=output)
    entry = tk.Entry(terminal)
    
    enter = tk.Button(terminal, 
                       text="↲",
                       height=0)
    


    # Set the output terminal to read-only
    output_text.config(font=("arial", 9),  width=100, height=30)

    # packing output
    output_text.pack()
    output.pack()

    # clearing terminal
    output_text.delete("1.0", "end")

    # this will be the output
    terminal_output_executed = ""

    # getting input from input field
    input_code = input_field.get("1.0", "end-1c")
    # input coded --> code
    code = input_code.splitlines()

    # input_code
    # input_code=input_field.get("1.0","end-1c")

    line_input = 1
    line = 0
    code_line = ""
    val = ""
    var_name = ""
    val_to_write = ""
    statement = False
    speed = False
    show_vars = False
    length_of_code = len(code)
    code_program = []

    # lists of variables and values
    variables = []
    vals = []

    # lists and their names
    list_names = []
    lists = []

    # lists of functions and their names
    func_names = []
    funcs = []

    if_list = ("==", "!=", "<", ">")
    keywords = ("for", "func", "while")
    equal_list = ("=", "+=")

    # filename = input("path: ")

    # WRITING CODE IN TERMINAL
    # if filename == "write":
    ##   while code_line != "r":
    #     code_line = input(  str(line_input) + " ")
    #    line_input += 1
    #   code.append(code_line)
    #  length_of_code = len(code)
    #           code_program.append(code_line)

    # else:
    #   with open( filename , "r", encoding='utf-8' )as f:
    #        for line in f.readlines():
    #             code_line = line.rstrip()
    #              code.append(code_line)
    #               length_of_code = len(code)
    #
    #           code_program.append(code_line)

    timer_start = timer()
    # make code to output
    # terminal_output_executed += "______________________________\n"
    # terminal_output_executed += "\n"

    x = 0
    # separate the code per every line
    while x < len(code):
        if type(code[x]) == str:
            separated_code = code[x].split()
        else:
            separated_code = code[x]

        if separated_code == []:
            separated_code.append("empty line.")

        # shut down program
        if "/end_program" == separated_code[0]:
            break

        # show running speed
        if "/run_speed" == separated_code[0]:
            speed = True

        # log every variables and lists at the end of the program
        if "/visible_values" == separated_code[0]:
            show_vars = True

        if (
            "/values" in separated_code
            and separated_code[0] not in keywords
            and ";" not in separated_code
        ):
            ind = separated_code.index("/values")

            terminal_output_executed += ("Values of variables: ", vals, "\n")

        # ignore comments
        if "//" in separated_code:
            index_slash = separated_code.index("//")
            for i in separated_code[index_slash:]:
                separated_code.remove(i)

        for i in range(len(separated_code)):

            # write var.változó ----> write "value of variable"
            # recignize variables and manipulate codeline
            if (
                i < len(separated_code)
                and type(separated_code[i]) == str
                and "var." in separated_code[i]
                and separated_code[0] not in keywords
            ):

                almost_var_name = separated_code[i]
                var_name = almost_var_name[4:]
                if var_name in variables:
                    l = variables.index(var_name)
                    separated_code[i] = vals[l]

            # recognize lists
            if (
                i < len(separated_code)
                and type(separated_code[i]) == str
                and "list." in separated_code[i]
                and separated_code[0] not in keywords
            ):
                almost_list_name = separated_code[i]
                list_name = almost_list_name[5:]
                list_index = separated_code[i + 1]
                if list_name in list_name:
                    l = list_names.index(list_name)
                    list_ = lists[l]
                if list_index == "all":
                    separated_code[i] = ", ".join(list_)
                    separated_code[i + 1] = ""
                else:
                    separated_code[i] = list_[int(list_index)]
                    separated_code[i + 1] = ""

                    # WORK ON THIS
            #  do multiple things in one line
            # example:  write szia ; write világ
            if (
                i <= len(separated_code)
                and ";" == separated_code[i]
                and separated_code[0] not in keywords
            ):
                index_of_end = separated_code.index(";")
                index_of_end += 1
                code.insert(x + 1, separated_code[index_of_end:])
                separated_code[index_of_end - 1 :] = "" * len(
                    separated_code[index_of_end - 1 :]
                )

            # length
            # var greet = hello world ||| write var.greet length  ---> 9
            if i < len(separated_code) and "<-length" == separated_code[i]:
                length = len(vals[variables.index(separated_code[i - 1])])
                separated_code[i - 1] = length
                separated_code.remove(separated_code[i])
                separated_code.append("")

            # LIST Length
            # var greet = hello world ||| write var.greet length  ---> 9
            if i < len(separated_code) and "<-list_length" == separated_code[i]:
                separated_code[i - 1] = len(
                    lists[list_names.index(separated_code[i - 1])]
                )
                separated_code.remove(separated_code[i])
                separated_code.append("")

        # add two integers
        if (
            "add:" in separated_code
            and separated_code[0] not in keywords
            and ";" not in separated_code
        ):
            ind = separated_code.index("add:")
            num1 = int(separated_code[ind + 1])
            num2 = int(separated_code[ind + 2])

            separated_code[ind] = str(num1 + num2)
            separated_code[ind + 1] = ""
            separated_code[ind + 2] = ""

        # substract the second number from the first
        if (
            "sub:" in separated_code
            and separated_code[0] not in keywords
            and ";" not in separated_code
        ):
            ind = separated_code.index("sub:")
            num1 = int(separated_code[ind + 1])
            num2 = int(separated_code[ind + 2])

            separated_code[ind] = str(num1 - num2)
            separated_code[ind + 1] = ""
            separated_code[ind + 2] = ""

            # divide the second number from the first
        if (
            "div:" in separated_code
            and separated_code[0] not in keywords
            and ";" not in separated_code
        ):
            ind = separated_code.index("div:")
            num1 = int(separated_code[ind + 1])
            num2 = int(separated_code[ind + 2])

            separated_code[ind] = str(num1 / num2)
            separated_code[ind + 1] = ""
            separated_code[ind + 2] = ""

            # substract the second number from the first
        if (
            "mul:" in separated_code
            and separated_code[0] not in keywords
            and ";" not in separated_code
        ):
            ind = separated_code.index("mul:")
            num1 = int(separated_code[ind + 1])
            num2 = int(separated_code[ind + 2])

            separated_code[ind] = str(num1 * num2)
            separated_code[ind + 1] = ""
            separated_code[ind + 2] = ""

        if (
            "round:" in separated_code
            and separated_code[0] not in keywords
            and ";" not in separated_code
        ):
            ind = separated_code.index("round:")
            num = float(separated_code[ind + 1])

            separated_code[ind] = round(num)
            separated_code[ind + 1] = ""

        if (
            "index:" in separated_code
            and separated_code[0] not in keywords
            and ";" not in separated_code
        ):
            h = separated_code.index("index:")
            index = int(separated_code[h + 1])
            variable_name = separated_code[h - 1]
            if variable_name in variables:
                value = vals[variables.index(variable_name)]
            elif variable_name in list_names:
                value = lists[list_names.index(variable_name)]
            separated_code[h - 1] = value[index]
            separated_code.remove(separated_code[h])
            separated_code.remove(separated_code[h])

        # recognize functions
        if (
            i < len(separated_code)
            and type(separated_code[i]) == str
            and "func." in separated_code[i]
        ):
            almost_func_name = separated_code[i]
            func_name = almost_func_name[5:]
            if func_name in func_names:
                l = func_names.index(func_name)
                # next line = function
                code.insert(x + 1, funcs[l])

                # functin' is not assigned

        # random number between two number
        if separated_code[0] not in keywords and "random:" in separated_code:
            o = separated_code.index("random:")
            low = int(separated_code[o + 1])
            high = int(separated_code[o + 2])
            rand_int = random.randint(low, high)
            separated_code[o + 1] = ""
            separated_code[o + 2] = ""
            separated_code[o] = str(rand_int)

        # random choice
        if separated_code[0] not in keywords and "ran_choice:" in separated_code:
            d = separated_code.index("ran_choice:")
            amount = separated_code[d + 1]
            ch_from = separated_code[d + 2]
            to_code = ""
            for n in range(int(amount)):
                to_code += random.choice(ch_from)
            separated_code[d] = to_code
            separated_code[d + 1] = " "
            separated_code[d + 2] = " "

        # random string generator
        # if separated_code[0] not in keywords  and "/random_gen:" in separated_code:
        #    terminal_output_executed += ("does work")
        #    x = separated_code.index("/random_gen:")
        #   if "length:" in separated_code:
        #        length_index = separated_code.index("length:")
        #        string_length =  int(separated_code[length_index + 1])
        #        separated_code[length_index] = ""
        #        separated_code[length_index + 1] = ""
        #        src_index = separated_code.index("src:")
        #        string_src =  separated_code[src_index + 1]
        #        separated_code[src_index] = ""
        #        separated_code[src_index + 1] = ""
        #        separated_code[x] = ''.join(random.choice("abcdefghijklmnopqrstvwxyqz") for x in range(string_length ))

        # random letter
        if separated_code[0] not in keywords and "/ran_letter" in separated_code:
            j = separated_code.index("/ran_letter")
            separated_code[j] = random.choice("abcdefghijklmnopqrstvwxyqz")

        # random number
        if separated_code[0] not in keywords and "/ran_num" in separated_code:
            u = separated_code.index("/ran_num")
            separated_code[u] = random.choice("1234567890")

        # random choice from list
        if separated_code[0] not in keywords and "ran_from_list:" in separated_code:
            z = separated_code.index("ran_from_list:")
            list_name = separated_code[z + 1]
            list_elements = lists[list_names.index(list_name)]
            separated_code[z] = random.choice(list_elements)
            separated_code[z + 1] = ""

        # lower
        if (
            "lower:" in separated_code
            and separated_code[0] not in keywords
            and ";" not in separated_code
        ):
            index_lower = separated_code.index("lower:")
            separated_code[index_lower] = ""
            # range because i need i as an int, not the ele
            for i in range(len(separated_code[index_lower + 1 :])):
                separated_code[index_lower + 1 + i] = separated_code[
                    index_lower + 1 + i
                ].lower()

        # upper
        if (
            "upper:" in separated_code
            and separated_code[0] not in keywords
            and ";" not in separated_code
        ):
            index_upper = separated_code.index("upper:")
            separated_code[index_upper] = ""
            # range because i need i as an int, not the ele
            for i in range(len(separated_code[index_upper + 1 :])):
                separated_code[index_upper + 1 + i] = separated_code[
                    index_upper + 1 + i
                ].upper()

        # sentence:   makes the first character uppercase, and adds dot to the end
        if (
            "sentence:" in separated_code
            and separated_code[0] not in keywords
            and ";" not in separated_code
        ):
            index_sen = separated_code.index("sentence:")
            separated_code[index_sen] = ""
            sentence_list = separated_code[index_sen + 1 :][0]
            first_l = sentence_list[0]
            # first letter -> uppercase
            sentence_str = first_l.upper() + sentence_list[1:]
            # adds dot
            sentence_str += "."
            separated_code[index_sen + 1 :] = sentence_str.split()

        # list to string
        if (
            "list_to_str:" in separated_code
            and separated_code[0] not in keywords
            and ";" not in separated_code
        ):
            index_lts = separated_code.index("list_to_str:")
            if len(separated_code) > 5:
                join = separated_code[index_lts + 2]
                join = join[1:-1]
                separated_code[index_lts + 2] = ""
            else:
                join = " "
            list_name = separated_code[index_lts + 1]
            list_index = list_name.index(list_name)
            result = join.join(lists[list_index])
            result = join.join(lists[list_index])
            var_name = separated_code[1]
            if var_name in variables:
                vals[variables.index(var_name)] = result
            else:
                vals.append(result)
                variables.append(var_name)
            separated_code[index_lts] = ""
            separated_code[index_lts + 1] = ""

        # string to list
        if (
            "str_to_list:" in separated_code
            and separated_code[0] not in keywords
            and ";" not in separated_code
        ):
            index_str = separated_code.index("str_to_list:")
            var_name = separated_code[index_str + 1]
            if len(separated_code) > 6:
                split = separated_code[index_str + 2]
                split = split[1:-1]
                separated_code[index_str + 2] = ""
            else:
                split = " "
            string = vals[variables.index(var_name)]
            result = string.split(split)
            lists[lists.index(separated_code[2])] = result
            separated_code[index_str + 1] = ""

        if (
            "check_list:" in separated_code
            and separated_code[0] not in keywords
            and ";" not in separated_code
        ):
            ind = separated_code.index("check_list:")
            list_name = separated_code[ind + 1]
            object = separated_code[ind + 2]
            list_elements = lists[list_names.index(list_name)]
            if object in list_elements:
                separated_code[ind] = "true"
            else:
                separated_code[ind] = "false"
            separated_code[ind + 1] = ""
            separated_code[ind + 2] = ""

        if (
            "time:" in separated_code
            and separated_code[0] not in keywords
            and ";" not in separated_code
        ):
            ind = separated_code.index("time:")
            code = separated_code[ind + 1]

            parts = code.split(":")

            hour = int(parts[0])
            minute = int(parts[1])
            second = int(parts[2])

            he_x = str(hour * 60 * 60 + minute * 60 + second)

            separated_code[ind] = he_x
            separated_code[ind + 1] = ""

        # store variables and their values
        # var változo = érték
        if separated_code[0] == "var" and separated_code[2] in equal_list:
            name = separated_code[1]
            # int as value
            if separated_code[3] == "int:":
                val = int(separated_code[4])
            elif separated_code[3] == "bool:":
                if separated_code[4] == "true":
                    val = "true"
                else:
                    val = "false"
            else:
                # var változo = input kérdés
                # input as value                          if it is an integer -> error
                if len(separated_code) > 3 and "scan:" in str(separated_code[3]):

                        question = " ".join(i for i in separated_code[4:])
                        font= ImageFont.truetype("arial.ttf", 9)
                        
                        entry.pack(side="left")
                        enter.pack(side="left")
                        
                        





                        # Create a boolean variable to track button press
                        button_pressed = False

                        # Define a function to handle button clicks
                        def on_button_click():
                            nonlocal button_pressed
                            button_pressed = True
                            entry.destroy()  # Remove the entry widget
                            enter.destroy()  # Remove the enter button

                            # Retrieve the entered value
                            ####val = str(entry.get())  # Correct way to get value
                            val = "hello biat"
                            vals.append(val)
                            variables.append(name)
                        # Bind the button click event to the function
                        enter.config(command=on_button_click)

                        # Enter the event loop to wait for the button press
                        while not button_pressed:
                            root.update_idletasks()
                            root.update()

                        # ... rest of your code using the retrieved value (val) ...






                        #val = entry.get()
                else:
                    val = separated_code[3:]
                if type(val) is list:

                    val = " ".join(val)
            # var változó += plusz érték
            # add to values
            if "+=" in separated_code[2]:
                space = ""
                terminal_output_executed += (
                    type(vals[int(variables.index(name))])
                ), "\n"
                if type(vals[int(variables.index(name))]) == "str":
                    terminal_output_executed += "working\n"
                    space = " "
                    val = separated_code[4:]
                    val = " ".join(val)
                    vals[int(variables.index(name))] += val

                # if value == integer
                if type(vals[int(variables.index(name))]) == "int":
                    space = " "
                    val = separated_code[3]
                    terminal_output_executed += (separated_code[3]), "\n"
                    val = " ".join(val)
                    vals[int(variables.index(name))] += int(val)

            # var változó = új érték
            # reassign values
            elif name in variables and "=" == separated_code[2] and name[0] != "!":
                vals[variables.index(name)] = val
            elif name not in variables:
                vals.append(val)
                variables.append(name)

        # store lists
        if separated_code[0] == "list" and separated_code[0] not in keywords:
            name = separated_code[1]
            list_type = separated_code[2]
            # adding ele to list
            if separated_code[2] == "append:":
                into_lists = separated_code[3:]
                l = list_names.index(name)
                lists[l].append(" ".join(into_lists[:]))
            # removing element from list
            if separated_code[2] == "remove:":
                to_remove = separated_code[3]
                l = list_names.index(name)
                lists[l].remove(to_remove)
            # clearing list out
            if separated_code[2] == "/clear":
                l = list_names.index(name)
                lists.remove(lists[l])
                list_names.remove(list_name)
            # declaring a list
            if (
                len(separated_code) > 3
                and separated_code[3] == "="
                and name not in list_names
            ):
                into_lists = separated_code[4:]
                list_names.append(name)
                # declaring an empty list
                if into_lists[0] == "/empty_list":
                    lists.append([])
                # list with value
                else:
                    lists.append(into_lists)

        # store functions
        # func funkction = do something /write hello world/
        if separated_code[0] == "func" and separated_code[2] == "=":
            function_name = separated_code[1]
            in_function = separated_code[3:]
            func_names.append(function_name)
            funcs.append(in_function)

            # automatically string
        # write hello world
        # writing
        if separated_code[0] == "write":
            to_write = separated_code[1:]
            terminal_output_executed += " ".join(to_write)
            terminal_output_executed += "\n"



        # while cycle

        if separated_code[0] == "while":
            if "var." in separated_code[1]:
                cycle_variable  = int(vals[variables.index(separated_code[1][4:])])
            else:
                cycle_variable = int( separated_code[1])
            if "var." in separated_code[3]:
                second_condition  = int(vals[variables.index(separated_code[3][4:])])
            else:
                second_condition = int(separated_code[3])
            symbol = separated_code[2]

            action = int( separated_code[4][1:-1])

            if symbol == "<":
                cycle_variable = cycle_variable
                while cycle_variable < second_condition:

                    #if "/cycle_variable" in separated_code:
                     #   separated_code[separated_code.index("/cycle_variable")] = str(cycle_variable)
                    index_of_koto = separated_code.index("-")
                    index_of_koto += 1
                    code.insert(x + 1, separated_code[index_of_koto:])
                    cycle_variable += action


            if symbol == "<=":
                cycle_variable = cycle_variable
                while cycle_variable <= second_condition:

                    #if "/cycle_variable" in separated_code:
                     #   separated_code[separated_code.index("/cycle_variable")] = str(cycle_variable)
                    index_of_koto = separated_code.index("-")
                    index_of_koto += 1
                    code.insert(x + 1, separated_code[index_of_koto:])
                    cycle_variable += action
            
            if symbol == ">":
                cycle_variable = cycle_variable
                while cycle_variable > second_condition:

                    #if "/cycle_variable" in separated_code:
                     #   separated_code[separated_code.index("/cycle_variable")] = str(cycle_variable)
                    index_of_koto = separated_code.index("-")
                    index_of_koto += 1
                    code.insert(x + 1, separated_code[index_of_koto:])
                    cycle_variable += action
                        
            if symbol == ">=":
                cycle_variable = cycle_variable
                while cycle_variable >= second_condition:

                    #if "/cycle_variable" in separated_code:
                     #   separated_code[separated_code.index("/cycle_variable")] = str(cycle_variable)
                    index_of_koto = separated_code.index("-")
                    index_of_koto += 1
                    code.insert(x + 1, separated_code[index_of_koto:])
                    cycle_variable += action
            

            if symbol == "!=":
                cycle_variable = cycle_variable
                while cycle_variable != second_condition:

                    #if "/cycle_variable" in separated_code:
                     #   separated_code[separated_code.index("/cycle_variable")] = str(cycle_variable)
                    index_of_koto = separated_code.index("-")
                    index_of_koto += 1
                    code.insert(x + 1, separated_code[index_of_koto:])
                    cycle_variable += action
            

            if symbol == "==":
                cycle_variable = cycle_variable
                while cycle_variable == second_condition:

                    #if "/cycle_variable" in separated_code:
                     #   separated_code[separated_code.index("/cycle_variable")] = str(cycle_variable)
                    index_of_koto = separated_code.index("-")
                    index_of_koto += 1
                    code.insert(x + 1, separated_code[index_of_koto:])
                    cycle_variable += action
            

        # for 10 write hello world
        # ______
        # for names <-list_length - write list.names var.i ; var i = add: var.i + 1
        # ______

        # for cycle
        if separated_code[0] == "for":
            for y in range(int(separated_code[1])):
                index_of_koto = separated_code.index("-")
                index_of_koto += 1
                code.insert(x + 1, separated_code[index_of_koto:])

        # if 5 == 6 than write true else if 5 != 5 than write true else write false
        # if statement
        if separated_code[0] == "if":
            statement = False
            first = separated_code[1]
            statement = separated_code[2]
            second = separated_code[3]
            than = separated_code.index("than") + 1
            # integers
            if separated_code[4] == "/int/":
                first = int(first)
                second = int(second)

            true_false = False
            if statement == ">":
                if first > second:
                    true_false = True
            if statement == "<":
                if first < second:
                    true_false = True
            if statement == "==":
                if first == second:
                    true_false = True
            if statement == "!=":
                if first != second:
                    true_false = True
            if statement == "in":
                if first in second:
                    true_false = True
            # true without else
            if true_false == True and "else" not in separated_code:
                code.insert(x + 1, separated_code[than:])

            # statement = false -> else
            if true_false == False and "else" in separated_code:
                index_of_else = separated_code.index("else")
                index_of_else += 1
                code.insert(x + 1, separated_code[index_of_else:])

            # statement = true -> ignore else
            if true_false == True and "else" in separated_code:
                index_of_else = separated_code.index("else")
                code.insert(x + 1, separated_code[0:index_of_else])

        x += 1
    # terminal_output_executed += ("______________________________\n")
    timer_end = timer()
    time = round(timer_end - timer_start, 5)
    if speed == True:
        terminal_output_executed += "Program ran in  " + str(time) + "seconds\n"

    # show variables and values
    if show_vars == True:
        terminal_output_executed += (vals), "\n"
        terminal_output_executed += (variables), "\n"

    # WRITING THE OUTPUT INTO THE TREMINAL
    # output_text.insert(tk.END, terminal_output_executed)
    # print(terminal_output_executed)

    # WRITING THE OUTPUT INTO THE TREMINAL
    # output_text.insert(tk.END, terminal_output_executed)
    # WRITING THE OUTPUT INTO THE TREMINAL
    output_text.insert(tk.END, terminal_output_executed)

    # output terminal automatically scrolled to lowest line after execution
    output_text.yview_moveto(1.0)

    output_text.config(state="disabled")





# UI


# main window
root = tk.Tk()
# windwos size
root.geometry("1366x768")
# root style
# title
root.title("PS editor")
# logo
# root.iconphoto(False, tk.PhotoImage(file="logo.png"))


buttons = ttk.Frame(master=root)
# settings menu opener
settings_ = ttk.Button(
    master=buttons,
    text="☰",
    command=lambda: settings(),
    style="my_custom_style.TButton",
)
settings_.pack(side="left", padx=3)


# import from files button
import_button = ttk.Button(
    master=buttons,
    text="Import",
    command=lambda: import_(),
    style="my_custom_style.TButton",
)
import_button.pack(side="left", padx=3)


# save text to file
save = ttk.Button(
    master=buttons,
    text="Save as",
    command=lambda: save_(),
    style="my_custom_style.TButton",
)
save.pack(side="left")


# execute button
button = ttk.Button(
    master=buttons, text="▶", command=lambda: run(), style="my_custom_style.TButton"
)
button.pack(side="right", 
            padx=(0, 0))


# label on top of code field
label_frame = ttk.Frame(master=buttons, width=30, height=10)
file_label = tk.Label(
    master=label_frame, 
    text="PyString 0.1.", 
    padx=5, 
    font=("Tahoma", 8)
)

file_label.pack(side="left")

close_button = ttk.Button(master=label_frame, 
                          text="",
                         style="my_custom_style.TButton")

close_button.pack(side="left")
label_frame.pack()

buttons.pack(padx=(0, 0), pady=2)

# playground
playground_frame = ttk.Frame(master=root)


# directory
directory_frame = ttk.Frame(master=root, width=15, height=100)
directory_button = ttk.Button(
    master=directory_frame,
    text="Import folder",
    command=lambda: browse_directory(),
    style="my_custom_style.TButton",
    width=15,
)

directory_frame.pack(side="left", padx=(10, 0))
directory_button.pack(side=tk.TOP, expand=False)


# clear input field
def clear_input_field():
    file_label.config(text="PyString 0.0.4")
    input_field.delete("1.0", tk.END)
    close_button.config(text="", command="")


imported_paths = []
# popup window where the user can choose the folder
def browse_directory():
    global path
    directory = filedialog.askdirectory()
    # get files from the choosen path
    files = [
        f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))
    ]
    # display files from directory
    directory_button.config()  # state="disabled", text=path)
    # clear input field before importing
    # avoid imported a folder more than one time
    if directory not in imported_paths:

        imported_paths.append(directory)
        # add folder to list of imported folders
        files_list = files
        tk.Label(master=directory_frame, text=directory, font=("hack", 7)).pack()

        # clear input field and append text from file to it
        def clear_and_import(file, directory):
            # label with filename on top of field
            # if file is image open it in new window
            # if imghdr.what(Path(os.path.join(directory, file))) == "png":
            # image size
            # im = Image.open(Path(os.path.join(directory, file)))
            # width, height = im.size
            # image_window = Toplevel(width=width, height=height)
            # canvas = Canvas(image_window)
            # canvas.pack(expand = YES, fill = BOTH)
            # image = PhotoImage(file = Path(os.path.join(directory, file)))
            # image not visual
            # canvas.create_image(0, 0, image = image, anchor = NW)
            # assigned the gif1 to the canvas object
            # canvas.image = image

            close_button.config(text="✖", command=lambda: clear_input_field())

            file_label.config(text=Path(os.path.join(directory, file)))

            # clear input fied
            input_field.delete("1.0", tk.END)
            # import txt
            input_field.insert("1.0", Path(os.path.join(directory, file)).read_text())

        for file in files_list:
            button = ttk.Button(
                master=directory_frame,
                text=file,
                width=15,
                command=lambda f=file: clear_and_import(f, directory),
                style="my_custom_style.TButton",
                # input_field.insert(
                #    "1.0", Path(os.path.join(directory, f)).read_text()),
            )
            button.pack(expand=False)
    else:
        messagebox.showwarning("Alert", "folder already opened")


# scrollbar
v = Scrollbar(
    root,
    orient="vertical",
)
v.pack(side=RIGHT, fill="y", pady=1)


# input field
input_code = tk.StringVar()
# , textvariable=input_code
input_field = tk.Text(
    master=playground_frame,
    height=270,
    width=190,
    yscrollcommand=v.set,
    font=("hack", 9)
)

# scrollbar
v.config(command=input_field.yview)


# settings page
def settings():

    # applying settings
    def apply_settings():
        # codefield font size
        integer_value = int(entry_.get())
        if 6 <= integer_value <= 60:
            # Do something with the integer value
            input_field.config(font=("monospace", integer_value))
            # messagebox.showinfo("results", "Conditions succesfully applied")
            # close settings page
            # settings.destroy()
        else:
            # close settings page
            # settings.destroy()
            messagebox.showerror(
                "Settings Error",
                "Error: Selected font size too large or too small. \nSettings will not be applyed!",
            )

    settings = tk.Tk()
    settings.geometry("500x500")
    settings.title("Settings")
    setting_frame = tk.Frame(master=settings, width=500, height=450)

    tk.Label(setting_frame, text="Font size in codefield ( 6 - 60 ):").pack()
    entry_ = tk.Entry(
        setting_frame,
    )
    entry_.insert(tk.END, "10")

    apply_frame = tk.Frame(master=settings)
    apply_button = tk.Button(
        master=apply_frame, text="Apply", command=lambda: apply_settings()
    )
    apply_button.place(relx=0.5, rely=1.0, anchor="center")

    options_frame = tk.Frame(master=settings)

    # theme
    tk.Label(options_frame, text="Theme").pack()
    #dark theme
    theme_button = tk.Button(
        options_frame, text="dark theme", command=lambda: dark_theme()
    )
    #light theme
    theme_button = tk.Button(
        options_frame, text="light theme", command=lambda: light_theme()
    )


    # theme settings
    def dark_theme():
        # applying light theme
        root.config(background="#19102a")
        input_field.config(background="#2b1d48", fg="white")
        file_label.config(background="#19102a", fg="white")

    
    # theme settings
    def light_theme():
        # applying light theme
        root.config(background="whtie")
        input_field.config(background="#0000000", fg="blck")
        file_label.config(background="#0000000", fg="black")


    # packing
    setting_frame.pack()
    entry_.pack()
    apply_frame.pack()
    apply_button.pack()
    options_frame.pack()
    theme_button.pack()


# button style
# Define the style with desired font size in the ttk theme
style = ttk.Style()
style.configure("my_custom_style.TButton", font=("hack", 8))


input_field.insert("1.0", "write hello world")

input_field.pack(side="left", fill=tk.BOTH, expand=True)

playground_frame.pack()

root.config(background="#DCDCDC")
# executing ktinker
# main window
root.mainloop()