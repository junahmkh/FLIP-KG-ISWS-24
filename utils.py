secret_key = "add your secret key for chatgpt api here"

def read_txt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        print("File content:")
        print(content)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return content
def save_txt_file(content, save_path):
    try:
        with open(save_path, 'w') as file:
            file.write(content)
        print(f"Content successfully saved to {save_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
def read_ttl_as_text(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")