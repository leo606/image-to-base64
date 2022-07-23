# from modules.open_dir import Directory
import os
import base64

imgs_dir = "/home/leo/Pictures/screenshots"
src_prefix = "data:image/jpeg;base64,"

out_file = "md_links"


def write_line_in_out_file(line, out_file):
    print("write")
    with open(out_file, "a") as file:
        file.write(line)


for file in os.listdir(imgs_dir):
    with open(f"{imgs_dir}/{file}", "rb") as file:
        img = file.read()
        img_b64 = (
            str(base64.encodebytes(img))
            .replace("\\n", "")  # replace the newline characters
            .replace("b'", "")  # replace the initial binary
            .replace("'", "")  # replace the final question mark
        )
        file_name = file.name.split("/")[-1].split(".")[0]
        line_to_write = f"![{file_name}]({src_prefix}{img_b64})\n"
        write_line_in_out_file(line_to_write, out_file)

# directory = Directory(imgs_dir)
# for file in directory:
#     print(f"{directory.path}/{file}")

# credits:
#   https://stackoverflow.com/questions/50817518/hard-code-markdown-images
