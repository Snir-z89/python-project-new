from utils import scores_file_name

scores_file = scores_file_name


def file_content():
    file_name = scores_file_name

    # Try reading the file's content and create a new one if not exist
    try:
        read_file = open(file_name, "r")
        print("Current score: " + read_file.read())
    except FileNotFoundError:
        print("The file doesn't exist! Creating a new one")
        write_to_file = open(file_name, "w")
        write_to_file.write("0")
    f = open(file_name, "r")
    current_content = f.read()
    return current_content


def add_score(diff):
    win_points = (int(diff) * 3) + 5
    current_content = file_content()
    new_points = int(win_points) + int(current_content)
    append_points = open(scores_file, "w")
    append_points.write(str(new_points))
    append_points.close()
    print("New Score:" + str(new_points))
