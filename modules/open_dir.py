import os

# for file in os.listdir(imgs_dir):
#     with open(f"{imgs_dir}/{file}", "rb") as file:
#         img = file.read()
#         img_b64 = (
#             str(base64.encodebytes(img))
#             .replace("\\n", "")  # replace the newline characters
#             .replace("b'", "")  # replace the initial binary
#             .replace("'", "")  # replace the final question mark
#         )
#         file_name = file.name.split("/")[-1].split(".")[0]
#         line_to_write = f"![{file_name}]({src_prefix}{img_b64})\n"
#         write_line_in_out_file(line_to_write, out_file)


class DirectoryIter:
    def __init__(self, directory_list):
        self.directory = directory_list
        self.index = 0

    def __next__(self):
        if self.index >= len(self.directory):
            raise StopIteration
        else:
            self.index += 1
            return self.directory[self.index - 1]


class Directory:
    def __init__(self, path):
        self.path = path
        self.files = os.listdir(path)

    def __iter__(self):
        return DirectoryIter(self.files)
