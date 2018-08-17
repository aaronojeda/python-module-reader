import pydoc


def main():
    module_name = input('What module do you want to get informed about? ')
    # the output file's name will be [module_name]_info.txt
    output_file = module_name + '_info.txt'
    f = open(output_file, 'w')
    # pydoc.plain to avoid unwanted characters
    module_info = pydoc.plain(pydoc.render_doc(module_name))
    f.write(module_info)
    f.close()
    # inform the user about the output
    print(module_name, 'module information has been stored in', output_file)


if __name__ == "__main__":
    main()
