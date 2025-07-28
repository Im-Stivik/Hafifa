from typing import Generator


class FileLineReader:
    """
    an object that generates input from a file stream.
    gives one line from the file at the time.
    """

    def __init__(self, input_file: str):
        """
        generates the input based on the given file stream.
        :param input_file: the file to read from
        """
        self.input_file = input_file

    def get_input(self) -> Generator[str, None, None]:
        """
        gives each line of the file stream in a generator

        :raises: FileNotFoundError: couldn't find the given file
        """
        with open(self.input_file) as lines:
            for line in lines:
                line = line[:-1]
                yield line
